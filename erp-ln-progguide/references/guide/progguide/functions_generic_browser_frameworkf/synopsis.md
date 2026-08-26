# Generic Browser Framework (GBF) synopsis
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

string
```
```

long
```
```

long
```
```

string
```
```

long
```
```

string
```
```

string
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
long
```
```
long
```
```

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
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [gbf.add.column()](gbf.add.column.md) | `(const string column.name(), const string column.label() mb, [boolean is.initially.hidden])` |
|  | [gbf.add.header()](gbf.add.header.md) | `(const string object.key(), const string object.description() mb, long object.value)` |
|  | [gbf.add.interior()](gbf.add.interior.md) | `(const string object.key(), const string object.description() mb, long object.value)` |
|  | [gbf.add.leaf()](gbf.add.leaf.md) | `(const string object.key(), const string object.description() mb, long object.value)` |
|  | [gbf.add.object()](gbf.add.object.md) | `(const string object.key(), const string object.description() mb, longobject.value, long obj.type, [long icon.set, long default.function.id, long help.function.id, long drop.function.id, long menumask, long text.color, long line.style, long context.menu.id])` |
|  | [gbf.current.library()](gbf.current.library.md) | `()` |
|  | [gbf.create.context.menu()](gbf.create.context.menu.md) | `()` |
|  | [gbf.delete.object()](gbf.delete.object.md) | `(long obj.id)` |
|  | [gbf.desc.to.column()](gbf.desc.to.column.md) | `(string column1, ...)` |
|  | [gbf.enable.drop()](gbf.enable.drop.md) | `(const string session.code, const string dllname, const string gbf.on.drop)` |
|  | [gbf.error.string()](gbf.error.string.md) | `(long error)` |
|  | [gbf.file.to.library()](gbf.file.to.library.md) | `(const string filename())` |
|  | [gbf.get.current.parent()](gbf.get.current.parent.md) | `()` |
|  | [gbf.get.cutcopy()](gbf.get.cutcopy.md) | `(long index, ref string obj.key(), ref string obj.desc() mb, ref long obj.value)` |
|  | [gbf.get.cutcopy.nr()](gbf.get.cutcopy.nr.md) | `()` |
|  | [gbf.get.description()](gbf.get.description.md) | `( long obj.id, ref string description() mb)` |
|  | [gbf.get.first.child()](gbf.get.first.child.md) | `( long obj.id, long force.read, ref long child.id, ref string child.key(), ref long child.value, ref long child.type)` |
|  | [gbf.get.key.desc.length()](gbf.get.key.desc.length.md) | `(ref long key.length, ref long desc.length)` |
|  | [gbf.get.next()](gbf.get.next.md) | `( long obj.id, ref long next.id, ref string next.key(), ref long next.value, ref long next.type)` |
|  | [gbf.get.object.info()](gbf.get.object.info.md) | `( long obj.id, ref string key(), ref string description(), ref long value, ref long type)` |
|  | [gbf.get.open.depth()](gbf.get.open.depth.md) | `(ref long open.depth)` |
|  | [gbf.get.open.strategy()](gbf.get.open.strategy.md) | `(ref long open.type)` |
|  | [gbf.get.parent()](gbf.get.parent.md) | `( long obj.id, ref long parent.id, ref string parent.key(), ref long parent.value)` |
|  | [gbf.get.previous()](gbf.get.previous.md) | `( long obj.id, ref long prev.id, ref string prev.key(), ref long prev.value, ref long prev.type)` |
|  | [gbf.get.print.options()](gbf.get.print.options.md) | `(ref long print.options)` |
|  | [gbf.get.read.levels()](gbf.get.read.levels.md) | `( ref long read.levels, [ref long show.levels])` |
|  | [gbf.get.refresh.strategy()](gbf.get.refresh.strategy.md) | `( ref long refresh.rate, ref long refresh.type)` |
|  | [gbf.get.resource()](gbf.get.resource.md) | `( long resource.type, ref resource.value, …)` |
|  | [gbf.get.search.strategy()](gbf.get.search.strategy.md) | `(ref long search.strategy)` |
|  | [gbf.get.selected()](gbf.get.selected.md) | `( long index, ref long obj.id, ref string obj.key(), ref long obj.value, ref long obj.type)` |
|  | [gbf.get.selected.nr()](gbf.get.selected.nr.md) | `()` |
|  | [gbf.get.sort.strategy()](gbf.get.sort.strategy.md) | `(ref long sort.strategy)` |
|  | [gbf.get.view.depth()](gbf.get.view.depth.md) | `(ref long view.depth)` |
|  | [gbf.init()](gbf.init.md) | `(const string library(), const string title(), [long default.menu, long default.button, long default.options, long standard.button, long default.context])` |
|  | [gbf.is.displayed()](gbf.is.displayed.md) | `(const long obj.id)` |
|  | [gbf.set.button()](gbf.set.button.md) | `( const string button.group(), const string normal.button(), const string selected.button(), const string insensitive.button(), const string button.name(), long menu.item, long add.space)` |
|  | [gbf.set.child.function()](gbf.set.child.function.md) | `(const string dll_id(), const string child.function.name(), long is.default)` |
|  | [gbf.set.buttonstate()](gbf.set.buttonstate.md) | `( long button.id, long button.state)` |
|  | [gbf.set.color()](gbf.set.color.md) | `(long color, const string color.desc())` |
|  | [gbf.set.column()](gbf.set.column.md) | `(long obj.id, const string column.name(), cont string object.desc() mb)` |
|  | [gbf.set.desc.length()](gbf.set.desc.length.md) | `(long desc.length)` |
|  | [gbf.set.drop.function()](gbf.set.drop.function.md) | `(const string dll_id(), const string drop.function.name(), long is.default)` |
|  | [gbf.set.header.icon()](gbf.set.header.icon.md) | `(const string icon.group(), const string icon(), long is.default, [const string icon.desc()]` |
|  | [gbf.set.help.function()](gbf.set.help.function.md) | `(const string dll_id(), const string help.function.name(), long is.default)` |
|  | [gbf.set.interior.icon()](gbf.set.interior.icon.md) | `(const string icon.group(), const string unselected.closed(), const string unselected.open(), const string selected.closed(), const string unselected.open(), long is.default, [const string icon.desc(), long context.menu]` |
|  | [gbf.set.key.desc.length()](gbf.set.key.desc.length.md) | `(long key.length, long desc.length)` |
|  | [gbf.set.key.length()](gbf.set.key.length.md) | `(long key.length)` |
|  | [gbf.set.label() *](gbf.set.labelxxx.md) | `(const string label1(), const string label2(), const string label3(), const string label4(), const string label5())` |
|  | [gbf.set.label() *](gbf.set.labelxxx.md) | `(const string label())` |
|  | [gbf.set.label() *](gbf.set.labelxxx.md) | `(const string label())` |
|  | [gbf.set.label() *](gbf.set.labelxxx.md) | `(const string label())` |
|  | [gbf.set.label() *](gbf.set.labelxxx.md) | `(const string label())` |
|  | [gbf.set.label() *](gbf.set.labelxxx.md) | `(const string label())` |
|  | [gbf.set.leaf.icon()](gbf.set.leaf.icon.md) | `(const string icon.group(),const string unselected(),const string selected(), long is.default,[const string icon.desc(), long context.menu]` |
|  | [gbf.set.menu.checked()](gbf.set.menu.checked.md) | `(long item.id)` |
|  | [gbf.set.menu.disabled()](gbf.set.menu.disabled.md) | `(long item.id)` |
|  | [gbf.set.menu.enabled()](gbf.set.menu.enabled.md) | `(long item.id)` |
|  | [gbf.set.menu.not.checked()](gbf.set.menu.not.checked.md) | `(long item.id)` |
|  | [gbf.set.menu.not.radio()](gbf.set.menu.not.radio.md) | `(long item.id)` |
|  | [gbf.set.menu.radio()](gbf.set.menu.radio.md) | `(long item.id)` |
|  | [gbf.set.menu.function()](gbf.set.menu.function.md) | `(const string dll_id(), const string menu.function.id(), long is.default)` |
|  | [gbf.set.menu.head()](gbf.set.menu.head.md) | `(string menu.text, [long maskbit, long multi.mask])` |
|  | [gbf.set.menu.item()](gbf.set.menu.item.md) | `( long menu.id, const string menu.text(), const string keystroke(), [ long is.default, long menu.function.id, long maskbit, long multi.mask, long std.button])` |
|  | [gbf.set.menu.state()](gbf.set.menu.md) | `(long item.id)` |
|  | [gbf.set.menu.state()](gbf.set.menu.md) | `(long item.id)` |
|  | [gbf.set.menu.state()](gbf.set.menu.md) | `(long item.id)` |
|  | [gbf.set.menu.separator()](gbf.set.menu.separator.md) | `(long menu.id)` |
|  | [gbf.set.menu.state()](gbf.set.menu.md) | `(long menu.id, long item.id, long disable, long checked, [long radio])` |
|  | [gbf.set.open.child() *](gbf.set.open.child.md) | `(long open.strategy)` |
|  | [gbf.set.open.depth()](gbf.set.open.depth.md) | `(long open.depth)` |
|  | [gbf.set.open.read() *](gbf.set.open.read.md) | `(long open.strategy)` |
|  | [gbf.set.open.strategy() *](gbf.set.open.md) | `(long open.strategy)` |
|  | [gbf.set.open.what() *](gbf.set.open.what.md) | `(long open.strategy)` |
|  | [gbf.set.print.options()](gbf.set.print.options.md) | `(long print.options)` |
|  | [gbf.set.read.levels()](gbf.set.read.levels.md) | `(long read.levels, [ long show.levels])` |
|  | [gbf.set.refresh.strategy()](gbf.set.refresh.strategy.md) | `(long refresh.rate, long refresh.type)` |
|  | [gbf.set.resource()](gbf.set.resource.md) | `(long resource.type, resource.value, …)` |
|  | [gbf.set.search.headers() *](gbf.set.search.headers.md) | `(long search.strategy)` |
|  | [gbf.set.search.sensitive() *](gbf.set.search.sensitive.md) | `(long search.strategy)` |
|  | [gbf.set.search.set() *](gbf.set.search.set.md) | `(long search.strategy)` |
|  | [gbf.set.search.strategy() *](gbf.set.searchxxx.md) | `(long search.strategy)` |
|  | [gbf.set.search.what() *](gbf.set.search.what.md) | `(long search.strategy)` |
|  | [gbf.set.selected()](gbf.set.selected.md) | `( long obj.id)` |
|  | [gbf.set.sort.strategy()](gbf.set.sort.strategy.md) | `(long sort.strategy)` |
|  | [gbf.set.std.menu() *](gbf.set.std.menu.md) | `(long menu.pattern, long disable, long checked)` |
|  | [gbf.set.std.menu.checked() *](gbf.set.std.menu.checked.md) | `(long menu.pattern)` |
|  | [gbf.set.std.menu.disabled() *](gbf.set.std.menu.disabled.md) | `(long menu.pattern)` |
|  | [gbf.set.std.menu.enabled() *](gbf.set.std.menu.enabled.md) | `(long menu.pattern)` |
|  | [gbf.set.std.menu.not.checked() *](gbf.set.std.menu.not.checked.md) | `(long menu.pattern)` |
|  | [gbf.set.tree.report.subtitle()](gbf.set.tree.report.subtitle.md) | `(const string sub.title(80) mb)` |
|  | [gbf.set.view.depth()](gbf.set.view.depth.md) | `(long view.depth)` |
|  | [gbf.synchronize.detail()](gbf.synchronize.detail.md) | `(long key.object)` |
|  | [gbf.sync.from.details()](gbf.sync.from.details.md) | `(long key.object, long update.mode` |
|  | [gbf.start()](gbf.start.md) | `([long read.levels, long show.levels])` |
|  | [gbf.update.deffunc()](gbf.update.deffunc.md) | `( long obj.id, long default.function.id)` |
|  | [gbf.update.desc()](gbf.update.desc.md) | `( long obj.id, const string object.description() mb)` |
|  | [gbf.update.dropfunc()](gbf.update.dropfunc.md) | `( long obj.id, long drop.function.id)` |
|  | [gbf.update.icon()](gbf.update.icon.md) | `( long obj.id, long icon.set)` |
|  | [gbf.update.menumask()](gbf.update.menumask.md) | `( long obj.id, long menumask)` |
|  | [gbf.update.object() *](gbf.update.md) | `(long obj.id, long object.description() mb [, long icon.set] [, long default.function.id] [, long drop.function.id] [, long menumask] [, long text.color] [, long line.style])` |
The following is a list of functions called by the Generic Browser Framework that must be defined within the application. The return values as described in the [Generic Browser Framework error codes and return values](error_codes_and_return_values.md), must be used otherwise the GBF may stop the application.
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

