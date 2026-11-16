# Expressions and operators
An expression is a combination of variables, constants, and operators, built up in accordance with certain rules.
The available operators can be divided into four categories: arithmetic, relational, logical, and conditional operators.
| | | |
|---|---|---|
| Class | Operator | Description |
| Arithmetic | - * / \ + - & | negation multiplication, division, remainder after division addition, subtraction string concatenation |
| Relational | = or EQ <> or NE < or LT <= or LE > or GT >= or GE | is equal to is not equal to (differs from) is less than is less than or equal to (is at most) is greater than is greater than or equal to (is at least) |
| Logical | AND, OR, NOT | logical and, logical or, logical negation |
| Conditional | ?: | if-then-else |
Most operators are binary operators. The negation operators are unary operators. The if-then-else operator is a ternary operator.
Expressions with unary operators have the general form:
```

operator operand
```
Expressions with binary operators have the following form, where each operand can be another expression, variable, or constant:
```

operand operator operand
```
The syntax for the ternary if-then-else operator is:
```

<condition> ? <then_expression> : <else_expression>
```
First, the <condition> is evaluated. If the result is TRUE, then the <then_expression> is evaluated and that is the result of the if-then-else operation (leaving the <else_expression> unevaluated).
Otherwise, the <else_expression> is evaluated and that is the result of the if-then-else operation (leaving the <then_expression> unevaluated).
For example:
```

quotient = denominator = 0 ? division_by_zero_error() : numerator / denominator
```
If `denominator` equals 0, then the function `division_by_zero_error` is called and its return value is assigned to `quotient` (leaving the illegal division by zero unevaluated).
Otherwise, `denominator` differs from 0, the well-defined expression `numerator / denominator` is evaluated and the result is assigned to `quotient`; the function `division_by_zero_error` is not called.
For further information on the different operator types, see the following sections:

- [Arithmetic operators](arithmetic_operators.md)

- [Relational operators](relational_operators.md)

- [Logical operators](logical_operators.md)

- [Operator precedence and associativity](operator_precedence.md)

- [Assignment](assignment_operator.md)

## Related topics
- [3GL programming language features: overview](overview.md)
