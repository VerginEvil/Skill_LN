# field.is.readonly()

## Syntax:
`function boolean field.is.readonly (UI template)( )`

## Description
You can use this hook in your UI script to define the conditions under which the field should become readonly in the UI. The [4GL engine](../glossary/glossary.md#fourgl_engine) uses this hook to determine whether the field must be enabled or made readonly.

## Return values
The hook should return TRUE in case the field is readonly. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will make the field appear readonly on the UI. In any other case the hook should return FALSE (i.e. the field is not readonly).

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## When called
- At the time the [4GL engine](../glossary/glossary.md#fourgl_engine) determines whether fields need to be disabled cq. enabled: this is done just before calling the *before.display.object* and the *when.field.changes* sections

- In case the field is defined as a [DAL2 Field dependencies](../functions_dal/dal2_field_dependencies.md) of another field and that other field changes.

- Easy disabling for fields is only supported for maintable fields in combination with DAL2 field dependencies. It is not supported for non-maintable form fields, or when no DAL2 is present.

- The [4GL engine](../glossary/glossary.md#fourgl_engine) also uses the DAL field hooks in order to determine whether the field must be disabled:

- First, the UI hook is called, if this returns TRUE, the field is made readonly. If this returns FALSE (or if it does not exist) the DAL is called. If the DAL indicates that the field is not editable, the field is made readonly.

## Example
```

function extern boolean fmfoc200.foty.is.readonly()
{
    if manual.order(fmfoc200.orno) then
        return(false)
    endif

    return(true)
}
```

## Related topics
- [UI Template](overview.md)

- [DAL2 Field dependencies](../functions_dal/dal2_field_dependencies.md)
