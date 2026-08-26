# at.base()

## Syntax:
`function long at.base( long process_id, string basic_variable_name, void unused, [ long position, ... ], <ref|const> <type> based_variable, [ long length, ... ] )`

## Description
Use this function to base one variable (the *based_variable*) on an external variable in another process (the *basic_variable*). The two variables then use the same memory area.

## Arguments
| | | |
|---|---|---|
| `long` | `process_id` |  The ID of the process in which the *basic_variable*) is declared. This process must be started before the current process and must be ended after the current process.  |
| `string` | `basic_variable_name` |  The name of the external *basic_variable* on which the *based_variable* is to be based. The *basic_variable* must be declared as EXTERN. The *basic_variable* must have the same type as the *based_variable*. If the *basic_variable* is declared as CONST, then the *based_variable* must also be declared as CONST.  |
| `void` | `unused` |  This argument is unused. The [bic compiler](../3gl_features/compiler.md) generates a warning about this argument, but the warning is suppressed by default. Use compiler option -W8 to switch it on.  |
| `[ long` | `position, ... ]` |  Optional additional *position* arguments, which specify the start position of the *based_variable* in the corresponding dimension of the *basic_variable*. The default start position is 1.  |
| `<ref|const> <type>` | `based_variable` |  The variable which will be based on the *basic_variable*. The *based_variable* must have the same type as the *basic_variable*. The *based_variable* must be declared as BASED. If the *basic_variable* is declared as CONST, then the *based_variable* must also be declared as CONST.  |
| `[ long` | `length, ... ]` |  Optional additional *length* arguments, which specify the length of the *based_variable* in the corresponding dimension. The length plus the start position must not exceed the length reserved for the *basic_variable*. If you pass value -1 for a specific *length* argument, the *based_variable* uses the memory space of the *basic_variable* from the specified start position to the end position. If you pass value 0 for a specific *length* argument, the *based_variable* uses the memory space of the *basic_variable* from the specified start position for the declared length of the *based_variable*.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## See also
[at.base()](at.base1.md)
Notes  If the variables are multidimensional long or double arrays, only the first element can differ in the declarations. This is because the array values are stored column by column.
If the process specified by *process_id* ends before the current process, the based variable can no longer be used. This is because the memory area allocated to the basic variable is freed. This can cause serious problems, such as a core dump or corrupted memory.

## Example
Process 1
```

EXTERN string base_string(20,2,2)
```
Process 2
```

string string_to_be_based(20,2) based
long proc_id1

proc_id1 = activate("session_name_of_process1")
at.base( proc_id1, "base_string", 1, 1, string_to_be_based, -1, -1 )
```

## Related topics
- [Variables (based) overview and synopsis](overview_and_synopsis.md)
