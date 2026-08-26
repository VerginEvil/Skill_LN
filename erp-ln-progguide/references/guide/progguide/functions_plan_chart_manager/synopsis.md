# Plan Chart Manager synopsis
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use the "Gantt And Schedule Charts" API.
```

long
```
```

void
```
```

void
```
```

long
```
```

long
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
```

void
```
| | | |
|---|---|---|
|  | [pcm.activate.session()](pcm.activate.session.md) | `( ref string session(), ref string title() )` |
|  | [pcm.change()](pcm.change.md) | `( long plan_id [, flag, value ] ... )` |
|  | [pcm.change.object()](pcm.change.object.md) | `( long plan_id, long object_id [, flag, value ] ... )` |
|  | [pcm.create()](pcm.create.md) | `( [ flag, value ] ...)` |
|  | [pcm.create.object()](pcm.create.object.md) | `( long plan_id, long object_type [, flag, value ] ... )` |
|  | [pcm.destroy()](pcm.destroy.md) | `( long plan_id )` |
|  | [pcm.destroy.object()](pcm.destroy.object.md) | `( long plan_id, long object_id )` |
|  | [pcm.get.data()](pcm.get.data.md) | `( long evt_type, ref string arglist(), ... )` |
|  | [pcm.lock()](pcm.lock.md) | `( long plan_id, long lock )` |
|  | [pcm.refresh()](pcm.refresh.md) | `( long plan_id )` |
|  | [pcm.send.bms.event()](pcm.send.bms.event.md) | `( long command, ref string arglist() )` |

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
