use crate::functions::{
    SYNTAX_CHOICE_SECTIONS, SYNTAX_DAL_FIELD_HOOK_SUFFIXES, SYNTAX_DAL_OBJECT_HOOKS,
    SYNTAX_KEYWORDS, SYNTAX_OTHER_KEYWORDS, SYNTAX_PREDEFINED_VARIABLES,
    SYNTAX_PROGRAM_SECTIONS, SYNTAX_REPORT_SECTIONS, SYNTAX_SQL_KEYWORDS,
    SYNTAX_STANDARD_DEFINES, SYNTAX_SUB_SECTIONS, SYNTAX_TEMPLATES,
};
use crate::types::{DalFieldHookSuffix, SyntaxTemplate};

pub fn keywords() -> &'static [&'static str] {
    SYNTAX_KEYWORDS
}

pub fn sql_keywords() -> &'static [&'static str] {
    SYNTAX_SQL_KEYWORDS
}

pub fn program_sections() -> &'static [&'static str] {
    SYNTAX_PROGRAM_SECTIONS
}

pub fn sub_sections() -> &'static [&'static str] {
    SYNTAX_SUB_SECTIONS
}

pub fn choice_sections() -> &'static [&'static str] {
    SYNTAX_CHOICE_SECTIONS
}

pub fn report_sections() -> &'static [&'static str] {
    SYNTAX_REPORT_SECTIONS
}

pub fn predefined_variables() -> &'static [&'static str] {
    SYNTAX_PREDEFINED_VARIABLES
}

pub fn standard_defines() -> &'static [&'static str] {
    SYNTAX_STANDARD_DEFINES
}

pub fn other_keywords() -> &'static [&'static str] {
    SYNTAX_OTHER_KEYWORDS
}

pub fn dal_object_hooks() -> &'static [&'static str] {
    SYNTAX_DAL_OBJECT_HOOKS
}

pub fn dal_field_hook_suffixes() -> &'static [DalFieldHookSuffix] {
    SYNTAX_DAL_FIELD_HOOK_SUFFIXES
}

pub fn templates() -> &'static [SyntaxTemplate] {
    SYNTAX_TEMPLATES
}
