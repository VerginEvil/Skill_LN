# CAST expression
With the CAST expression you can convert a value to a different data type or assign a type to a parameter.

## Syntax
```

<cast expression>
    ::= CAST ( Value expression AS <cast type> )
      | CAST ( Parameter AS <parameter cast type> )

<cast type>
    ::= INTEGER | DATE | TIMESTAMP | CHAR[( <string length> )] | VARCHAR( <string length> )

<string length>
	::= Integer constant

         <parameter cast type>
    ::= INTEGER | REAL | DATE | TIMESTAMP | STRING | RAW
```

## Syntactical restrictions
*I.* The *<value expression>* shall not be a *<parameter>*.
*II.* The value of *<string length>* shall be greater than 0.

## Syntactical restrictions
The value of *Parameter* is restricted to the name of a column. A syntax error will result when any other type of expression is used.

## Semantics
If the *<string length>* is omitted than a string length of 1 is implicit.
The cast of a *<value expression>* results in a value of type *<cast type>*. Only a limited set of casts is supported as shown in following table. A hyphen ('-') indicates that the combination is not allowed, where as '+' indicates a valid combination. (the left column is the data type of the *<value expression>*, the header row is the *<cast type>*)
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| CAST | I | R | S | D | T | ID | IS | Ra |
| I | - | - | + | - | - | - | - | - |
| R | - | - | - | - | - | - | - | - |
| S | + | - | - | - | - | - | - | - |
| D | - | - | - | - | + | - | - | - |
| T | - | - | - | + | - | - | - | - |
| ID | - | - | - | - | - | - | - | - |
| IS | - | - | - | - | - | - | - | - |
| Ra | - | - | - | - | - | - | - | - |
I=Integer R=Real S=String (Char or Varchar) D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw
Casting a date value to type timestamp, preserves the year to month part and adds the hour to minute part '00:00:00'. Casting a timestamp value to type date, preserves the year to month part but removes the hour to second part.
Casting an integer value to type string (char or varchar) results in the string representation of the integer value. If the target is too short, then the result is undefined. Casting a string value to type integer results in the integer representation of the string value. The string value must consist of an optional minus sign ('-') immediately followed by a consecutive sequence of digits only. The string may be enclosed by spaces. Otherwise the result is undefined.
The cast of a *<parameter>* assigns the type *<parameter cast type>* to the *<parameter>*. The cast expression itself will also be of type *<parameter cast type>*.

## Examples
The following CAST expression converts a timestamp value *startime* to a variable length string with maximum length 80.
```

CAST ( startime AS VARCHAR(80) )
```
The following CAST expression assigns the type *integer* to the parameter *param*.
```

CAST ( :param AS INTEGER )
```
The following CAST expression assigns the type *raw* to the parameter *param*.
```

CAST ( :param AS RAW )
```

## Resolving type conflicts on parameters
The cast operator is used to properly type parameters in case of ambiguities or in case of possible type conflicts.
In the following example, both *param1* and *param2* cannot be typed, because each type is comparable to itself.
```

:param1 = :param2
```
This problem can be resolved using the CAST expression.
```

:param1 = CAST( :param2 AS STRING )
```
In the following example the first comparison types *param* as *date*, while the second comparison types it as *real*.
```

:param = hiredate  or  :param = 0
```
Using the CAST expression this can be resolved.
```

:param = hiredate  or  CAST( :param AS DATE ) = 0
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
