# Arithmetic operators
The arithmetic operations are:
| | |
|---|---|
| Operator | Description |
| - | negation (unary minus operator) |
| + | addition |
| - | subtraction (binary minus operator) |
| * | multiplication |
| / | division |
| \ | remainder after division |
| & | string concatenation |
Arithmetic operators perform arithmetic operations on the operands. Arithmetic operations on booleans are not allowed. All arithmetic operators, except string concatenation, must have operands of numerical type.
If one operand of a binary arithmetic operator is of type long and the other of type double, then implicit long to double type conversion is performed on the long operand and the result of the expression is of double type.
For example:
```

 45/30 is equal to 1
             | 45 and 30 are both LONG so the result is LONG
 45/30.0 is equal to 1.5
             | 30.0 is a DOUBLE so the result is a DOUBLE
```
The concatenation operator concatenates expressions, variables, or constants of string type.

## Unspecified behavior
When the result of an arithmetic operation on integer valued operands is outside the integer value range supported by the bshell, then the behavior of the bshell is unspecified.
In practice, when the exact result of such an operation is outside the supported value range, a wrap-around effect takes place: the exact value is converted by repeatedly adding or subtracting 2^ BitCountOfLong until the value is in the supported signed BitCountOfLong-bit value range. But notice: this behavior is not part of the official specification. Do not rely on it! Different versions of the bshell may behave differently and the same bshell version may behave differently on different platforms!
[Bshell resource debug_long64](../misc/bshell_resources.md) may be used to log overflow during runtime evaluation of integer arithmetic expressions.

## Compile time evaluation of constant integer expressions
The bic compiler has some functionality to evaluate expressions at compile time. For integer arithmetic, this is restricted to the following binary operations:
| | |
|---|---|
| Operator | Description |
| + | addition |
| - | subtraction (binary minus operator) |
| * | multiplication |
| / | division |
| \ | remainder after division |
So, no compile time evaluation of integer expressions is done for:
| | |
|---|---|
| Operator | Description |
| - | negation (unary minus operator) |
It is important to realize that integer expressions evaluated by bic at compile time are evaluated independent of the evaluation mechanism used by the bshell. Internally, bic does not even use signed arithmetic, but unsigned 32-bit arithmetic. Unsigned 32-bit arithmetic is well-defined in the sense that overflow is defined to cause wrap around back to the unsigned 32-bit range [0 … 2^32 - 1]. The only place where bic prevents such a wrap around is in the case of subtractions: when bic detects that the result of a subtraction will be negative, then the subtraction is not done by bic at compile time, but is postponed in order to be done by the bshell at run time.
The resulting unsigned 32-bit value of the compile time evaluation is interpreted at run time by the bshell. The value is wrapped from the unsigned 32-bit value range to the signed BitCountOfLong-bit value range supported by the bshell.
When the bshell is in 64-bit mode, such a (possibly value-changing!) action is not needed: the unsigned 32-bit value range is completely within the signed 64-bit value range.
[Bic compiler option -W32](compiler.md) may be used to generate warnings for constant integer arithmetic expressions of which any intermediate exact *unsigned* 32-bit result is outside the signed 32-bit value range, so it is in the range [2^31 … 2^32 - 1].
[Bshell resource debug_long64](../misc/bshell_resources.md) may be used to log runtime loading of all constant integer arithmetic expressions or only of those of which the exact *unsigned* 32-bit result is outside the signed 32-bit value range, so it is in the range [2^31 … 2^32 - 1].

## Examples
```

       LONG lng_1, lng_2
       DOUBLE doub
       STRING strg_1(16), strg_2(50), strg_3(10), strg_4(20)
```
| | |
|---|---|
| Expression | Result |
| `lng_2 = 8\3` | The variable lng_2 contains 2, which is the remainder after dividing 8 by 3..  |
| `lng_1 = lng_2 + 3` | The variable lng_1 now contains 5. |
| `doub = lng_1 * 2.0` | The variable lng_1 is multiplied by 2.0; the result (10.0) is stored in doub.  |
| `doub = 45 / 30` |  The variable doub now equals 1.0. Note that 45 and 30 are both longs, so the result of the expression is 1. Converted to double for storing in the result, this becomes 1.0.  |
| `doub = 45 / 30.0` | The variable doub now contains 1.5. |
| `strg_1 = "hel" & "lo"` | The variable strg_1 now contains the value "hello".  |
| `strg_2 = strg_3 & strg_4` | The contents of strg_3 and strg_4 are concatenated and placed in strg_2.  |
| `0x7b000000 + 0x20012345` |  Compile time evaluation to `0x9b012345`, which is greater than `2^31 - 1` (i.e. `0x7fffffff`) Wrapping this value to the signed 32-bit value range results in negative value `-0x64fedcbb` (i.e. `0x9b012345 - 2^32`). Wrapping this value to the signed 64-bit value range results in unchanged positive value `0x000000009b012345`.  |
| `-0x65000000 + 0x012345` | Run time addition to same negative value `-0x64fedcbb` (i.e. `0x9b012345 - 2^32`) as in previous example.  |
| `-(0x65000000 - 0x012345)` |  Compile time subtraction `0x65000000 - 0x012345` results in positive value `0x64fedcbb`. Unary negation is done at run time, resulting in same negative value `-0x64fedcbb` (i.e. `0x9b012345 - 2^32`) as in previous examples.  |

## Related topics
- [3GL programming language features: overview](overview.md)
- [Expressions and operators](expressions_and_operators.md)
