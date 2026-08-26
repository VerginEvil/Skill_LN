# set.tree.font()

## Syntax:
`function void set.tree.font( string tree_name, long visible_level, long font, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This changes the font used for nodes at a particular level in a specified tree. Use *load.font()* to load the font that you want to use.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree for which you want to change the font.  |
| `long` | `visible_level` |  This is a number, in the range 1 to 3, that specifies the node level to which the new font is to be applied. Visible level 1 specifies the highest level currently visible in the tree. Visible level 3 specifies levels three and below. See [view.tree()](view.tree.md).  |
| `long` | `font` |  The font to be applied to the specified node level.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree for which the font must be changed. If you do not include this argument, the new font is applied to the specified level in all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long mask, font, proc_id
long request(FNTMAXSIZE)
long reply(FNTMAXSIZE)

proc_id = create.tree("test", "Test Structure Chart Manager")

mask = FNTHEIGHT + FNTWEIGHT + FNTSLANT
fnt.weight(request) = FNTMEDIUM
fnt.height(request) = 12
fnt.slant(request) = FNTROMAN
font = load.font(current.display(), mask, request, reply)
set.tree.font("test", 1, font, proc_id)
```

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
