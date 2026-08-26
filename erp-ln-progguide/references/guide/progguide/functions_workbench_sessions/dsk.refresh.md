# dsk.refresh()

## Syntax:
`function void dsk.refresh( long processId, long arg, string title )`

## Description
Send a request to the Workbench client to initiate a refresh and bring the Workbench session window into view. When a before.refresh callback was registered this callback function will be called before the refresh request is sent to the Workbench client. A before.refresh callback can be registered by using [dsk.set.before.refresh()](dsk.set.before.refresh.md) in a Workbench 3GL-session.
Note  This function is usually called by the session which started the Workbench 3GL session.

## Arguments
| | | |
|---|---|---|
| `long` | `processId` |  The process id of the Workbench 3GL session. Before calling this function make sure that this Workbench 3GL session is still running. This can be checked with function: [pstat()](../functions_processes/pstat.md).  |
| `long` | `arg` |  A parameter which will be passed to the Workbench 3GL session. Usually this is an XML object id.  |
| `string` | `title` |  a (new) title of the Workbench. When no new title is needed you can pass an empty string.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Workbench Sessions overview](overview.md)
- [Workbench Sessions synopsis](synopsis.md)
