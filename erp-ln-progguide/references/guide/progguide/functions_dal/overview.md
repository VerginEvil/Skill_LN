# Data Access Layer

## Overview
In BAAN applications, the [4GL engine](../glossary/glossary.md#fourgl_engine) provides the default functionality for a session. Changes or additions to the default functionality for a session are programmed in a UI-script (for UI specific tasks) and DAL (for Business Logic related tasks)
Programmers create a user interface (UI) script to change the default behavior of a session and a DAL script to program all the logical integrity rules for a particular table. So the DAL ensures the logical integrity of the database. As in previous versions of the software, the database server ensures the referential integrity of the database.
The DAL script for a particular table has the same name as that table. It is implemented as a DLL that can be accessed by user interface scripts (via the [4GL engine](../glossary/glossary.md#fourgl_engine)) and by other DALs. The following diagram illustrates the overall relationship of these components.

## Database integrity checks
The following are examples of some logical integrity rules that could be programmed in a DAL script:

- When customers have reached their credit limit, they cannot order further items.

- If the invoice for an order has been printed, the order cannot be changed.

- If the current VRC of a user is not equal to the package VRC of the program script, the script cannot be compiled.

Programming database integrity checks in a separate DAL script has two main advantages:

- *Code reuse:* The integrity rules do not have to be replicated in each session that uses a particular table.

- External applications can access the database via nthe DAL.

For an overview of the interaction between the user interface, the [4GL engine](../glossary/glossary.md#fourgl_engine), and the DAL, see [UI, DAL, and STP interaction](dal_ui_and_stp_interaction.md).

## Business methods
In addition to performing data integrity checks, the DAL provides business methods for handling non-interactive database modifications such as printing sales orders or posting all orders to history.
A business method is a function that performs a task that involves manipulating and/or checking one or more tables in the database. The function is programmed in a DAL script and can be called directly from a UI script. It must be programmed in the DAL script of the most relevant table.
Users can activate a business method with a single command. There is then no further user interaction. The UI script calls the relevant function in the DAL script. The function performs all operations to complete the required task. The user must wait until the business method finishes before continuing with other tasks. However, if a [Progress indicators overview and synopsis](../functions_progress_indicators/overview_and_synopsis.md) is provided, the user can cancel the business method by clicking on the Cancel button.
The UI script starts a business method by calling the [dal.start.business.method()](../functions_db_operations/dal.start.business.method.md) function

## Extended DAL (DAL2)
The DAL2 concept is an extension of the DAL concept, that allows better re-use of business logic. See [Extended DAL (DAL2)](dal2_overview.md) for more information.

## Related topics
- [DAL terminology](dal_glossary.md)

- [UI, DAL, and STP interaction](dal_ui_and_stp_interaction.md)

- [DAL hooks](dal_hooks.md)

- [Data Access Methods (DAM)](dam.md)

- [Property methods](property_methods.md)

- [Query extensions](query_extensions.md)

- [Communication with STP and CDAS](communication_with_stp_and_cdas.md)

- [Transition issues (BAAN IV to Infor Enterprise Server)](transition_issues_baan_iv_to_baanerp.md)

- [Extended DAL (DAL2)](dal2_overview.md)
