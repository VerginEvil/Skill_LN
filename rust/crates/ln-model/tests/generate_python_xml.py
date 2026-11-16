import sys
import json
from pathlib import Path

# Add ln_studio_skill/tools to sys.path
repo_root = Path(__file__).resolve().parents[4]
tools_dir = repo_root / "ln_studio_skill" / "tools"
sys.path.insert(0, str(tools_dir))

from generate_ln_table import generate_table_xml, generate_label_xml, generate_domain_xml
from generate_ln_session import generate_session_xml
from generate_ln_library import generate_library_xml
from generate_ln_menu import generate_menu_xml
from generate_ln_message import generate_message_xml
from generate_ln_question import generate_question_xml
from generate_ln_function import generate_function_xml
from generate_ln_additional import generate_additional_xml
from generate_ln_report import generate_report_xml

def main():
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        raw = sys.argv[1]
    else:
        raw = sys.stdin.read()

    req = json.loads(raw)
    ctype = req.get("type")
    spec = req.get("spec", {})
    app = req.get("app", "EXTce01107")
    ver = req.get("ver", "B61O_a_ext")

    if ctype == "table":
        xml = generate_table_xml(spec, application=app)
    elif ctype == "label":
        name = spec["name"]
        desc = spec.get("description", name)
        length = spec.get("length")
        xml = generate_label_xml(name, desc, version_id=ver, application=app, length=length)
    elif ctype == "domain":
        xml = generate_domain_xml(spec, version_id=ver, application=app)
    elif ctype == "session":
        t_spec = req.get("table_spec")
        ui_script = spec.get("script")
        xml = generate_session_xml(spec, table_spec=t_spec, application=app, ui_script_code=ui_script)
    elif ctype == "library":
        script = spec.get("script")
        xml = generate_library_xml(spec, application=app, script_override=script)
    elif ctype == "menu":
        xml = generate_menu_xml(spec, application=app)
    elif ctype == "message":
        xml = generate_message_xml(spec, application=app)
    elif ctype == "question":
        xml = generate_question_xml(spec, application=app)
    elif ctype == "function":
        xml = generate_function_xml(spec, application=app)
    elif ctype == "additional":
        xml = generate_additional_xml(spec, application=app)
    elif ctype == "report":
        xml = generate_report_xml(spec, application=app)
    else:
        raise ValueError(f"Unknown component type '{ctype}'")

    sys.stdout.write(xml)

if __name__ == "__main__":
    main()
