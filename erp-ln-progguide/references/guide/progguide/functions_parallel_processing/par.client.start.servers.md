# par.client.start.servers()

## Syntax:
`function boolean par.client.start.servers( long group.id, [ long options ] )`

## Description
This function is used to actually start the application servers (Bshells) for the indicated group.

## Arguments
| | | |
|---|---|---|
| `long` | `group.id` |  ID which is returned by a previous call to [par.init.client.to.server()](par.init.client.to.server.md).  |
| `[ long` | `options ]` |  Optional argument which can be set to the values: CONTINUE_ON_SERVER_ERRORS and NO_REFS. These values can be combined for instance: CONTINUE_ON_SERVER_ERRORS+NO_REFS. When the option CONTINUE_ON_SERVER_ERRORS is not set (which is the default), processing will stop when one server aborts unexpectedly. When this option is set, processing will continue as long as there is one server available for processing messages. When the option NO_REFS is set, the server Bshells will not perform any database reference checking. Use this option with great care to prevent database corruption! This option requires a Bshell TIV level of at least 1752.  |

## Return values
| | |
|---|---|
| true | When all application servers started successfully |
| false | When one or more application servers could not be started |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
