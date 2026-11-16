# DsCgpPolyline

## Description
A DsCgpPolyline subobject defines a line to be drawn between a number of specified points in the parent window. The points are stored in the DsNpointArray attribute. If the first and last points coincide, the lines are joined according to the setting of the DsNgcJoinStyle attribute. The parent window is always a DsCgwindow object.

## Events
A DsCgpPolyline object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNgcBackground (long) | [CSG] | The rgb value that defines the background color of the subobject. |
| DsNgcCapStyle (long) | [CSG] | This controls the appearance of line ends. Possible values are: GCCAPBUTT Lines are square at the endpoint. GCCAPROUND Lines are terminated by a circular arc whose. diameter equals the line width |
| DsNgcForeground (long) | [CSG] | The rgb value that defines the foreground color of the graphical part. |
| DsNgc (long) | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the object. |
| DsNgcJoinStyle (long) | [CSG] | Defines how corners are drawn. Possible values are: GCJOINMITER The outer edges of the two lines extend to meet at an angle. GCJOINROUND Lines are joined by a circular arc whose diameter equals the line width and which is centered on the join point. |
| DsNgcLineStyle (long) | [CSG] | The line and border style for a graphical part. Possible values are: GCLINESOLID Normal line. GCLINEDOUBLEDASH Line stippled, using DsNgcForeground and DsNgcBackground colors. GCLINEONOFFDASH Line stippled, using DsNgcForeground and the window's background color. |
| DsNgcLineWidth (long) | [CSG] | The width of lines and borders, in pixels. |
| DsNobjectType (long) | [G] | The subobject type. |
| DsNpointArray (long array) | [CSG] | The array containing the positions of the points. The point array must be filled as follows: points(1,1) contains the x-coordinate of the first point points(1,2) contains the y-coordinate of the first point points(number of points,1) contains the x-coordinate of the last point points(number of points,2) contains the y-coordinate of the last point All coordinates must be specified in pixels relative to the upper-left corner of the parent window. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the polyline object relative to the reference object. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
