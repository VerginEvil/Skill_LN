# Call.TransferToWorkOrder

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1379-1381

```baan
DLL:   tsextclmapi
This function is available from     2023.05 (KB2286841  ).
Syntax: long Call.TransferToWorkOrder(
domain  tcorno           iCall,
domain  tcorno           iWorkOrder,
domain  tcyesno          iContinueWhenStartOrFinishTimesNotSet,
domain  tcyesno          iRemoveLinkToFCO,
domain  tcyesno          iCreateActivityLineUnderPresentWorkOrder,
domain  tcyesno          iCreateNewOrderWhenMultipleOpenOrdersPresent,
ref     domain  tcyesno          oCallIsBlocked,
ref     domain  tcorno           oWorkOrder,
ref     domain  tsmdm.acln       oActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the transfer of a call to a work order.
Based on the provided input arguments this transfer process can
be controlled. It can be indicated to continue the transfer
process or to stop. These are situations for which in LN UI a
question is asked whether the transfer process should continue
or stop.
When one open work order exists for the same Item/Serial and
same Project/Element/Activity, and
iCreateActivityLineUnderPresentWorkOrder is set to
Yes, a new work order activity line will be created for this
work order. In this case iWorkOrder is ignored.
When iCreateActivityLineUnderPresentWorkOrder is set
to No, a new work order and activity line is generated.
When multiple open work orders are present to which the call
can be transferred, it is only possible to transfer the call
when iWorkOrder is supplied, and is one of the open work
orders. When iWorkOrder is not supplied it is not possible to
transfer the call to one of these work orders as it is not
possible to make a selection.
When iCreateNewOrderWhenMultipleOpenOrdersPresent is
set to Yes a new work order and activity line will be
generated.
Note that when Call Management parameter 'Allow Transfer of
Calls to same Order in Depot Repair' is No, always a new
work order and activity line is generated.
Before transferring the call, based on the blocking settings
defined in the Call Management parameters, it is checked if the
call must be blocked. When the call is set to blocked, the call
cannot be transferred and output argument oCallIsBlocked
will be set to Yes.
Pre:    None.
Post:   This function sets a retry              -point and will commit and/or abort
the transaction.
Input:  iCall
Call Number: Mandatory
iWorkOrder
Work Order: Not mandatory
iContinueWhenStartOrFinishTimesNotSet
Continue transfer when the Latest Solution Start Time
is not set on the call or the Latest Solution Finish
Time is later than the Latest Solution Start Time.
(mandatory Yes/No)
iRemoveLinkToFCO
When Call is linked to a Field Change Order, and
iRemoveLinkToFCO is No, the Call will not be
transferred. Otherwise, the Call is transferred, and
the Field Change Order will be emptied.
(mandatory Yes/No)
iCreateActivityLineUnderPresentWorkOrder
When there is one open work order present for the
same Item/Serial, and same Project/Element/Activity,
and iCreateActivityLineUnderPresentWorkOrder is set to
Yes, a new work order activity line will be
created for this work order.
When iCreateActivityLineUnderPresentWorkOrder is set
to No, a new work order and activity line is
generated.
(mandatory Yes/No)
iCreateNewOrderWhenMultipleOpenOrdersPresent
When multiple open work orders are present, the next
situations are distinguished:
Value   | iWorkOrder    | Call transferred to
--------                              |---------------|--------------------
Yes     | ignored       | new work order
No      | ""            | not tranferred                               --> error
No      | valid         | iWorkOrder
No      | invalid       | not tranferred                               --> error
(mandatory Yes/No)
Output: oCallIsBlocked
Indicates if the call is set to blocked.
oWorkOrder
The new or existing work order number to which the
call is transferred.
oActivityLine
The new work order activity line number to which the
call is transferred.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0    :  Transfer successful or Call is Blocked
<> 0 :  Error occurred
```
