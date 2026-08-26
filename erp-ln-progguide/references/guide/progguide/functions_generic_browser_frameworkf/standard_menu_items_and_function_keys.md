# standard menu items and function keys

## Standard menuitems
The GBF allows to define a set of standard menu items, see [gbf.init()](gbf.init.md).
| | | | |
|---|---|---|---|
| Menu | Sub- menu | Key | Description |
| File | New | Ctrl+N | Insert a new object, implemented by the application  |
|  | Open all | Ctrl+O | Open all interior nodes whose children have already been read before (so do not read what is not yet there, see *read all*)  |
|  | Read all | Ctrl+R | Read the whole tree into memory (but do not show it, see *open all*)  |
|  | Refresh | F5 | Refresh the current contents using the current refresh strategy  |
|  | Font… |  | Start change font dialog. |
|  | Save | Ctrl+S | Save the given object or whole tree |
|  | Save + Exit | Ctrl+Q | Save the given object or whole tree and exit the GBF  |
|  | Print Options… |  | Set some print options, which will be used when the GBF starts printing  |
|  | Print | Ctrl+P | Print the whole object tree as it is currently displayed  |
|  | Exit | Alt+F4 | Exit the GBF |
| Edit | Undo | Ctrl+Z | Undo, implemented by application |
|  | Cut | Ctrl+X | Cut, implemented by application |
|  | Copy | Ctrl+C | Copy, implemented by application |
|  | Paste | Ctrl+V | Paste, implemented by application |
|  | Delete | Delete | Delete, implemented by application |
|  | Text | Ctrl+T | Text, implemented by application |
| Find | By description… | Ctrl+F |  Start searching for objects where the given pattern matches parts of the object description. Note: the Ctrl+F starts the last search which is either a “By description…” or a “By code…” search.  |
|  | By code… |  |  Start searching for objects where the given pattern matches parts of the object key. Note: the Ctrl+F starts the last search which is either a “By description…” or a “By code…” search.  |
|  | First |  | Set focus on the first found object, only enabled if there are found objects. If object not shown on the screen then display it including all its parents  |
|  | Next | Ctrl+G |  Set focus on the next found object. If the current object is already the last found object, then leave the focus on this last object. Only enabled when there are found objects. If object not shown on the screen then display it including all its parents.  |
|  | Previous | Ctrl+ Shift+G | Set focus on the previous found object. If the current object is already the first object, then leave the focus on this first object. Only enabled when there are found objects. If object not shown on the screen then display it including all its parents.  |
|  | Last |  |  Set focus on the last object only enabled when there are found objects. If object not shown on the screen then display it including all its parents.  |
|  | Search in current set |  | Only what is currently in GBF memory will be searched through.  |
|  | Read before search |  |  Before the search is started, everything which is NOT yet known to the GBF is asked (see gbf.get.childrengbf.get.children ) from the main application, that is the whole set is used to search in this is the GBF.SEARCH.ALLsearch strategy (see gbf.set.search.strategy() ).  |
|  | Match case |  |  Do not ignore case differences this is the GBF.SEARCH.SENSITIVE search strategy (see gbf.set.search.strategy()).  |
| Sort | None |  | Do not sort the objects and keep the order in which they are handed over by the main application.  |
|  | By description |  | Sort the objects using their description. |
|  | By code |  | Sort the objects using their key. |
|  | Ascending |  |  Sort in ascending mode. Only enabled when sort option is not none  |
|  | Descending |  |  Sort in descending mode. Only enabled when sort option is not none.  |
|  | Match case |  |  Do not ignore case differences. Only enabled when sort option is not none.  |
| Group | New | Ctrl+ Shift+N | Insert a new group object, Implemented by the application.  |
|  | First |  | Go to the oldest brother of the current selected item, which is the first child object of the parent of the current selected object.  |
|  | Previous |  | Go to the previous brother of the current selected object.  |
|  | Next |  | Go to the next brother of the current selected object.  |
|  | Last |  | Goto the last brother of the current selected item, which is the last child object of the parent of the current selected object.  |
| Help | Contents |  | Give a table of contents of all available Help within the current session that is using the GBF.  |
|  | What’s This? | Shift + F1 | Starts the context sensitive Help, which gives detailed Help on the next selected item (including menu items, buttons, keystrokes and so on).  |
|  | Color Descriptions… |  | Starts the special Color Descriptions (ttgbf1310m000) session that shows all used text colors in the GBF when at least one text.color has been used, see also [gbf.set.color()](gbf.set.color.md).  |
|  | Icon Descriptions… |  | Starts the Icon Descriptions (ttgbf1320m000) session that shows all used icons, with a description of what these icons mean. See also icon.desc of [gbf.set.interior.icon()](gbf.set.interior.icon.md) and [gbf.set.leaf.icon()](gbf.set.leaf.icon.md).  |
|  | Using Browser | F2 | Gives Help on how to use the GBF at runtime. |
|  | Using Session | F1 | Gives help on how to use the current session which is build using the GBF. Starts the help associated with the current session, which is identified by the global: prog.name$.  |
|  | About… |  | Show the About box of the GBF. |

