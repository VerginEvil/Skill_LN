# UI, DAL, and STP interaction

## Overview
A DAL script contains all the logic integrity rules for a particular object set. These rules are referred to as hooks and they can be programmed for every possible manipulation of an object in the object set. For each session with a main table, the [4GL engine](../glossary/glossary.md#fourgl_engine) ensures that the integrity rules for the table are checked each time an insert, update or delete operation is performed on an object of the table.
If there is no DAL script for the particular object set being accessed, no logic integrity checks are performed
A DAL script can contain hooks that prevent access to the database and hooks that prevent data being passed back to the user interface. The former are executed before the database action. The latter are performed after the database action.

## Example
If a user changes the address of a customer on a form, the [4GL engine](../glossary/glossary.md#fourgl_engine) changes the address for that customer in the database via the DAL. If you want certain restrictions to apply to the update action, you can program a property hook in the DAL of the session’s main table to impose these restrictions. For example:
```

when the address changes:
    if changed into something valid then
        accept
    else
        reject
    endif
```

## UI function calls
The UI script can use either the [Database operations overview](../functions_db_operations/overview.md) functions or the [Data Access Methods (DAM)](dam.md) to manipulate the database. The db.* functions are direct database calls. They do not use the DAL. In this case, any logic integrity checks required must be programmed in the UI script itself. This means that they cannot be reused by other sessions. In preference, use the DAL Data Access Methods. These access the database via the DAL, so all necessary checks are automatically performed.

## Function flow
When the DAL is used to manipulate the database, the main steps involved are as follows:

- The user issues a command through the user interface to access a record in the database.

- The [4GL engine](../glossary/glossary.md#fourgl_engine) loads the appropriate DAL and calls the hooks in the DAL to check the integrity rules for the object.

- If the particular database action is permitted, the [4GL engine](../glossary/glossary.md#fourgl_engine) issues the appropriate database call.

- After the database has been updated, the DAL can perform further checks to determine whether or not data is passed back to the user interface.

- The [4GL engine](../glossary/glossary.md#fourgl_engine) passes data back to the user interface (provided that the integrity rules permit this).

The following diagram illustrates this flow:

## One-way interaction
Note that because the DAL can be used in situations where there is no user interface, the DAL cannot call functions in the UI.

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [DAL hooks](dal_hooks.md)

- [Data Access Methods (DAM)](dam.md)

- [Property methods](property_methods.md)

- [Query extensions](query_extensions.md)

- [Communication with STP and CDAS](communication_with_stp_and_cdas.md)

- [Transition issues (BAAN IV to Infor Enterprise Server)](transition_issues_baan_iv_to_baanerp.md)
