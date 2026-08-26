# at.base()

## Syntax:
`function long at.base( <ref|const> <type> basic_value, [ long position, ... ], <ref|const> <type> based_variable, [ long length, ... ] )`

## Description
Use this function to base one variable (the *based_variable*) on another variable or value (the *basic_value*). The *based_variable* then uses the same memory area as the *basic_value*.

## Arguments
| | | |
|---|---|---|
| `<ref|const> <type>` | `basic_value` |  The array or string value on which the *based_variable* will be based. The *basic_value* must have the same type as the *based_variable*. If the *basic_value* is not suitable as a reference argument, then it is considered as a const argument and the *based_variable* must be declared as CONST.  |
| `[ long` | `position, ... ]` |  Optional additional *position* arguments, which specify the start position of the *based_variable* in the corresponding dimension of the *basic_value*. The default start position is 1.  |
| `<ref|const> <type>` | `based_variable` |  The variable which will be based on the *basic_value*. The *based_variable* must have the same type as the *basic_value*. The *based_variable* must be declared as BASED. If the *basic_value* is considered as a const argument, then the *based_variable* must be declared as CONST.  |
| `[ long` | `length, ... ]` |  Optional additional *length* arguments, which specify the length of the *based_variable* in the corresponding dimension. The length plus the start position must not exceed the length reserved for the *basic_value*. If you pass value -1 for a specific *length* argument, the *based_variable* uses the memory space of the *basic_value* from the specified start position to the end position. If you pass value 0 for a specific *length* argument, the *based_variable* uses the memory space of the *basic_value* from the specified start position for the declared length of the *based_variable*.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## See also
[at.base()](at.base2.md)
Notes  If the variables are multidimensional long or double arrays, only the first element can differ in the declarations. This is because the array values are stored column by column.
The *based_variable* starts using the same memory area as the *basic_value*. As soon as that memory area is no longer used for the representation of the *basic_value*, it is also no longer allowed to access it via the *based_variable*. This restricts the useful possibilities for the *basic_value* argument to variables and literal string values. All other possibilities for the *basic_value* argument use temporary memory, which becomes invalid after the call to the at.base function.
Do not reallocate *basic_variable* (with *alloc.mem()*). Doing this can cause serious problems, such as a core dump or corrupted memory.

## Example
In this example, the contents of the variable long_to_be_based(1, 1) are equal to the value of basic_long(4, 1). That is, a matrix of 2 by 5 longs.
```

long basic_long(5, 5)
long long_to_be_based(3, 5) based

at.base(basic_long, 4, 1, long_to_be_based, -1, 0)
```
Or:
```

at.base(basic_long, 4, 1, long_to_be_based, 2, 5)
```

## Related topics
- [Variables (based) overview and synopsis](overview_and_synopsis.md)
