# Allowed functions
The Generic Browser Framework (GBF) goes through several states during its lifecycle from the start till the end of a session.
| | |
|---|---|
| State | Description |
| GBF chaos (Yellow) | This state indicates that the main session has started, but no actions to the GBF have been done yet, hence the state of the GBF is undetermined and no functions, except [gbf.init()](gbf.init.md) should be used.  |
| GBF initialized (Blue) | This state indicates that a [gbf.init()](gbf.init.md) has been received, which means that the GBF is initializing itself, and waiting for a gbf.start(). In this state the main session is still in control.  |
| GBF running (Green) | This state indicates that now the GBF is in control, due to a [gbf.start()](gbf.start.md). The GBF will be in control until it is told to terminate.  |
| GBF terminated (Red) | This state indicates that the GBF just has relinquished control and handed it back to the main session. In this state some settings can still be retrieved from the GBF. The GBF waits for session termination or for a new [gbf.init()](gbf.init.md).  |
The next table lists in which state the GBF functions are allowed to be used:
| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
|  | State: |  |  |  |  |  |  |  |  |
| Function | Yellow | Blue | Green | Red |  |  |  |  |  |
| gbf.add.object |  |  | yes: 3, 4 |  |  |  |  |  |  |
| gbf.current.library | yes | yes | yes | yes |  |  |  |  |  |
| gbf.create.context.menu |  | yes |  |  |  |  |  |  |  |
| gbf.enable.drop |  | yes |  |  |  |  |  |  |  |
| gbf.error.string | yes | yes | yes | yes |  |  |  |  |  |
| gbf.delete.object |  |  | yes: 5 |  |  |  |  |  |  |
| gbf.drag.drop |  |  | yes |  |  |  |  |  |  |
| gbf.get.cutcopy |  |  | yes | yes |  |  |  |  |  |
| gbf.get.cutcopy.nr |  |  | yes | yes |  |  |  |  |  |
| gbf.file.to.library | yes | yes | yes | yes |  |  |  |  |  |
| gbf.get.description |  |  | yes | yes |  |  |  |  |  |
| gbf.get.current.parent |  |  | yes: 1, 3, 4 |  |  |  |  |  |  |
| gbf.get.first.child |  |  | yes: 1, 2, 5, 6, 7 | yes |  |  |  |  |  |
| gbf.get.icon |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.key.desc.length |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.next |  |  | yes: 1, 2, 5, 6, 7 | yes |  |  |  |  |  |
| gbf.get.object.info |  |  | yes | yes |  |  |  |  |  |
| gbf.get.next |  |  | yes: 1, 2, 5, 6, 7 | yes |  |  |  |  |  |
| gbf.get.open.depth |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.open.strategy |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.parent |  |  | yes: 1, 2, 5, 6, 7 | yes |  |  |  |  |  |
| gbf.get.print.options |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.read.levels |  |  | yes | yes |  |  |  |  |  |
| gbf.get.refresh.strategy |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.resource |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.search.strategy |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.selected |  |  | yes: 1, 2, 5, 6, 7 | yes |  |  |  |  |  |
| gbf.get.selected.nr |  |  | yes | yes |  |  |  |  |  |
| gbf.get.sort.strategy |  | yes | yes | yes |  |  |  |  |  |
| gbf.get.children |  |  | yes |  |  |  |  |  |  |
| gbf.get.top.level |  |  | yes |  |  |  |  |  |  |
| gbf.help.selected |  |  | yes |  |  |  |  |  |  |
| gbf.init | yes | yes |  | yes |  |  |  |  |  |
| gbf.is.displayed |  | yes | yes | yes |  |  |  |  |  |
| gbf.menu.selected |  |  | yes |  |  |  |  |  |  |
| gbf.save |  |  | yes |  |  |  |  |  |  |
| gbf.set.button |  | yes | yes |  |  |  |  |  |  |
| gbf.set.buttonstate |  | yes | yes |  |  |  |  |  |  |
| gbf.set.color |  | yes | yes |  |  |  |  |  |  |
| gbf.set.child.function |  | yes | yes |  |  |  |  |  |  |
| gbf.set.drop.function |  | yes | yes |  |  |  |  |  |  |
| gbf.set.help.function |  | yes | yes |  |  |  |  |  |  |
| gbf.set.header.icon |  | yes | yes |  |  |  |  |  |  |
| gbf.set.interior.icon |  | yes | yes |  |  |  |  |  |  |
| gbf.set.key.desc.length |  | yes |  |  |  |  |  |  |  |
| gbf.set.label |  | yes | yes |  |  |  |  |  |  |
| gbf.set.leaf.icon |  | yes | yes |  |  |  |  |  |  |
| gbf.set.menu.function |  | yes | yes |  |  |  |  |  |  |
| gbf.set.menu.head |  | yes |  |  |  |  |  |  |  |
| gbf.set.menu.item |  | yes |  |  |  |  |  |  |  |
| gbf.set.menu.separator |  | yes |  |  |  |  |  |  |  |
| gbf.set.menu.state |  | yes | yes |  |  |  |  |  |  |
| gbf.set.open.depth |  |  |  |  |  |  |  |  |  |
| gbf.set.open.strategy and so on. |  | yes | yes |  |  |  |  |  |  |
| gbf.set.print.options |  | yes | yes | yes |  |  |  |  |  |
| gbf.set.read.levels |  |  | yes |  |  |  |  |  |  |
| gbf.set.refresh.strategy |  | yes | yes |  |  |  |  |  |  |
| gbf.set.resource |  | yes | yes |  |  |  |  |  |  |
| gbf.set.search.strategy etc |  | yes | yes |  |  |  |  |  |  |
| gbf.set.selected |  | yes |  |  |  |  |  |  |  |
| gbf.set.sort.strategy |  | yes | yes |  |  |  |  |  |  |
| gbf.set.std.menu |  | yes | yes |  |  |  |  |  |  |
| gbf.start |  | yes |  |  |  |  |  |  |  |
| gbf.set.tree.report.subtitle | yes | yes | yes | yes |  |  |  |  |  |
| gbf.update.object |  |  | yes: 1, 2, 5, 6, 7 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
In the GBF running state there are further restrictions if the yes is followed by a sequence of numbers. These numbers refer to:
| | |
|---|---|
| 1. | gbf.bms.received() |
| 2. | gbf.drag.drop() |
| 3. | gbf.get.children() |
| 4. | gbf.get.top.level() |
| 5. | gbf.menu.selected() |
| 6. | gbf.help.selected() |
| 7. | gbf.save() |
It can be that this is not enforced by the GBF, so for example a gbf.get.first.child() call during a gbf.get.top.level()can be run without an error.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
