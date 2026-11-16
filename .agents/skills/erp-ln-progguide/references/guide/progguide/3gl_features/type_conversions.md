# Type conversion
A value of a certain type can be converted to a value of a different type.
For example, integer value 6 of type long can be converted to its decimal representation "6" of type string (and vice versa).

## Explicit type conversion
When a specific function is used to perform the type conversion, then this is called *explicit type conversion*.
For example, the function [str$()](../functions_string_operations/str.md) can be used to convert a value of type long to its decimal representation of type string.
The documentation of such a function should carefully describe the conversion process.
Such a function may have additional arguments which can be used to control certain details of the conversion process.

## Implicit type conversion
When no specific function is used to perform the type conversion, then this is called *implicit type conversion*.
For example, the function [get.var()](../functions_variables_interprocess_transfer/get.var.md) can be used to retrieve the value of a certain variable and store that value into a different variable of a possibly different type.
Such an implicit conversion cannot be controlled by additional function arguments.
It is important to use the same implicit conversion mechanism as much as possible in all circumstances. This allows to describe the conversion mechanism in a single central place and to refer to it by a phrase like "the usual implicit type conversion is done where applicable".

## Specific type conversions
In the sections below, several (not all!) type conversions are described in more detail.
For each type conversion, first a list of functions is given where the type conversion is explicit.
Then, a list of functions is given where the type conversion is implicit.
Finally, the implicit type conversion algorithm is described in detail.

