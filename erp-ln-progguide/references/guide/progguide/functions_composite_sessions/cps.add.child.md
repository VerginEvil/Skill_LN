# cps.add.child()

## Syntax:
`function long cps.add.child( const string session.code, long bars, const string title, long splitpane )`

## Description
Add a child session to this controller, which will be shown and started in the frame of the composite controller. This session will be shown in the passed split pane. To a split pane exactly two objects must be added: sessions and/or split panes. The order of adding these objects to the split pane determines the order on the screen (left/right or top/bottom).

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  The code of the child session  |
| `long` | `bars` |  Indicates which bars must be shown for this composite child. Possible values are:CPS.TOOLBAR and CPS.MENUBAR. These values can be combined for instance: CPS.TOOLBAR+CPS.MENUBAR  |
| `const string` | `title` |  Contains the title string for this child session. When empty, no title bar will be shown for this composite child session.  |
| `long` | `splitpane` |  id of the split pane in which this session will be shown  |

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
