#!/usr/bin/env python3
"""
LN Studio Syntax & Code Completion Extractor

Extracts syntax highlighting keywords, program sections, subsections, choice sections,
report sections, predefined variables, standard defines, DAL object/field hooks,
and code templates directly from the pinned LN Studio installation JARs.

Outputs:
  - references/studio_syntax_completion.json
  - references/STUDIO_SYNTAX_COMPLETION.md
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional

from ln_workspace_manager import get_studio_installation_path


def find_studio_jars(studio_path: Path) -> List[str]:
    """Locate essential OSGi jars and plugins wildcard from LN Studio installation."""
    target_names = {
        "lnstudio_commonui.jar",
        "lnstudio_commoncore.jar",
        "threegl_parser.jar",
        "threegl_scanner.jar",
        "fourglstudio_core.jar",
    }
    found_jars: List[str] = []

    osgi_dir = studio_path / "configuration" / "org.eclipse.osgi"
    if osgi_dir.exists():
        for root, _, files in os.walk(osgi_dir):
            for f in files:
                if f in target_names:
                    found_jars.append(str(Path(root) / f))

    plugins_wildcard = str(studio_path / "plugins" / "*")
    found_jars.append(plugins_wildcard)

    return found_jars


def extract_dictionaries_via_java(studio_path: Path) -> Dict[str, Any]:
    """Execute temporary Java runner to reflectively extract constants from LN Studio JARs."""
    cp_entries = find_studio_jars(studio_path)
    if not cp_entries:
        raise FileNotFoundError(f"No JAR files found under {studio_path}")

    cp = ";".join(cp_entries)

    java_code = r'''
import java.lang.reflect.Field;
import java.util.*;
import com.infor.ln.studio.common.ui.script.constants.*;
import com.infor.ln.studio.common.ui.script.codeassist.CodeCompletion;

public class StudioDictionaryExtractor {
    private static void add2DArray(Map<String, Object> map, String key, String[][] arr) {
        List<String> list = new ArrayList<>();
        if (arr != null) {
            for (String[] row : arr) {
                if (row != null && row.length > 0 && row[0] != null) {
                    list.add(row[0]);
                }
            }
        }
        map.put(key, list);
    }

    public static void main(String[] args) {
        Map<String, Object> result = new LinkedHashMap<>();
        try {
            add2DArray(result, "keywords", IScriptEditorKeywords.KEYWORDS);
            add2DArray(result, "sql_keywords", IScriptEditorSQLKeywords.SQL_KEYWORDS);
            add2DArray(result, "program_sections", IScriptEditorProgramSections.PROGRAM_SECTIONS);
            add2DArray(result, "sub_sections", IScriptEditorSubSections.SUB_SECTIONS);
            add2DArray(result, "choice_sections", IScriptEditorChoiceSections.CHOICE_SECTIONS);
            add2DArray(result, "report_sections", IScriptEditorReportSections.REPORT_SECTIONS);
            add2DArray(result, "predefined_variables", IScriptEditorPredefinedVariables.PREDEFINED_VARIABLES);
            add2DArray(result, "standard_defines", IScriptEditorStandardDefines.STANDARD_DEFINES);
            add2DArray(result, "other_keywords", IScriptEditorOther.OTHER_KEYWORDS);

            // DAL Object Hooks
            List<String> dalObjHooks = new ArrayList<>();
            if (CodeCompletion.DAL_OBJECT_HOOKS != null) {
                for (Object o : CodeCompletion.DAL_OBJECT_HOOKS) {
                    if (o != null) dalObjHooks.add(o.toString());
                }
            }
            result.put("dal_object_hooks", dalObjHooks);

            // DAL Field Hook Suffixes
            List<Map<String, String>> dalFieldHooks = new ArrayList<>();
            Field dfhField = CodeCompletion.class.getDeclaredField("DAL_FIELD_HOOK_SUFFIXES");
            dfhField.setAccessible(true);
            Object[] hooks = (Object[]) dfhField.get(null);
            if (hooks != null) {
                for (Object h : hooks) {
                    Map<String, String> hookInfo = new LinkedHashMap<>();
                    for (Field f : h.getClass().getDeclaredFields()) {
                        f.setAccessible(true);
                        Object val = f.get(h);
                        hookInfo.put(f.getName(), val != null ? val.toString() : "");
                    }
                    dalFieldHooks.add(hookInfo);
                }
            }
            result.put("dal_field_hook_suffixes", dalFieldHooks);

            // Print as JSON
            StringBuilder sb = new StringBuilder();
            sb.append("{");
            boolean firstKey = true;
            for (Map.Entry<String, Object> entry : result.entrySet()) {
                if (!firstKey) sb.append(",\n");
                firstKey = false;
                sb.append("\"").append(entry.getKey()).append("\": ");
                Object val = entry.getValue();
                if (val instanceof List) {
                    List<?> list = (List<?>) val;
                    sb.append("[");
                    for (int i = 0; i < list.size(); i++) {
                        if (i > 0) sb.append(", ");
                        Object item = list.get(i);
                        if (item instanceof Map) {
                            Map<?, ?> m = (Map<?, ?>) item;
                            sb.append("{");
                            boolean firstSub = true;
                            for (Map.Entry<?, ?> sub : m.entrySet()) {
                                if (!firstSub) sb.append(", ");
                                firstSub = false;
                                sb.append("\"").append(sub.getKey()).append("\": \"")
                                  .append(escape(sub.getValue().toString())).append("\"");
                            }
                            sb.append("}");
                        } else {
                            sb.append("\"").append(escape(item.toString())).append("\"");
                        }
                    }
                    sb.append("]");
                }
            }
            sb.append("}");
            System.out.println(sb.toString());
        } catch (Exception e) {
            e.printStackTrace(System.err);
            System.exit(1);
        }
    }

    private static String escape(String s) {
        return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\r", "\\r");
    }
}
'''
    with tempfile.TemporaryDirectory() as tmpdir:
        java_file = Path(tmpdir) / "StudioDictionaryExtractor.java"
        java_file.write_text(java_code, encoding="utf-8")

        cmd = ["java", "-cp", f"{cp};{tmpdir}", str(java_file)]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if proc.returncode != 0:
            raise RuntimeError(f"Java extraction failed (code {proc.returncode}):\n{proc.stderr}")

        return json.loads(proc.stdout)


def extract_templates_from_jar(studio_path: Path) -> List[Dict[str, str]]:
    """Extract 4GL code templates from plugins/com.infor.ln.studio.common.ui_*.jar."""
    import zipfile

    plugins_dir = studio_path / "plugins"
    target_jar: Optional[Path] = None
    if plugins_dir.exists():
        for f in os.listdir(plugins_dir):
            if f.startswith("com.infor.ln.studio.common.ui_") and f.endswith(".jar"):
                target_jar = plugins_dir / f
                break

    if not target_jar or not target_jar.exists():
        return []

    templates: List[Dict[str, str]] = []
    with zipfile.ZipFile(target_jar) as z:
        if "codetemplates/DefaultFourglTemplates.xml" not in z.namelist():
            return []

        xml_data = z.read("codetemplates/DefaultFourglTemplates.xml")
        prop_data = z.read("codetemplates/fourgl.template.properties").decode("utf-8", errors="replace")

        props: Dict[str, str] = {}
        for line in prop_data.splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                props[k.strip()] = v.strip()

        root = ET.fromstring(xml_data)
        for t in root.findall("template"):
            tid = t.get("id", "")
            name = t.get("name", "")
            desc = t.get("description", "")
            if name.startswith("%"):
                name = props.get(name[1:], name)
            if desc.startswith("%"):
                desc = props.get(desc[1:], desc)
            pattern = t.text or ""
            templates.append({
                "id": tid,
                "name": name,
                "description": desc,
                "pattern": pattern.strip(),
            })

    return templates


def build_markdown_documentation(data: Dict[str, Any], studio_path: Path) -> str:
    """Generate comprehensive reference Markdown document."""
    lines: List[str] = [
        "# LN Studio Syntax & Code Completion Reference Catalog",
        "",
        "> Canonical reference extracted from LN Studio 10.8 (build 0640).",
        f"> **Source Installation**: `{studio_path}`",
        "",
        "## Summary",
        "",
        f"- **Keywords**: {len(data.get('keywords', []))}",
        f"- **SQL Keywords**: {len(data.get('sql_keywords', []))}",
        f"- **Program Sections**: {len(data.get('program_sections', []))}",
        f"- **Subsections**: {len(data.get('sub_sections', []))}",
        f"- **Choice Sections**: {len(data.get('choice_sections', []))}",
        f"- **Report Sections**: {len(data.get('report_sections', []))}",
        f"- **Predefined Variables**: {len(data.get('predefined_variables', []))}",
        f"- **Standard Defines**: {len(data.get('standard_defines', []))}",
        f"- **DAL Object Hooks**: {len(data.get('dal_object_hooks', []))}",
        f"- **DAL Field Hook Suffixes**: {len(data.get('dal_field_hook_suffixes', []))}",
        f"- **Code Templates**: {len(data.get('templates', []))}",
        "",
        "---",
        "",
        "## 1. Program Sections (`IScriptEditorProgramSections`)",
        "",
        "Top-level execution sections in LN 4GL scripts:",
        "",
        "| Section Header | Description |",
        "|---|---|",
    ]
    for s in sorted(data.get("program_sections", [])):
        lines.append(f"| `{s}` | Standard LN Studio program section |")

    lines.extend([
        "",
        "### Dynamic Program Sections",
        "- `field.<field_name>:` — Field-specific UI logic (e.g., `field.txcmg011.cdec:`)",
        "- `choice.<choice_name>:` — Form command / standard choice handler",
        "- `form.<form_num>:` — Form-level event handler",
        "- `group.<group_num>:` — Form group handler",
        "- `header.<report_num>:`, `detail.<report_num>:`, `before.<report_num>:`, `after.<report_num>:` — Report layout sections",
        "- `functions:` — 3GL/4GL function definitions",
        "",
        "---",
        "",
        "## 2. Subsections (`IScriptEditorSubSections`)",
        "",
        "Subsections nested inside program sections (e.g., `field.*:`, `choice.*:`, `main.table.io:`):",
        "",
        "| Subsection | Category |",
        "|---|---|",
    ])
    for s in sorted(data.get("sub_sections", [])):
        category = "Field Hook"
        if "choice" in s:
            category = "Choice Hook"
        elif "delete" in s or "write" in s or "read" in s:
            category = "Table IO Hook"
        lines.append(f"| `{s}` | {category} |")

    lines.extend([
        "",
        "---",
        "",
        "## 3. Choice Sections (`IScriptEditorChoiceSections`)",
        "",
        "Standard choice events in UI sessions:",
        "",
        "| Choice Section | Description |",
        "|---|---|",
    ])
    for s in sorted(data.get("choice_sections", [])):
        lines.append(f"| `{s}` | Standard Session Choice Section |")

    lines.extend([
        "",
        "---",
        "",
        "## 4. DAL Object Hooks (`CodeCompletion.DAL_OBJECT_HOOKS`)",
        "",
        "Object-level DAL 2 hooks executed during CRUD lifecycle:",
        "",
        "| Hook Name | Lifecycle Phase |",
        "|---|---|",
    ])
    for h in data.get("dal_object_hooks", []):
        lines.append(f"| `{h}()` | Standard DAL 2 Object Hook |")

    lines.extend([
        "",
        "---",
        "",
        "## 5. DAL Field Hook Suffixes (`CodeCompletion.DAL_FIELD_HOOK_SUFFIXES`)",
        "",
        "Property hooks for DAL 2 scripts and Table Extensions (`.est`):",
        "",
        "| Suffix | Return Type | Arguments | Default Body |",
        "|---|---|---|---|",
    ])
    for h in data.get("dal_field_hook_suffixes", []):
        lines.append(f"| `<table.column>{h.get('suffix')}` | `{h.get('returnValue')}` | `{h.get('arguments')}` | `{h.get('body')}` |")

    lines.extend([
        "",
        "---",
        "",
        "## 6. Predefined Variables & Standard Defines",
        "",
        f"- **Total Predefined Variables**: {len(data.get('predefined_variables', []))}",
        f"- **Total Standard Defines**: {len(data.get('standard_defines', []))}",
        "",
        "Commonly used:",
        "- `actual.occ`, `attr.changed`, `attr.conv`, `curr.key`, `dal.change.object`, `spool.device`",
        "- `DAL_GET_FIRST`, `DAL_GET_NEXT`, `DAL_GET_PREV`, `DAL_GET_LAST`, `DAL_GET_CURR`, `DALHOOKERROR`",
        "",
        "---",
        "",
        "## 7. 4GL Code Templates",
        "",
    ])
    for t in data.get("templates", []):
        lines.extend([
            f"### {t.get('name')}",
            f"> {t.get('description')}",
            "",
            "```4gl",
            t.get("pattern", ""),
            "```",
            "",
        ])

    return "\n".join(lines)


def extract_and_save(studio_path: Optional[Path] = None,
                     output_json: Optional[Path] = None,
                     output_md: Optional[Path] = None) -> Dict[str, Any]:
    """Run full extraction and persist JSON & Markdown catalogs."""
    if not studio_path:
        studio_path = get_studio_installation_path()

    if not studio_path.exists():
        raise FileNotFoundError(f"LN Studio installation not found at: {studio_path}")

    base_dir = Path(__file__).resolve().parent.parent
    if not output_json:
        output_json = base_dir / "references" / "studio_syntax_completion.json"
    if not output_md:
        output_md = base_dir / "references" / "STUDIO_SYNTAX_COMPLETION.md"

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)

    print(f"Extracting dictionaries from LN Studio: {studio_path}")
    data = extract_dictionaries_via_java(studio_path)

    templates = extract_templates_from_jar(studio_path)
    data["templates"] = templates

    output_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote JSON dictionary catalog to: {output_json}")

    md_content = build_markdown_documentation(data, studio_path)
    output_md.write_text(md_content, encoding="utf-8")
    print(f"Wrote Markdown documentation to: {output_md}")

    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract LN Studio Syntax & Code Completion Dictionaries")
    parser.add_argument("--studio-path", type=Path, default=None, help="Path to LN Studio installation")
    parser.add_argument("--output-json", type=Path, default=None, help="Output JSON path")
    parser.add_argument("--output-md", type=Path, default=None, help="Output Markdown path")
    args = parser.parse_args()

    try:
        extract_and_save(studio_path=args.studio_path, output_json=args.output_json, output_md=args.output_md)
    except Exception as e:
        print(f"Error during extraction: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
