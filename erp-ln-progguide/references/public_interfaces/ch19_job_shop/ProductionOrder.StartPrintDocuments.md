# ProductionOrder.StartPrintDocuments

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 777-778

```baan
DLL:   tiextsfcapi
This function is available from     2023.04 (KB2274307  ).
Syntax: long ProductionOrder.StartPrintDocuments(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcsite           iSite,
domain  tcpdno           iFromProductionOrder,
domain  tcpdno           iFromOrderGroup,
domain  tcpdno           iToProductionOrder,
domain  tcpdno           iToOrderGroup,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Print Production Order
Documents(tisfc0408m000).
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
This argument determines whether user defaults are used.
User defaults should take precendence when
iIgnoreSelectionFields is set to false.
iSite
Site (mandatory) if Site concept is active.
iFromProductionOrder
From Production Order field selection field is filled
with this value. (used when iIgnoreSelectionFields
is false and NCRS is not applicable)
iFromOrderGroup
From Order Group selection field is filled with this
value. (used when iIgnoreSelectionFields is false
and NCRS is not applicable)
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
