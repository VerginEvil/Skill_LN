# ProjectActivity.SetInsertMode

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1705-1707

```baan
DLL:   tpextpssapi
This function is available from     2022.12 (KB2271119  ).
Syntax: long ProjectActivity.SetInsertMode(
domain  tcmcs.str30      iInsertMode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function sets the Insert Mode when creating new
activities for a Project. The Insert Mode indicates if the
new Activity is for a Top Activity, a Child Activity or
a Milestone and allows proper Activity DAL handling.
-                             To create a TOP activity, call the interface with
iInsertMode set to "TopActivity". The parent activity
(tppss200.pact) must remain empty in this case.
-                             To create a child activity, call the interface with
iInsertMode set to "ChildActivity". A parent activity
must exist and be specified as such (in tppss200.pact)
while filling the tppss200 record in this case.
-                             To create a Milestone, call the interface with
iInsertMode set to "Milestone". A parent activity
must exist and be specified as such (in tppss200.pact)
while filling the tppss200 record in this case.
To make sure that the selected insert mode is taken into account
properly, this public interface must be called before calling
dal.new.object() or dal.copy.object() for tppss200.
Note that there is no need to reset this insert mode after the
Activity has been created. The DAL of the Activities table
handles this automatically as it saves the data. This also means
that the insert mode must be set before the creation of each
activity separately.
Example:
if isspace(ParentActivity) then
ReturnValue = ProjectActivity.SetInsertMode(
"TopActivity",
ExceptionMessage,
ExceptionID)
else
ReturnValue = ProjectActivity.SetInsertMode(
"ChildActivity",
ExceptionMessage,
ExceptionID)
endif
if ReturnValue <> 0 then
return(ReturnValue)
endif
ReturnValue = dal.new.object("tppss200")
if ReturnValue <> 0 then
return(ReturnValue)
endif
dal.set.field("tppss200.cprj", MyProject)
dal.set.field("tppss200.cpla", MyPlan")
dal.set.field("tppss200.cact", NewActivity)
...
if not isspace(ParentActivity) then
dal.set.field("tppss200.pact", ParentActivity)
endif
ReturnValue = dal.save.object("tppss200")
if ReturnValue <> 0 then
return(ReturnValue)
endif
Pre:    None
Post:   None
Input:  iInsertMode             Indicates what kind of Activity is
being created, mandatory.
Possible values are:
-                                               TopActivity
-                                               ChildActivity
-                                               Milestone
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Successful
<> 0                                          - An error occurred
```

## Public Interfaces for ProjectAccounting

The following functions are available: ProjectAccounting.GenerateInterimResults ProjectAccounting.GlobalApprove ProjectAccounting.ProcessTransactions
