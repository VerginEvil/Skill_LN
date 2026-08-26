# Generic Browser Framework error codes and return values
The GBF error codes must be interpreted as follows:
| | |
|---|---|
| >= 0 |  Successful completion If the function at hand has a meaningful non-zero return value, for example, an object identification (usually given as obj.id), or count of objects, then that number will be returned. If the function only returns a status, for example, update successful, then 0 will be returned.  |
| < 0 |  Unsuccessful completion The actual returned number indicates a more precise reason of the failure. See also the function [gbf.error.string()](gbf.error.string.md) which translates any of these error codes and return values into its mnemonic string.  |
Possible successful completion return values (thus all >= 0) and their meaning:
| | |
|---|---|
| Mnemonic | Meaning |
| 0 | Generic successful completion return value |
| GBF.CYCLE | Cycles detected |
| GBF.NO.CHILDREN | Given object by its obj.id does not have any children |
| GBF.NO.READ.CHILDREN | Children of obj.id are not yet read |
| GBF.LAST | Returned next object is last sibling |
| GBF.TOP.LEVEL | Returned parent is top (root) level |
Possible error return values (thus all < 0) and their meaning is:
| | |
|---|---|
| Mnemonic | Meaning |
| GBF.ARG.ERROR | Cannot store value in given argument |
| GBF.CHILD.ABORT | Application requested GBF termination |
| GBF.CHILD.EXIT | Application requested GBF exiting |
| GBF.DRAW.ERROR | Drawing failed: bitmap, line, shadow |
| GBF.EXPR.ERROR | Search expression error |
| GBF.ICON.EMPTY | Given icon string is empty |
| GBF.ICON.LOAD.ERROR | Icon could not be found and/or loaded |
| GBF.ILL.BITMAP | Illegal bitmap given |
| GBF.ILL.BUTTON | The given button is illegal. |
| GBF.ILL.DLL | Given DLL is unknown |
| GBF.ILL.FUNCTION | Given function is unknown |
| GBF.ILL.ICON | Given icon identification is unknown |
| GBF.ILL.LENGTH | Illegal key or description length |
| GBF.ILL.LEVEL | illegal level specified in [gbf.start()](gbf.start.md) |
| GBF.ILL.MENU.ID | Given menu.id is unknown |
| GBF.ILL.OBJECT | Unknown object reference given |
| GBF.ILL.OPEN.TYPE | Illegal open type given |
| GBF.ILL.REFRESH.RATE | Given refresh rate is illegal |
| GBF.ILL.REFRESH.TYPE | Illegal refresh type given |
| GBF.ILL.RESOURCE.TYPE | Unknown resource type specified |
| GBF.ILL.RESOURCE.VALUE | Invalid value for this resource type |
| GBF.ILL.SEARCH.TYPE | Illegal search type given |
| GBF.ILL.SORT.TYPE | Illegal sort type given |
| GBF.ILL.STATE | Illegal GBF state for this function |
| GBF.INTERNAL.ERROR | Internal error of the GBF |
| GBF.MAX.MENU | Too many menus or submenus defined |
| GBF.MENU.EMPTY | Given menu string is empty |
| GBF.NO.BUTTONS | The specified button does not exist |
| GBF.NO.DEFAULT.ICONS | GBF could not load all default icons |
| GBF.NO.GRAPHICS | GBF cannot run on an ASCII display |
| GBF.NO.LABEL | GBF configured without this label |
| GBF.NO.MEMORY | Not enough memory |
| GBF.NO.MENU | Not enough memory for menu |
| GBF.NO.MORE.RESOURCES | No more (free) resources available |
| GBF.NOT.EXPECTED | GBF did not expect this function call |
| GBF.NOT.INTERIOR | Given object is not an interior object |
| GBF.SEQ.IO.ERROR | Errors with sequential file I/O |
| GBF.STOP.READING | Reading stop on user request |
There is no general recipe about what to do with these errors. Some errors are typically development errors, such as: GBF.ILL.RESOURCE.TYPE, GBF.ILL.LENGTH, whereas others are typically run time errors when running at the customer site, such as: GBF.NO.MEMORY or GBF.SEQ.IO.ERROR. If an error occurs on a user action (if the user pushed a button, selected a menu item and so on.) a generic message should be given which tells the user that the operation failed. Since (in general) the user is unaware of the details there should be no detailed message given. In all cases it is advised to log these errors. The GBF will log some of these errors into a persistent log file. This log file is: $BSE/log.<kk><mmm>, where the <kk> is the package name of the current session and <mmm> the module name of the current session (or in other words: the first 5 characters of the current session name), where the session name is the current value of the global: prog.name$.
Sample code could be:
```

long    retval
retval = gbf.SomeGBFFunction(arg1, arg2, …)
if retval < 0 then
        mess("operation failed", 1)
        return (0)      | or: return (GBF.DO.EXIT)
endif
```

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
