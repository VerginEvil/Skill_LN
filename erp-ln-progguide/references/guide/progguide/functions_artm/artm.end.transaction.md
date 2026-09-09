# artm.end.transaction()

## Syntax:
`function long artm.end.transaction( long artm.transaction.id, long tran.status, [ long metric.type, void metric.value ] )`

## Description
Marks the end of a transaction instance that was started with artm.begin.transaction(). artm.end.transaction () should be called from the application program just after each transaction instance ends.

## Arguments
| | | |
|---|---|---|
| `long` | `artm.transaction.id` |  The unique handle from the artm.begin.transaction () call that marked the start of this transaction instance. Artm.transaction.id must be passed in each artm.end.transaction() call. Many transaction instances may be carried out at the same time from this and other applications, so this handle is essential for the measurement agent to identify which transaction instance is stopping. If artm.transaction.id is less than zero, this artm.end.transaction () call will be treated as a NULL operation, and a negative value is returned.  |
| `long` | `tran.status` |  The completion code of the transaction, as determined by the application: ARTM.TRANSACTION.SUCCESS Use this value when the operation is completed normally and as expected. ARTM.TRANSACTION.ABORTED Use this value when there was a fundamental failure in the system. ARTM.TRANSACTION.FAILED Use this value in application where the transaction worked properly, but no result was generated.  |
| `[ long` | `metric.type ]` |  The metrics, as defined in artm.define.transaction.class(), can be updated here. Each metric consists of an id, which determines the type of metric, and its current value. The value must be of the correct type. See artm.define.transaction.class() for the types. The amount of metrics must not exceed the amount as defined in artm.define.transaction.class(). The metrics must also be passed in the same sequence. It is possible to skip the metrics you don’t want to pass. In that case, pass ARTM.METRIC.SKIP as the metric type, and omit the metric value. If the last metrics are of this type, you don’t need to pass them at all.  |
| `[ void` | `metric.value ]` |    |

## Return values
| | |
|---|---|
| >= 0 | Success |
| < 0 | An error occurred in communicating with the measurement agent, or ARTM is switched off. The most likely cause is passing an invalid value for artm.transaction.id. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Application Response Time Measurement (ARTM) Overview](artm_overview.md)

- [Application Response Time Measurement (ARTM) Synopsis](artm_synopsis.md)

- [Application Response Time Measurement (ARTM) Debugging](artm_debugging.md)

- [Application Response Time Measurement (ARTM) Error Codes](artm_error_codes.md)

- [Application Response Time Measurement (ARTM) Examples](artm_examples.md)
