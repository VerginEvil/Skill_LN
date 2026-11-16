# Secondary toolbars overview and synopsis

## Overview
Use the *create.extra.toolbar()* function to add a secondary toolbar to a session. Buttons on the toolbar represent form commands; they provide an alternative means of executing those commands.
You can create the button images yourself (as.gif files) or you can reuse existing images, where appropriate. Before you can add buttons to a secondary toolbar, you must import the.gif files with session "Addtional Files (ttadv2570m000)". This session will put the.gif files in the dictionary according the specified package and module.
A Button image (.gif file) must default be present as additional file in the same package/module combination as used by the session, unless the following syntax for the "gif_file" argument is used: [package][module]:gif_file.
Buttons on secondary toolbars are automatically disabled or enabled when the corresponding form commands are disabled or enabled (see [disable.commands()](../functions_form_and_form_field_operations/disable.commands.md)).
The length of the secondary toolbars depends on the showed icons.

## Synopsis
```

long
```
| | | |
|---|---|---|
|  | [create.extra.toolbar()](create.extra.toolbar.md) | `( string form_command, string gif_file [, string form_command, string gif_file...] )` |
