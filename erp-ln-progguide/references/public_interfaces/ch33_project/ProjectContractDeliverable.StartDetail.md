# ProjectContractDeliverable.StartDetail

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContractDeliverable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1712-1712

```baan
DLL:   tpextpdmapi
This function is available from 2023.10 (KB2308375).
Syntax: long ProjectContractDeliverable.StartDetail(
long             iStartMode,
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
domain  tcpono           iDeliverable,
domain  tcpono           iSchedule,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Contract Deliverables
(tppds7100m100) when this function is called without
passing the iSchedule otherwise, starts session
Contract Deliverables Schedule (tppdm7100m200)
in detail mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iContract       - Contract; Mandatory
iContractLine   - Contract Line, Optional
iDeliverable    - Deliverable, Mandatory
iSchedule       - Schedule, Optional
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