- [Long to string type conversion](#long_to_string_type_conversion)

- [String to long type conversion](#string_to_long_type_conversion)

- [Long to double type conversion](#long_to_double_type_conversion)

- [Double to long type conversion](#double_to_long_type_conversion)

- [Long to boolean type conversion](#long_to_boolean_type_conversion)

## Long to string type conversion
[Explicit](#explicit_type_conversion) long to string type conversion is performed or may be performed during the execution of the following functions.
The resulting string value is the formatted decimal, octal, or hexadecimal representation of the long value.
| | |
|---|---|
| Function | Remark |
| [sprintf$()](../functions_formatting_io/sprintf.md) | when using a format with one of the following type conversion specifiers: 'd', 'o', 'lo', 'x', 'lx' |
| [vsprintf$()](../functions_formatting_io/vsprintf.md) | when using a format with one of the following type conversion specifiers: 'd', 'o', 'lo', 'x', 'lx' |
[Implicit](#implicit_type_conversion) long to string type conversion may occur during the execution of the following functions. The list may be incomplete.
| | |
|---|---|
| Function | Remark |
| [concat$()](../functions_string_operations/concat.md) | when any of the supplied values is of type long |
| [edit$()](../functions_formatting_io/edit.md) | when supplying a long value |
| [exec_dll_function()](../functions_dll/exec_dll_function.md) | when receiving a long return value in a string variable |
| [exec_function()](../functions_dll/exec_function.md) | when receiving a long return value in a string variable |
| [exit()](../functions_starting_and_stopping_programs/exit.md) | when supplying a long exit value |
| [get.indexed.var()](../functions_variables_interprocess_transfer/get.indexed.var.md) | when getting a value from a long array and storing it in a string variable |
| [get.string.arg()](../functions_varying_arguments/get.string.arg.md) | when getting a long argument |
| [get.var()](../functions_variables_interprocess_transfer/get.var.md) | when getting a long variable and storing it in a string variable |
| [parse_and_exec_function()](../functions_dll/parse_and_exec_function.md) | when receiving the value of a long argument in the return call string, and when receiving a long return value in a string variable |
| [put.indexed.var()](../functions_variables_interprocess_transfer/put.indexed.var.md) | when putting a long value in a string array |
| [put.long.arg()](../functions_varying_arguments/put.long.arg.md) | when putting into a string argument |
| [put.var()](../functions_variables_interprocess_transfer/put.var.md) | when putting a long value in a string variable |
| [sprintf$()](../functions_formatting_io/sprintf.md) | when a long value is supplied where according to the type conversion specifier ("%s" or "%@<format>@") a string value is expected |
| [str$()](../functions_string_operations/str.md) | when supplying a long input value |
| [vsprintf$()](../functions_formatting_io/vsprintf.md) | when a long value is supplied where according to the type conversion specifier ("%s" or "%@<format>@") a string value is expected |
When implicit long to string type conversion occurs, the resulting string value is the unformatted decimal representation of the long value, determined according to the following algorithm.
| | |
|---|---|
| Integer input value i | Decimal representation |
| i < 0 | a minus sign '-', followed by the decimal representation of the absolute value of i. |
| 0 ≤ i < 10 | the single digit character from the range '0' … '9', corresponding to i. |
| 10^n ≤ i < 10^(n+1) for some positive integer value n | a string of n+1 decimal digits; the first n decimal digits are the decimal representation of i / 10; the final decimal digit is the decimal representation of i \ 10. |
Apart from the exact contents of the decimal representation, it is important to take notice of its string length.
From the algorithm described above, the following schema can be derived.
| | | | |
|---|---|---|---|
| String length n | Exactly fitting negative integer input value i | Exactly fitting non-negative integer input value i | Acceptable integer input value i |
| n = 1 |  | 0 ≤ i < 10 | 0 ≤ i < 10 |
| n > 1 | -10^(n-1) < i ≤ -10^(n-2) | 10^(n-1) ≤ i < 10^n | -10^(n-1) < i < 10^n |
| For example: |  |  |  |
| n = 2 | -10 < i ≤ -1 | 10 ≤ i < 100 | -10 < i < 100 |
| n = 3 | -100 < i ≤ -10 | 100 ≤ i < 1,000 | -100 < i < 1,000 |
| n = 10 | -1,000,000,000 < i ≤ -100,000,000 | 1,000,000,000 ≤ i < 10,000,000,000 | -1,000,000,000 < i < 10,000,000,000 |
| n = 11 | -10,000,000,000 < i ≤ -1,000,000,000 | 10,000,000,000 ≤ i < 100,000,000,000 | -10,000,000,000 < i < 100,000,000,000 |
| n = 19 | -1,000,000,000,000,000,000 < i ≤ -100,000,000,000,000,000 | 1,000,000,000,000,000,000 ≤ i < 10,000,000,000,000,000,000 | -1,000,000,000,000,000,000 < i < 10,000,000,000,000,000,000 |
| n = 20 | -10,000,000,000,000,000,000 < i ≤ -1,000,000,000,000,000,000 | 10,000,000,000,000,000,000 ≤ i < 100,000,000,000,000,000,000 | -10,000,000,000,000,000,000 < i < 100,000,000,000,000,000,000 |
Notice, that the decimal notation of the signed 32-bit value range is [-2,147,483,648 … 2,147,483,647], implying that 11 string positions must be reserved to cover the complete range.
Notice, that the decimal notation of the signed 64-bit value range is [-9,223,372,036,854,775,808 … 9,223,372,036,854,775,807], implying that 20 string positions must be reserved to cover the complete range.

## String to long type conversion
[Explicit](#explicit_type_conversion) string to long type conversion is performed during the execution of the following functions.
| | |
|---|---|
| Function | Remark |
| [lval()](../functions_string_operations/lval.md) | Implicit bounds |
| [string.to.bounded.long()](../functions_string_operations/string.to.bounded.long.md) | Explicit bounds |
[Implicit](#implicit_type_conversion) string to long type conversion may occur during the execution of the following functions. The list may be incomplete.
| | |
|---|---|
| Function | Remark |
| [abs()](../functions_mathematical_operations/abs.md) | when a string value is supplied |
| [exec_dll_function()](../functions_dll/exec_dll_function.md) | when receiving a string return value in a long variable |
| [exec_function()](../functions_dll/exec_function.md) | when receiving a string return value in a long variable |
| [get.indexed.var()](../functions_variables_interprocess_transfer/get.indexed.var.md) | when getting a value from a string array and storing it in a long variable |
| [get.long.arg()](../functions_varying_arguments/get.long.arg.md) | when getting a string argument |
| [get.var()](../functions_variables_interprocess_transfer/get.var.md) | when getting a string variable and storing it in a long variable |
| [parse_and_exec_function()](../functions_dll/parse_and_exec_function.md) | when supplying a value for a long argument, and when receiving a string return value in a long variable |
| [put.indexed.var()](../functions_variables_interprocess_transfer/put.indexed.var.md) | when putting a string value in a long array |
| [put.string.arg()](../functions_varying_arguments/put.string.arg.md) | when putting into a long argument |
| [put.var()](../functions_variables_interprocess_transfer/put.var.md) | when putting a string value in a long variable |
| [sprintf$()](../functions_formatting_io/sprintf.md) | when a string value is supplied where according to the type conversion specifier (e.g. "%d") a long value is expected |
| [string.scan()](../functions_formatting_io/string.scan.md) | when supplying a long reference argument |
| [vsprintf$()](../functions_formatting_io/vsprintf.md) | when a string value is supplied where according to the type conversion specifier (e.g. "%d") a long value is expected |
When (explicit or implicit) string to long type conversion occurs, the resulting long value is the numerical value of the decimal representation found in the string.
Initial white space in the string is ignored.
The decimal representation is expected to contain an optional '+' or '-' sign, followed by a sequence of decimal digits '0' … '9'.
When an unexpected character is encountered, that character and any further string contents are ignored.
If the string value cannot be interpreted as the decimal representation of a numerical value, then the value 0 is used.
If the exact numerical value is greater than the maximum value 2^( [BitCountOfLong](data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](data_types.md#BitCountOfLong)-bit range, then that maximum value is used.
If the exact numerical value is less than the minimum value -2^( [BitCountOfLong](data_types.md#BitCountOfLong)-1) of the signed [BitCountOfLong](data_types.md#BitCountOfLong)-bit range, then that minimum value is used.

## Long to double type conversion
There are no functions available for [explicit](#explicit_type_conversion) long to double type conversion.
[Implicit](#implicit_type_conversion) long to double type conversion may occur during the execution of the following operators and functions. The list may be incomplete.
| | |
|---|---|
| Function | Remark |
| [Assignment](assignment_operator.md) | when assigning a long value to a variable of type double |
| [Arithmetic operators](arithmetic_operators.md) | when one operand is of type long and the other of type double, the long operand is converted to double |
| [Relational operators](relational_operators.md) | when one operand is of type long and the other of type double, the long operand is converted to double |
| [exec_dll_function()](../functions_dll/exec_dll_function.md) | when receiving a long return value in a double variable |
| [exec_function()](../functions_dll/exec_function.md) | when receiving a long return value in a double variable |
| [get.indexed.var()](../functions_variables_interprocess_transfer/get.indexed.var.md) | when getting a value from a long array and storing it in a double variable |
| [get.double.arg()](../functions_varying_arguments/get.double.arg.md) | when getting a long argument |
| [get.var()](../functions_variables_interprocess_transfer/get.var.md) | when getting a long variable and storing it in a double variable |
| [parse_and_exec_function()](../functions_dll/parse_and_exec_function.md) | when receiving a long return value in a double variable |
| [put.indexed.var()](../functions_variables_interprocess_transfer/put.indexed.var.md) | when putting a long value in a double array |
| [put.long.arg()](../functions_varying_arguments/put.long.arg.md) | when putting into a double argument |
| [put.var()](../functions_variables_interprocess_transfer/put.var.md) | when putting a long value in a double variable |
| [sprintf$()](../functions_formatting_io/sprintf.md) | when a long value is supplied where according to the type conversion specifier ("%e" or "%f" or "%g") a double value is expected |
| [vsprintf$()](../functions_formatting_io/vsprintf.md) | when a long value is supplied where according to the type conversion specifier ("%e" or "%f" or "%g") a double value is expected |
When [long](data_types.md#long) to [double](data_types.md#double) type conversion occurs, the intention is that the resulting double value has the same numerical value as the original long value.
Integer values in the signed 32-bit range can be represented without loss of precision.
At the edges of the signed 32-bit value range, neighboring floating point numbers have a distance of 2^-22.
However, the full signed 64-bit integer value range cannot be represented without loss of precision.
At the edges of the signed 64-bit value range, neighboring floating point numbers have a distance of 2^10.
When there is no floating number of which the numerical value is exactly equal to the long value, then the nearest lower or nearest higher floating point number is used. The exact choice (lower or higher) is left unspecified and may be machine specific.

## Double to long type conversion
[Explicit](#explicit_type_conversion) double to long type conversion is performed during the execution of the following functions.
| |
|---|
| Function |
| [int()](../functions_mathematical_operations/int.md) |
[Implicit](#implicit_type_conversion) double to long type conversion may occur during the execution of the following operators and functions. The list may be incomplete.
| | |
|---|---|
| Function | Remark |
| [Assignment](assignment_operator.md) | when assigning a double value to a variable of type long |
| [exec_dll_function()](../functions_dll/exec_dll_function.md) | when receiving a double return value in a long variable |
| [exec_function()](../functions_dll/exec_function.md) | when receiving a double return value in a long variable |
| [get.indexed.var()](../functions_variables_interprocess_transfer/get.indexed.var.md) | when getting a value from a double array and storing it in a long variable |
| [get.long.arg()](../functions_varying_arguments/get.long.arg.md) | when getting a double argument |
| [get.var()](../functions_variables_interprocess_transfer/get.var.md) | when getting a double variable and storing it in a long variable |
| [parse_and_exec_function()](../functions_dll/parse_and_exec_function.md) | when receiving a double return value in a long variable |
| [put.indexed.var()](../functions_variables_interprocess_transfer/put.indexed.var.md) | when putting a double value in a long array |
| [put.double.arg()](../functions_varying_arguments/put.double.arg.md) | when putting into a long argument |
| [put.var()](../functions_variables_interprocess_transfer/put.var.md) | when putting a double value in a long variable |
| [sprintf$()](../functions_formatting_io/sprintf.md) | when a double value is supplied where according to the type conversion specifier (e.g. "%d") a long value is expected |
| [vsprintf$()](../functions_formatting_io/vsprintf.md) | when a double value is supplied where according to the type conversion specifier (e.g. "%d") a long value is expected |
When (explicit or implicit) [double](data_types.md#double) to [long](data_types.md#long) type conversion occurs, the intention is that the resulting long value is a good approximation of the original double value.
During explicit double to long type conversion (i.e. when the function [int()](../functions_mathematical_operations/int.md) is used), some additional rounding is done beforehand.
The actual type conversion means that the fractional part of the floating point value is discarded, leaving only its integer part.
If the exact resulting integer value is outside the signed [BitCountOfLong](data_types.md#BitCountOfLong)-bit range of the long data type, then the result is undefined.

## Long to boolean type conversion
[Explicit](#explicit_type_conversion) long to boolean type conversion is performed or may be performed during the execution of the following functions. The list may be incomplete.
| |
|---|
| Function |
| [ltob()](../functions_boolean/ltob.md) |
[Implicit](#implicit_type_conversion) long to boolean type conversion may occur during the execution of the following code constructs. The list may be incomplete.
Implicit long to boolean type conversion will (in almost all cases) cause a compilation warning; in the future it will cause a compilation error.
| | |
|---|---|
| Code construct | Remark |
| [IF <condition> THEN](the_if_then_else_statement.md#if-then-endif) | when <condition> is of type long |
| [ELIF <condition> THEN](the_if_then_else_statement.md#elif-then) | when <condition> is of type long |
| [WHILE <condition> <statements> ENDWHILE](iterations.md#while_statement) | when <condition> is of type long |
| [REPEAT <statements> UNTIL <condition>](iterations.md#repeat_statement) | when <condition> is of type long |
When (explicit or implicit) long to boolean type conversion occurs, long value 0 is converted to boolean value FALSE and any other long value is converted to boolean value TRUE.

## Related topics
- [3GL programming language: overview](overview.md)

- [Data types](data_types.md)
