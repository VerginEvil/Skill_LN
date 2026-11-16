# Application Response Time Measurement (ARTM) Synopsis
```
long
```
```
( string tran.name(128), string tran.detail(128), [long metric.type, string metric.name(44)] )
```
```
long
```
```
( long artm.transaction.id, long tran.status, [long metric.type, void metric.value] )
```
```
long
```
```
( long artm.transaction.class.id, [long metric.type, void metric.value] )
```
```
long
```
```
( long artm.transaction.id, [long metric.type, void metric.value] )
```
```
long
```
```
( long artm.transaction.id, long tran.status,[long metric.type, void metric.value] )
```
| | | |
|---|---|---|
|  | [artm.define.transaction.class()](artm.define.transaction.class.md) |  |
|  | [artm.redefine.transaction.class()](artm.redefine.transaction.class.md) |  |
|  | [artm.begin.transaction()](artm.begin.transaction.md) |  |
|  | [artm.update.transaction()](artm.update.transaction.md) |  |
|  | [artm.end.transaction()](artm.end.transaction.md) |  |

## Related topics
- [Application Response Time Measurement (ARTM) Overview](artm_overview.md)

- [Application Response Time Measurement (ARTM) Error Codes](artm_error_codes.md)

- [Application Response Time Measurement (ARTM) Debugging](artm_debugging.md)

- [Application Response Time Measurement (ARTM) Examples](artm_examples.md)
