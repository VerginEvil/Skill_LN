# DsCbarMenu

## Description
A DsCbarMenu object defines a menu bar and associated drop-down and cascaded menus. The menu bar is displayed across the top of a main window (DsCmwindow), below the title bar.
An application creates the entire menu with a single *create.object()* call. Subsequently, it can use *change.object()* toadd, remove, change, enable, and disable menu items.
Remember to specify the identification number of the DsCbarMenu object in the DsNbarMenu attribute of the parent window.

## Events
A DsCbarMenu object can generate the following event type:
| |
|---|
| EVTMENUSELECT |

## Attributes
| | | | |
|---|---|---|---|
|  DsNcommandList (long array)  | [CS] |  Use this to set the state of menu items and to remove menu items. The array contains one or more index/attribute pairs. The index is an index into the list created by DsNmenuData. The menu entry identified by each index (1-based) is set to the associated attribute value. Possible attribute values are: DSMENUNORMAL DSMENUDISABLED DSMENUCHECKED DSMENUREMOVE DSMENURADIOBUTTON You can modify or remove multiple menu items with a single *change.object()* call.  |  |
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |  |
|  DsNfunction (long)  | [CS] |  Specifies whether menu items are to be added before or after the point specified by DsNrefCommand. Possible values are: DSMENUINSERT (default) DSMENUAPPEND  |  |
|  DsNmenuData (void)  | [CSG] |  This contains the menu data in binary format. The data includes the structure of the menu, menu item names, shortcut and access keys, and the state and ID (return value) of menu items. The data must start with a header containing the following fields: long Version number (currently always 1). long Number of entries to follow. This is followed by multiple entries in the following format: long Menu hierarchy level. long Unique command identifier. Separators must always be assigned an ID of -1; cascaded menu entries must always be assigned an ID of 0. string Null terminated name string (mb). long State of menu items – possible values are: DSMENUNORMAL DSMENUDISABLED DSMENUCHECKED DSMENUREMOVE DSMENURADIOBUTTON You can use DsNmenuData to create a new menu and also to add items to existing menus.  |  |
|  DsNobjectType (long)  | [G] | The object type. |  |
|  DsNparent (long)  | [G] | The ID of the parent object. |  |
|  DsNrefCommand (long)  | [S] | This contains the index (1-based offset) of the menu position where menu items are to be added or inserted.  |  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |  |

## Examples
The following is an example of DsNmenuData data used to create a new menu:
*Version/Count* 1/ 12
| | | | |
|---|---|---|---|
| Level | ID | Name | Flag |
| 1 | 0 | &File | 0 |
| 2 | 15 | &Save | 0 |
| 2 | -1 | - | 0 |
| 2 | 23 | &Print\tCtrl + P | 0 |
| 2 | -1 | - | 0 |
| 2 | 37 | E&xit\tAlt + F4 | 0 |
| 1 | 0 | &Edit | 0 |
| 2 | 17 | &Undo | 0 |
| 2 | -1 | - | 0 |
| 2 | 6 | &Find... | 0 |
| 1 | 0 | &Help | 0 |
| 2 | 72 | &Contents | 0 |
The following function call creates the menu specified in DsNmenuData:
barmenu.id = create.object(barmenu_id, DsCbarMenu, parentWindow,
DsNmenuData, data, size)
The following is an example of DsNmenuData used to add new entries to the menu:
*Version/Count* 1/2
| | | | |
|---|---|---|---|
| Level | ID | Name | Flag |
| 2 | 90 | &Redo | 0 |
| 2 | 901 | &Delete | 0 |
The following function call adds the new entries after the Undo menu item:
```

change.object(barmenu_id, DsNmenuData, data, size, DsNrefCommand,
        8, DsNfunction, DSMENUAPPEND)
```
The following code disables the Print menu item and removes the Undo menu item:
```

long commandlist(4)

commandlist(1) = 4                      | index of Print menu item
commandlist(2) = DSMENUDISABLE
commandlist(3) = 8                      | index of Undo menu item
commandlist(4) = DSMENUREMOVE

change.object(barmenu.id, DsNcommandList, commandlist, 4)
```

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
