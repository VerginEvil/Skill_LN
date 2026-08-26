# 'No hints' hint
By default the driver generates a hint for each query it sends to the RDBMS (assuming the RDBMS supports hints of course). With the hint 'no hints' you tell the driver not to generate these default hints. The 'no hint' hint can be specified in combination with other hints. This may seem contradictory, however there are cases in which this can be useful. For information on this see the link to the section on execution plans in a distributed environment below.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
- [Hints in a distributed environment](hints_in_a_distributed_environment.md)
