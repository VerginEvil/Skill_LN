#!/usr/bin/env python3
"""
LN Studio Build 0640 Knowledge Extractor

Extracts:
1. Function Catalog (2,274 bshell functions) from `functionlist.xml` -> `index/functions_db.json`
2. Editor Syntax Dictionaries (Keywords, Sections, DAL Hooks, Snippets) -> `references/studio_syntax_completion.json` & `STUDIO_SYNTAX_COMPLETION.md`
3. Official Script Templates from `com.infor.ln.studio.common.core_*.jar` -> `templates/*.cln`, `*.dal`, `*.ue`
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

DEFAULT_STUDIO_PATH = Path(r"d:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64")


def find_studio_path(cli_path: Optional[str] = None) -> Path:
    if cli_path:
        p = Path(cli_path)
        if p.exists():
            return p
    env_p = os.environ.get("LN_STUDIO_PATH")
    if env_p and Path(env_p).exists():
        return Path(env_p)
    if DEFAULT_STUDIO_PATH.exists():
        return DEFAULT_STUDIO_PATH
    raise FileNotFoundError(
        f"LN Studio installation path not found. Please provide --studio-path. Checked: {DEFAULT_STUDIO_PATH}"
    )


def extract_return_type(name: str, syntax: str, desc: str = "") -> str:
    """Extract return type from syntax definition."""
    s = syntax.replace("\xa0", " ").strip()
    if name == "prcm.get.aspect":
        return "string"

    # Pattern: [function ] [extern ] [return_type] <name> (
    pattern = (
        r"^(?:function\s+)?(?:extern\s+)?(?:(domain\s+[a-zA-Z0-9_.]+|\[[^\]]+\]|[a-zA-Z0-9_#]+(?:\s*\([^)]*\))?)\s+)?"
        + re.escape(name)
        + r"\s*\("
    )
    m = re.match(pattern, s, re.IGNORECASE)
    if m and m.group(1):
        rt = m.group(1).strip()
        return rt

    # Check common prefixes or keywords in syntax
    if s.startswith("void ") or " void " in s:
        return "void"
    if s.startswith("long ") or " long " in s:
        return "long"
    if s.startswith("string ") or " string " in s:
        return "string"
    if s.startswith("boolean ") or " boolean " in s:
        return "boolean"
    if s.startswith("double ") or " double " in s:
        return "double"

    # Default fallback
    return "void"


def parse_functionlist_xml(studio_path: Path, skill_path: Path) -> Dict[str, Any]:
    """Parse com.infor.ln.studio.apps.progguide_*/help/index/functionlist.xml into functions_db dict."""
    plugins_dir = studio_path / "plugins"
    flist_file: Optional[Path] = None
    for item in plugins_dir.glob("com.infor.ln.studio.apps.progguide_*"):
        candidate = item / "help" / "index" / "functionlist.xml"
        if candidate.exists():
            flist_file = candidate
            break

    if not flist_file or not flist_file.exists():
        raise FileNotFoundError(f"functionlist.xml not found under {plugins_dir}")

    tree = ET.parse(flist_file)
    root = tree.getroot()

    guide_dir = skill_path / "references" / "guide"
    functions_db: Dict[str, Any] = {}

    for elem in root.findall("Function"):
        name = elem.findtext("Name", "").strip()
        if not name:
            continue

        deprecated = elem.attrib.get("Deprecated", "").lower() == "yes"
        trusted = elem.attrib.get("Trusted", "").lower() == "yes"
        internal = elem.attrib.get("Internal", "").lower() == "yes"
        include = elem.attrib.get("include", "").strip()

        script_type = elem.findtext("ScriptType", "all").strip()
        syntax = elem.findtext("Syntax", "").replace("\xa0", " ").strip()
        desc = elem.findtext("Description", "").strip()
        help_id = elem.findtext("HelpID", "").strip()

        # Check doc_path
        doc_path: Optional[str] = None
        if help_id:
            rel_candidate = help_id.strip("/") + ".md"
            full_guide_path = guide_dir / rel_candidate
            if full_guide_path.exists():
                doc_path = f"references/guide/{rel_candidate}"

        return_type = extract_return_type(name, syntax, desc)

        entry = {
            "name": name,
            "syntax": syntax,
            "return_type": return_type,
            "script_type": script_type,
            "trusted": trusted,
            "deprecated": deprecated,
            "internal": internal,
            "include": include,
            "description": desc,
            "help_id": help_id,
            "doc_path": doc_path,
        }

        if name not in functions_db:
            functions_db[name] = entry
        else:
            # Overloaded or duplicate function in functionlist.xml
            existing = functions_db[name]
            if "overloads" not in existing:
                existing["overloads"] = [
                    {
                        "syntax": existing["syntax"],
                        "return_type": existing["return_type"],
                        "help_id": existing["help_id"],
                        "doc_path": existing["doc_path"],
                    }
                ]
            existing["overloads"].append({
                "syntax": syntax,
                "return_type": return_type,
                "help_id": help_id,
                "doc_path": doc_path,
            })
            # Prefer doc_path matching function name over generic synopsis
            if (not existing["doc_path"] or name not in Path(existing["doc_path"]).stem) and doc_path and name in Path(doc_path).stem:
                existing["syntax"] = syntax
                existing["return_type"] = return_type
                existing["help_id"] = help_id
                existing["doc_path"] = doc_path
                existing["description"] = desc

    return functions_db


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


def extract_editor_dictionaries_java(studio_path: Path) -> Dict[str, Any]:
    """Extract syntax completion dictionaries using Java reflection against LN Studio JARs."""
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

            List<String> dalObjHooks = new ArrayList<>();
            if (CodeCompletion.DAL_OBJECT_HOOKS != null) {
                for (Object o : CodeCompletion.DAL_OBJECT_HOOKS) {
                    if (o != null) dalObjHooks.add(o.toString());
                }
            }
            result.put("dal_object_hooks", dalObjHooks);

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


def extract_ui_code_templates(studio_path: Path) -> List[Dict[str, str]]:
    """Extract 4GL code templates from plugins/com.infor.ln.studio.common.ui_*.jar."""
    plugins_dir = studio_path / "plugins"
    target_jar: Optional[Path] = None
    for f in plugins_dir.glob("com.infor.ln.studio.common.ui_*.jar"):
        target_jar = f
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
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                props[k.strip()] = v.strip()

        root = ET.fromstring(xml_data)
        for tpl in root.findall("template"):
            raw_name = tpl.attrib.get("name", "")
            raw_desc = tpl.attrib.get("description", "")
            context = tpl.attrib.get("context", "")
            pattern = tpl.text or ""

            name_key = raw_name.lstrip("%")
            desc_key = raw_desc.lstrip("%")

            name = props.get(name_key, raw_name)
            desc = props.get(desc_key, raw_desc)

            templates.append({
                "id": raw_name,
                "name": name,
                "description": desc,
                "context": context,
                "pattern": pattern.strip(),
            })

    return templates


def extract_official_script_templates(studio_path: Path, output_dir: Path) -> List[Path]:
    """Extract official ScriptTemplates from com.infor.ln.studio.common.core_*.jar."""
    plugins_dir = studio_path / "plugins"
    core_jar: Optional[Path] = None
    for f in plugins_dir.glob("com.infor.ln.studio.common.core_*.jar"):
        core_jar = f
        break

    if not core_jar or not core_jar.exists():
        raise FileNotFoundError(f"com.infor.ln.studio.common.core_*.jar not found in {plugins_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    mapping = {
        "ScriptTemplates/Bol": "Bol.cln",
        "ScriptTemplates/Dal": "Dal.dal",
        "ScriptTemplates/DalTwo": "DalTwo.dal",
        "ScriptTemplates/Function": "Function.cln",
        "ScriptTemplates/Integration": "Integration.cln",
        "ScriptTemplates/Report": "Report.cln",
        "ScriptTemplates/ThreeGL": "ThreeGL.cln",
        "ScriptTemplates/UIDatabase": "UIDatabase.cln",
        "ScriptTemplates/UserExitDLL": "UserExitDLL.ue",
    }

    extracted: List[Path] = []
    with zipfile.ZipFile(core_jar) as z:
        for jar_path, out_name in mapping.items():
            if jar_path in z.namelist():
                content = z.read(jar_path).decode("utf-8", errors="replace")
                out_file = output_dir / out_name
                out_file.write_text(content, encoding="utf-8")
                extracted.append(out_file)

    return extracted


def generate_syntax_completion_markdown(data: Dict[str, Any]) -> str:
    """Generate STUDIO_SYNTAX_COMPLETION.md from extracted dictionaries."""
    lines = [
        "# Infor LN Studio Syntax & Code Completion Reference",
        "",
        "> Extracted from Infor LN Studio 10.8 Build 0640 (`lnstudio_commonui.jar` & `common.core_*.jar`).",
        "",
        "## 1. 4GL Keywords (80)",
        "",
        ", ".join(f"`{k}`" for k in sorted(data.get("keywords", []))),
        "",
        "## 2. Embedded SQL Keywords (92)",
        "",
        ", ".join(f"`{k}`" for k in sorted(data.get("sql_keywords", []))),
        "",
        "## 3. Program Sections",
        "",
    ]
    for s in data.get("program_sections", []):
        lines.append(f"- `{s}`")
    lines.append("")

    lines.append("## 4. Subsections")
    lines.append("")
    for s in sorted(data.get("sub_sections", [])):
        lines.append(f"- `{s}`")
    lines.append("")

    lines.append("## 5. Choice Sections")
    lines.append("")
    for s in sorted(data.get("choice_sections", [])):
        lines.append(f"- `{s}`")
    lines.append("")

    lines.append("## 6. Report Sections")
    lines.append("")
    for s in data.get("report_sections", []):
        lines.append(f"- `{s}`")
    lines.append("")

    lines.append("## 7. Predefined Variables (176)")
    lines.append("")
    lines.append(", ".join(f"`{v}`" for v in sorted(data.get("predefined_variables", []))))
    lines.append("")

    lines.append("## 8. Standard Defines (49)")
    lines.append("")
    lines.append(", ".join(f"`{d}`" for d in sorted(data.get("standard_defines", []))))
    lines.append("")

    lines.append("## 9. DAL Object Hooks (15)")
    lines.append("")
    for h in data.get("dal_object_hooks", []):
        lines.append(f"- `{h}`")
    lines.append("")

    lines.append("## 10. DAL Field Hook Suffixes (10)")
    lines.append("")
    lines.append("| Suffix | Return Value | Arguments | Default Body |")
    lines.append("|---|---|---|---|")
    for hook in data.get("dal_field_hook_suffixes", []):
        suffix = hook.get("suffix", "")
        ret = hook.get("returnValue", "")
        args = hook.get("arguments", "")
        body = hook.get("body", "")
        lines.append(f"| `{suffix}` | `{ret}` | `{args}` | `{body}` |")
    lines.append("")

    lines.append("## 11. Official 4GL Templates (12)")
    lines.append("")
    for tpl in data.get("templates", []):
        lines.append(f"### {tpl.get('name')} (`{tpl.get('id')}`)")
        lines.append(f"*{tpl.get('description')}*")
        lines.append("```baan")
        lines.append(tpl.get("pattern", ""))
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def generate_enriched_function_index(functions_db: Dict[str, Any], skill_path: Path) -> str:
    """Generate enriched FUNCTION_INDEX.md with Cloud Governance badges and single-line format."""
    guide_dir = skill_path / "references" / "guide" / "progguide"

    # 1. Map all functions into groups
    groups: Dict[str, List[str]] = {}

    for name in sorted(functions_db.keys(), key=lambda s: s.lower()):
        f = functions_db[name]
        hid = f.get("help_id", "").strip("/").split("/")
        grp = "general"
        if len(hid) >= 2:
            g = hid[1]
            if g.startswith("functions_"):
                g = g[len("functions_"):]
            grp = g

        badges: List[str] = []
        badges.append("[Cloud: Trusted]" if f.get("trusted") else "[Cloud: Untrusted]")
        if f.get("deprecated"):
            badges.append("[Deprecated]")
        if f.get("script_type"):
            badges.append(f"[Scope: {f.get('script_type')}]")
        if f.get("include"):
            badges.append(f"[Inc: <{f.get('include')}>]")

        badge_str = " ".join(badges)
        syntax = " ".join(f.get("syntax", "").split())
        doc = f.get("doc_path") or f"index/functions_db.json#{name}"

        # Clean single-line entry
        entry = f"- **{name}** | {badge_str} | `{syntax}` -> `{doc}`"
        groups.setdefault(grp, []).append(entry)

        # If there are overloads, list variants
        if "overloads" in f:
            for idx, ov in enumerate(f["overloads"]):
                if ov.get("syntax") != f.get("syntax") or ov.get("doc_path") != f.get("doc_path"):
                    ov_sig = " ".join(ov.get("syntax", "").split())
                    ov_doc = ov.get("doc_path") or f"index/functions_db.json#{name}"
                    ov_entry = f"- **{name}** (variant {idx+1}) | {badge_str} | `{ov_sig}` -> `{ov_doc}`"
                    groups.setdefault(grp, []).append(ov_entry)

    # 2. Also find overview/synopsis markdown files that are not functions
    function_docs = set()
    for f in functions_db.values():
        if f.get("doc_path"):
            function_docs.add(f.get("doc_path"))
        if "overloads" in f:
            for ov in f["overloads"]:
                if ov.get("doc_path"):
                    function_docs.add(ov.get("doc_path"))

    if guide_dir.exists():
        for md_file in sorted(guide_dir.rglob("*.md")):
            rel = md_file.relative_to(skill_path).as_posix()
            if rel not in function_docs:
                p_name = md_file.parent.name
                if p_name.startswith("functions_"):
                    p_name = p_name[len("functions_"):]
                entry = f"- **{md_file.stem}**  -> `{rel}`"
                groups.setdefault(p_name, []).append(entry)

    # 3. Assemble document
    total_funcs = len(functions_db)
    lines = [
        "# Baan/LN 4GL Function Index",
        "",
        f"{total_funcs} authoritative bshell functions (Infor LN Studio build 0640). Grep this file, then Read the referenced .md file.",
        "",
        "> Format: `- **<name>** | [Cloud: <Trusted|Untrusted>] [Deprecated] [Scope: <type>] [Inc: <<header>>] | <syntax> -> <doc_link>`",
        "",
    ]

    for grp in sorted(groups.keys(), key=lambda s: s.lower()):
        lines.append(f"## {grp}")
        lines.append("")
        for item in sorted(groups[grp], key=lambda s: s.lower()):
            lines.append(item)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract LN Studio build 0640 knowledge into erp-ln-progguide.")
    parser.add_argument("--studio-path", default=str(DEFAULT_STUDIO_PATH), help="Path to LN Studio root")
    parser.add_argument("--skill-path", default="erp-ln-progguide", help="Path to erp-ln-progguide skill root")
    parser.add_argument("--skip-java", action="store_true", help="Skip Java reflection and use existing extracted json")
    args = parser.parse_args()

    studio_path = find_studio_path(args.studio_path)
    skill_path = Path(args.skill_path)

    print(f"=== LN Studio Knowledge Extraction Pipeline ===")
    print(f"Studio Root: {studio_path}")
    print(f"Skill Root : {skill_path}")

    # 1. Parse functionlist.xml -> functions_db.json
    print("\n[1/3] Parsing functionlist.xml (2,274 bshell functions)...")
    functions_db = parse_functionlist_xml(studio_path, skill_path)
    idx_dir = skill_path / "index"
    idx_dir.mkdir(parents=True, exist_ok=True)
    db_file = idx_dir / "functions_db.json"
    db_file.write_text(json.dumps(functions_db, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    print(f"-> Generated {db_file} ({len(functions_db)} functions)")

    # 2. Extract Syntax & Completion Dictionaries
    print("\n[2/3] Extracting editor dictionaries & code templates...")
    if args.skip_java:
        existing_json = skill_path / "references" / "studio_syntax_completion.json"
        if not existing_json.exists():
            existing_json = Path("ln_studio_skill/references/studio_syntax_completion.json")
        data = json.loads(existing_json.read_text(encoding="utf-8"))
    else:
        try:
            data = extract_editor_dictionaries_java(studio_path)
        except Exception as e:
            print(f"Warning: Java reflection failed: {e}. Falling back to baseline json.")
            existing_json = Path("ln_studio_skill/references/studio_syntax_completion.json")
            data = json.loads(existing_json.read_text(encoding="utf-8"))

    # Also extract 12 UI templates
    ui_templates = extract_ui_code_templates(studio_path)
    if ui_templates:
        data["templates"] = ui_templates

    ref_dir = skill_path / "references"
    ref_dir.mkdir(parents=True, exist_ok=True)
    dict_json = ref_dir / "studio_syntax_completion.json"
    dict_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"-> Generated {dict_json}")

    dict_md = ref_dir / "STUDIO_SYNTAX_COMPLETION.md"
    dict_md.write_text(generate_syntax_completion_markdown(data), encoding="utf-8")
    print(f"-> Generated {dict_md}")

    # 3. Extract ScriptTemplates from common.core jar
    print("\n[3/3] Extracting official script templates...")
    tpl_dir = skill_path / "templates"
    extracted_tpls = extract_official_script_templates(studio_path, tpl_dir)
    print(f"-> Extracted {len(extracted_tpls)} templates to {tpl_dir}:")
    for tpl in extracted_tpls:
        print(f"   - {tpl.name}")

    # 4. Generate Enriched FUNCTION_INDEX.md
    print("\n[4/4] Generating enriched FUNCTION_INDEX.md with Cloud Governance badges...")
    func_index_md = generate_enriched_function_index(functions_db, skill_path)
    func_index_file = ref_dir / "FUNCTION_INDEX.md"
    func_index_file.write_text(func_index_md, encoding="utf-8")
    print(f"-> Generated {func_index_file}")

    print("\nExtraction successfully completed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
