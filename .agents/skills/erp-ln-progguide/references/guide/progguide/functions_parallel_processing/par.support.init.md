# par.support.init()

## Syntax:
`function boolean par.support.init( ref long group.number, ref long tot.nr.servers )`

## Description
This function is used to initialize the communication for a support session. This function must be called at the start of a session which can be used as a parallel processing support session.
A session which acts as a parallel processing support session is used to handle questions from parallel processing servers. A parallel processing support session cannot at the same time be a parallel processing client session or a parallel processing server session.
Usually a support session runs without a user interface. Therefore such a session must call function [tc.ignore.process()](../functions_webtop/tc.ignore.process.md) during startup.

## Arguments
| | | |
|---|---|---|
| `ref long` | `group.number` |  Output argument which will be set to the current group number of which this support session will be a member.  |
| `ref long` | `tot.nr.servers` |  Output argument which will be set to the total number of servers in this group.  |

## Return values
| | |
|---|---|
| true | When this session is running in parallel processing support session mode. |
| false | When this session is not running in parallel processing support session mode. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)

- [Parallel Application Processing Examples](examples.md)
