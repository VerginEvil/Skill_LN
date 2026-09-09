# cps.init()

## Syntax:
`function long cps.init( [ long cps.type ] )`

## Description
Initialize the Composite Session Controller. This must be the first cps function called by the 3GL-Script. When this session was started from a parent session in modeless mode, this function will reactive the parent session. So any imports which must be done by this session from the parent should be done before this function is called.

## Arguments
| | |
|---|---|
| CPS.MULTIPLE_SESSIONS | Standard Composite Session. This is the default. |
| CPS.TREE_DETAIL_SESSION | A Tree-Detail Session. |

## Return values
| | |
|---|---|
| 0 | on success |
| -1 | on failure |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)

- [Composite Sessions Code Examples](examples.md)
