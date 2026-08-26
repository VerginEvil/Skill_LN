# DsCgrid

## Description
A DsCgrid object is a rectangular child window that displays a spreadsheet grid. Cells in the grid can contain not only data but also controls such as text boxes, list boxes, and check boxes.

## Events
A DsCgrid object can generate the following events:
EVTCHANGEFOCUS
EVTGRIDEVENT
EVTKEYPRESS
EVTSETFOCUS

## Attributes
| | | |
|---|---|---|
|  DsNbackground (long)  | [S] | Specifies the background color (as an rgb value) for selected cells. The possible values are 0 to 16777215. When not specified, the background adopts the Windows standard.  |
|  DsNcolHeader (boolean)  | [CG] | Specifies whether or not the grid includes column headers. The default is TRUE.  |
|  DsNcolumn (long)  | [SQ] | Use this to select a column in the grid. The value of the attribute is the column number (0-based index). In combination with DsNrow, this attribute selects an individual cell.  |
|  DsNcolumns (long)  | [CSG] | The number of columns in the grid. The default is 1.  |
|  DsNcolWidth (long array)  | [CSQ] |  Use this to specify the width of the grid columns. You fill the array with the width values for each column, starting with the first column. If you specify only one value, all columns are set to that width. If you first use DsNcolumn to select a column, the width specified is applied to the selected column. The width can be any value between 0 and 32768. By default, all columns are the same width, the actual width depending on the width of the grid.  |
|  DsNcontrol (long)  | [SQ] |  Use to create a control object in selected cell(s). Possible values are: DSEDIT Edit control (text box) (default). DSSTATIC Static label field. DSDDLISTBOX Drop-down list box. DSCHECKBOX Check-box. DSZOOMEDIT Zoom edit field. For an edit control, use DsNmaxLength to specify the maximum number of input characters for the field. For a drop-down list box, use DsNenum to specify the list box contents. For a check box, use the values 1 and 0 to select/deselect the control. For a drop-down list box, select the list box entry to be displayed by specifying its index number in the list.  |
|  DsNeditable (boolean)  | [SQ] | Specifies whether or not an edit control is read-only. The default is FALSE.  |
|  DsNenum (string)  | [SQ] |  Specifies the contents of a drop-down list box. Separate the individual list items using \n. For example: item1\nitem2\nitem3\n  |
|  DsNfontSet (long)  | [SQ] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the entire grid or to selected cells. The default font is the Windows default font.  |
|  DsNforeground (long)  | [S] | Specifies the text color (as an rgb value) for selected cells. The possible values are 0 to 16777215. When not specified, the Windows standard is used.  |
|  DsNfreezeColumns (boolean)  | [SG] | Use to freeze and unfreeze column(s) selected by the user. The default value is FALSE.  |
|  DsNgridEnableSelection (long)  | [CG] |  Specifies user selection options. Possible values are: DSGRIDSELFULL All selection actions (default). DSGRIDSELNONE No selection actions. DSGRIDSELROW Row selection. DSGRIDSELCOL column selection. DSGRIDSELTABLE Grid selection. DSGRIDSELCELL Cell selection. DSGRIDSELMULTIPLE Multiple selections. DSGRIDSELSHIFT Extend selection by pressing SHIFT. DSGRIDSELKEYBOARD Selection with SHIFT+Arrow Key. You can combine all the above values.  |
|  DsNgridFooter (boolean)  | [CSG] | Specifies whether or not the last row in the grid has a special style. In this special style, the font and top border are bold and the background color is that defined for 3D objects in the Windows standard color scheme.  |
|  DsNgridSetState (long)  | [S] |  The state of a grid selection. Possible values are: DSGRIDSTATEMARK Mark the selection. DSGRIDSTATEUNMARK Unmark the selection. DSGRIDSTATESETFOCUS Set focus on the selection (single cell only). DSGRIDSTATESETSENSITIVE Make the selection sensitive. DSGRIDSTATESETINSENSITIVE Make the selection insensitive. You cannot combine these values.  |
|  DsNgridType (long)  | [CG] |  The grid type. Possible options are: DSGRIDTYPENORMAL Normal grid functionality (default). DSGRIDTYPEDISPLAY Read-only functionality. DSGRIDTYPEEDIT Edit functionality. DSGRIDTYPEVEERTEDIT Vertical edit functionality.  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNjustify (long)  | [SQ] |  Use this to specify the justification for data in selected cells. Possible values are: DSJUSTIFYRIGHT DSJUSTIFYLEFT (default) DSJUSTIFYCENTER  |
|  DsNmaxLength (long)  | [SQ] | The maximum number of input characters for an edit control field. This can be any value from 0 to 4096. 4096 is the default value.  |
|  DsNrange (long array)  | [SQ] |  Use this to select a range of cells. The array is filled as follows: start_row_num + start_col_num + end_row_num + end _col_num  |
|  DsNrow (long)  | [SQ] | Use this to select a row in the grid. The value of the attribute is the row number (0-based index). In combination with DsNcolumn, this attribute selects an individual cell.  |
|  DsNrowHeader (boolean)  | [CG] | Specifies whether or not the grid includes row headers. The default is TRUE.  |
|  DsNrowHeight (long array)  | [CSQ] |  Use this to specify the height of the grid rows. You fill the array with the height values for each row, starting with the first row. If you specify only one value, all rows are set to that height. If you first use DsNrow to select a row, the height specified is applied to the selected row. The height can be any value between 0 and 32768. By default, all rows are the same height, the actual height depending on the font size.  |
|  DsNrows (long)  | [CSG] | The number of rows in the grid. The default is 1 row.  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNstringArray (void)  | [SQ] | A one-dimensional array that holds data values for selected cell(s). When filling multiple cells, separate the data values with null characters. The data is filled from left to right and from top to bottom. |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
