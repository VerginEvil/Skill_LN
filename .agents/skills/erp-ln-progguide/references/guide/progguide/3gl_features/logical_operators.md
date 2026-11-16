# Logical operators
Logical operators perform logical operations on their operands. The logical negation operator NOT is a unary operator. The other logical operators (AND and OR) are binary operators.
The operands of logical operators must be boolean expressions.
If any operand is an expression of type long, implicit [long to boolean type conversion](type_conversions.md#long_to_boolean_type_conversion) is performed. This will cause a compilation warning; in the future it will cause a compilation error.
The following table illustrates the results of logical operations:
| | | | | |
|---|---|---|---|---|
| A | B | NOT A | A AND B | A OR B |
| FALSE | FALSE | TRUE | FALSE | FALSE |
| FALSE | TRUE | TRUE | FALSE | TRUE |
| TRUE | FALSE | FALSE | FALSE | TRUE |
| TRUE | TRUE | FALSE | TRUE | TRUE |
The evaluation of the AND and the OR operations is *short-circuited*, i.e. the evaluation of the right operand is skipped when its value is not needed for determining the result of the operation.
For the AND operation, this implies the following. First the left operand is evaluated. If the result is FALSE, then that is the result of the AND operation (leaving the right operand unevaluated). Otherwise, the right operand is evaluated and that is the result of the AND operation.
Likewise, for the OR operation, first the left operand is evaluated. If the result is TRUE, then that is the result of the OR operation (leaving the right operand unevaluated). Otherwise, the right operand is evaluated and that is the result of the OR operation.
For example:
```

is_integer_multiple = denominator <> 0 AND numerator \ denominator =  0
failure             = denominator =  0 OR  numerator \ denominator <> 0
```
If `denominator` equals 0, the illegal operations 'remainder after division by zero' are left unevaluated; `is_integer_multiple` is set to FALSE and `failure` is set to TRUE. Otherwise, `denominator` differs from 0, the well-defined expressions `numerator \ denominator` are evaluated, the results are compared to 0, and the results of the comparisons are assigned to `is_integer_multiple` and `failure`.

## Related topics
- [3GL programming language: overview](overview.md)

- [Expressions and operators](expressions_and_operators.md)
