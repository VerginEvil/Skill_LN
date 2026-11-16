# Project.GetCostRateTask

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1692-1693

```baan
DLL:   tpextpdmapi
This function is available from 2026.04 (KB3650826).
Syntax: long Project.GetCostRateTask(
domain  tccprj           iProject,
domain  tppdm.task       iTask,
boolean          iConsiderContract,
domain  tppdm.cspa       iElement,
domain  tppdm.cact       iActivity,
domain  tpptc.cstl       iExtension,
domain  tcemno           iEmployee,
boolean          iCostControl,
domain  tccuni           iRequestedUnit,
domain  tcccur           iCurrency,
ref     domain  tppdm.abfc       oCostRate,
ref     domain  tcccur           oCostRateCurrency,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the cost rate and cost rate currency
for the given Task.
Pre:    Not Applicable. This function does not require a retry point and
does not perform transaction management.
Post:   Not Applicable. No commit or abort is performed.
Input:  iProject                - Project. Mandatory
iTask                   - Task. Mandatory
iConsiderContract       - Consider Contract. Mandatory (True/False)
True, Sold-to Business Partner will get from the
Contract,Contract Line and this Sold-to Business
Partner
will be used to get the Labor rates.
False, Labor rates will get from the Project
level.
iElement                - Element. Optional
If iElement is passed and iConsiderContract is
True
Sold-to Business Partner will get from the
Contract, Contract Line which is linked to
iElement.
iActivity               - Activity. Optional
If iActivity is passed and iConsiderContract is
True
Sold-to Business Partner will get from the
Contract, Contract Line which is linked to
iActivity.
iExtension              - Extension. Optional
If iExtension is passed then Sold-to Business
Partner
will get from the Extension linked to iProject.
iEmployee               - Employee. Optional
If iEmployee passed and the Path for Hours Labor
Rate
is by Employee or Trade Group in iProject then
the Labor rates will get from the Employee.
iCostControl            - Cost Control. Mandatory (True/False)
True, Labor Rate will consider from
Hours Accounting Level.
False, Labor Rate will consider from
Actual Budget Level.
iRequestedUnit          - Requested Unit. Optional
iCurrency               - Currency. Optional
Output: oCostRate               - Cost Rate
oCostRateCurrency       - Cost Rate Currency
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Cost Rate determined successfully
<> 0                    - Cost Rate not determined
```
