# ProductionOrder.StartClose

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 772-773

```baan
DLL:   tiextsfcapi
This function is available from 2023.05 (KB2274114).
Syntax: long ProductionOrder.StartClose(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcsite           iFromSite,
domain  tcpdno           iFromProductionOrder,
domain  tcpdno           iFromOrderGroup,
domain  tcsite           iToSite,
domain  tcpdno           iToProductionOrder,
domain  tcpdno           iToOrderGroup,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Close Production Orders
(ticst0201m000).
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
This argument determines whether user defaults are used.
User defaults should take precendence when
iIgnoreSelectionFields is set to false.
iFromSite
Site : if specified Site concept must be active.
From Site field selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
iFromProductionOrder
From Production Order field selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
iFromOrderGroup
From Order Group selection field is filled with this
value. (used when iIgnoreSelectionFields is false
and NCRS is not applicable)
iToSite
Site : if specified Site concept must be active.
To Site field selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
iToProductionOrder
To Production Order field selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
iToOrderGroup
To Order Group selection field is filled with this
value. (used when iIgnoreSelectionFields
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
