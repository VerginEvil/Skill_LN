# Synopsis
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```
long
```
```
long
```
```

long
```
```

long
```
```

long
```
```
long
```
```
long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

boolean
```
```

boolean
```
```

boolean
```
```

boolean
```
```

boolean
```
```

boolean
```
```

boolean
```
| | | |
|---|---|---|
|  | [plcm.init](plcm_init.md) | `(string title, long initial.types [,long options])` |
|  | [plcm.add.root.activity](plcm_add_root_activity.md) | `(string root.activity.id, string root.activity.name)` |
|  | [plcm.add.root.resource](plcm_add_root_resource.md) | `(string root.resource.id, string root.resource.name)` |
|  | [plcm.add.activity](plcm_add_activity.md) | `(string parent.activity.id, string activity.id, string activity.name, [long start.date, long end.date], [long completion.percentage])` |
|  | [plcm.add.resource](plcm_add_resource.md) | `(string parent.resource.id, string resource.id, string resource.name, [long quantity])` |
|  | [plcm.add.constraint](plcm_add_constraint.md) | `(string activity.id.from, string activity.id.to, long constraint.type)` |
|  | [plcm.add.reservation](plcm_add_reservation.md) | `(string activity.id, string resource.id)` |
|  | [plcm.add.activity.marker()](plcm_add_activity_marker.md) | `(string activity.id, long icon.id, long date_time, string tooltip, string legend.id)` |
|  | [plcm.add.activity.property](plcm_add_activity_property.md) | `(string property.id, string property.label)` |
|  | [plcm.get.default.availability](plcm_get_activity_unavailability.md) | `(const string activity.id(), const long i.start.date, const long i.end.date)` |
|  | [plcm.set.activity.unavailability](plcm_set_activity_unavailability.md) | `(const string activity.id(), const long no.elements, const long start.date(), const long end.date(), const string description(,) mb, const string legend.id(,) mb)` |
|  | [plcm.set.activity.property](plcm_set_activity_property.md) | `(string activity.id, string property.id, string property.value)` |
|  | [plcm.set.activity.property.date](plcm_set_activity_property_date.md) | `(string activity.id, string property.id, domain ttutc utc.value)` |
|  | [plcm.add.resource.property](plcm_add_resource_property.md) | `(string property.id, string property.label)` |
|  | [plcm.get.resource.unavailability](plcm_get_resource_unavailability.md) | `(const string resource.id(), const long i.start.date, const long i.end.date)` |
|  | [plcm.set.resource.unavailability](plcm_set_resource_unavailability.md) | `(const string resource.id(), const long no.elements, const long start.date(), const long end.date(), const string description(,) mb, const string legend.id(,) mb)` |
|  | [plcm.set.resource.property.value](plcm_set_resource_property_value.md) | `(string resource.id, string property.id, [string property.value])` |
|  | [plcm.delete.activity](plcm_delete_activity.md) | `(string activity.id)` |
|  | [plcm.delete.resource](plcm_delete_resource.md) | `(string resource.id)` |
|  | [plcm.delete.constraint](plcm_delete_constraint.md) | `(string activity.id.from, string activity.id.to, long constraint.type)` |
|  | [plcm.delete.reservation](plcm_delete_reservation.md) | `(string activity.id , string resource.id)` |
|  | [plcm.move.activity](plcm_move_activity.md) | `(string activity.id, long start.date, long end.date)` |
|  | [plcm.create.legend.entry](plcm_create_legend_entry.md) | `(string legend.id, long color, string description)` |
|  | [plcm.set.legend.for.activity](plcm_set_legend_for_activity.md) | `(string activity.id, string legend.id)` |
|  | [plcm.set.slack.for.activity()](plcm_set_slack_for_activity.md) | `(string activity.id, long start.date, long end.date, string legend.id)` |
|  | [plcm.set.legend.for.activity.division](plcm_set_legend_for_activity_division.md) | `(string activity.id, string legend.id, long start.percentage, long end.percentage)` |
|  | [plcm.set.activity.name](plcm_set_activity_name.md) | `(string activity.id, string name)` |
|  | [plcm.set.activity.start.date](plcm_set_activity_start_date.md) | `(string activity.id, long start.date)` |
|  | [plcm.set.activity.end.date](plcm_set_activity_end_date.md) | `(string activity.id, long end.date)` |
|  | [plcm.set.activity.completion.percentage](plcm_set_activity_completion_percentage.md) | `(string activity.id, long completion.percentage)` |
|  | [plcm.set.resource.name](plcm_set_resource_name.md) | `(string resource.id, string name)` |
|  | [plcm.set.resource.quantity](plcm_set_resource_quantity.md) | `(string resource.id, long quantity)` |
|  | [plcm.add.command](plcm_add_command.md) | `(string command.id, const string command.text())` |
|  | [plcm.start](plcm_start.md) | `()` |
|  | [plcm.clear](plcm_clear.md) | `()` |
|  | [plcm.command.performed](plcm_command_performed.md) | `(string command.id, const long activities.context.count, const string activities.context(,), const long resources.context.count, const string resources.context(,))` |
|  | [plcm.activity.moved](plcm_activity_moved.md) | `(string activity.id, long start.date, long end.date)` |
|  | [plcm.activity.deleted](plcm_activity_deleted.md) | `(const string activity.id)` |
|  | [plcm.activity.action.performed](plcm_activity_action_performed.md) | `(const string activity.id)` |
|  | [plcm.resource.deleted](plcm_resource_deleted.md) | `(const string resource.id)` |
|  | [plcm.constraint.deleted](plcm_constraint_deleted.md) | `(const string activity.id.from, const string activity.id.to, const long constraint.type)` |
|  | [plcm.reservation.changed](plcm_reservation_changed.md) | `(const string activity.id, const string old.resource.id, const new.resource.id)` |
|  | [plcm.reservation.deleted](plcm_reservation_deleted.md) | `(const string activity.id, const string resource.id)` |
