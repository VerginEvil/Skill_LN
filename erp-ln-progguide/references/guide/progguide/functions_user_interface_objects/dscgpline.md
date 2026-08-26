# DsCgpLine

## Description
A DsCgpLine subobject defines a line to be drawn between two specified points in the parent window. The parent window is always a DsCgwindow object.

## Events
A DsCgpLine object does not generate events.

## Attributes
| | | |
|---|---|---|
|  DsNattribute (long)  | [CSG] |  The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden.  |
|  DsNgcBackground (long)  | [CSG] | The rgb value that defines the background color of the graphical part.  |
|  DsNgcCapStyle (long)  | [CSG] |  This controls the appearance of line ends. Possible values are: GCCAPBUTT Lines are square at the end point. GCCAPROUND Lines are terminated by a circular arc whose diameter equals the line width.  |
|  DsNgcForeground (long)  | [CSG] | The rgb value that defines the foreground color of the graphical part.  |
|  DsNgc (long)  | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the subobject.  |
|  DsNgcLineStyle (long)  | [CSG] |  The line style for the subobject. Possible values are: GCLINESOLID Normal line. GCLINEDOUBLEDASH Line stippled, using DsNgcForeground and DsNgcBackground colors. GCLINEONOFFDASH Line stippled, using DsNgcForeground and the window's background color.  |
|  DsNgcLineWidth (long)  | [CSG] | The width of lines and borders, in pixels. |
|  DsNobjectType (long)  | [G] | The subobject type. |
|  DsNrefSubObject (long)  | [CS] | The ID of the subobject used as a reference by DsNsequence.  |
|  DsNsequence (long)  | [CS] |  The position of the line relative to the reference subobject. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject.  |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNxo, DsNxn, DsNyo, DsNyn (long)  | [CSG] | The line is drawn between two points in the parent window. The DsNxo and DsNyo attributes specify the x- and y-coordinates of the start point, relative to the upper-left corner of the parent window. The DsNxn and DsNyn attributes specify the x- and y-coordinates of the end point, relative to the upper-left corner of the parent window.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
