# bit.and(), bit.exor(), bit.in(), bit.inv(), bit.or()

## bit.and

## Syntax:
`function long bit.and( long pattern1, long pattern2 )`

## Description
Bitwise AND function

## Arguments
| | | |
|---|---|---|
| `long` | `pattern1` |    |
| `long` | `pattern2` |    |

## Return values
The function bit.and returns the bitwise AND of the supplied input values.
Each bit in the two’s complement representation of the result is set if and only if each of the corresponding bits in the two’s complement representation of the supplied input values is set.
Notice that the behavior of this function does not depend on the width of the used two’s complement representation.

## Context
This function is implemented in the porting set and can be used in all script types.

## bit.exor

## Syntax:
`function long bit.exor( long pattern1, long pattern2 )`

## Description
Bitwise exclusive OR function

## Arguments
| | | |
|---|---|---|
| `long` | `pattern1` |    |
| `long` | `pattern2` |    |

## Return values
The function bit.exor returns the bitwise exclusive OR of the supplied input values.
Each bit in the two’s complement representation of the result is set if and only if exactly one of the corresponding bits in the two’s complement representation of the supplied input values is set.
Notice that the behavior of this function does not depend on the width of the used two’s complement representation.

## Context
This function is implemented in the porting set and can be used in all script types.

## bit.in

## Syntax:
`function boolean bit.in( long pattern1, long pattern2 )`

## Description
Bitwise IN function

## Arguments
| | | |
|---|---|---|
| `long` | `pattern1` |    |
| `long` | `pattern2` |    |

## Return values
The function bit.in returns whether the bitset represented by the first input value is a subset of the bitset represented by the second input value.
Boolean value true is returned if and only if each bit in the two’s complement representation of the first input value is set only if also the corresponding bit in the two’s complement representation of the second input value is set; otherwise, boolean value false is returned, indicating that at least one bit in the two’s complement representation of the first input value is set while the corresponding bit in the two’s complement representation of the second input value is not set.
The function call `bit.in(pattern1, pattern2)` returns the same boolean value as the expression `bit.and(pattern1, bit.inv(pattern2)) = 0`
Notice that the behavior of this function does not depend on the width of the used two’s complement representation.

## Context
This function is implemented in the porting set and can be used in all script types.

## bit.or

## Syntax:
`function long bit.or( long pattern1, long pattern2 )`

## Description
Bitwise OR function

## Arguments
| | | |
|---|---|---|
| `long` | `pattern1` |    |
| `long` | `pattern2` |    |

## Return values
The function bit.or returns the bitwise OR of the supplied input values.
Each bit in the two’s complement representation of the result is set if and only if at least one of the corresponding bits in the two’s complement representation of the supplied input values is set.
Notice that the behavior of this function does not depend on the width of the used two’s complement representation.

## Context
This function is implemented in the porting set and can be used in all script types.

## bit.inv

## Syntax:
`function long bit.inv( long value )`

## Description
Bitwise inversion.

## Arguments
| | | |
|---|---|---|
| `long` | `value` |    |

## Return values
The function bit.inv returns the two’s complement inversion of the input value.
Each bit in the two’s complement representation of the result is set if and only if the corresponding bit in the two’s complement representation of the supplied input value is not set.
The sum of the input value and the return value will be -1 (two’s complement: all bits set).
A much simpler specification of this function might be: it returns -1 - value.
Notice that this function is its own inverse: bit.inv(bit.inv(value)) = -1 - (-1 - value) = value.
Notice that the behavior of this function does not depend on the width of the used two’s complement representation.

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  You can also use the mathematical operators +, -, and / for computing bit operations. The operands must be declared as variables of type SET. You can declare such a variable only with a domain declaration where the domain is of database type SET.

- The operator + equates to the function *bit.or()*.

- The operator * equates to the function *bit.and()*.

- The operator / equates to the function *bit.exor()*.

- The operator - equates to a special form of the function *bit.and()*. That is, `a-b` for sets equates to `bit.and(a, bit.inv(b))` for longs. If the SET variables are represented as longs, the following example explains the - operator: `0101 0110 ---- 0001`

- When using SET constants as operands, the keyword IN equates to the function *bit.in()*. The following example illustrates the use of bit operations on SET constants. Note that EMPTY is a keyword for the empty set; all bits are zero (set value 0).
```

    domain cf a,b        | domain declaration: cf, a, and b are of type SET
                         | see also the function cf$()
    a = empty            | clear a
    a = cf.dim           | set a to dim
    a = a + cf.reverse   | add/enable reverse
    a = a - cf.dim       | delete/disable dim
    a = a / cf.underline | toggle underline

    a in b
    if ( a in b ) then
         message( "All elements of a are in b" )
    endif
    if ( cf.reverse * a ) then
         message( "a contains reverse" )
    endif
    if ( a ) then
         message( "a contains at least one argument" )
    endif
    if ( a=empty ) then
         message( "a is an empty set" )
    endif
```
The following diagrams illustrate how set operations work (a and b are sets):

## Examples
The following examples illustrate how these functions work, using 5-bit two’s complement representation of integer values.
```
10xyz
```
```
11000
```
```
11001
```
```
11010
```
```
11011
```
```
11100
```
```
11101
```
```
11110
```
```
11111
```
```
00000
```
```
00001
```
```
00010
```
```
00011
```
```
00100
```
```
00101
```
```
00110
```
```
00111
```
```
01xyz
```
| | |
|---|---|
| integer value | 5-bit two’s complement representation |
| -16 … -9 |  |
| -8 |  |
| -7 |  |
| -6 |  |
| -5 |  |
| -4 |  |
| -3 |  |
| -2 |  |
| -1 |  |
| 0 |  |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 … 15 |  |
```

bit.and(5,-4) = 4
```
```

bit.exor(5,-4) = -7
```
```

bit.or(5,-4) = -3
```
```

00101
11100
-----
00100
```
```

00101
11100
-----
11001
```
```

00101
11100
-----
11101
```
```

bit.inv(6) = -7
```
```

bit.in(5,-4) = false
```
```

bit.in(4,-4) = true
```
```

00110
-----
11001
```
```

00101
11100
-----
11110
```
```

00100
11100
-----
11111
```

## Related topics
- [Bit operations: overview and synopsis](bit_operations_overview_and_synopsis.md)
