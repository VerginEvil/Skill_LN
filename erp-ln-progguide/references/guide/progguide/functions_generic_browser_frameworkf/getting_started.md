# Getting started
This topic gives the first few steps to build a main application from scratch all the way up to a full application. The focus of the chapter is to get a script running. For readibility reasons the checking of return values and error handling is removed from the examples. It is advised to use the [Example](example.md) as a reference while reading this section.

## Minimal script:
1. In the include section of the main application, add the following: `#include <bic_gbf> | all GBF defines`
1. In the main function (or where appropriate) add: `gbf.init(gbf.current.library(), “”, GBF.MENU.ALL, GBF.BUTTON.ALL, GBF.OPT.DEFAULT + GBF.OPT.DEBUG)`
1. After this add: `gbf.start()`
1. Be sure to add the GBF library to the application in the Maintain Sessions (ttadv2100m000) session. In this session go to form 2 and click on *Scripts*, which should start the Maintain Program Scripts/Libraries (ttadv2130s000) session. Now click on *Libraries* and add the “ttgbfsrvlib” library.
1. Now the application can be compiled and run. There may be an error popup: “No top level function defined”, but that is OK for this moment.

## Basic Script
1. 1. 1.Add the function gbf.get.top.level() to the main application. Be sure to return 0. A compile and run of the program should now work without the previous described error popup.
1. 2. 2.Next fill the body of gbf.get.top.level(), by telling the GBF which are the top level objects. See also the manual page for gbf.add.interior(). function extern long gbf.get.top.level() { gbf.add.interior(“top key”, “top description”, 0) return (0) }
1. 3. 3.Compile and run the application and see what happens. In general the body of this function will contain a more elaborate SELECT statement.

## Normal Script
Now more objects have to be added to the script, which can be done using the function: [gbf.get.children()](gbf.get.children.md). See also [gbf.add.leaf()](gbf.add.leaf.md) and [gbf.add.object()](gbf.add.object.md).
Example:
```

function extern long gbf.get.children(const string key(), long
value, long level)
{
        gbf.add.leaf("leaf key 1", "leaf description 1", 0)
        gbf.add.leaf("leaf key 2", "leaf description 2", 0)
        gbf.add.leaf("leaf key 3", "leaf description 3", 0)
        return (0)
}
```
Compile and run the application and see what happens. In general the body of this function will contain a more elaborate SELECT statement.

## Full Script
Now the essential frame work of how to use the GBF is complete. More and more features may now be added. Do not forget to remove the GBF.OPT.DEBUG flag. The next table lists the functions and options that you can use to implement a feature.
| | |
|---|---|
| Feature | Functions and options to implement the feature  |
| buttons | gbf.init() and use the GBF.BUTTON options, gbf.set.button(),gbf.set.menu.item(), gbf.get.resource(), gbf.set.resource()  |
| debugging | gbf.init(), and use the GBF.OPT.DEBUG / GBF.OPT.POP.UP options  |
| cut, copy & paste | gbf.init(), gbf.menu.selected(), gbf.get.cutcopy(), gbf.get.cutcopynr()  |
| drag and drop |  gbf.init() and use the GBF.OPT.DRAG.DROP option, gbf.set.drop.function(),gbf.drag.drop()  |
| help | gbf.init(), gbf.set.help.function(), gbf.add.object(), gbf.help.selected()  |
| icons |  gbf.init() and use the GBF.OPT.SHADOWS option gbf.set.interior.icon(), gbf.set.leaf.icon(), gbf.add.object(), gbf.update.object()  |
| initialization | gbf.file.to.library(), gbf.current.library(),gbf.init(), gbf.start()  |
| labels | gbf.init() and use the GBF.OPT.NO.LABELS/GBF.OPT.<nr>.LABELS options, gbf.add.object()  |
| menus | gbf.init() and use the GBF.MENU options, gbf.set.menu.function(), gbf.set.menu.head(), gbf.set.menu.item(), gbf.set.menu.separator(), gbf.set.menu.state(), gbf.set.std.menu()  |
| multiple select | gbf.init() and use the GBF.OPT.MULTIPLE option, gbf.get.selected(), gbf.set.selected(), gbf.drag.drop(), gbf.menu.selected()  |
| object management |  gbf.add.header(), gbf.add.interior(), gbf.add.leaf(),gbf.add.object(), gbf.get.description(), gbf.set.drop.function(), gbf.update.object(), gbf.get.key.desc.length(), gbf.set.key.desc.length() see also the return values of: gbf.drag.drop() and gbf.menu.selected()  |
| open and close of nodes |  gbf.init() and use the GBF.MENU.FILE.READ/OPEN options, gbf.get.open.depth(), gbf.get.open.strategy(), gbf.set.open.depth(), gbf.set.open.strategy()  |
| printing | gbf.init(),gbf.set.tree.report.subtitle() |
| saving | gbf.init(), gbf.menu.selected() |
| selecting | gbf.init() and use the GBF.OPT.UNSELECT / GBF.OPT.NO.UNSELECT options  |
| searching | gbf.get.search.startegy(), gbf.set.search.startegy(), gbf.set.search.sensitive(), gbf.set.search.set(), gbf.set.search.what()  |
| sorting | gbf.get.sort.startegy(), gbf.set.sort.startegy()  |
| tree walking | gbf.get.current.parent(), gbf.get.first.child(), gbf.get.next(), gbf.get.parent(), gbf.is.displayed()  |
| window configuration | gbf.init() and use the GBF.OPT.1.WINDOW/GBF.OPT.2.WINDOWS, GBF.OPT.FORCE.SHADOW, GBF.OPT.<nr>.LABELS, GBF.OPT.FONT options, but see also gbf.get.resource(), gbf.set.resource(), gbf.add.object()  |

## Fan Out
In some (very large) applications you may need to fan out to different functions on the same action. For example selecting a menu item on an object will (if nothing has been changed) call gbf.menu.selected(). However, if the main application has different kinds of leaf nodes, it must call the right function, so the code in the main application will look like:
```

function extern long gbf.menu.selected(long obj.id,
                                const string object.key(),
                                long object.value,
                                long menu.option)
{
        long    retval
        on case menu.option
        case this.menu: | note: this.menu must be
                                | defined using gbf.set.menu.item()
                if  then
                        retval = do.menu.1(obj.id,
object.key,object.value, menu.option)
                else    if  then
                                retval = do.menu.2(obj.id,
object.key,object.value, menu.option)
                                else    if  then
                                        retval = do.menu.3(obj.id,
object.key,object.value, menu.option)
                …
                                endif
                        endif
                endif
                break
        case …:
                …
                break
        endcase

        return (…)
}
```
In other words the fan out to the different functions is done in the main application itself.
Another solution to this problem is that the GBF will do the fan out. This can be accomplished by setting the default function for the object during the gbf.add.object() to a value that was returned from a preceding gbf.set.child.function(). Now this function will be called instead of gbf.menu.selected(). In other words the fan out is done by the GBF.
This mechanism can also be applied for:
| | | |
|---|---|---|
| Fan out on | Function to set the fan out function  | Add to object |
|  children (for interior nodes)  | gbf.set.child.function | gbf.add.object |
| drag and drop | gbf.set.drag.drop | gbf.add.object |
| help | gbf.set.help.function | gbf.add.object |
| menu | gbf.set.menu.function, gbf.set.menu.item | gbf.add.object |

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
