# query.sub.object()

## Syntax:
`function long query.sub.object( long object_id, long sub_object_id, long attribute_in, value_in, size_in, void value_in, long size_in, long attribute_in, ref void value_out, ref long size_out )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information about a specified subobject, based on specified attribute values. For example, you can query a DsCgpOleSite subobject for data in a specific format.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  The ID of the object to which the subobject belongs.  |
| `long` | `sub_object_id` |  The ID of the subobject within the specified object.  |
| `long` | `attribute_in, value_in, size_in` |  You can use one or more sets of these arguments to specify the input attributes for the query. For each attribute you specify, you must include the attribute type and the attribute value. For attributes of type void data or long array, you must also include the size of the data or array.  |
| `void` | `value_in` |    |
| `long` | `size_in` |    |
| `long` | `attribute_in` |  You can use one or more sets of these arguments to specify the output of the query. For each attribute you specify, you must include the attribute type. The function returns the current value of the attribute. For attributes of type void data or long array, it also returns the size of the data or array.  |
| `ref void` | `value_out` |    |
| `ref long` | `size_out` |    |

## Return values
TRUE success
FALSE error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
