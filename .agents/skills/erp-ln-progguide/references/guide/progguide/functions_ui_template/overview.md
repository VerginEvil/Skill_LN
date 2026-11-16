# UI Template

## Overview
The [4GL engine](../glossary/glossary.md#fourgl_engine) supports automatic disabling of fields and commands. Instead of using functions like [disable.fields()](../functions_form_and_form_field_operations/disable.fields.md) and [disable.fields()](../functions_form_and_form_field_operations/disable.fields.md), a set of so-called hooks can be used that describe under which conditions a field or command is enabled. The [4GL engine](../glossary/glossary.md#fourgl_engine) will call these hooks at the right moment and based on the outcome, the corresponding field or command will be disabled or enabled.
The following UI template topics are supported by the [4GL engine](../glossary/glossary.md#fourgl_engine):

- [field.is.readonly()](field.is.readonly.md)

- [standard.command.is.allowed()](standard.command.is.allowed.md)

- [form.command.is.allowed()](form.command.is.allowed.md)

Note  In order to enable automatic disabling of fields and commands, you must #include <bic_4gl2> in your UI script.

## Related topics
- [Extended DAL (DAL2)](../functions_dal/dal2_overview.md)
