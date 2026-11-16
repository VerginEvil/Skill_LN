# expr.compile()

## Syntax:
`function long expr.compile( string expression )`

## Description
This function compiles the specified expression and returns an ID number for the compiled expression. The expression can be evaluated subsequently using [l.expr()](l.expr.md), [d.expr()](d.expr.md), or [s.expr$()](s.expr.md). Because variables included in the expression must be known at runtime, they must be declared as external variables.
A compiled expression can be evaluated repeatedly without recompilation. In each evaluation the current values of the referenced variables are used.

## Arguments
| | | |
|---|---|---|
| `string` | `expression` |  Expression to compile.  |

## Return values
An ID for the compiled expression.

## Context
This function is implemented in the porting set and can be used in all script types.

## Expression
The expression consists of a comma-separated list of subexpressions.
```
<expression> ::= <subexpression> [ { , <subexpression> }... ]
```
The comma can be considered here as a binary comma operator (or 'sequencing operator'). It is only available at the highest level. The comma in other comma-separated lists, such as function parameter lists and numerical ranges, is not this comma operator.
The comma operator is intended for sequencing the evaluation of multiple subexpressions, especially of their side effects (e.g. assignments).
The subexpressions are evaluated (including any side effects) in left-to-right order. The evaluation results are discarded, except for that of the rightmost subexpression. The evaluation result of the rightmost subexpression is the result of the comma-separated list of subexpressions.
For example: `a:= 3, b:= 7, c - 8`. First the assignment to variable *a* is done. Then the assignment to variable *b* is done. Then the expression `c - 8` is evaluated and the resulting value is the result of the full expression `a:= 3, b:= 7, c - 8`.

## Subexpression
Each subexpression is either a simple expression or an assignment.
```

<subexpression>
    ::= <simple expression>
      | <assignment>

<assignment>
    ::= <left hand side> := <right hand side>

<right hand side>
    ::= <simple expression>
```
The left hand side of an assignment specifies a storage location. Use the syntax as described below for external variable access in simple expressions.
The right hand side of an assignment is evaluated and the result is stored in the storage location specified by the left hand side of the assignment.
The result of evaluating the right hand side of an assignment is also the evaluation result of that assignment. An assignment cannot be used as an operand in a simple expression.

## Simple expression
Each simple expression can include any of the following features.

- Literal decimal integer values. For example: `123`

- Literal decimal floating point values. For example: `123.456`

- Literal string values. For example: `"abc"`

- COMPNR.MAX ( = the maximum company number )

- PI ( = 3.14159265... )

- TRUE

- FALSE

- $$ This represents the optional *value* argument passed to [l.expr()](l.expr.md), [d.expr()](d.expr.md), or [s.expr$()](s.expr.md). In expressions on forms, this represents the current field name. For example: `$$ IN [30,40]`

- $# In expressions on forms, this represents the current domain name.
```
<variable name>
```
```
<variable name> [ ( <start position> [ ; <substring length> ] ) ]
```
```
<variable name> ( <index> [ { , <index> }... ] )
```
```
<variable name> ( <start position> { , <index> }... [ ; <substring length> ] )
```
| | |
|---|---|
| Variable type | Access syntax |
| Long or double |  |
| String |  |
| Long or double array |  |
| String array |  |

- The number of indices (including the start position) must be equal to the number of dimensions of the array.

- The start position is 1-based, i.e. start position 1 specifies the begin of the string variable (or of the string array element specified by the other indices).

- The indices are 1-based, i.e. each index must evaluate to at least the value 1 and to at most the value of the corresponding dimension.

- An individual character of a string can be accessed by specifying it as a substring with explicit length 1.

However, access to substrings of multibyte string variables and of multibyte string array elements is not well-supported.

- The start position of a substring of a multibyte string variable or of a multibyte string array element is byte-based rather than character-based. E.g. when the first character of a string is a (four-byte) multibyte character, then start position 5 (rather than 2) must be used for a substring starting at the second character.

- The optional explicit length of a substring of a multibyte string variable or of a multibyte string array element is byte-based rather than character-based. E.g. the length of a substring containing exactly one (four-byte) multibyte character must be specified as 4 (rather than as 1).
| | | |
|---|---|---|
| Class | Operator | Description |
| Arithmetic | - ^ * / \ + - & | negation exponentiation multiplication, division, remainder addition, subtraction string concatenation |
| Relational | = <> < <= > >= | is equal to is not equal to (differs from) is less than is less than or equal to (is at most) is greater than is greater than or equal to (is at least) Notice that identifiers EQ, NE, LT, LE, GT, and GE *cannot* be used for these operators! |
| Logical | AND OR NOT | logical and logical or logical negation |
| Conditional | ?: | if-then-else |

