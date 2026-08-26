# ProductionOrderHours.InsertActiveLine

> Chapter: Chapter 45 Public Interfaces for Time Management
>
> Group: Public Interfaces for ProductionOrderHours
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1897-1898

```baan
DLL:   bpexttmmapi
This function is available from     2023.02 (KB2272425  ).
Syntax: long ProductionOrderHours.InsertActiveLine(
domain  tcncmp           iLogisticCompany,
domain  tcorno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcemno           iEmployee,
domain  tcdate           iStartDateTime,
domain  tcyesno          iSetupTimeIndicator,
domain  tctano           iTask,
domain  bptmm.mcno       iMachine,
domain  tccwoc           iWorkCenter,
ref     domain  tcccp.yrno       oYear,
ref     domain  tcccp.peri       oPeriod,
ref     domain  bpmdm.serd       oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to create a production hours line with
status Active.
Pre:    Caller must set retry              -point.
Post:   Caller must commit/abort transaction.
Input:  iLogisticCompany                      - Logistic Company      (Mandatory)
iProductionOrder                              - Production Order      (Mandatory)
iOperation                                    - Operation             (Mandatory)
iEmployee                                     - Employee              (Mandatory)
iStartDateTime                                - Start Date and Time   (Mandatory)
iSetupTimeIndicator                           - Setup Time Indicator  (Mandatory)
Possible values :
Yes             (tcyesno.yes)
No              (tcyesno.no)
iTask                                         - Task                  (Mandatory)
iMachine                                      - Machine               (Not Mandatory)
iWorkCenter                                   - Work Center           (Mandatory)
Output:
oYear                                         - Year
oPeriod                                       - Period
oSequence                                     - Sequence
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Active Production Order Hours Line
Inserted.
<> 0                                          - Active Production Order Hours Line not
inserted.
```
