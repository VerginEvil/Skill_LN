# cps.add.tree.detail.session()

## Syntax:
`function long cps.add.tree.detail.session( const string detail.session.code )`

## Description
Add a Tree-Detail session to detail area. Standard the detail session of cps.set.tree.detail is shown. The added tree detail can be activated with the function gbf.synchronize.detail(). Maximum of 4 Sessions can be added.

## Arguments
| | | |
|---|---|---|
| `const string` | `detail.session.code` |  The session code of the detail session which can be displayed in the detail area.  |

## Return values
| | |
|---|---|
| 0 | on success |
| -1 | on failure |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2390.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)

- [Composite Sessions Code Examples](examples.md)
