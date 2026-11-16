# Row mode hint
There are two row mode hints: 'first rows' and 'all rows'. The first rows hint advises the query processor to evaluate the query in such a way that the first rows can be returned as quickly as possible. This hint may, for example, be used for queries that fetch rows for displaying purposes. Here it is important to have the first few records as quickly as possible. The all rows hint advises to do the opposite. It advises the query processor to execute the query so that the entire set is returned as quickly as possible. This is appropriate for queries in batch runs.
A row mode hint is only applicable to the Oracle level-2 driver. For any other driver this hint is ignored.

## Related topics
- [Hint types](hint_types.md)

- [Query hints overview](overview.md)
