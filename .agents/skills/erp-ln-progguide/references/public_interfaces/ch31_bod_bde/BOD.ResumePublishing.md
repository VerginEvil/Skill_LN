# BOD.ResumePublishing

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1680-1680

```baan
DLL:   tcextbodapi
This function is available from 2022.11 (KB2267552).
Syntax: long BOD.ResumePublishing(
boolean          iAllBods,
domain  tcbod.name       iNoun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function resumes the publishing of all BODs or one
specified BOD in the current process.
Pre:    Function BOD.InterruptPublishing() should have been called to
interrupt the publishing.
Post:   N/A
Output:
iAllBods                - true: The publishing of all BODs in the
current process is resumed.
false: The publishing of the specified
BOD in the current process is resumed.
Value false is not allowed if function
BOD.InterruptPublishing() was called
with iAllBods as true.
iNoun                   - The (protected) Noun for which the
publishing must be resumed.
Mandatory if iAllBods is false. Not
needed / ignored if iAllBods is true.
oExceptionMessage       - A message if the return value is not equal
to 0. This message contains the root cause of
the request failure.
oExceptionID            - An ID that refers to all error information
if the return value is <> 0.
Use the functions in Exception to get
all relevant information.
Return:
0                       - The action to resume the publishing was set
successfully.
<> 0                    - The action to resume the publishing can not be
set.
```
