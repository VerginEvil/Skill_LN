# vsprintf$()

## Syntax:
`function string vsprintf$( string format, [ void... ] )`

## Description
This acts the same as [sprintf$()](sprintf.md), except that the arguments to be substituted for the substitution symbols in the *format* argument are not known until run time.

## Arguments
| | | |
|---|---|---|
| `string` | `format` |  contains zero or more ordinary characters and substitution symbols  |
| `[ void` | `... ]` |  One or more expressions to be replaced in the format  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
extern string my.message(256) mb
function void create.my.message ( string X(14),... )
{
my.message = vsprintf$( form.text$(X),... )
}

## Related topics
- [Formatting input and output - overview and synopsis](overview_and_synopsis.md)

- [sprintf$()](sprintf.md)
