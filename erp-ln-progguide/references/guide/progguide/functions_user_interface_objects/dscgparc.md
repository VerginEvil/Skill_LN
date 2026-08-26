# DsCgpArc

## Description
A DsCgpArc object defines a circular or elliptical arc inside a rectangle. The center of the circle or ellipse is the center of the rectangle. The major and minor axes are specified by the width and height attributes respectively. The parent object is always a graphical window (DsCgwindow).

## Events
A DsCgpArc object does not generate events.

## Attributes
| | | |
|---|---|---|
|  DsNangle (long)  | [CSG] | Specifies the start of the arc relative to the three-o'clock radial from the center of the arc. Angles are specified in degrees (maximum 360 degrees). Positive values indicate counter-clockwise motion and negative values indicate clockwise motion.  |
|  DsNattribute (long)  | [CSG] |  The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden.  |
|  DsNgc (long)  | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the object.  |
|  DsNgcBackground (long)  | [CSG] | The rgb value that defines the background color of the subobject.  |
|  DsNgcCapStyle (long)  | [CSG] |  This controls the appearance of line ends. Possible values are: GCCAPBUTT Lines are square at the end point. GCCAPROUND Lines are terminated by a circular arc whose diameter equals the line width.  |
|  DsNgcForeground (long)  | [CSG] | The rgb value that defines the foreground color of the subobject.  |
|  DsNgcLineStyle (long)  | [CSG] |  The line and border style for the subobject. Possible values are: GCLINESOLID Normal line. GCLINEDOUBLEDASH Line stippled, using DsNgcForeground and DsNgcBackground colors. GCLINEONOFFDASH Line stippled, using DsNgcForeground and the window's background color.  |
|  DsNgcLineWidth (long)  | [CSG] | The width of lines and borders, in pixels. |
|  DsNheight (long)  | [CSG] | The height of the bounding rectangle, in pixels. |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNrefSubObject (long)  | [CS] | The ID of the subobject used as a reference by DsNsequence.  |
|  DsNrotation (long)  | [CSG] |  Specifies the angle of the arc relative to the DsNangle value. Angles are specified in degrees (maximum 360 degrees). Positive values indicate counter-clockwise motion and negative values indicate clockwise motion.  |
|  DsNsequence (long)  | [CS] |  The position of the arc relative to the reference object. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject.  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that contains a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the bounding rectangle, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the upper-left corner of the bounding rectangle, relative to the upper-left corner of the parent window.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the upper-left corner of the bounding rectangle, relative to the upper-left corner of the parent window.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
