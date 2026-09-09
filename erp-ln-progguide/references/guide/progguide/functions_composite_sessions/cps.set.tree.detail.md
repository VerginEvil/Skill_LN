# cps.set.tree.detail()

## Syntax:
`function long cps.set.tree.detail( const string tree.session.code, const string detail.session.code, [ long divider, const string tree.title ] )`

## Description
Sets the GBF session and Details sesion of a Tree-Detail session. The GBF session and Details session will be shown and started in the frame of the composite controller.

## Arguments
| | | |
|---|---|---|
| `const string` | `tree.session.code` |  The code of the GBF-tree session.  |
| `const string` | `detail.session.code` |  The code of the Details session.  |
| `[ long` | `divider ]` |  Specifies the divider location as a percentage of the Tree-Detail session total size. This must be a number between 0 and 100. As default the frontend decide what percentage will be used.  |
| `[ const string` | `tree.title ]` |  Specifiess the title that will be displayed in the toolbar above the Tree. When empty, no title will be displayed in the toolbar above the Tree. As default the title of the GBF session will be used.  |

## Return values
| | |
|---|---|
| 0 | on success |
| -1 | on failure |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2230.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)

- [Composite Sessions Code Examples](examples.md)
