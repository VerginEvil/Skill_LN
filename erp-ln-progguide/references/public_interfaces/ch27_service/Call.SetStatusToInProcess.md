# Call.SetStatusToInProcess

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1365-1367

```baan
DLL:   tsextclmapi
This function is available from     2026.07 (KB3676338  ).
Syntax: long Call.SetStatusToInProcess(
domain  tcorno           iCall,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function changes the status of a Call to In Process and
therefore provides the same functionality as the form command
In Process on session tsclm1100m000.
The default functional behavior of this public interface is
that the Support Engineer is assigned, changed, or retained
to the current user, regardless of the initial value of the
field.
This public interface also provides the option to change the
status to In Process for another Support Engineer.
-                       If the system must always use the support engineer defined
on the call, the arguments AssignCallToMe and
AssignInProcessCallToMe must be set to tcyesno.no.
If the user only wants this behavior when the call is not yet
In Process, only AssignCallToMe must be set to tcyesno.no.
-                       If the system must not use the Support Engineer assigned
to the call, but instead assign a different support engineer,
the SupportEngineer argument must be filled. In this case, the
arguments AssignCallToMe and AssignInProcessCallToMe are ignored.
This function can only be used if the call is not blocked and
the current status of the call is not beyond In Process. If a
call with a later status is passed, no action is performed and
the function returns 0.
Note: the public interface does not update the timer.
Pre:    A db.retry.point() must have been specified.
Before calling Call.SetStatusToInProcess(), call
ProcessingOptionSet.Create() and assign the value to
iProcessingOptionSet.
Post:   An abort.transaction() or commit.transaction() must be executed.
After the call, the option set can be deleted by calling
ProcessingOptionSet.Delete().
Input:  iCall                                 - The Call for which the status must be
set to In Process; mandatory.
iProcessingOptionSet                          - Processing Option Set: a processing
option set number referring to a
processing option set containing at
least one valid option; mandatory.
NAME                    TYPE                    DEFAULT
================================================================
SupportEngineer         domain  tcemno          ""
The engineer to whom the call should be assigned.
If this argument is filled, the arguments AssignCallToMe
and AssignInProcessCallToMe are ignored and the
field will always be filled with the given value.
SupportDepartment       domain  tccwoc          ""
The Support Department to which the call is assigned.
If the argument is filled, the field is set explicitly.
If empty, the system defaults the field based on the
engineer.
AssignCallToMe          domain  tcyesno         tcyesno.yes
If the SupportEngineer is filled, this argument is
ignored.
Session behavior:
If the call is assigned to another engineer, the Support
Engineer is changed to the current user executing the
In Process form command.
Public interface behavior:
If tcyesno.yes, the Support Engineer is replaced by the
current user, conforming to the session behavior
described above.
If tcyesno.no, the call status is changed to In Process
for the already assigned Support Engineer, without
changing the Support Engineer.
AssignInProcessCallToMe domain  tcyesno         tcyesno.yes
If the SupportEngineer is filled, this argument is
ignored.
Session behavior:
If the call is assigned to another engineer, the Support
Engineer is changed to the current user executing the
In Process form command.
Public interface behavior:
If tcyesno.yes, the Support Engineer is replaced by the
current user, conforming to the session behavior
described above.
If tcyesno.no, the call status is changed to In Process
for the already assigned Support Engineer, without
changing the Support Engineer, even if the status was
In Process already.
Output: oExceptionMessage                     - The last message, if any is found.
If more than one message is given,
these are present in the oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No error
<> 0                                          - An error occurred.
```
