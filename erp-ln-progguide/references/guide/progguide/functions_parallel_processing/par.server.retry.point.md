# par.server.retry.point()

## Syntax:
`function void par.server.retry.point( )`

## Description
This function is used for setting a not real retry point after a db.retry.point (). It must be used together with function [par.server.retry.hit()](par.server.retry.hit.md). See section: [Parallel Application Processing Database Retries](retries.md) for a further explanation.

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
