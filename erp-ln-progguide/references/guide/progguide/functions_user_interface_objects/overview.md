# User interface objects overview
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated. The Programmable Dialogs API can be used as an alternative.
Infor Enterprise Server provides a library of user interface objects and subobjects that you can use as the building blocks for a complete graphical user interface. The available object types include windows, graphs, graphical images, and a wide range of user interface controls such as menu bars, toolbars, scroll bars, list boxes, check boxes, and so on. The available subobjects consist of graphical parts, such as arcs, lines, and rectangles, which you can create in graphical windows.
Each object and subobject includes a set of attributes that defines its appearance and state. Infor Enterprise Server provides a set of functions that you can use to create and manipulate objects and subobjects, and to set and retrieve their attributes.
Each object and subobject has an identification number that is unique for all bshell processes.
Notes  You must always use the [rgb()](../functions_color/rgb.md) function to compose colors.
In the lists of attributes for each object type, the following flags are used:
| | |
|---|---|
| C | You can define the attribute when creating the object with the functions *create.object()*, *create.sub.object()*, or *create.sub.object.by.id()*.  |
| S | You can define the attribute when changing the object with the functions *change.object()* or *change.sub.object()*.  |
| G | You can read the attribute with the functions *get.object()* or *get.sub.object()*.  |
| Q | You can query the attribute with the functions *query.object()* or *query.sub.object()*.  |

## Related topics
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
