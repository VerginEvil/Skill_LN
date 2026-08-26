# DsCfield

## Description
A DsCfield object provides a rectangular child window where the user can enter and edit text. It can be defined to support a single line or multiple lines of text. A DsCfield object provides the same functionality as a Windows text box (also referred to as an edit control).

## Events
A DsCfield object can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTFIELDSELECT

## Attributes
| | | |
|---|---|---|
|  DsNcolumns (long)  | [CSG] |  The width of the text box, in characters. For proportional fonts, the width is based on the widest character of the font. DsNwidth and DsNcolumns are mutually exclusive attributes. If both are zero, the window width is determined by the length of the string it contains and the font used.  |
|  DsNconvertSoftReturn (long)  | [CSG] |  Specifies whether or not soft returns in a multiline text box must be converted to hard returns. Possible values are: TRUE Soft returns are converted to hard returns (default). FALSE Soft returns are not converted to hard returns.  |
|  DsNeditable (long)  | [CSG] |  Specifies whether or not users can edit the text string. Possible values are: TRUE User can edit text string (default). FALSE User cannot edit text string.  |
|  DsNeditMode (long)  | [CG] |  Specifies how the TAB key is handled. Possible values are: DSNORMALEDITMODE TAB generates a change focus event (default). DSTEXTEDITORMODE TAB is inserted in the text.  |
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNfieldData (void)  | [CSG] | The contents of the text box. Use this attribute if the string length is greater than 4Kb. Otherwise, use DsNstring. The string must be null terminated.  |
|  DsNfontSet (long)  | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the object's text. If this attribute is not set, the Windows default font is used.  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNjustify (long)  | [CG] |  Specifies the alignment of text in a multiline window. The possible values are : DSJUSTIFYLEFT (default) DSJUSTIFYRIGHT DSJUSTIFYCENTER  |
|  DsNmaxLength (long)  | [CSG] | Specifies the maximum length of the text string that a user can enter from the keyboard.  |
|  DsNmultiLine (boolean)  | [CG] |  Specifies whether the text box supports multiple lines of text or only a single line. Possible values are: TRUE Multiline. FALSE Single line (default). DsNmultiLine and DsNpasswordField are mutually exclusive options.  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNoffset (long)  | [S] | The offset (position) in the text box where the data in DsNstring or DsNfieldData is to be inserted. If this attribute is not specified, the new text overwrites the current text.  |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNpasswordField (boolean)  | [CG] | Specifies a password-type text box. That is, characters entered in the text box are displayed as asterisks. DsNmultiLine and DsNpasswordField are mutually exclusive options.  |
|  DsNrows (long)  | [CSG] | The number of rows in a multiline text box. DsNheight and DsNrows are mutually exclusive attributes. If both are zero, the window height depends on the settings of the DsNfontSet, DsNstring, and DsNmultiLine attributes.  |
|  DsNselectionArray (long array)  | [CSG] | The current position of the cursor or selection in the text box. The array contains two longs that represent the start and end position of the selection (zero-based index). When the two values are the same, this represents the position of the cursor.  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNsize (long)  | [G] | The length of the string in the text box, including the null character at the end of the string.  |
|  DsNstring (string)  | [CSG] | The contents of the text box. The string can be a maximum of 4Kb. For long strings, use DsNfieldData instead.  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNtoolTip (string)  | [CSG] | The tooltip string associated with the text box. This is displayed when the user positions the mouse pointer over the window for one second or more. The string can be a maximum of 80 characters.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |
|  DsNwordWrap (long)  | [CG] |  Specifies whether word wrap is enabled or disabled in a multiline text box. Possible values are: TRUE Word wrap on (default). FALSE Word wrap off.  |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
