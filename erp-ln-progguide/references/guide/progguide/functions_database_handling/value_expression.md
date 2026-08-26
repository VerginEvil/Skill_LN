# Value expression
The value expression defines a value.

## Syntax
```

<value expression>
       ::= Operator + (add)
         | Operator - (subtract)
         | Operator * (multiply)
         | Operator / (divide)
         | Operator \ (modulo)
         | Operator & (concatenation)
         | ( <value expression> )
         | Sub query
         | Set function specification
         | Substring and array indexing
         | CASE expression (searched)
         | CASE expression (simple)
         | CAST expression
         | TRIM function
         | ml_one_lang function
         | ENUM_DESCRIPTION function
         | TEXT_CONTENT function
         | Column reference
         | Parameter
         | Integer constant
         | Real constant
         | String constant
         | Raw constant
         | Date constant
         | Timestamp constant
         | Enumerate constant
         | EMPTY constant
         | CURRENT_DATE
         | CURRENT_TIMESTAMP
```

## Syntactical restrictions
*I.* The *<column reference>* shall not reference an array column and its *column name* shall not identify an index name (e.g. _index1), a combined column name (e.g. cmba) or be the identifier `_compnr`.
*II.* The degree and cardinality of the *<scalar subquery>* both shall be 1.

## Examples
The following expression specifies the string 'City'.
```

'City'
```
The following expression adds the integer constants 3 and 4.
```

3 + 4
```
The following expression takes the substring of the string 'Big city' starting at position 6 and with length 2. The result is the string 'it'.
```

'Big city'(6;2)
```
The following expression takes the first phone number of an employee. The column dbtst120.phoneno is an array column consisting of three strings.
```

dbtst120.phoneno(1)
```
The following expression multiplies the maximum of the salaries of all employees with a factor 1.3.
```

1.3 * ( select max(salary) from dbtst120 )
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
