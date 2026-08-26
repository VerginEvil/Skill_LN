# Expressions and operators
An expression is a combination of variables, constants, and operators, built up in accordance with certain rules. There are two main kinds of operators: unary and binary. All operators, except the negation operators, are binary. Expressions with unary operators have the general form:
```

operator operand
```
Expressions with binary operators have the following form, where each operand can be another expression, variable, or constant:
```

operand operator operand
```
The available operators can be divided into four categories: arithmetic, relational, logical, and control operators.
| | | |
|---|---|---|
| Class | Operator | Description |
| Arithmetic |  - * / + - \ &  |  negation multiply/divide/add/subtract remainder after division string concatenation  |
| Relational |  = or EQ <> or NE > or GT < or LT >= or GE <= or LE  |  is equal to is not equal to is greater than is less than is equal to or greater than is equal to or less than  |
| Logical | AND, OR, NOT | logical 'and', 'or' and negation |
| Control | ? : | question mark expression |
The question mark expression is a special type of expression. The syntax is:
If the condition is TRUE, expr_1 is executed. If the condition is FALSE, expr_2 is executed. For example:
```

<condition> ? <expr_1> : <expr_2>
```
If the condition is TRUE, expr_1 is executed. If the condition is FALSE, expr_2 is executed. For example:
```

lng_1 = (a >= b) ? a : b
        | if condition a >= b is TRUE lng_1 gets the value of a,
        | else lng_1 gets the value of b.
```
If boolean variabele bl is TRUE, expr_1 is executed. If bl is FALSE, expr_2 is executed. For example:
```

bl ? <expr_1> : <expr_2>
```
For further information on the different operator types, see the following sections:
- [Arithmetic operators](arithmetic_operators.md)
- [Relational operators](relational_operators.md)
- [Logical operators](logical_operators.md)
- [Operator precedence](operator_precedence.md)
- [Assignment Operator](assignment_operator.md)

## Related topics
- [3GL programming language features: overview](overview.md)
