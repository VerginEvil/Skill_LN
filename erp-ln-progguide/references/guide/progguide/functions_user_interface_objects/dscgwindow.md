# DsCgwindow

## Description
A graphical window (DsCgwindow) is a window in which applications can draw graphical parts such as lines, rectangles, polygons, and so on. Graphical windows also support user interface controls such as buttons, edit controls, list boxes, and so on.
Note that after changes to graphical parts, the graphical window in not redrawn until DsNsetState is set to DSUPDATE or until the window is repainted by the windows system.
Graphical windows support the following subobjects:
- [DsCgpArc](dscgparc.md)
- [DsCgpComposite](dscgpcomposite.md)
- [DsCgpGroupBox](dscgpgroupbox.md)
- [DsCgpHeader](dscgpheader.md)
- [DsCgpImage](dscgpimage.md)
- [DsCgpLine](dscgpline.md)
- [DsCgpOleSite](dscgpolesite.md)
- [DsCgpPie](dscgppie.md)
- [DsCgpPolygon](dscgppolygon.md)
- [DsCgpPolyline](dscgppolyline.md)
- [DsCgpRectangle](dscgprectangle.md)
- [DsCgpText](dscgptext.md)

## Events
A DsCgwindow can generate the following events:
EVTBUTTONPRESS
EVTBUTTONRELEASE
EVTBUTTONDPRESS
EVTBUTTONMOTION
EVTOLEEVENT

## Attributes
| | | |
|---|---|---|
|  DsNbackground (long)  | [CSG] | The rgb value that defines the background color of the object. If this attribute is not specified, the object inherits the background color of its parent. If none of the parent objects specify a background color, the resource workAreaBackground is used.  |
|  DsNborderColor (long)  | [CSG] | The rgb value that defines the color of the object's border.  |
|  DsNborderWidth (long)  | [CSG] | The width of the object's border, in pixels. |
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNfirstSubObject (long)  | [SQ] | The object ID of the subobject that is be drawn above all other subobjects. Setting this attribute changes the drawing order of subobjects.  |
|  DsNgridColor (long)  | [CSG] | The color of the grid lines in the gwindow. The default is black.  |
|  DsNgridHeight (long)  | [CSG] | The spacing (in pixels) between horizontal grid lines. If this is not specified, horizontal gridlines are not displayed.  |
|  DsNgridWidth (long)  | [CSG] | The spacing (in pixels) between vertical grid lines. If this is not specified, vertical gridlines are not displayed.  |
|  DsNgridX (long)  | [CSG] | The x-coordinate (in pixels) of the first grid line relative to the left border of the window. The default is 0.  |
|  DsNgridY (long)  | [CSG] | The y-coordinate (in pixels) of the first grid line relative to the top border of the window. The default is 0.  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNinferiorPointerCursor (long)  | [CSG] |  The shape of the inferior mouse pointer when positioned over the gwindow. A child of a gwindow inherits this mouse pointer, unless otherwise specified. This attribute is overruled by a DsNsuperiorPointerCursor attribute set for the window itself or for ancestor windows. It is also overruled by a DsNinferiorPointerCursor setting in descendant windows. Possible values are: DSCDEFAULT (default) DSCPENCIL DSCARROW DSCQUESTIONARROW DSCCROSSHAIR DSCSPLITHORIZONTAL DSCFLEUR DSCSPLITVERTICAL DSCHAND DSCSPRAYCAN DSCMAGNIFY DSCWATCH DSCAPPSTARTING DSCNODROP  |
|  DsNlastSubObject (long)  | [SQ] | The object ID of the subobject that is be drawn beneath all other subobjects. Setting this attribute changes the drawing order of subobjects.  |
|  DsNnextSubObject (long)  | [SQ] | The object ID of the subobject that is drawn under the subobject specified by DsNrefSubObject. Setting this attribute changes the drawing order of subobjects.  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNprevSubObject (long)  | [SQ] | The object ID of the subobject that is drawn above the subobject specified by DsNrefSubObject. Setting this attribute changes the drawing order of subobjects.  |
|  DsNrefSubObject (long)  | [SQ] | The object ID of the subobject used as a reference by DsNnextSubObject, DsNprevSubObject, and DsNsequence. |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNsubObject (long)  | [Q] | Use this attribute in a query operation to retrieve information about a subobject of the gwindow.  |
|  DsNsubObjectArray (long array)  | [Q] | Use this attribute in a query operation to retrieve information about subobjects within a specified area of the gwindow.  |
|  DsNsuperiorPointerCursor (long)  | [CSG] |  The shape of the superior mouse pointer when positioned over the gwindow. A child of a gwindow always inherits this mouse pointer. This attribute overrules any DsNinferiorPointerCursor attribute set for the window and all mouse pointers set for descendant windows. Possible values are: DSCDEFAULT DSCPENCIL DSCARROW DSCQUESTIONARROW DSCCROSSHAIR DSCSPLITHORIZONTAL DSCFLEUR DSCSPLITVERTICAL DSCHAND DSCSPRAYCAN DSCMAGNIFY DSCWATCH DSCAPPSTARTING DSCNODROP  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
