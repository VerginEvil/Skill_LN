# ProjectBudget.GenerateControlData

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectBudget
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1701-1701

```baan
DLL:   tpextptcapi
This function is available from     2026.05 (KB3666609  ).
Syntax: long ProjectBudget.GenerateControlData(
domain  tccprj           iProject,
domain  tppdm.yeno       iNetChange,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to Generate Control Data for 1 Project
& set project activity status to 'Executed' in
Activities by Project table tppdm682.
Transaction management is handled by the Public Interface.
Pre:    None.
Post:   None.
Input:  iProject                              - Project. Mandatory
iNetChange                                    - Net Change. Mandatory
Allowed Values:
tppdm.yeno.yes                                - Process only changed records
tppdm.yeno.no                                 - Process all records
Output:
oExceptionMessage                             - The last message if any message is
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
