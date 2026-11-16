# Integer constant
The integer constant specifies an integer value.

## Syntax
```

<integer constant>
    ::= [-]<digit>...
```

## Syntactical restrictions
The value of the integer constant must lie in the range [–2147483647..+2147483647].
Values outside this range are promoted to a [Real constant](real_constant.md).

## Semantics
The data type of an integer constant is *integer*, *date*, *timestamp*, *interval days* or *interval seconds*. The data type depends on the context in which the integer is used.
For example, in the following comparison the left value expression ( *hiredate*) is of type *date* and hence the integer constant is also of type *date*, because this is the only valid data type [comparable](comparable_datatypes.md) to data type *date*.
```

hiredate = 717337
```
As another example, in the following expression the *hiredate* is of type *date* and hence the integer constant is of type *interval days*, because this is the only valid data type that can be combined with data type *date* for the [Operator + (add)](ve_add.md).
```

hiredate + 1
```
This example shows that it is not always possible to derive the correct type for an integer constant. In the following expression the integer constant can be either of type *date* or of type *interval days*, because both types are valid for the [Operator - (subtract)](ve_subtract.md) when the left value expression is of type *date*.
```

hiredate - 1
```

## Examples
```

123
-47
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
