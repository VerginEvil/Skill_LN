# register.webpart.handler()

## Syntax:
`function void register.webpart.handler( const string type, const string handler )`

## Description
Registers a handler for the specified message type. When a message of this type is received from a webpart the specified function is called.

## Arguments
| | | |
|---|---|---|
| `const string` | `type` |  The message type.  |
| `const string` | `handler` |  The name of the function that should be called. This function must be defined in the script that calls the register.webpart.handler function.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Notes  This function is only usable in WebUI.

## Related topics
- [publish.webpart.message()](publish.webpart.message.md)