long
```
| | | |
|---|---|---|
|  | [gbf.bms.received()](gbf.bms.received.md) | `( long sender.id, const string mask(), const string mss(), long length)` |
|  | [gbf.drag.drop()](gbf.drag.drop.md) | `( long drag.obj, const string drag.key(), long drag.value, long drag.type, long drop.obj, const string drop.key(), long drop.value, long drop.type, long button.mode)` |
|  | [gbf.get.children()](gbf.get.children.md) | `( const string object.key(), long object.value, long cur.level)` |
|  | [gbf.get.top.level()](gbf.get.top.level.md) | `()` |
|  | [gbf.help.selected()](gbf.help.selected.md) | `( long obj.id, const string object.key(), long object.value, long help.value)` |
|  | [gbf.menu.selected()](gbf.menu.selected.md) | `( long obj.id, const string object.key(), long object.value, long menu.option)` |
|  | [gbf.on.drag()](gbf.on.drag.md) | `(long to.pid, const string to.session, long drag.obj, const string drag.key, long drag.value, long drag.type, reference long collection )` |
|  | [gbf.on.drop()](gbf.on.drop.md) | `(long from.pid, long collection, long drop.obj, const string drop.key, long drop.value, long drop.type, boolean copy)` |
|  | [gbf.on.selection()](gbf.on.selection.md) | `( long obj.id, long obj.type, long transition)` |
|  | [gbf.save()](gbf.save.md) | `( long obj.id, const string object.key(), long object.value, long save.type)` |

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
