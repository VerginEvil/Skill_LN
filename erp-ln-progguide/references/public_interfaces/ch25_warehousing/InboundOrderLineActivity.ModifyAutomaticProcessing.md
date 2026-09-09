# InboundOrderLineActivity.ModifyAutomaticProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundOrderLineActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1076-1078

```baan
DLL:   whextinhapi
This function is available from 2020.05 (KB2117931).
Syntax: long InboundOrderLineActivity.ModifyAutomaticProcessing(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.prty       iProcedureType,
domain  tcmcs.st20m      iActivity mb,
domain  tcyesno          iAutomatic,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will update the automatic attribute of the inbound
order line activity that is provided. The automatic field will
only be updated if the activity is applicable and the value
of the automatic attribute is different than the value passed in
variable iAutomatic. Depending on the order type, warehouse and
inspection setup some activities are not applicable.
For example the handling unit inbound advices are not applicable
if the receiving warehouse is not location controlled.
Pre:    db.retry.point should be set
Post:   commit or abort transaction depending on the return value.
Input:  iOrderOrigin            - Mandatory
iOrderNumber            - Mandatory
iOrderLine              - Optional (inbound line can be 0)
iOrderSequence          - Optional (inbound sequence can
be 0)
iProcedureType          - Mandatory
Allowed Values:
Receipt Procedure
(whinh.prty.receipt.line)
Inspection Procedure
(whinh.prty.receipt.inspect)
iActivity               - Mandatory
Allowed Values:
The values are depending on the
procedure type.
Receipt Procedure:
"whinh3412m100" -
Print Goods Received
Note
"whinh3512m000" -
Warehouse Receipts
"whinh3201m000" -
Generate Inbound Advice
"whinh3415m000"
Generate Storage List
"whinh3525m100"
Confirm Storage List
"whinh3203m000" -
Putaway Inbound Advice
Inspection Procedure:
"whinh3201m000" -
Generate Inbound Advice
"whinh3415m000"
Generate Storage List
"whinh3525m100"
Confirm Storage List
"whinh3203m000" -
Putaway Inbound Advice
iAutomatic              - Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