## Standard keystrokes
| | | |
|---|---|---|
| Key | Restriction | Description |
| Alt+F4 |  | Shortcut for menu: File exit |
| Alt+F4 | during read | Asks to stop for further reading. |
| Ctrl+C | during read | Asks to stop for further reading. |
| Ctrl+C | normal operation | Shortcut for menu: Edit copy |
| Ctrl+F |  | Shortcut for menu: Find by description |
| Ctrl+G |  | Shortcut for menu: Find next |
| Ctrl+Shift+G |  | Shortcut for menu: Find previous |
| Ctrl+N |  | Shortcut for menu: File new |
| Ctrl+Shift+N |  | Shortcut for menu: Group new |
| Ctrl+O |  | Shortcut for menu: File open all |
| Ctrl+P |  | Shortcut for menu: File print |
| Ctrl+Q |  | Shortcut for menu: File save + exit |
| Ctrl+R |  | Shortcut for menu: File read all |
| Ctrl+S |  | Shortcut for menu: File save |
| Ctrl+T |  | Shortcut for menu: Edit text |
| Ctrl+V |  | Shortcut for menu: Edit paste |
| Ctrl+X |  | Shortcut for menu: Edit cut |
| Ctrl+Z |  | Shortcut for menu: Edit undo |
| ESCAPE | during read | asks to stop for further reading. |
| Delete |  | Shortcut for menu: Edit Delete. |
| F1 |  | Shortcut for menu: Help using session . |
| Shift+F1 |  | Shortcut for menu: Help what’s this ? (context sensitive help). |
| F2 |  | Shortcut for menu: Help using browser. |
| F5 |  | Shortcut for menu: File refresh. |
| - or Shift - | on open interior node | Close this interior node. |
| + or Shift + | on closed interior node | Open this interior node. |
| Backspace | not on top level node | Go to parent. |
| Left Arrow | not on top level node | Go to parent. |
| Shift+Left Arrow | open interior node | Close node and go to parent. |
| Ctrl+Left Arrow |  | Go to the ancestor to which the cycle line goes, or if not in a cycle go to the parent.  |
| Right Arrow | interior node is open and has children | Go to first child. |
| Shift+Right Arrow | closed interior node | Open node (get the children) and go to first child.  |
| Ctrl+Right Arrow | on interior node |  Go to the first or next (great-…-grand) child which has a cycle line to the current selected object. So the first time a Ctrl+Right Arrow is given focus is set to the first cycle child, the next Ctrl+Right Arrow goes to the next child which has the same cycle ancestor If no cycle then go to the first child.  |
| Up Arrow |  | Go to previous object, in other words the object above this one.  |
| Ctrl+Up Arrow | not on first object of parent | Go to previous brother. |
| Down Arrow |  | Go to next object, in other words the object beneath this one  |
| Ctrl+Down Arrow | not on last object of parent | Go to next brother |
| Home |  | Set focus on top object |
| Ctrl+Home | one object selected | Go to oldest brother, in other words first child of parent of object  |
| Ctrl+Home | no record selected | Go to top object. |
| End |  | Set focus on last object in tree. |
| Ctrl+End | one object selected | Go to youngest brother, in other words last child of parent of obj.  |
| Ctrl+End | no object selected | go to last object in tree. |
| Page Down | one object selected | Set focus on last visible object on screen. |
| Page Down | no object selected | Set focus on last object in tree. |
| Page Up | one object selected | Set focus on an object above the current selected object such that this old current object is just visible after the operation.  |
| Page Up | no object selected | Set focus on top object. |
|  |  |  |
When the restriction is not met, for example right arrow on a leaf node, no action is taken.

## Special KeyStrokes during Read
When the GBF is reading (that is: it is currently busy with a lot of gbf.get.children()’s then this may be a lengthy process, which can make the impression that the application ‘ hangs’. After each gbf.get.children()function it is checked to see whether the end user wants to stop this lengthy operation. The way to stop this is by pressing any button, or by hitting the ESCAPE key, CTRL+C or Alt+F4. If this is the case then a question is asked whether or not the reading should really be stopped or not. Note that the number of objects currently in memory of the GBF is also shown, so one can monitor the progress.
When the progress bar is used (see option GBF.OPT.PROGRESS in [gbf.init()](gbf.init.md)) then also the current number of total items is displayed. When the STOP button is pressed still the above mentioned question will be asked.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [Messages and questions](messages_and_questions.md)
