# spool.buf()

## Syntax:
`function long spool.buf( const string buffer, long length )`

## Description
This sends the contents of the *buffer* argument to the current spooler. The current spooler must be already open. The name of the current spooler is available in the predefined variable *spool.id*.
No new line characters or other separators are sent to the spooler. To include these, you must program them in the buffer yourself. The *length* argument specifies the length of the send string. If this is 0, the spooler calculates the length of the buffer at runtime.

## Arguments
| | | |
|---|---|---|
| `const string` | `buffer` |    |
| `long` | `length` |    |

## Return values
0: success
<> 0: error

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Spooling overview and synopsis](overview_and_synopsis.md)
