# Interprocess communication (bshell) synopsis

## BMS messages
```

void
```
```

void
```
```

string
```
```

long
```
```

long
```
| | | |
|---|---|---|
|  | [bms.add.mask()](bms.add.mask.md) | `( string mask(32) [, long processno] )` |
|  | [bms.delete.mask()](bms.delete.mask.md) | `( string mask(32) [, long processno] )` |
|  | [bms.receive$()](bms.receive.md) | `( [ref long level, long wait.flag, ref string mask()] )` |
|  | [bms.receive.buffer()](bms.receive.buffer.md) | `( ref string broadcast(), ref long no.bytes [, long level, long wait.flag, ref string mask()] )` |
|  | [bms.send()](bms.send.md) | `( string broadcast(2048), long level_or_evt[(EVTMAXSIZE)], string mask(32), long processno [, long no.bytes] )` |

## Bucket messages
```

string
```
```

long
```
```

long
```
| | | |
|---|---|---|
|  | [receive.bucket$()](receive.bucket.md) | `( ref long processno )` |
|  | [send.bucket()](send.bucket.md) | `( long processno, string bucket(100) )` |
|  | [send.wait()](send.wait.md) | `( long processno, string bucket(100) )` |

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)
- [Interprocess communication (bshell) overview](overview.md)
