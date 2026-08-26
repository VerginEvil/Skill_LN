# Project.Activate

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1670-1671

```baan
DLL:   tpextpdmapi
This function is available from     2021.10 (KB2208839  ).
Syntax: long Project.Activate(
domain  tccprj           iProject,
boolean          iUserInteraction,
ref             boolean          oCanceledbyUser,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will Activate the given Project.
After the Project is Activated, the next Automatic Steps in the
Project Procedure will be executed.
This function must not be called within a logical transaction
as this function will have its own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iProject                      - The Project that needs to be Activated
(Mandatory).
iUserInteraction
Possible values are:
TRUE                               -  The function is called from a LN Session, the
user could be asked to confirm certain
exceptions (like the project is not linked to a
contract or a capital project has no assets).
FALSE                               - The function is called from a background process,
the project activation continues without user
interaction.
Note that, when this argument is true, the user may
reject certain exceptions. As this is by decision of the
user, it is not considered an error and the return value
of the public interface is zero (no error) if this
occurs. To allow the calling program to recognize and
handle this situation, the output argument
oCanceledbyUser will be set to true in this case.
Output:
oCanceledbyUser                       - If this public interface was called
with iUserInteraction = true and the
user rejects an exception, this
argument is returned as true to
indicate that the project activation
was canceled by the user.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The Project is Activated, or the
activation was canceled by the user.
<> 0                                          - An error occurred
```
