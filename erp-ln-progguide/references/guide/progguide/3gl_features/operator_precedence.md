# Operator precedence and associativity
An expression can include a number of operators, variables, and constants. The overall result is calculated in accordance with the rules of precedence and associativity described here.
The following table lists all operators in order of decreasing precedence.
An operator with a certain precedence is bound tighter (as if by parentheses) to its arguments than any operator with a lower precedence. For example, the expression `3 + 4 * 5` is interpreted as `3 + ( 4 * 5 )`, evaluating to 23, rather than as `( 3 + 4 ) * 5`, evaluating to 35, because multiplication has a higher precedence than addition.
As another example, the expression `NOT -a < b` is interpreted as `NOT ( ( -a ) < b )`, rather than as `( NOT -a ) < b` or as `NOT -( a < b )` because comparison has a lower precedence than arithmetic negation and a higher precedence than logical negation.
Binary and ternary operators that have the same precedence are bound to their arguments in the direction of their associativity. For example, the expression `a + b - c` is interpreted as `( a + b ) - c`, rather than as `a + ( b - c )` because of the left-to-right associativity of addition and subtraction.
As another example, the expression `condition_1 ? then_value_1: condition_2 ? then_value_2: else_value` is interpreted as `condition_1 ? then_value_1: ( condition_2 ? then_value_2: else_value )`, rather than as `( condition_1 ? then_value_1: condition_2 ) ? then_value_2: else_value` because of the right-to-left associativity of the if-then-else operator.
| | | | |
|---|---|---|---|
| Operator | Description | Precedence | Associativity |
| - | arithmetic negation | 9 |  |
| * / \ | multiplication division remainder after division | 8 | left to right |
| & | string concatenation | 7 | left to right |
| + - | addition subtraction | 6 | left to right |
| = or EQ <> or NE < or LT <= or LE > or GT >= or GE | equal different less at most greater at least | 5 | none |
| NOT | logical negation | 4 |  |
| AND | logical and | 3 | left to right |
| OR | logical or | 2 | left to right |
| ?: | if-then-else | 1 | right to left |
You can use parentheses to force a specific binding of an operator to its operands. For example:
```

The result of the expression 3+4*5     is 23
The result of the expression (3+4)*5   is 35
The result of the expression 10/2*5    is 25
The result of the expression 10/(2*5)  is 1
```
In case of doubt, always use parentheses. This makes the program easier to read.

- The operators NOT (logical negation) and - (arithmetic negation) are unary operators, the operator ?: (if-then-else) is a ternary operator, all others are binary operators.

- Relational operators cannot be 'chained'. This means that e.g. the usual mathematical notation `a ≤ b ≤ c` should in 3GL not be written as `a <= b <= c` but rather as `a <= b AND b <= c`.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Expressions and operators](expressions_and_operators.md)
