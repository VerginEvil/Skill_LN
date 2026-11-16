# ProductionOrder.StartResetStatus

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 780-780

```baan
DLL:   tiextsfcapi
This function is available from 2023.09 (KB2298685).
Syntax: long ProductionOrder.StartResetStatus(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcsite           iSite,
domain  tcpdno           iFromProductionOrder,
domain  tcpdno           iToProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Reset Production Orders Status
(ticst0203m000).
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
This argument determines whether user defaults are used.
User defaults should take precendence when
iIgnoreSelectionFields is set to false.
iSite
Site selection field is filled with this value.
Optional (used when iIgnoreSelectionFields is false and
NCRS is not applicable)
iFromProductionOrder
From Production Order selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
iToProductionOrder
To Production Order selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
Output: ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    Error Occurred
```
