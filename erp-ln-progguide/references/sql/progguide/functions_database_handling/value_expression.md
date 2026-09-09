# Value expression
The value expression defines a value.

## Syntax
```

<value expression>
    ::= <value expression> + <value expression>
      | <value expression> - <value expression>
      | <value expression> * <value expression>
      | <value expression> / <value expression>
      | <value expression> \ <value expression>
      | <value expression> || <value expression>
      | ( <value expression> )
      | <scalar subquery>
      | <set function specification>
      | <substring and array indexing>
      | <searched case expression>
      | <simple case expression>
      | <cast expression>
      | <trim function>
      | <ml_one_lang function>
      | <enum description function>
      | <text content function>
      | <substring function>
      | <coalesce>
      | <extract expression>
      | <upper lower function>
      | <column reference>
      | <parameter>
      | <integer constant>
      | <real constant>
      | <string constant>
      | <raw constant>
      | <date constant>
      | <timestamp constant>
      | <interval constant>
      | <enumerate constant>
      | <empty constant>
      | <current date>
      | <current timestamp>
```

## Syntactical restrictions
*I.* The *<**column reference**>* shall not reference an array column and its *column name* shall not be the identifier `"company_nr"`.
*II.* The [degree](sql_glossary.md#Degree) and [cardinality](sql_glossary.md#Cardinality) of the *<**scalar subquery**>* both shall be 1.

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
