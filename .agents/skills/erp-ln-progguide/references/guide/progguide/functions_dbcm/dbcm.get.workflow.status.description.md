# dbcm.get.workflow.status.description()

## Syntax:
`function long dbcm.get.workflow.status.description( const string tbl.name$, ref string wf.status.desc$, [ const string fld.name, void fld.value,... ] )`

## Description
Returns the workflow status description of an object instance for the given table in the current company based on a list of field/value pairs or the primary key field values of the current record buffer.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name$` |  A table code, like "tdsls400".  |
| `ref string` | `wf.status.desc$` |  the returned workflow status description like "Draft" or "Pending" or "Not Applicable" if dbcm is not active for the given table. In case of an error this will be an empty string.  |
| `[ const string` | `fld.name ]` |    |
| `[ void` | `fld.value ]` |    |
| `[` | `... ]` |  List of field/value pairs in the format "ppmmm999.ffff", value. In case of array elements specify the field as "ppmmm9999.ffff(element)". In case no list of field/value pairs is supplied, the fields of the primary index (index1) and their field values in the current record buffer are used.  |

## Return values
| | |
|---|---|
| 0 | In case of success, wf.status.desc$ contains the workflow status description. |
| -1 | Invalid number of arguments |
| -2 | Invalid table specified in tbl.name$ |
| -3 | tbl.name$ is not a root table of any object type |
| -4 | Cannot read Runtime DD of tbl.name$ |
| -5 | Cannot determine the object type for tbl.name$ |
| -6 | Cannot select the object type for tbl.name$ |
| -7 | Cannot construct a valid query to find the object instance |
| -8 | Cannot execute the query to find the object instance |
| -9 | Cannot find matching object instance |
| -10 | Multiple object instances found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Example code
The code below shows an example on how to retrieve the workflow status description for a report extension using `dbcm.get.workflow.status.description()`. In this example, field/value pairs are used to specify the object instance.
```

| ext.workflow.stat is a Calculated Field in a Report Extension.
function extern void ext.workflow.stat.calculate()
{
    domain  tcmcs.st70m     description

    if dbcm.get.workflow.status.description(
                                        "tfacp200",
                                        description,
                                        "tfacp200.ttyp", r.trans.type,
                                        "tfacp200.ninv", r.inv.number) = 0 then
        ext.workflow.stat = description
    else
        | Internal error, do not print workflow status
        ext.workflow.stat = ""
    endif
}
```

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
