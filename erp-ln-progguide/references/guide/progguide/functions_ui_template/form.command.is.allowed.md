# form.command.is.allowed()

## Syntax:
`#include <bic_4gl2>`
`function extern boolean form.command.is.allowed( )`

## Description
You can use this hook to define the conditions under which the form command should become enabled in the UI. The [4GL engine](../glossary/glossary.md#fourgl_engine) will use this hooks to determine whether the form command must be enabled or disabled.

## Return values
The hook should return TRUE in case the form command is allowed. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will enable the form command on the UI. In any other case the hook should return FALSE.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## When called
Form commands are handled based on the Command Availability setting in the Form Commands session (ttadv3118s000):

- *Command Availability Always*

- The disabling of these form commands may depend on the values of the view fields. Therefore, these form commands are handled only when the session has view fields (form type 3). This applies to both overview and details sessions. The [4GL engine](../glossary/glossary.md#fourgl_engine) handles these commands just before the *read.view* sub-event of the *main.table.io* event section is executed.

- *Command Availability One Record Selected and Records Selected*

- In overview sessions these form commands are handled when one or more records are marked. The [4GL engine](../glossary/glossary.md#fourgl_engine) handles these commands just before the *after.choice* sub-event of the *choice.mark.occur* event section is executed.In details sessions these commands are handled when the occurrence is being displayed again. This is just before the *before.display.object* event section is executed.

- *Command Availability Never*

- These commands are never handled.

See [standard.command.is.allowed()](standard.command.is.allowed.md) for more information regarding the event sections, and the type of commands that are handled when these events are executed.
The form.command.is.allowed hook can also be used in print/processing sessions in case they have a main table. The form command availability must be set to One Record Selected or Records Selected.

- The [4GL engine](../glossary/glossary.md#fourgl_engine) will also use the DAL [business.method.is.allowed()](../functions_dal/business.method.is.allowed.md) hook to determine whether the form commands must be enabled or disabled.

- First, the UI hook will be called. If this returns FALSE, the command will be disabled, if it returns TRUE (or if it does not exist), the DAL [business.method.is.allowed()](../functions_dal/business.method.is.allowed.md) hook will be called. If this returns FALSE, the command will be disabled, else it will be enabled.

- When multiple records are selected, the form.command.is.allowed is not executed, but the commands are just enabled/disabled based on the setting of the form command.

## Example
```

function extern boolean address.fmfoc200.sfad.is.allowed()
{
    if isspace(fmfoc200.sfad) then
        return(false)
    endif

    return(true)
}
```

## Related topics
- [UI Template](overview.md)

- [standard.command.is.allowed()](standard.command.is.allowed.md)
