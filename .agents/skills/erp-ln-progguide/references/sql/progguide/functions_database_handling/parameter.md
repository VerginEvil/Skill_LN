# Parameter
The parameter specifies a value that can vary from execution to execution.

## Syntax
```

<parameter>
    ::= ?
      | :<digit>...
      | :<identifier>
```

## Semantics
The type of a parameter is any of the available SQL data types. The context in which the parameter is used determines the actual data type.
For example, in the following comparison the left value expression ( *hiredate*) is of type *date* and hence the parameter is also of type *date*, because this is the only valid data type [comparable](comparable_datatypes.md) to data type *date*.
```

hiredate = :1
```
As another example, in the following expression both parameters must be of type *string* or of type *raw*, because these are the only valid types for the [Operator & (string concatenation)](ve_concat.md).
```

:1 & :2
```
As another example, in the following expression both parameters must be of type *raw*, because this is the only valid type for the [Operator & (string concatenation)](ve_concat.md) given that the right hand side of the comparison is of type *raw*.
```

:1 & :2 = x'ABCD'
```
This example shows that it is not always possible to derive the correct type for a parameter. In the following expression the parameters can be of any SQL type, because each type is comparable with itself.
```

:1 = :2
```

## Examples
```

?
:1
:my.long
:my.string$
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
