# Interprocess communication (OS level) synopsis

## Message queues
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

long
```
| | | |
|---|---|---|
|  | [close.message()](close.message.md) | `( long key [, long fast] )` |
|  | [open.message()](open.message.md) | `( long project, string name$, long action [, long fast] )` |
|  | [recv.message()](recv.message.md) | `( long key, long sender.key, long time, ref string message$ [, long fast] )` |
|  | [send.message()](send.message.md) | `( long dest.key, long sender.key, string message$ [, long fast] )` |

## Pipes
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
| | | |
|---|---|---|
|  | [pipe.clearerr()](pipe.clearerr.md) | `( long pipe_id )` |
|  | [pipe.close()](pipe.close.md) | `( long pipe_id )` |
|  | [pipe.eof()](pipe.eof.md) | `( long pipe_id )` |
|  | [pipe.error()](pipe.error.md) | `( long pipe_id )` |
|  | [pipe.flush()](pipe.flush.md) | `( long pipe_id )` |
|  | [pipe.gets()](pipe.gets.md) | `( ref string line(80), long nr_of_bytes, long pipe_id )` |
|  | [pipe.open()](pipe.open.md) | `( string pathnm(128), string openmode(2))` |
|  | [pipe.puts()](pipe.puts.md) | `( string line(80), long pipe_id )` |
|  | [pipe.read()](pipe.read.md) | `( ref string buffer(1024), long nr_of_bytes, long pipe_id )` |
|  | [pipe.write()](pipe.write.md) | `( string buffer(1024), long nr_of_bytes, long pipe_id)` |

## Related topics
- [Interprocess communication (OS level) overview](overview.md)
