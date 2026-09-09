# artm.redefine.transaction.class()

## Syntax:
`function long artm.redefine.transaction.class( string tran.name(128), [ long metric.type, string metric.name(44) ] )`

## Description
Updates the metrics of a predefined session transaction class at the beginning of a session.
The 4GL-Engine normally defines a transaction class (without metrics) on session startup for each form command to be measured. If the 4GL-developer wants to do an update on this transaction with specific metrics, they must redefine the transaction class themselves.
Call this function in section before.program.
Note: if you redefine an existing form command transaction class, you must also handle the start and stop of the transaction yourself. The 4GL-Engine will not take care of this anymore.
Implement begin.transaction() in the begin and end.transaction() in the end of the function that is attached to the form command.

## Arguments
| | | |
|---|---|---|
| `string` | `tran.name(128)` |  The name of the form command function. It must be unique within the application. The 4GL-Engine determines through this name which transaction you want to redefine. Therefore, it must match the function’s name exactly.  |
| `[ long` | `metric.type ]` |  It is possible to pass several metrics to ARTM. These metrics give information about the status of a transaction. Artm.define.transaction.class() is used to define the metrics to be used in the transaction class. Each metric consists of an id, which determines the type of metric, and a descriptive name. Five metrics can be passed at a maximum. These metrics may be chosen arbitrarily from the following list: ARTM.COUNTER (long) A counter must be used when it makes sense to add up the values over an interval. Examples are bytes printed and records written. ARTM.GAUGE (long) A gauge must be used instead of a counter when it is not meaningful to add up the values over an interval. An example is the amount of memory used. ARTM.NUMERIC (long) A numeric id is simply a numeric value that is used as an identifier, and not as a measurement value. Examples are message numbers and error codes. ARTM.CODE (string(8)) A measurement agent should process a string in the same way as a numeric id. As with numeric ids it is not meaningful to do arithmetic operations on a string value.  |
| `[ string` | `metric.name(44) ]` |    |

## Return values
| | |
|---|---|
| >= 0 | The unique transaction class id. This id has to be passed to function artm.begin.transaction() for each transaction of this class. |
| < 0 | The registering of the class failed. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Application Response Time Measurement (ARTM) Overview](artm_overview.md)

- [Application Response Time Measurement (ARTM) Synopsis](artm_synopsis.md)

- [Application Response Time Measurement (ARTM) Debugging](artm_debugging.md)

- [Application Response Time Measurement (ARTM) Error Codes](artm_error_codes.md)

- [Application Response Time Measurement (ARTM) Examples](artm_examples.md)
