# Execution plan hints
The hints are divided into two groups:
- *Execution plan hints*, hints that influence the actual execution plan of the query
- *General hints*; hints that do not influence the execution plan but that may influence other parameters, like for example buffer sizes.   The table below shows which hint belongs to which group:
| | |
|---|---|
| Execution plan hints | General hints |
| Index hint | Buffer hint |
| Row mode hint | Array fetching hint |
| Ordered hint | Array size hint |
| String hint | 'No hints' hint |
For the Oracle level-2 driver the execution plan hints are translated into native hints and added to the SQL query that is sent to the Oracle RDBMS. The execution plan hints are added according to the following rules:
1. If there are execution plan hints specified then no default hints are added. The execution plan hints replace the default hints.
1. The string hint is always the first hint in the hint text added to the SQL query.
1. If there are no execution plan hints but there is a 'no hints' hint, then no hints are added at all.
1. If there are no execution plan hints and the 'no hints' hint is not specified default hints are generated.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
