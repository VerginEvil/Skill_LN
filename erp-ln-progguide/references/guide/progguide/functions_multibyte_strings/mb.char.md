# mb.char()

## Syntax:
`function long mb.char( long code_point )`

## Description
This function tests whether a specified code point represents a single-byte character, a multibyte character, or something else. It is mainly used in conjunction with the [next.event()](../events/next.event.md) function, which returns a character as a long value.

## Arguments
| | | |
|---|---|---|
| `long` | `code_point` |  The code point to be assessed. Before being interpreted as a code point, the supplied value is wrapped to the unsigned 32-bit value range [0 … 2^32 - 1] (i.e. [0 … 0xffffffff]) by repeatedly adding or subtracting 2^32 until the value is in the unsigned 32-bit value range.  |

## Return values
| | | |
|---|---|---|
| Return value | Code point range | Description |
| 2 | [0x9b000000 … 0x9bffffff] | The supplied value is the code point of a multibyte [TSS](../misc/tss.md) character. |
| 1 | [1 … 0xff] | The supplied value is the code point of a non-zero single-byte [TSS](../misc/tss.md) character. |
| 0 | 0 | The supplied value is zero. |
| [0x100 … 0x9affffff] | The supplied value is not the code point of any [TSS](../misc/tss.md) character, but may indicate some non-character key (for example, a function key). |  |
| [0x9c000000 … 0xffffffff] | The supplied value is not expected and is assessed as ‘not the code point of any [TSS](../misc/tss.md) character’. In earlier versions of the bshell (before [bshell TIV](../tiv/tiv_overview.md) [level 2340](../tiv/tiv_2340.md)), the supplied value is assessed as the code point of a multibyte [TSS](../misc/tss.md) character (return value 2). |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
This example filters out function keys but processes other characters.
```

LONG event(EVTMAXSIZE)
LONG code_point

code_point = evt.keypress.key(event)
IF mb.char( code_point ) <> 0 THEN
        STRING key(1) MB
        key = mb.long.to.str$(code_point)
        | use key
ENDIF
```

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
