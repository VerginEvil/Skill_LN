# Workflow.DisableSubmit

> Chapter: Chapter 44 Public Interfaces for Object Configuration Management
>
> Group: Public Interfaces for Workflow
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1911-1912

```baan
DLL:   tcextocmapi
This function is available from 2023.02 (KB2220087).
Syntax: long Workflow.DisableSubmit(
domain  tcmcs.str6       iObjectType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   A Workflow Model contains Object Types which contain tables.
This function disables the Workflow action Submit for the tables
related to the Object Type. The related tables are checked out,
but are not submitted for approval. The Workflow action Submit is
disabled for updates in the current process.
This function can be used in a process that updates multiple tables
and the update in one table is automatically submitted for approval.
Then another update on that table in the same process results in an
error message: <Object> has the 'Pending' status. To avoid this error,
the function Workflow.DisableSubmit() should be called before the
first update on the table and function Workflow.EnableSubmit() should
be called after the first update on the table.
Example:
Updating the Name of a Business Partner (tccom100.nama) will
automatically update the Search Key of all roles of that Business
Partner. If the Invoice-from role is active for the BP, tccom122.seak
is updated and the tccom122 record is automatically checked out and
submitted if Object Type "TCIFBP" is enabled. If the same process
wants to make an update on the Invoice-from role for the BP (tccom122),
the error Invoice-from Business Partner [<BP>] has the 'Pending' status
is returned. The Workflow.DisableSubmit() function can be used before
updating tccom100.nama to disable the submit for tccom122 (Object
Type "TCIFBP"). The Workflow.EnableSubmit() function can be used
after updating tccom100.nama and before updating Invoice-from BP data
(tccom122) to enable the submit for tccom122 and other tables.
Coding example:
long            return.value
domain  tcmcs.s999m     exception.message
long            exception.id
return.value = Workflow.DisableSubmit(
"TCIFBP",
exception.message,
exception.id)
if return.value <> 0 then
dal.set.error.message("@" & exception.message)
return(return.value)
endif
|* Update tccom100.nama
|* dal.save.object("tccom100")
|* Automatically tccom122.seak is updated, object is checked out
|* and submit function is called; submit is not executed.
return.value = Workflow.EnableSubmit(
exception.message,
exception.id)
if return.value <> 0 then
dal.set.error.message("@" & exception.message)
return(return.value)
endif
|* Update tccom122 data
|* dal.save.object("tccom122")
|* Checked out Object is updated and submitted for Workflow approval.
Pre:    none
Post:   Function Workflow.EnableSubmit() must be called to enable the
Workflow action Submit of all Object Types . Submitting the checked
out Objects is required as well if this is not yet done.
Input:  iObjectType             - object type (mandatory)
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success
<> 0                    - An error occurred
```
