# DB DLL Overview

## Overview
A DB DLL (DBDLL) is a DLL with the same name as a standard DAL with the extension 'db'. E.g. 'whinh200db' for table whinh200. A DBDLL can be implemented in order to be able to log database actions (insert update or delete) by means of specific hooks that will be executed by the 4GL engine and/or DAL Engine. Stand-alone database operations (not triggered by saves and deletes of the 4GL engine or DAL Engine) are also extended to perform the extra business logic before and after performing the actual database operation. In this way it is possible to log database actions.

## Interaction with 4GL Engine / DAL Engine
When present, the DB DLL for a certain table will be loaded by the 4GL engine/DAL Engine by the time the DAL for this particular table will be loaded. In situations where no DAL is present this will be the moment at which a DAL would be loaded if it existed. This means that there is no need to have a DAL in order to make use of the DBDLL.

## Interaction with db operations
When one of the following database operations is executed stand-alone (so not as part of the standard save/deletes of the 4GL Engine or DAL Engine):
- [db.insert()](../functions_db_operations/db.insert.md)
- [db.update()](../functions_db_operations/db.update.md)
- [db.delete()](../functions_db_operations/db.delete.md)  and the DB DLL for the related table is present, the DBDLL will be loaded prior the database operation. This means that there is no need to have a DAL or a session in order to make use of the DBDLL. During the execution of the hooks (initiated by a database operation) the boolean initiated.by.dal will be false.

## Preconditions
A DLL becomes a DBDLL when it meets the following conditions:
- Its name is consisting of the table code with 'db' as suffix, like whinh200db
- It includes bic_dal, as follows: `#include <bic_dal>`

## Restrictions
A DBDLL is treated like a regular DAL. This means all kind of DAL related functionality can be used, like:
- Function ` [with.old.object.values.do()](../functions_db_operations/with.old.object.values.do.md)`
- Function ` [with.object.set.do()](../functions_db_operations/with.object.set.do.md)`
- Pre-defined variable `subdal`  Note however that the following restrictions apply:
- Business methods cannot be implemented in a DBDLL Instead the business logic should be programmed in another (separate) general DLL.
- It is strongly discouraged to define other external functions in a DBDLL and link the DBDLL directly to other scripts. Instead, use a normal general DLL. (This also applies to regular DALs).   The execution of db hooks can be enabled/disable with the following commands
- ` [disable.db.dll()](disable.db.dll.md)`
- ` [enable.db.dll()](enable.db.dll.md)`

## DB Hooks
A DBDLL script can contain the following hooks:
- ` [db.before.insert()](db.before.insert.md)`
- ` [db.after.insert()](db.after.insert.md)`
- ` [db.before.update()](db.before.update.md)`
- ` [db.after.update()](db.after.update.md)`
- ` [db.before.delete()](db.before.delete.md)`
- ` [db.after.delete()](db.after.delete.md)`

## Flow of hooks
In case a DAL is involved, as well as a UE DLL, the flow of the hooks is as follows (example of an insert):
- 1. ue.before.before.save.object (in UE DLL)
- 2. before.save.object (in DAL)
- 3. ue.after.before.save.object (in UE DLL)
- 4. db.before.insert (in DB DLL)
- 5. <actual db.insert>
- 6. db.after.insert (in DB DLL)
- 7. ue.before.after.save.object (in UE DLL)
- 8. after.save.object (in DAL)
- 9. ue.after.after.save.object (in UE DLL)

## Related topics
- [Data Access Layer](../functions_dal/overview.md) [DB DLL Overview](overview.md)
