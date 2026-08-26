# Structure ChartManager synopsis
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated.
`#include <bic_eis>`
```

void
```
```

long
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
| | | |
|---|---|---|
|  | [create.node()](create.node.md) | `( string tree_name(25), string parent_id(25), string node_id(25), string node_desc(80), long node_class [, long process_id ] )` |
|  | [create.tree()](create.tree.md) | `( string tree_name(25), string tree_title(80) )` |
|  | [create.tree.button()](create.tree.button.md) | `( string tree_name(25), long button_id, string button_desc(80) [, long process_id ] )` |
|  | [destroy.tree()](destroy.tree.md) | `( string tree_name(25) [, long process_id ] )` |
|  | [get.tree.default()](get.tree.default.md) | `( )` |
|  | [get.tree.node.dpress()](get.tree.node.dpress.md) | `( ref long event(), ref long process_id, ref string node_id() )` |
|  | [get.tree.node.press()](get.tree.node.press.md) | `( ref long event(), ref long process_id, ref string node_id() )` |
|  | [get.tree.push.button()](get.tree.push.button.md) | `( ref long event(), ref long process_id, ref long button_id, ref string node_id() )` |
|  | [set.node.class()](set.node.class.md) | `( string tree_name(25), string node_id(25), long node_class [, long process_id ] )` |
|  | [set.node.class.color()](set.node.class.color.md) | `( string tree_name(25), long node_class, long class_color [, long process_id ] )` |
|  | [set.tree.background()](set.tree.background.md) | `( string tree_name(25), long color [, long process_id ]` |
|  | [set.tree.font()](set.tree.font.md) | `( string tree_name(25), long visible_level, long font [, long process_id ] )` |
|  | [set.tree.foreground()](set.tree.foreground.md) | `( string tree_name(25), long color [, long process_id ] )` |
|  | [set.tree.linewidth()](set.tree.linewidth.md) | `( string tree_name(25), long visible_level, long linewidth [, long process_id ] )` |
|  | [set.tree.name()](set.tree.name.md) | `( string tree_name(25), string tree_title(80) [, long process_id ] )` |
|  | [view.tree()](view.tree.md) | `( string tree_name(25), string node_id(25), long depth [, long process_id ] )` |

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Tree structures: example](example.md)
