# Project.UpdateStatus

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1697-1698

```baan
DLL:   tpextpdmapi
This function is available from 2024.11 (KB3540370).
Syntax: long Project.UpdateStatus(
domain  tccprj           iProject,
domain  tppdm.psts       iFromProjectStatus,
domain  tppdm.psts       iToProjectStatus,
domain  tppdm.psts       iNewStatus,
domain  tppdm.yeno       iWorkAuthorizationStatus,
domain  tppdm.pstf       iFinancialResultStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to Update the status of project.
This function offers similar functionality as session
(tppdm6202m000 - Update of Project Status).
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iProject                - Project. Mandatory
iFromProjectStatus      - From Project Status. Optional
iToProjectStatus        - To Project Status. Optional
iNewStatus              - New Status. Mandatory
Allowed values for iFromProjectStatus, iToProjectStatus and
iNewStatus are:
tppdm.psts.free         - Free
tppdm.psts.construction - Active
tppdm.psts.finished     - Finished
tppdm.psts.closed       - Closed
iWorkAuthorizationStatus- Work Authorization Status. Optional
iFinancialResultStatus  - Financial Result Status. Optional
Allowed values for iFinancialResultStatus are:
tppdm.pstf.free           - Free
tppdm.pstf.definite.before- Determine Result
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Successful
<> 0                    - An error occurred
```
