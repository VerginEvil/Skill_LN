# string.scan()

## Syntax:
`function long string.scan( string value$, string format$, [ void ... ] )`

## Description
This function scans the supplied *value$* string argument for fields matching the conversion symbols in the supplied *format$* string argument and stores the field values in the subsequent remaining reference arguments.

## Arguments
**
******
| | | |
|---|---|---|
| `string` | `value$` |  Input string value to be scanned, looking for input fields matching the conversion symbols in the *format$* argument. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS. An input field is defined as all characters up to the current separator character or up to a character that does not match the type of the corresponding conversion symbol.  |
| `string` | `format$` |  Format string, containing a mixture of conversion symbols and ordinary characters. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS. A conversion symbol consists of the percent character '%', followed by a specific character sequence. For this moment, only one of the single letter sequences 'd', 'f', or 's' is allowed. Any other character sequence that might follow the percent character is reserved for future use and the current behavior of the function string.scan for such a conversion symbol is undefined.  |
| `[ void` | `... ]` |  Reference arguments to which the field values scanned from the *value$* string argument must be assigned. Implicit conversion from type string to the type of the corresponding reference argument is performed. Typical (but not enforced) usage is to supply a reference argument of type string for conversion symbol %s, a reference argument of type double for conversion symbol %f and a reference argument of type long for conversion symbol %d.  |

## Return values
This function returns the number of successfully scanned and assigned fields. This implies that the returned value will not be greater than the number of conversion symbols in the *format$* string and also not greater than the number of supplied reference arguments to assign field values to. The returned value will be even less than both mentioned numbers when the match of a conversion symbol fails.
Reference arguments past the number returned by this function are left untouched.

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
The field value matched by a conversion symbol can be an empty string. If that empty field value is followed in the *value$* string by the current separator character, then the empty field value is considered valid.
In most other cases an empty field value is considered invalid. There is one somewhat strange exception to this; it may be considered a bug, but this behavior is maintained for backward compatibility reasons. A field value is considered valid, even if it is empty, when it is followed in the *value$* string by a [terminating NULL character](../3gl_features/null_characters_in_strings.md). However, any subsequent (obviously empty) field value is considered invalid, further matching fails and no further processing is done.
In the remaining cases (i.e. when the empty field value is followed in the *value$* string by a character that does not match the type of the current conversion symbol or when the end of the *value$* string is reached for a different reason than a [terminating NULL character](../3gl_features/null_characters_in_strings.md)), the empty field value is considered invalid; the match fails and no further processing is done.

## Example
Consider the following function call:
string.scan( input_string$, "%d|%f", var.long, var.double )
In this case, the function expects *input_string$* to contain two separate numeric values. It reads the input string until it meets a pipe character '|' (this is the separator specified in the *format$* argument). It then converts the characters read (excluding the separator) to a long value and stores that value in the *var.long* variable. The function then continues scanning the input string using the next conversion symbol in the *format$* argument.
```

double D
long L
string S(80)
long ret
ret = string.scan( "string 123 456.78", "%s %d %f", S, L, D )
    | S contains "string", L contains 123, D contains 456.78, ret contains 3.
ret = string.scan( "string|123|456.78", "%s|%d|%f", S, L, D )
    | S contains "string", L contains 123, D contains 456.78, ret contains 3.
```

## Related topics
- [Formatting input and output - overview and synopsis](overview_and_synopsis.md)
