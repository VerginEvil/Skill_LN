# dbcm.select.object.instance()

## Syntax:
`function long dbcm.select.object.instance( const string toid$ )`

## Description
Selects the specified Object instance and also its Object Type.
When a particular Object instance is selected, only that particular checked-out object is taken into account when the database is accessed. Other checked-out instances of the same Object Type or checked-out instances of other Object Types are not taken into account.
Important Note  The Object instance and its Object Type override any earlier selected instance and type. They remain in effect until the end of the current 3GL function. After return from the current 3GL function, the instance and type selection are set back to the values that they had in the calling 3GL function. When the program jumps back to a [retry point](../functions_database_handling/retry_points.md), the instance and type selection are set back to the values that they had at the moment that the retry point was set.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id, which identifies a specific checked-out business object.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example code
The example below shows that the scope of the selected object instance is limited to the function in which `dbcm.select.object.instance()` is called and any child functions. (Note that this can be done in a stacked way.) In case a function has selected an object instance, then on return from the function, the previous selected object instance becomes the current one again.
In this way there is no need for the application to reset the selected object instance before returning from a function.
```

domain tttoid toid$

function main()
{
	toid$ = dbcm.get.object.id$()
	| toid$ = "" (no object instance has been selected yet)

	| select object instance "001   xxx"
	dbcm.select.object.instance("001    xxx")

	toid$ = dbcm.get.object.id$()
	| toid$ = "001    xxx"

	| now call some_function(), which will select object type "001    yyy"
	some_function()

	| show that the object type is "001    xxx" again
	toid$ = dbcm.get.object.id$()
	| toid$ = "001    xxx"
}

function some_function()
{
	toid$ = dbcm.get.object.id$()
	| toid$ = "001    xxx"

	| now select object type "001    yyy"
	dbcm.select.object.instance("001    yyy")

	toid$ = dbcm.get.object.id$()
	| toid$ = "001    yyy"
}
```

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
