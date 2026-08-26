# artm.define.transaction.class()

## Syntax:
`function long artm.define.transaction.class( string tran.name(128), string tran.detail(128), [ long metric.type, string metric.name(44) ] )`

## Description
Assigns a unique identifier to a transaction class, and optionally to describe the format of additional data passed on by artm.begin.transaction (), artm.update.transaction(), and the artm.end.transaction() calls. This is normally done during the initialization of the specified application. The value returned by artm.define.transaction.class() is passed as a parameter in artm.begin.transaction() calls to identify which class of transaction is starting.
A transaction class is a description of a unit of work, such as Check Account Balance. Any number of transaction classes can be defined within each application.

## Arguments
| | | |
|---|---|---|
| `string` | `tran.name(128)` |  The unique name of a transaction class. It is defined for each transaction class by the application developer. It must be unique within the application.  |
| `string` | `tran.detail(128)` |  Additional information about a transaction class. If no tran.detail is associated with this transaction, the string must be empty.  |
| `[ long` | `metric.type ]` |  It is possible to pass several metrics to ARTM. These metrics give information about the status of a transaction. Artm.define.transaction.class() is used to define the metrics to be used in the transaction class. Each metric consists of an id, which determines the type of metric, and a descriptive name. Five metrics can be passed at a maximum. These metrics may be chosen arbitrarily from the following list: ARTM.COUNTER (long) A counter must be used when it makes sense to add up the values over an interval. Examples are bytes printed and records written. ARTM.GAUGE (long) A gauge must be used instead of a counter when it is not meaningful to add up the values over an interval. An example is the amount of memory used. ARTM.NUMERIC (long) A numeric id is simply a numeric value that is used as an identifier, and not as a measurement value. Examples are message numbers and error codes. ARTM.CODE (string(8)) A measurement agent should process a string in the same way as a numeric id. As with numeric ids it is not meaningful to do arithmetic operations on a string value.  |
| `[ string` | `metric.name(44) ]` |  |
-
-
-
-

## Return values
| | |
|---|---|
| >= 0 | The unique transaction class id. This id has to be passed to function artm.begin.transaction() for each transaction of this class.  |
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
