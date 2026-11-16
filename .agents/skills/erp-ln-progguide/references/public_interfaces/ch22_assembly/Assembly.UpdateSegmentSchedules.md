# Assembly.UpdateSegmentSchedules

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for Assembly
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 855-856

```baan
DLL:   tiextascapi
This function is available from 2021.09 (KB2204511).
Syntax: long Assembly.UpdateSegmentSchedules(
domain  cpcom.plnc       iScenario,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Update the Assembly Segment Schedules in a Planning Scenario.
Transaction management is handled within the Public Interface.
Pre:    Scenario must be initialized.
There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:
iScenario               - Planning Scenario (Mandatory).
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - If the Segment Schedules were properly
updated or no updates were required.
<> 0                    - Otherwise.
```