- Exponentiation The ^ operator (exponentiation) is not available in 3GL. The ^ operator is a binary operator, so the syntax is `<operand> ^ <operand>`. The ^ operator is [left-associative](../3gl_features/operator_precedence.md). Its [precedence](../3gl_features/operator_precedence.md) is lower than that of the unary - operator (arithmetic negation) and higher than that of the * operator (multiplication), the / operator (division), and the \ operator (remainder). The result of an exponentiation is the value of the left <operand> raised to the power of the right <operand>. Where applicable, the operands are implicitly converted to type double. For example: the expression `2^3` evaluates to double value 8.0.

- Integer division In [3GL expression evaluation](../3gl_features/expressions_and_operators.md), integer division evaluates to an integer (i.e. type long) value; for example, the expression `45/30` evaluates to long value 1. However, in runtime expression evaluation, integer division evaluates to a floating point (i.e. type double) value; for example, the expression `45/30` evaluates to double value 1.5.

- Division by zero and remainder after division by zero In [3GL expression evaluation](../3gl_features/expressions_and_operators.md), (remainder after) division by zero triggers a runtime error. However, in runtime expression evaluation, (remainder after) division by zero does not trigger any error. It silently evaluates to double value 0.0 (or to long value 0 for remainder of a long value after division by long value 0).

- The logical AND and OR operators. In [3GL expression evaluation](../3gl_features/expressions_and_operators.md), the evaluation of the [logical AND and OR operators](../3gl_features/logical_operators.md) is *short-circuited*, i.e. the evaluation of the right operand is skipped when its value is not needed for determining the result of the operation. However, in runtime expression evaluation, both operands are evaluated (including any side effects). The result of the AND operation is TRUE if and only if both operands evaluated to TRUE. The result of the OR operation is FALSE if and only if both operands evaluated to FALSE. For example, consider the following expression for determining whether $$ is the square of an integer value: `0 <= $$ AND pow( int( sqrt( $$ ) ), 2 ) = $$`. Even when the first operand `0 <= $$` evaluates to FALSE, still the second operand `pow( int( sqrt( $$ ) ), 2 ) = $$` is evaluated and causes a floating point error (illegal operation: square root of a negative value). In order to work around such a situation, consider a variant like this: `0 <= $$ AND pow( int( sqrt( $$ < 0 ? 0.0: $$ ) ), 2 ) = $$`. When the first operand `0 <= $$` evaluates to FALSE, the evaluation of the second operand `pow( int( sqrt( $$ < 0 ? 0.0: $$ ) ), 2 ) = $$` boils down to `pow( int( sqrt( 0.0 ) ), 2 ) = $$`, which is further evaluated to value FALSE without causing a floating point error.

- The conditional if-then-else operator. In [3GL expression evaluation](../3gl_features/expressions_and_operators.md), dependent on the result of the evaluation of the first operand, either the second or the third operand is evaluated and that is the result (leaving the other operand unevaluated). However, in runtime expression evalation, all three operands are evaluated (including any side effects) and dependent on the result of the evaluation of the first operand, the result is one of the other two results. For example: `square < 0 ? -1.0: sqrt( square )`. Even when condition `square < 0` evaluates to TRUE, still operand `sqrt( square )` is evaluated and causes a floating point error (illegal operation: square root of a negative value). In order to work around such a situation, consider a variant like this: `square < 0 ? -1.0: sqrt( square < 0 ? 0.0: square )`. When condition `square < 0` evaluates to TRUE, the evaluation of operand `sqrt( square < 0 ? 0.0: square )` boils down to `sqrt( 0.0 )`, which is further evaluated to value 0.0 without causing a floating point error.

- The IN keyword. Use this to check whether a value lies within a specified range, or a string value matches a string regular expression.

