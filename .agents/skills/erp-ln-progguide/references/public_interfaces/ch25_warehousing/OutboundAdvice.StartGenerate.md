# OutboundAdvice.StartGenerate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1198-1199

```baan
DLL:   whextinhapi
This function is available from 2022.07 (KB2243668).
Syntax: long OutboundAdvice.StartGenerate(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whinh.oorg       iFromOrderOrigin,
domain  tcorno           iFromOrderNumber,
domain  tcwset           iFromOrderSet,
domain  tcpono           iFromOrderLine,
domain  whinh.oorg       iToOrderOrigin,
domain  tcorno           iToOrderNumber,
domain  tcwset           iToOrderSet,
domain  tcpono           iToOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Generate Outbound Advice
(whinh4201m000). Depending on the main table of the calling
session, Non-Consecutive Record Selection (NCRS) is used.
When the main table is:
Warehousing Orders      (whinh200) or
Outbound Order Lines    (whinh220) or
Planned Loads/Shipments (whinh480) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, (empty) From/To selection fields will not be
filled in the session.
iFromOrderOrigin
From Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderNumber
From Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderSet
From Order Set selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderLine
From Order Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderOrigin
To Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderNumber
To Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderSet
To Order Set selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderLine
To Order Line selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
