# dbcm.select.object.type()

## Syntax:
`function long dbcm.select.object.type( const string obj.type$ )`

## Description
Selects the specified Object Type. Also deselects any selected Object instance.
When a particular Object Type is selected, checked-out objects of that type are taken into account, when the database is accessed.
Important Notes  The empty Object instance and the specified Object Type override any earlier selected instance and type. They remain in effect until the end of the current 3GL function. After return from the current 3GL function, the instance and type selection are set back to the values that they had in the calling 3GL function. When the program jumps back to a [retry point](../functions_database_handling/retry_points.md), the instance and type selection are set back to the values that they had at the moment that the retry point was set.
Inproper use of this function can lead to data corruption.

## Arguments
| | | |
|---|---|---|
| `const string` | `obj.type$` |  An object type code as defined in the Object Configuration Management model. This is a string of max 6 characters.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Example code
The example below shows that the scope of the selected object type is limited to the function in which `dbcm.select.object.type()` is called and any child functions. (Note that this can be done in a stacked way.) In case a function has selected an object type, then on return from the function, the previous selected object type becomes the current one again.
In this way there is no need for the application to reset the selected object type before returning from a function.
```

string	obj.type$(6)

function main()
{
	obj.type$ = dbcm.get.object.type$()
	| obj.type$ = "" (no object type has been selected yet)

	| select object type "001"
	dbcm.select.object.type("001")

	obj.type$ = dbcm.get.object.type$()
	| obj.type$ = "001"

	| now call some_function(), which will select object type "002"
	some_function()

	| show that the object type is "001" again
	obj.type$ = dbcm.get.object.type$()
	| obj.type$ = "001"
}

function some_function()
{
	obj.type$ = dbcm.get.object.type$()
	| obj.type$ = "001"

	| now select object type "002"
	dbcm.select.object.type("002")

	obj.type$ = dbcm.get.object.type$()
	| obj.type$ = "002"
}
```

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
