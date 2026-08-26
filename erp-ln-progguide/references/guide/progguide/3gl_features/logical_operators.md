# Logical operators
Logical operators perform logical operations on their operands. The operator NOT is unary, so it has only one operand. The operands of logical operators can be logical expressions, relational expressions, variables or constants of type boolean.
The following table illustrates the results of logical expressions:
| | | | | |
|---|---|---|---|---|
| A | B | NOT A | A AND B | A OR B |
| FALSE | FALSE | TRUE | FALSE | FALSE |
| FALSE | TRUE | TRUE | FALSE | TRUE |
| TRUE | FALSE | FALSE | FALSE | TRUE |
| TRUE | TRUE | FALSE | TRUE | TRUE |
Variabeles of type BOOLEAN should be used.
In the past variables or expressions of type LONG could be used as boolean. If a long expression resulted in the value zero, it was evaluated as FALSE. If the result was not equal to zero, it was evaluated as TRUE.
Usage of a long in this way will cause a warning, in the future it will cause an error.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Expressions and operators](expressions_and_operators.md)
