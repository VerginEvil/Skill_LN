# Operator precedence
An expression can include a number of operators, variables, and constants. The overall result is calculated in accordance with the rules of precedence described here. For example, because multiplication has precedence over addition, the result of the expression (3 + 4 * 5) is 23 and not 35.
The following table lists all operators in order of decreasing precedence. Operators with high precedence are evaluated before operators with lower precedence. Operators on the same line in the table have the same precedence. If they occur in one expression, they are evaluated from left to right.
| | |
|---|---|
| Operator | Associativity |
| - (negation) | right to left |
| * / \ | left to right |
| & | left to right |
| + - (minus) | left to right |
| = > < <> <= >= | none |
| NOT | right to left |
| AND | left to right |
| OR | left to right |
| ?: | right to left |
You can use parentheses to force a specific precedence. For example:
```

The result of the expression 3+4*5     is 23
The result of the expression (3+4)*5   is 35
The result of the expression 10/2*5    is 25
The result of the expression 10/(2*5)  is 1
```
In case of doubt, always use parentheses. This makes the program easier to read.
Notes
- The operators NOT and - (negation) are unary, the others are binary.
- Relational operators cannot be 'chained'. This means that e.g. the mathematically usual notation `A ≤ B ≤ C` should not be written in 3GL as `A <= B <= C` but as `A <= B AND B <= C`.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Expressions and operators](expressions_and_operators.md)
