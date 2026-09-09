# DAL Change Management hooks
In order to support Workflow Document Authorization, the DAL layer has been extended to support a number of new hooks. These hooks are executed by the Database Change Management (DBCM) layer (see [Database Change Management (DBCM) overview](../functions_dbcm/overview.md)).
Note that these hooks should only be implemented in the DAL of the root table of a Business Object.

## Available object hooks
- [on.submit()](on.submit.md)

- [on.recall()](on.recall.md)

- [on.reject()](on.reject.md)

- [on.set.draft()](on.set.draft.md)

- [on.set.approved()](on.set.approved.md)

- [on.set.recalled()](on.set.recalled.md)

## Related topics
- [Data Access Layer](overview.md)

- [Database Change Management (DBCM) overview](../functions_dbcm/overview.md)
