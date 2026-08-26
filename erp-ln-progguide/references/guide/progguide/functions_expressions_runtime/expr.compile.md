# expr.compile()

## Syntax:
`function long expr.compile( string expression )`

## Description
This compiles the specified expression and returns an ID number for the compiled expression. The expression can be executed subsequently using [l.expr()](l.expr.md), [d.expr()](d.expr.md), or [s.expr$()](s.expr.md). Because variables included in the expression must be known at runtime, they must be declared as external variables.
You can execute compiled expressions multiple times without recompiling. The current values of the variables are used each time.

## Arguments
| | | |
|---|---|---|
| `string` | `expression` |  Expression to compile.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Features
The expression can include any of the following features:
Literal decimal integer values. For example: `123`
Literal decimal floating point values. For example: `123.456`
Literal string values. For example: `"abc"`
The following named constants:
- COMPNR.MAX ( = the maximum company number )
- PI ( = 3.14159265... )
- TRUE
- FALSE  The following symbolic names:
-  $$
This represents the optional value argument passed to [l.expr()](l.expr.md), [d.expr()](d.expr.md), or [s.expr$()](s.expr.md).
In expressions on forms, this represents the current field name.
For example: `$$ IN [30,40]`
-  $#
In expressions on forms, this represents the current domain name.
External variable read access. For example: `a`
External variable write access (assignment). For example: `a := 5`
Merged expressions, separated by commas (,). For example: `a:=3, b:=7, c-8`
Operators. These have the same function as in normal expressions. Integer division is an exception. Normally, integer division returns an integer (for example, 45/30 returns 1). With these functions, integer division returns a double (for example, 45/30 returns 1.5).
The IN keyword. Use this to check whether a value lies within a specified range, or a string value matches a string regular expression.
Conditional expressions. For example: `a < 0 ? -a : a`
Numerical ranges. For example: `a IN [12,30]` or `a IN [12,30] [50,100] [200,500]`
The following functions:
| | | | | | | |
|---|---|---|---|---|---|---|
| abs() | acos() | asc() | asin() | atan() | chr() | cos() |
| cosh() | edit() | exp() | int() | len() | log() | log10() |
| min() | max() | pos() | pow() | round() | rpos() | sin() |
| sqrt() | str() | strip() | tan() | tanh() | val() |  |
| | |
|---|---|
| `time()` |  current time in HHMM format  |
| `date()` |  current date in number of days since January 1, 0001  |
| `date(YYYY,MM,DD)` |  specified date in number of days since January 1, 0001 for example: `date() IN [ date(1988,1,1), date(1992,1,1) ]`  |
| `utc()` |  current date and time in UTC long format  |
| `utc(YYYY,MM,DD,HH,MM,SS)` |  specified local date/time in UTC long format; input values must be in signed 32-bit value range; if exact result is negative or greater than the maximum value 2^( BitCountOfLong-1) - 1 of the signed BitCountOfLong-bit range, then error value -1 is returned  |
| `fmin()` |  Returns the minimum value of a 4GL variable, domain, or table field. See [set.fmin()](../functions_mathematical_operations/set.fmin.md) for an explanation of how the attributes of the concerned domain may influence the result.  |
| `fmax()` |  Returns the maximum value of a 4GL variable, domain, or table field. See [set.fmax()](../functions_mathematical_operations/set.fmax.md) for an explanation of how the attributes of the concerned domain may influence the result.  |

## String regular expressions
A string regular expression is a constant string and must appear on the right hand side of the IN operator. Note that it must be *constant*, which excludes the use of $$ as regular expression. String regular expressions can contain the following characters:
| | |
|---|---|
| `^` |  means the beginning of the string  |
| `$` |  means the end of the string  |
| `.` |  means any character  |
| `*` |  takes the previous character 0 or more times  |
| `[]` |  means one of the characters between [ ] for example: `[abcd123] or [a-z] or [a-zA-Z]`  |
| `[^]` |  means any character except the characters after ^  |
| `{m}` |  means the previous character exactly *m* times. *m* must be an integer in the range 0..255.  |
| `{m,}` |  means the previous character at least *m* times. *m* must be an integer in the range 0..255.  |
| `{m,n}` |  means the previous character at least *m* times and at most *n* times. *m* and *n* must be integers in the range 0..255, and *m* must be less than or equal to *n*.  |
| `(re) \n` |  means the same string of characters matched by the *n* th parenthesized regular expression. *n* must be an integer in the range 1..9.  |
| `\` |  take the following character literally. This is the escape character and removes any special meaning from the character that follows. Note the \n construction above. Also note that the \ character does not play a special role in "ordinary" 3GL strings.  |
| `""` |  means a single double-quote within a string  |
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
You can retrieve the length and position from the result with [store.long()](../functions_string_operations/store.long.md) and [load.short()](../functions_string_operations/load.short.md).

## Integer arithmetic
Integer arithmetic in runtime expression evaluation is performed in the signed 64-bit value range: [-2^63 … 2^63 - 1].
In older porting sets (with [bshell TIV level](../tiv/tiv_overview.md) less than [2000](../tiv/tiv_2000.md)), signed 32-bit values are used for integer arithmetic in runtime expression evaluation.
When during runtime expression evaluation an assignment of an integer value to a bshell variable is performed, a value check is done.
If the integer value is greater than the maximum value 2^( BitCountOfLong-1) - 1 of the signed BitCountOfLong-bit range, then that maximum value is assigned.
If the integer value is less than the minimum value -2^( BitCountOfLong-1) of the signed BitCountOfLong-bit range, then that minimum value is assigned.

## Return value
An ID for the compiled expression.

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
