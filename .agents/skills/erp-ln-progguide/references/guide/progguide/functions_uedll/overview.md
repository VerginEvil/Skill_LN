# User Exit DLL Overview

## Overview
A User Exit DLL (UEDLL) is a DLL that will reside outside the standard software. It will have the same name as a standard DAL with the extension 'ue' (for 'user exit'). E.g. 'whinh200ue' for table whinh200. Customers can implement a UEDLL in order to be able to define extra business logic before and after the standard 'before' and 'after' handling of saves and deletes, by means of specific hooks that will be executed by the [4GL engine](../glossary/glossary.md#fourgl_engine) and/or DAL Engine. Stand-alone database operations (not triggered by saves and deletes of the [4GL engine](../glossary/glossary.md#fourgl_engine) or DAL Engine) are also extended to perform the extra business logic before and after performing the actual database operation. In this way it is possible to e.g. conditionally publish data changes to the outside world.

## Interaction with 4GL Engine / DAL Engine
When present, the User Exit DLL for a certain table will be loaded by the [4GL engine](../glossary/glossary.md#fourgl_engine)/DAL Engine by the time the DAL for this particular table will be loaded. In situations where no DAL is present this will be the moment at which a DAL would be loaded if it existed. This means that there is no need to have a DAL in order to make use of the UEDLL.

## Interaction with db operations
When one of the following database operations is executed stand-alone (so not as part of the standard save/deletes of the 4GL Engine or DAL Engine):

- [db.insert()](../functions_db_operations/db.insert.md)

- [db.update()](../functions_db_operations/db.update.md)

- [db.delete()](../functions_db_operations/db.delete.md)

and the User Exit DLL for the related table is present, the UEDLL will be loaded prior the database operation. This means that there is no need to have a DAL or a session in order to make use of the UEDLL.

## Preconditions
A DLL becomes a UEDLL when it meets the following conditions:

- Its name is consisting of the table code with 'ue' as suffix, like whinh200ue

- It includes bic_dal, as follows: `#include <bic_dal>`

## Restrictions
A UEDLL is treated like a regular DAL. This means all kind of DAL related functionality can be used, like:

- Function [with.old.object.values.do()](../functions_db_operations/with.old.object.values.do.md)

- Function [with.object.set.do()](../functions_db_operations/with.object.set.do.md)

- Pre-defined variable `subdal`

Note however that the following restrictions apply:

- Business methods cannot be implemented in a UEDLL Instead the business logic should be programmed in another (separate) general DLL.

- It is strongly discouraged to define other external functions in a UEDLL and link the UEDLL directly to other scripts. Instead, use a normal general DLL. (This also applies to regular DALs).

## User Exit Hooks
A UEDLL script can contain the following hooks:

- [ue.before.before.save.object()](ue.before.before.save.object.md)

- [ue.after.before.save.object()](ue.after.before.save.object.md)

- [ue.before.after.save.object()](ue.before.after.save.object.md)

- [ue.after.after.save.object()](ue.after.after.save.object.md)

- [ue.before.before.destroy.object()](ue.before.before.destroy.object.md)

- [ue.after.before.destroy.object()](ue.after.before.destroy.object.md)

- [ue.before.after.destroy.object()](ue.before.after.destroy.object.md)

- [ue.after.after.destroy.object()](ue.after.after.destroy.object.md)

- [disable.ue.dll()](disable.ue.dll.md)

- [enable.ue.dll()](enable.ue.dll.md)

- [disable.table.extension()](disable.table.extension.md)

- [enable.table.extension()](enable.table.extension.md)

- [ue.get.origin()](ue.get.origin.md)

## Related topics
- [Data Access Layer](../functions_dal/overview.md)
