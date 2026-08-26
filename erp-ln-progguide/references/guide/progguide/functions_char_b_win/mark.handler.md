# mark.handler()

## Syntax:
`function long mark.handler( ref long mark.table() )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This enables a user to mark one or more records on an ASCII form. On return, the *mark.table* argument indicates which records are marked. Each element in the *mark.table* array corresponds to a record on the form. If an array element is set to 1, the corresponding record is marked. If it set to 0, the corresponding array element is not marked.
The predefined variables *marked* and *mark.status* are not affected by this function.

## Arguments
| | | |
|---|---|---|
| `ref long` | `mark.table()` |  |

## Return values
0 no records marked
1 one or more records marked

## Context
This function is implemented in the porting set and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

| if records 3 and 8 are marked, the following is true
| mark.table(3) = 1
| mark.table(8) = 1
| other elements are 0 (false)

for i=1 to filled.occ
                if mark.table(i) then
                                do.occ(i, some_function)
                endif
endfor
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
- [mark.occ()](../functions_form_and_form_field_operations/mark.occ.md)
