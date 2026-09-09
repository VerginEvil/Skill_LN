# ProjectBudget.StartGenerateControlData

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectBudget
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1721-1722

```baan
DLL:   tpextptcapi
This function is available from 2025.12 (KB3631460).
Syntax: long ProjectBudget.StartGenerateControlData(
domain  tccprj           iFromProject,
domain  tccprj           iToProject,
domain  tppdm.yeno       iNetChange,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to start the session
Generate Control Data (tpptc1230m000).
Transaction management is handled by the Public Interface.
Pre:    None
Post:   None
Input:  iFromProject            - From Project. Optional
iToProject              - To Project. Optional
iNetChange              - Net Change. Mandatory
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
