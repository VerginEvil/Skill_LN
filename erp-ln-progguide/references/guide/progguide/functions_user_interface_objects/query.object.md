# query.object()

## Syntax:
`function long query.object( long object_id, long attribute_in, void value_in, long size_iin, long attribute_in, ref void value_out, ref long size_out )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information about a specified object, based on specified attribute values. For example, you can query a DsCgwindow object for the ID of the subobject that is located at specified x- and y-coordinates within the gwindow. Or you can query a DsCgrid object for the type of control that a specified column contains.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  The ID of the object to be queried, as returned by [create.object()](create.object.md) when the object was created.  |
| `long` | `attribute_in` |  You can use one or more sets of these arguments to specify the input attributes for the query. For each attribute you specify, you must include the attribute type (for example, DsNcolumns), and the attribute value. For attributes of type void data or long array, you must also include the size of the data or array.  |
| `void` | `value_in` |  |
| `long` | `size_iin` |  |
| `long` | `attribute_in` |  You can use one or more sets of these arguments to specify the output of the query. For each attribute you specify, you must include the attribute type (for example, DsNcontrol). The function returns the current value of the attribute. For attributes of type void data or long array, it also returns the size of the data or array.  |
| `ref void` | `value_out` |  |
| `ref long` | `size_out` |  |

## Return values
TRUE success
FALSE error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Examples
The following are examples of some of the situations in which you can use the *query.object()* function:

## Example 1
To retrieve the ID of the subobject located at a specified position within a graphical window. If there is more than one subobject at the specified location, the function returns the ID of the uppermost subobject.
```

long mwin_id, gwin_id, gp1, gp2, gp3, part
mwin_id = create.object( DsCmwindow, current.display(),
        DsNbackground,  RGB.BLACK,
        DsNminHeight,   400,
        DsNminWidth,    650,
        DsNflags,       DSNORMALSTATE+DSAUTORESIZE )
gwin_id = create.object( DsCgwindow, mwin_id,
        DsNbackground,  RGB.BLUE,
        DsNwidth,       200,
        DsNheight,      100,
        DsNx,           30,
        DsNy,           30 )
update.object( gwin_id )
gp1 = create.sub.object( gwin_id, DsCgpRectangle,
        DsNgcBackground, RGB.WHITE,
        DsNheight,       50,
        DsNwidth,        50,
        DsNx,            0,
        DsNy,            0 )
gp2 = create.sub.object( gwin_id, DsCgpArc,
        DsNgcBackground, RGB.BLACK,
        DsNheight,       20,
        DsNwidth,        20,
        DsNx,            10,
        DsNy,            10 )
gp3 = create.sub.object( gwin_id, DsCgpLine,
        DsNgcBackground, RGB.RED,
        DsNxo,           1,
        DsNyo,           1,
        DsNxn,           1,
        DsNyn,           200 )
update.object( mwin_id )
query.object( gwin_id,
        DsNx,         20,
        DsNy,         20,
        DsNsubObject, part )
        | part contains the value of gp2
```

## Example 2
To retrieve the IDs of the subobjects that occur within a particular area of a graphical window.
```

   long part.list(20)    | max. 20 parts
   long num.parts
   query.object( gwin_id,
                 DsNx,         5,
                 DsNy,         5,
                 DsNsize,      20,        | maximum number of parts
                 DsNwidth,     30,
                 DsNheight,    30,
                 DsNsubObjectArray, part.list, num.parts )
```
The argument now contains the number of subobjects that occur within the specified area (in this case, 2). The array contains the IDs of the subobjects (in this example, it contains the IDs of gp1 and gp2).

## Example 3
To retrieve the ID of the subobject that in on the top of the subobject stack. If the DsCgwindow object does not contain any parts, 0 is returned.
```

query.object( gwin_id, DsNfirstSubObject, part )
   | part contains the ID of gp1
```

## Example 4
To retrieve the ID of the subobject on the bottom of the subobject stack. If the DsCgwindow object does not contain any parts, 0 is returned.
```

query.object( gwin_id, DsNlastSubObject, part )
   | part contains the ID of gp3
```

## Example 5
To retrieve the ID of the subobject that follows a specified reference subobject in the subobject stack. The stack is built from top to bottom. So the function returns the ID of the subobject below the reference subobject. If the reference subobject is the last subobject in the stack, 0 is returned.
```

query.object( gwin_id, DsNrefSubObject, gp2, DsNnextSubObject, part )
   | part contains the ID of gp3
```

## Example 6
To retrieve the ID of the subobject that precedes the specified reference subobject in the subobject stack. The stack is built from top to bottom. So the function returns the ID of the subobject above the reference subobject. If the reference subobject is the first subobject in the stack, 0 is returned.
```

query.object( gwin_id, DsNrefSubObject, gp2, DsNprevSubObject, part )
     | part contains the ID of gp1
```

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
