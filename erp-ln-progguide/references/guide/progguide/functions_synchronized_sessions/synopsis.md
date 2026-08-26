# Synchronized sessions synopsis

## Dialog synchronization
```

void
```
```
void
```
| | | |
|---|---|---|
|  | [set.synchronized.dialog()](set.synchronized.dialog.md) | `( string sess_code )` |
|  | [set.dynamic.synchronized.dialog()](set.dynamic.synchronized.dialog.md) | `( const string sessioncode, [const string parent.field, const string child.field], ... )` |

## Child synchronization
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
| | | |
|---|---|---|
|  | [start.synchronized.child()](start.synchronized.child.md) | `( string sess_code [, string parent.var, string child.var ...], [long start.mode])` |
|  | [start.synchronized.child.with()](start.synchronized.child.with.md) | `( const long cmd )` |
|  | [stop.synchronized.child()](stop.synchronized.child.md) | `( long child.id )` |
|  | [synchronize.with.child()](synchronize.with.child.md) | `( long child.id )` |

## Other
```

long
```
| | | |
|---|---|---|
|  | [refresh.parent()](refresh.parent.md) | `( long occurrence )` |
```

void
```
| | | |
|---|---|---|
|  | [set.insert.in.detail.session()](set.insert.in.detail.session.md) | `( string sess_code [, string parent.var, string child.var ...]` |

## Related topics
- [Synchronized sessions overview](overview.md)
- [Child synchronization sample program](example.md)