- Numerical ranges. For example: `a IN [12,30]` or `a IN [12,30] [50,100] [200,500]`.
| | | | | | | |
|---|---|---|---|---|---|---|
| abs() | acos() | asc() | asin() | atan() | chr() | cos() |
| cosh() | edit() | exp() | int() | len() | log() | log10() |
| min() | max() | pos() | pow() | round() | rpos() | sin() |
| sqrt() | str() | strip() | tan() | tanh() | val() |  |
| | |
|---|---|
| `time()` | current time in HHMM format |
| `date()` | current date in number of days since January 1, 0001 |
| `date(YYYY,MM,DD)` | specified date in number of days since January 1, 0001 for example: `date() IN [ date(1988,1,1), date(1992,1,1) ]` |
| `utc()` | current date and time in [UTC](../functions_date_time_zones/overview.md#utc) long format |
| `utc(YYYY,MM,DD,HH,MM,SS)` | specified local date/time in [UTC](../functions_date_time_zones/overview.md#utc) long format; input values must be in signed 32-bit value range; if exact result is negative or greater than the maximum value 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range, then error value -1 is returned |
| `fmin()` | Returns the minimum value of a 4GL variable, domain, or table field. See [set.fmin()](../functions_mathematical_operations/set.fmin.md) for an explanation of how the attributes of the concerned domain may influence the result. |
| `fmax()` | Returns the maximum value of a 4GL variable, domain, or table field. See [set.fmax()](../functions_mathematical_operations/set.fmax.md) for an explanation of how the attributes of the concerned domain may influence the result. |
| | |
|---|---|
| asc | Individual bytes are summed. Hexadecimal value 0x9B is *not* recognized as the beginning of a four-byte [TSS-encoded](../misc/tss.md) character 9B *pp* *qq* *rr*. |
| chr | The supplied value is wrapped to the unsigned 8-bit (rather than 32-bit) value range [0 … 255] (i.e. [0 … 0xff]) by repeatedly adding or subtracting 2^8 until the value is in the unsigned 8-bit value range. |
| edit |  |
| len | Individual bytes are counted. Hexadecimal value 0x9B is *not* recognized as the beginning of a four-byte [TSS-encoded](../misc/tss.md) character 9B *pp* *qq* *rr*. The function behaves as bshell function [len.in.bytes()](../functions_string_operations/len.in.bytes.md) rather than as bshell function [len()](../functions_string_operations/len.md). |
| pos |  |
| rpos |  |
| strip | Each individual byte is considered as a character. Hexadecimal value 0x9B is *not* recognized as the beginning of a four-byte [TSS-encoded](../misc/tss.md) character 9B *pp* *qq* *rr*. An incomplete TSS character at the end of the string value is *not* detected and prevents stripping of space characters before the incomplete TSS character. |

- The following functions. Handling of multibyte string values as arguments for these functions is not well-supported. Each byte in such an argument is handled as a separate character. This may be observable in the following functions.

## String regular expressions
A string regular expression is a constant string and must appear on the right hand side of the IN operator. Note that it must be *constant*, which excludes the use of $$ as regular expression. String regular expressions can contain the following characters:
| | |
|---|---|
| `^` | means the beginning of the string |
| `$` | means the end of the string |
| `.` | means any character |
| `*` | takes the previous character 0 or more times |
| `[]` | means one of the characters between [ ] for example: `[abcd123] or [a-z] or [a-zA-Z]` |
| `[^]` | means any character except the characters after ^ |
| `{m}` | means the previous character exactly *m* times. *m* must be an integer in the range 0..255. |
| `{m,}` | means the previous character at least *m* times. *m* must be an integer in the range 0..255. |
| `{m,n}` | means the previous character at least *m* times and at most *n* times. *m* and *n* must be integers in the range 0..255, and *m* must be less than or equal to *n*. |
| `(re) \n` | means the same string of characters matched by the *n* th parenthesized regular expression. *n* must be an integer in the range 1..9. |
| `\` | take the following character literally. This is the escape character and removes any special meaning from the character that follows. Note the \n construction above. Also note that the \ character does not play a special role in "ordinary" 3GL strings. |
| `""` | means a single double-quote within a string |
The result of a regular expression that includes IN is 0 if the expression is FALSE. If the expression is TRUE, the result is a long containing 4 bytes. The first two bytes contain the length of the substring; the last 2 bytes contain the position of the substring in the string.
| | | |
|---|---|---|
| Expression | Result |  |
| length | position |  |
| "abcdefg" IN "def" | 3 | 4 |
| "abcdefg" IN "^def$" |  | FALSE |
| "abcdefg" IN "^[a-z]*$" | 7 | 1 |
| "abcdefg" IN "^a" | 1 | 1 |
| "abcdefg" IN "^b" |  | FALSE |
| "abcdefg" IN "g$" | 1 | 7 |
| "abcdefg" IN "^a.*g$" | 7 | 1 |
| "abcdefg" IN "^[^a].*" |  | FALSE |
| "abcdefg" IN "^[^b-z]" | 1 | 1 |
| "creative" IN "[tea]{3}" | 3 | 3 |
| "abracadabra" IN "(bra).*\1" | 10 | 2 |
| "ab*de" IN "\*" | 1 | 3 |
The length and position can be retrieved from the result with [store.long()](../functions_string_operations/store.long.md) and [load.short()](../functions_string_operations/load.short.md), as shown in the example below.

## Integer arithmetic
Integer arithmetic in runtime expression evaluation is performed in the signed 64-bit value range: [-2^63 … 2^63 - 1].
In older porting sets (with [bshell TIV level](../tiv/tiv_overview.md) less than [2000](../tiv/tiv_2000.md)), signed 32-bit values are used for integer arithmetic in runtime expression evaluation.
When during runtime expression evaluation an assignment of an integer value to a bshell variable is performed, a value check is done.
If the integer value is greater than the maximum value 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range, then that maximum value is assigned.
If the integer value is less than the minimum value -2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range, then that minimum value is assigned.

## Example
```

long       expr_id, lng, length_res, pos_res
string     tmp(4)
expr_id    = expr.compile( """abcdefg"" IN ""def""" )
lng        = l.expr( expr_id )
store.long( lng, tmp )
length_res = load.short( tmp(1;2) ) | length_res contains 3
pos_res    = load.short( tmp(3;2) ) | pos_res contains 4
```

## Related topics
- [Runtime expressions: overview and synopsis](overview_and_synopsis.md)
