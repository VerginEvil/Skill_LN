# Call.TransferToServiceOrderV2

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1388-1390

```baan
DLL:   tsextclmapi
This function is available from 2023.05 (KB2286782).
Syntax: long Call.TransferToServiceOrderV2(
domain  tcorno           iCall,
domain  tcorno           iServiceOrder,
domain  tcyesno          iContinueWhenStartOrFinishTimesNotSet,
domain  tcyesno          iContinueNoDurationSetForEmergencyCall,
domain  tcyesno          iContinueNoEngineerSetForEmergencyCall,
domain  tcyesno          iGenerateFCOForSerializedItem,
domain  tcyesno          iContinueWhenFCOWillBeUnlinked,
domain  tcyesno          iContinueWhenPlannedTimesCannotBeDetermined,
domain  tcyesno          iContinueWhenPlannedFinishAfterAgreedFinishTime,
domain  tcyesno          iCreateActivityLineUnderPresentServiceOrder,
domain  tcyesno          iCreateNewOrderWhenMultipleOpenOrdersPresent,
domain  tcyesno          iSetStatusToPlanned,
ref     domain  tcyesno          oCallIsBlocked,
ref     domain  tcorno           oServiceOrder,
ref     domain  tsmdm.acln       oActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the transfer of a call to a service order.
Based on the provided input arguments this transfer process can
be controlled. It can be indicated to continue the transfer
process or to stop. These are situations for which in LN UI a
question is asked whether the transfer process should continue
or stop.
When one open service order exists for the same sold-to business
partner, invoice-to business partner and service office, and
iCreateActivityLineUnderPresentServiceOrder is set to Yes, a
new service order activity line will be created for this service
order. In this case iServiceOrder is ignored.
When iCreateActivityLineUnderPresentServiceOrder is set
to No, a new service order and activity line are generated.
When multiple open service orders are present to which the call
can be transferred, it is only possible to transfer the call
when iServiceOrder is supplied and is one of the open service
orders.
When iServiceOrder is not supplied it is not possible to
transfer the call to one of these service orders as it is not
possible to make a selection.
When iCreateNewOrderWhenMultipleOpenOrdersPresent is
set to Yes a new service order and activity line will be
generated.
Note that when Call Management parameter 'Matching Service Order
Numbers' is set to Yes, always a new service order and
activity line are generated.
Before transferring the call, based on the blocking settings
defined in the Call Management parameters, it is checked if the
call must be blocked. When the call is set to blocked, the call
cannot be transferred and output argument oCallIsBlocked will be
set to Yes.
Pre:    None.
Post:   This function sets a retry-point and will commit and/or abort
the transaction.
Input:  iCall
Call Number: Mandatory
iServiceOrder
Service Order: Not mandatory
iContinueWhenStartOrFinishTimesNotSet
Continue transfer when the Latest Solution Start Time
is not set on the call or the Latest Solution Finish
Time is later than the Latest Solution Start Time?
(mandatory Yes/No)
iContinueNoDurationSetForEmergencyCall
Continue transfer when the call is an emergency call and
no duration is set on the call and Call parameters?
(mandatory Yes/No)
iContinueNoEngineerSetForEmergencyCall
Continue transfer when the call is an emergency call and
no service engineer is set on the call?
(mandatory Yes/No)
iGenerateFCOForSerializedItem
When a Field Change Order is linked to the call and
a serialized item is set on the call and
iGenerateFCOForSerializedItem is set to Yes, a Field
Change Order Line will be generated instead of
transferring the call to a service order.
(mandatory Yes/No)
iContinueWhenFCOWillBeUnlinked
Continue transfer when a Field Change Order is linked to
the call and an anonymous item is set on the call as
this transfer will remove the link between the FCO and
the call.
(mandatory Yes/No)
iContinueWhenPlannedTimesCannotBeDetermined
Continue transfer when the service order planned start
or planned finish time could not be determined?
(mandatory Yes/No)
iContinueWhenPlannedFinishAfterAgreedFinishTime
Continue transfer when the service order planned finish
time will exceed the agreed finish time of the call?
(mandatory Yes/No)
iCreateActivityLineUnderPresentServiceOrder
When there is one open service order present for the
same sold-to business partner, invoice-to business
partner and service office, and
iCreateActivityLineUnderPresentServiceOrder is set to
Yes, a new service order activity line will be
created for this service order.
When iCreateActivityLineUnderPresentServiceOrder is set
to No, a new service order and activity line are
generated.
(mandatory Yes/No)
iCreateNewOrderWhenMultipleOpenOrdersPresent
When multiple open service orders are present, the next
situations are distinguished:
Value   | iServiceOrder | Call transferred to
--------|---------------|--------------------
Yes     | ""            | new service order
Yes     | valid         | iServiceOrder
Yes     | invalid       | new service order
No      | ""            | not tranferred --> error
No      | valid         | iServiceOrder
No      | invalid       | not tranferred --> error
(mandatory Yes/No)
iSetStatusToPlanned
Indicates if the new service order/activity line must be
set to status Planned.
(mandatory Yes/No)
Output: oCallIsBlocked
Indicates if the call is set to blocked.
oServiceOrder
The new or existing service order number to which the
call is transferred.
oActivityLine
The new service order activity line number to which the
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
