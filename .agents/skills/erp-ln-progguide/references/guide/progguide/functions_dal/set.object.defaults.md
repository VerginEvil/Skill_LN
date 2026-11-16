# set.object.defaults()

## Syntax:
`function long set.object.defaults( )`

## Description
Use this hook to fill a new record with defaults.
Before this hook will be called a db.set.to.default() has been executed; therefore it is not necessary to assign values that are already present in the table definition.
This is hook is executed by OpenWorld through a BOI in case of a DAL_NEW or in case of a DAL2 DAL, when an insert is started.
Note: This hook only contains assignments.

## Return values
The hook returns 0 if the hook has been executed successfully.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Example
```

function extern long set.object.defaults()
{
    tisfc001.efdt = utc.num()       |* reference date
    tisfc001.prdt = utc.num()       |* production start date
    tisfc001.prcd = 999             |* priority

    return(0)
}
```
