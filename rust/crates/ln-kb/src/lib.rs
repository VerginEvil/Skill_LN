pub mod doc_search;
pub mod functions;
pub mod syntax;
pub mod types;

pub use doc_search::{find_progguide_references_dir, search_docs, MAX_OUTPUT_CHARS};
pub use functions::{all_functions, lookup_function, search_functions};
pub use syntax::{
    choice_sections, dal_field_hook_suffixes, dal_object_hooks, keywords, other_keywords,
    predefined_variables, program_sections, report_sections, sql_keywords, standard_defines,
    sub_sections, templates,
};
pub use types::{DalFieldHookSuffix, DocHit, DocSearchResult, FunctionEntry, SyntaxTemplate};
