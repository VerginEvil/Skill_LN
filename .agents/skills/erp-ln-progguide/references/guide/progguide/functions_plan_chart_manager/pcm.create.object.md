# pcm.create.object()

## Syntax:
`function long pcm.create.object( long plan_id, long object_type, [ long flag, long value, long flag, value ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This creates an object of the specified type – for example, a menu item, an activity, a relation, or a marker.
The function returns the *object_id*, which in turn is used in the functions [pcm.change.object()](pcm.change.object.md) and [pcm.destroy.object()](pcm.destroy.object.md) to identify the particular object to be changed or deleted. The *object_id* is also used in submenus and with subactivities in order to indicate the parent of the menu or activity.

## Arguments
| | | |
|---|---|---|
| `long` | `plan_id` |  The ID of the plan to which you want to add the new object.  |
| `long` | `object_type` |  The object type. The possible values are: [PCM_OT_MENU - menu object](menu_object.md) a menu item [PCM_OT_BUTTON – button object](button_object.md) a button to which you can link sessions or options [PCM_OT_TIMESCALE – time scale object](time_scale_object.md) a time scale [PCM_OT_DELAY – delay time object](delay_time_object.md) delay time (that is, non workdays) [PCM_OT_COLUMN – column object](column_object.md) a column containing an activity description [PCM_OT_ACTIVITY – activity object](activity_object.md) an activity [PCM_OT_RELATION – relation object](relation_object.md) a relation [PCM_OT_MARKER – marker object](marker_object.md) an activity marker  |
| `[ long` | `flag ]` |  Use these arguments to define the object's attributes. For each attribute you specify, you must include the attribute type (for example, PcmMenuName or PcmTimescaleVisible), and the attribute value. The attributes of each object are listed in the section describing that object.  |
| `[ long` | `value ]` |  Use these arguments to define the object's attributes. For each attribute you specify, you must include the attribute type (for example, PcmMenuName or PcmTimescaleVisible), and the attribute value. The attributes of each object are listed in the section describing that object.  |
| `[ long` | `flag, value ]` |  Use these arguments to define the object's attributes. For each attribute you specify, you must include the attribute type (for example, PcmMenuName or PcmTimescaleVisible), and the attribute value. The attributes of each object are listed in the section describing that object.  |

## Return values
The function returns a unique ID for the new object.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
