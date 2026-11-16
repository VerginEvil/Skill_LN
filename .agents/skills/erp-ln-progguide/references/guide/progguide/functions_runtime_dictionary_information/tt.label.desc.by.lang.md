# tt.label.desc.by.lang()

## Syntax:
`function string tt.label.desc.by.lang( string label_code(19), string language(1), [ long label_width, long label_height, domain ttadv.cont label_context ] )`

## Description
Returns the label description of the specified label in the specified language.

## Arguments
| | | |
|---|---|---|
| `string` | `label_code(19)` |  The label code, including the package code.  |
| `string` | `language(1)` |  The language in which the label decsription should be.  |
| `[ long` | `label_width ]` |  Maximum width of the label description. Default is 70.  |
| `[ long` | `label_height ]` |  Maximum height of the label description. Default is 1.  |
| `[ domain ttadv.cont` | `label_context ]` |  The label's context. The possible values are: [tt.label.desc()](tt.label.desc.md) Default is ttadv.cont.general: General Use (for labels on forms and reports).  |

## Return values
Label description of specified label code in specified language.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Remarks
This function is available from TIV level 1501.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)

- [Tools Interface Version (TIV)](../tiv/tiv_overview.md)
