# DsCgpOleSite

## Description
A DsCgpOleSite subobject defines a rectangle that can embed an OLE object. The parent window is always a DsCgwindow object.

## Events
A DsCgpOleSite subobject does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNappName (string) | [CS] | The name of the application in which the OLE object is embedded. |
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNdata (void) | [CSGQ] | Specifies the binary data that contains the OLE object. |
| DsNdocName (string) | [CS] | The name of the document in which the OLE object is embedded. |
| DsNerror (long) | [G] | Specifies the error code returned when a *change.object()* request fails. |
| DsNformat (long) | [CQ] | The format of the data in DsNdata. Possible values are: DSFORMATNATIVE Native object format defined by server application (default). DSFORMATTEXT ASCII text format. DSFORMATBITMAP Bitmap format. DSFORMATMETAFILE Metafile format. DSFORMATDIB Device independent bitmap format. DSFORMATWAVE Wave file format. DSFORMATUNICODETEXT Unicode text format. DSFORMATENHANCEDMETAFILE Enhanced metafile format. DSFORMATRICHTEXT RTF format DSFORMATEMBEDSOURCE Embedded source format. DSFORMATEMBEDDEDOBJECT Embedded object format. DSFORMATLINKSOURCE Link source format. DSFORMATOBJECTDESCRIPTOR Object description format. DSFORMATLINKSOURCEDESCRIPTOR Link source description format. DSFORMATOWNERLINK Owner link format. DSFORMATFILENAME File name format. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |
| DsNname (string) | [CS] | The name of the local file that contains the OLE object. |
| DsNobjectType (long) | [G] | The subobject type. |
| DsNprogId (string) | [CS] | OLE objects are registered with a unique program identifier. This attribute specifies that ID. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the object relative to the reference subobject. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject |
| DsNsize (long) | [GQ] | The size of the data in DsNdata. |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNverb (long) | [S] | The action to be performed on the OLE object. |
| DsNwidth (long) | [CSG] | The width of the subobject, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the subobject's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the subobject's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
