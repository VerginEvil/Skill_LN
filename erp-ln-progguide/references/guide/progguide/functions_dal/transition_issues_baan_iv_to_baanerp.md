# Transition issues (BAAN IV to Infor Enterprise Server)

## 4GL event sections
This table lists the 4GL event sections that have been moved to the DAL in Infor Enterprise Server. It also lists the DAL methods that replace these sections.
If a DAL script exists for a particular table, the 4GL engine calls the methods in the DAL to perform the relevant integrity checks. Any corresponding 4GL event sections in the UI script are ignored. If there is no DAL for the table, the 4GL event sections are executed.
| | |
|---|---|
| 4GL event sections | DAL methods |
|  field.< *x* >: check.input:  | function extern long < *x* >.check()  |
|  main.table.io: before.read:  | function extern long before.get.object() |
|  main.table.io: after.read:  | function extern long after.get.object() |
|  main.table.io: before.write:  | function extern long before.save.object() |
|  main.table.io: after.write:  | function extern long after.save.object() |
|  main.table.io: before.rewrite:  | function extern long before.save.object() |
|  main.table.io: after.rewrite:  | function extern long after.save.object() |
|  main.table.io: before.delete:  | function extern long before.destroy.object() |
|  main.table.io: after.delete:  | function extern long after.destroy.object() |

## 4GL functions
This table lists those 4GL UI functions that have DAL equivalents. If a DAL exists for a particular table, it is preferable to use the DAL functions instead of the 4GL UI functions.
| | |
|---|---|
| 4GL function | DAL function |
| on.main.table() | with.object.set.do() |
| on.old.occ() | with.old.object.values.do() |
| set.input.error() |  dal.set.error.message() return(DALHOOKERROR)  |
| skip.io() |  dal.set.error.message() return(DALHOOKERROR)  |
| abort.io() |  dal.set.error.message() return(DALHOOKERROR)  |
| db.update() | dal.update() |
| db.delete() | dal.destroy() |
| db.insert() | dal.new() |
If a function is used only in the DAL, you should move it to the DAL. If a function is used in both the DAL and the UI, you can move it to the DAL (the UI can call functions in the DAL but not vice versa). Alternately, you can store the function in a separate DLL that is linked to both the UI and the DAL.

## Session codes
The DAL does not recognize session codes ( *prog.name$*) and so cannot evaluate them. However, in the case where integrity checks must be session dependent, a solution is to evaluate properties instead of session codes. For example, you could identify a field or a combination of fields whose value(s) uniquely identify the session. Or you could add a property to the object set and give this property a value that is unique to the session.

## Predefined variables
The predefined variable *previous.choice* is not supported in the DAL, as the DAL does not recognize standard commands. Instead, the first argument in the *before.save.object()* and *after.save.object()* hooks indicates if an insert or update operation caused the save operation. Note that for the DAL, the copy command is an insert operation.
The predefined variable *before.update.check* is not supported in the DAL. In Infor Enterprise Server, field checks are executed both after field input and before the database operation. The programmer cannot influence when these checks are performed. Note that in the CDAS, checking is programmed in the *dal.set.property()* hook and not in the *dal.after.save.object()* hook.

## Questions
It is not possible to ask for user input during the execution of DAL hooks. If hooks contain conditions that depend on user input, set the condition before the hook is called. Alternately, handle the user input and check the conditions after completion of the database operations.

## Messages
The DAL cannot display error messages directly. However, you can set an error message in the DAL with the *dal.set.error.message()* method. The DAL can notify the calling process of an error by returning the value DALHOOKERROR. The process can then display the error message. Messages can be stacked before they are retrieved by the UI.

## Non-table fields
Only table fields are checked in the DAL. Checks for non-database fields must still be programmed in the UI script.

## Include files
When writing a Data Access Layer, you must include bic_dal. To use progress indicators and Data Access Methods in your UI, you must include bic_dam.

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
