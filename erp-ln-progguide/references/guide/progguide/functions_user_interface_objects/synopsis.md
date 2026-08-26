# User interface objects synopsis
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated. The Programmable Dialogs API can be used as an alternative.
```

void
```
```

void
```
```

long
```
```

long
```
```

long
```
```

long
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

long
```
```

long
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

long
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
| | | |
|---|---|---|
|  | [change.object()](change.object.md) | `( long object_id [, long attribute, value [, size] ] ... )` |
|  | [change.sub.object](change.sub.object.md) | `( long object, long sub_object_id [, long attribute, value [, size] ] ... )` |
|  | [compress.pixmap()](compress.pixmap.md) | `( long colormap(), long num_colors, string pixmap(), long width, long height, ref string buffer(), ref long buffer_length )` |
|  | [create.object()](create.object.md) | `( long type, long parent_object [, long attribute, value [, size] ] ... )` |
|  | [create.sub.object()](create.sub.object.md) | `( long object, long type, [, long attribute, value [, size] ] ... )` |
|  | [create.sub.object.by.id()](create.sub.object.by.id.md) | `( long object, long sub_object_id, long type [, long attribute, value [, size] ] ... )` |
|  | [decompress.pixmap()](decompress.pixmap.md) | `( string buffer(), ref long colormap(), ref string pixmap() )` |
|  | [destroy.object()](destroy.object.md) | `( long object_id )` |
|  | [destroy.sub.object()](destroy.sub.object.md) | `( long object, long sub_object_id )` |
|  | [get.object()](get.object.md) | `( long object_id [, long attribute, ref value [, ref value] ] ... )` |
|  | [get.pixmap.info()](get.pixmap.info.md) | `( ref string buffer(), ref long num_colors, ref long width, ref long height )` |
|  | [get.sub.object()](get.sub.object.md) | `( long object, long sub_object_id [, long attribute, ref value [, ref size] ] ... )` |
|  | [inherit.object()](inherit.object.md) | `( long process_nr, long object_id )` |
|  | [lower.object()](lower.object.md) | `( long object_id )` |
|  | [map.object()](map.object.md) | `( long object_id )` |
|  | [query.object()](query.object.md) | `( long object_id [, long attribute, value [, size] ] ... [, long attribute, ref value [, ref size] ] ... )` |
|  | [query.sub.object()](query.sub.object.md) | `( long object_id, long sub_object_id [, long attribute, value [, size] ] ... [, long attribute, ref value [, ref size] ] ... )` |
|  | [raise.object()](raise.object.md) | `( long object_id )` |
|  | [set.focus()](set.focus.md) | `( long object_id )` |
|  | [set.sensitive()](set.sensitive.md) | `( long object_id, long status )` |
|  | [unmap.object()](unmap.object.md) | `( long object_id )` |
|  | [unset.focus()](unset.focus.md) | `( long object_id )` |
|  | [update.object()](update.object.md) | `( long object_id )` |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
