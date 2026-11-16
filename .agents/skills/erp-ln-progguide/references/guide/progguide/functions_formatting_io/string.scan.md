# string.scan()

## Syntax:
`function long string.scan( string value$, string format$, [ void... ] )`

## Description
This function scans the supplied *value$* string argument for fields matching the conversion symbols in the supplied *format$* string argument and stores the field values in the subsequent remaining reference arguments.

## Arguments
| | |
|---|---|
| Conversion symbol | Description |
| %d | Conversion symbol matching the decimal representation of an integer value: a sequence of decimal digits '0', …, '9', optionally preceded by a minus sign '-'. |
| %f | Conversion symbol matching the decimal representation of a floating point value: a sequence of decimal digits '0', …, '9' and at most one decimal point '.', optionally preceded by a minus sign '-', optionally followed by an exponent part: the letter 'e' or 'E', an optional plus sign '+' or minus sign '-' and a sequence of decimal digits '0', …, '9'. |
| %s | Conversion symbol matching the representation of a string value: a sequence of characters not equal to the current separator character. |
When a conversion symbol is immediately followed by an ordinary character, then that ordinary character serves as the separator character during the match of the conversion symbol. When a conversion symbol is immediately followed by a next conversion symbol, then the default value for the separator character during the match of the conversion symbol is a space character ' '. When a conversion symbol is not followed by any further character (i.e. it is at the end of the *format$* string), then there is no separator character during the match of the conversion symbol.
A separator character matches at most one occurrence of itself in the *value$* string. Any other ordinary character in the *format$* string matches any number (including zero) of occurrences of itself in the *value$* string.

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
