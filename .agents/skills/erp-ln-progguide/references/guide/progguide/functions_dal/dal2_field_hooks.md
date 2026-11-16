# DAL2 Field hooks
In the DAL2 concept the property check hook is replaced by a number of field hooks.
DAL2 introduces the following field hooks for field validation:

- [field.is.never.applicable()](field.is.never.applicable.md)

- [field.is.applicable()](field.is.applicable.md)

- [field.is.readonly()](field.is.readonly.md)

- [field.is.derived()](field.is.derived.md)

- [field.is.mandatory()](field.is.mandatory.md)

- [field.is.valid()](field.is.valid.md) (For non-enum fields)

- [field.enum.is.applicable()](field.enum.is.applicable.md) (For enum fields - one hook for each enum value)

- [field.enum.is.never.applicable()](field.enum.is.never.applicable.md) (For enum fields - one hook for each enum value)

A number of these hooks is used by the [4GL engine](../glossary/glossary.md#fourgl_engine) to perform automatic disabling/enabling of maintable fields. E.g. if a field is found to be readonly, that field is disabled in the UI.
DAL2 also supports updating values of other fields after a field change. See [DAL2 Field dependencies](dal2_field_dependencies.md). This allows the DAL to be used to update dependent fields. As a result the UI script's *when.field.changes* event section does not have to be used anymore for maintable fields.
The following hook supports this:

- [field.update()](field.update.md)

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
