# DAL2 Flow of field hooks

## Overview

## Flow for checking a field's value
```

dal.validate.field(long mode)
{
    if field is empty ("", 0, 0.0 or empty) then
        if not field.is.never.applicable() and field.is.applicable() then
            if mode = DAL_UPDATE and field.is.readonly() then
                return(DALHOOKERROR)
            endif
            if field.is.derived() then
                return(DALHOOKERROR)
            endif
            if field.is.mandatory() then
                return(DALHOOKERROR)
            endif
        endif
    else
        if field is enum field then
            if field value <> default value then
                if field.is.never.applicable() then
                    return(DALHOOKERROR)
                endif
                if not field.is.applicable() then
                    return(DALHOOKERROR)
                endif
            endif
            if mode = DAL_UPDATE and field.is.readonly() then
                return(DALHOOKERROR)
            endif
            if field.is.derived() then
                return(DALHOOKERROR)
            endif
            if not field.enum.is.applicable() then
                return(DALHOOKERROR)
            endif
            if not field.enum.is.never.applicable() then
                return(DALHOOKERROR)
            endif
        else
            if mode = DAL_UPDATE and field.is.readonly() then
                return(DALHOOKERROR)
            endif
            if field.is.derived() then
                return(DALHOOKERROR)
            endif
            if not field.is.valid() then
                return(DALHOOKERROR)
            endif
        endif
    endif
    | Field is valid
    return(0)
}
```
Note that the [field.is.derived()](field.is.derived.md) hook is only called in case:

- the DAL is not a SUBDAL ( `SUBDAL = false`)

- the DAL is running in the Data Input or Integration context (See [DAL Context](dal_context.md) for more info.

## Flow for updating the field's value
```

dal.update.field(long mode)
{
    if field.is.never.applicable() or not field.is.applicable() then
        make field empty
    else
        if mode = DAL_NEW or not field.is.readonly() then
            call field.update()
            call fieldname.make.valid()
        endif
    endif
}
```

## Flow for getting the field's UI state
```

dal.get.field.state(long mode)
{
    if not field.is.applicable() then
        return(DISABLED)
    else
        if (mode = DAL_UPDATE and field.is.readonly()) or field.is.derived() then
            return(READONLY)
        else
            return(ENABLED)
        endif
    endif
}
```

## Related topics
- [DAL2 Field hooks](dal2_field_hooks.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)
