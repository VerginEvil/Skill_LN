# choice.report()

## Syntax:
`function long choice.report( ref string reportname(15) )`

## Description
This returns the name of a report from the session data in the data dictionary. The report is taken from the group defined in the predefined variable *reportgrp* (default = 1). If there is more than one report in the group, the user is presented with a menu from which to select the required report.
The returned name consists of 15 characters, starting with an “r”. The language code is not included in the name. If you call [brp.open()](brp.open.md) with the report name returned by this function, the report is opened with the user language. If you call [brp.open.language()](brp.open.language.md) with the report name returned by this function, the report is opened with the specified language.

## Arguments
| | | |
|---|---|---|
| `ref string` | `reportname(15)` |    |

## Return values
> 0 sequence number of report in the group
-1 report not found, or no report selected by user

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  The [4GL engine](../glossary/glossary.md#fourgl_engine) calls *choice.report()* immediately before execution of the *on.choice* subsection of a *choice.print.data* section. By default a report from report group 1 is retrieved. To retrieve a report from a different group, you can assign any group to the predefined variable *reportgrp* in the *before.choice* subsection of the *choice.print.data* section.

## Example 1
```

choice.print.data:
on.choice:
| choice.report()is always called by the 4GL engine
      brp_id = brp.open( reportname, "", 1 )
           | report from default group 1
```

## Example 2
```

choice.print.data:
before.choice:
     reportgrp = 2
on.choice:
     brp_id = brp.open( reportname, "", 1 ) | report from group 2
```

## Example 3
```

function choice.and.open.report()
{
        if choice.report( repname ) <= 0 then
                return
        endif
        lfn.report = brp.open( repname, dep.device, 1 )
}
```

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)

- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
