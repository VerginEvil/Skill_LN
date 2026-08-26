# Set function specification
The set function specification applies a function to an argument.

## Syntax
```

<set function specification>
    ::= COUNT(*)
      | <set function type> ( Value expression )

<set function type>
    ::= MIN | MAX | SUM | COUNT | AVG
```

## Syntactical restrictions
The *<value expression>* shall not contain an outer column reference, a [subquery](sub_query.md) or a *<set function specification>*.

## Semantics
The following table shows the data types that are allowed for each set function specification and the resulting data type. A hyphen ('-') indicates that the combination is not allowed.
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
|  | I | R | S | D | T | ID | IS | Ra |
| MIN | I | R | S | D | T | ID | IS | Ra |
| MAX | I | R | S | D | T | ID | IS | Ra |
| AVG | R | R | - | - | - | - | - | - |
| SUM | I | R | - | - | - | ID | IS | - |
| COUNT | I | I | I | I | I | I | I | I |
I=Integer R=Real S=String D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw
A set function specification applies a function to a group of values. Usually, the group of values is defined by using the [GROUP BY clause](group_by.md). The MIN function calculates the minimum value of the values. The MAX function calculates the maximum value of the values. The SUM function calculates the sum of the values. The AVG function calculates the average of the values. The COUNT function counts the number of values.
All functions, except COUNT, ignore NULL values. It may be the case that what remains is an empty set. All functions, except COUNT, give NULL as a result when applied to an empty set. The COUNT function gives 0 as a result on an empty set.

## Examples
*Example 1*: The following set function specification calculates the average of the salaries of all employees with the same education level.
```

SELECT edlevel, AVG( salary )
FROM dbtst120
GROUP BY edlevel
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
