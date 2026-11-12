pub mod datatypes;
pub mod dom_surgery;
pub mod generators;
pub mod inspector;
pub mod path_resolver;
pub mod schema;
pub mod validator;
pub mod yaml_compiler;

pub use datatypes::{is_line_number_column, NativeDatatype};
pub use dom_surgery::{
    clone_component_xml, escape_4gl_to_xml, extract_script, find_standalone_script_file,
    inject_script, pre_put_merge_and_guard, unescape_xml_to_4gl, DomSurgeryError,
    PrePutGuardError,
};
pub use generators::*;
pub use inspector::{
    current_iso_timestamp, default_unmapped_log_path, inspect_unknown_nodes,
    inspect_unknown_nodes_with_log_path, InspectorError, UnmappedPacket,
};
pub use path_resolver::*;
pub use schema::{
    get_owtemplate, get_script_template, get_tde_schema, get_templates_catalog,
    lookup_class, lookup_root_component, ClassMeta, FieldMeta, OwTemplate,
    RootComponentInfo, ScriptTemplate, TdeSchema, TemplatesCatalog,
};
pub use validator::{
    validate_activity, ActivityValidator, ValidationDiagnostic, ValidationReport,
    ValidationSeverity, MANAGED_EXTENSIONS, VALID_DATATYPES,
};
pub use yaml_compiler::{
    compile_schema_to_tde, CompileError, CompileResult, DeclarativeSchema, GeneratedFile,
};
