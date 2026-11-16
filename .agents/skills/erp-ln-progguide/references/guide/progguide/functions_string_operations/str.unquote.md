# str.unquote$()

## Syntax:
`function string str.unquote$( const string string$ )`

## Description
Removes surrounding (double or single) quotes from a string. If the string is not surrounded by a pair of quotes, the string itself is returned. The quote at the end of the string must be the same as the quote at the start of the string.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
the string without the surrounding quotes, if any

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Examples
```

string	result$(30)

|* note that in 3GL double quotes in string literals have to be escaped
|* by adding an extra double quote;

|* call to str.unquote$()                      input string     result$ contains
|-----------------------------------------------------------------------------------
result$ = str.unquote$("""hello""")         |* "hello"          hello
result$ = str.unquote$("'hello'")           |* 'hello'          hello
result$ = str.unquote$("""hello'")          |* "hello'          "hello'
result$ = str.unquote$("""""")              |* ""               <empty string>
result$ = str.unquote$("''")                |* ''               <empty string>
result$ = str.unquote$("""hello"" there""") |* "hello" there"   hello" there
result$ = str.unquote$("'hi ""there""'")    |* 'hi "there"'     hi "there"
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
