# copy.to.clipboard()

## Syntax:
`function void copy.to.clipboard( const string text )`

## Description
Copies the provided text string to the system clipboard. The input text can be of unlimited length and may contain multiple lines. Line breaks within the text can be represented as either Carriage Return (CR, '\r') or Carriage Return followed by Line Feed (CRLF, '\r\n'). The function does not return any value.
Behavior:

- Sends the entire content of argument text to the clipboard.

- Handles both single-line and multi-line strings transparently.

- No return value or error code is provided.

## Arguments
| | | |
|---|---|---|
| `const string` | `text` |  The string content to copy to the clipboard. Supports multiline strings with CR or CRLF line separators.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2590.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Usage Notes

- Ensure the text is properly encoded and formatted before passing to the function.

- The clipboard content will be replaced by the provided text

- This function is intended for use cases where clipboard text transfer is needed without feedback.

## Related topics
- [Text fields overview](overview.md)
