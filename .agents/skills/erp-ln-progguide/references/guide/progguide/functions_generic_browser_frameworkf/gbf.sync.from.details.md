# gbf.sync.from.details()

## Syntax:
`#include <bic_gbf>`
`function long gbf.sync.from.details( long key.object, long update.mode )`

## Description
This function will be called by the GBF if the GBF is part of a Tree-Detail and a change was made on the Details part by the user.
The application should decide which part of the tree should be refreshed. In the key.object the key of the record that triggered the synchronization is set. The key.object can be used to determine which part of the tree should be refreshed. The update.mode can also be used to optimize the refreshing of the Tree. Also the selected key-field variables, that are used to set the node selection in the Tree in the functions [gbf.get.children()](gbf.get.children.md) and [gbf.get.top.level()](gbf.get.top.level.md), should be set.

## Arguments
| | |
|---|---|
| GBF_TD_NEW | Record with the key values of key.object has been added |
| GBF_TD_UPDATE | Record with the key values of key.object has been changed |
| GBF_TD_DELETE | Record with the key values of key.object has been deleted |
| GBF_TD_REFRESH | Record with the key values of key.object is currently displayed |

## Return values
The return value is treated in the same way as with the [gbf.menu.selected()](gbf.menu.selected.md) function. The values GBF.DO.RESTART.LEVEL or GBF.DO.RESTART.TREE are the ones most commonly used in this function.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2230.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Key fields Object overview](../functions_keyfields/overview.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)
