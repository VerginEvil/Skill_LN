# SalesOrder.StartPrintAcknowledgement

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 331-332

```baan
DLL:   tdextslsapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long SalesOrder.StartPrintAcknowledgement(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tccom.bpid       iFromBusinessPartner,
domain  tcorno           iFromSalesOrder,
domain  tccwoc           iFromSalesOffice,
domain  tccom.bpid       iToBusinessPartner,
domain  tcorno           iToSalesOrder,
domain  tccwoc           iToSalesOffice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Print Sales Order
Acknowledgement/RMAs (tdsls4401m000). Depending on the main
table of the calling session, Non                      -Consecutive Record Selection
(NCRS) is used.
When the main table is:
Sales Orders            (tdsls400) or
Sales Order Lines       (tdsls401) or
Sales Order Activities  (tdsls413) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromBusinessPartner
From Business Partner selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromSalesOrder
From Sales Order selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromSalesOffice
From Sales Office selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable)
iToBusinessPartner
To Business Partner selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToSalesOrder
To Sales Order selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToSalesOffice
To Sales Office selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```
