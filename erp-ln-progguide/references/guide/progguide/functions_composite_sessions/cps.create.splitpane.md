# cps.create.splitpane()

## Syntax:
`function long cps.create.splitpane( long orientation, long divider, [ long splitpane ] )`

## Description
Create a split pane which can either hold another split pane or a child session. There can only be one top-level split pane created. This function may not be called before the call to [cps.init()](cps.init.md)

## Arguments
| | | |
|---|---|---|
| `long` | `orientation` |  Specifies the splitter orientation: CPS.HORIZONTAL or CPS.VERTICAL  |
| `long` | `divider` |  Specifies the divider location as a percentage of the split panes total size. This must be a number between 0 and 100.  |
| `[ long` | `splitpane ]` |  optional id of the parent splitpane  |

## Return values
| | |
|---|---|
| <> 0 | The id of the created splitpane |
| 0 | When this funcion fails |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.

## Related topics
- [Composite Sessions overview](overview.md)
- [Composite Sessions synopsis](synopsis.md)
- [Composite Sessions Code Examples](examples.md)
