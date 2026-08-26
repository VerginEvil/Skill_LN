# ServiceOrder.Cancel

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1404-1406

```baan
DLL:   tsextsocapi
This function is available from     2022.04 (KB2233575  ).
Syntax: long ServiceOrder.Cancel(
const   domain  tcorno           iServiceOrder fixed,
const   domain  tccdis           iCancelReason fixed,
const   domain  tsmdm.text       iCancelReasonText,
const   domain  tsmdm.date       iCancelLocalDate,
const   domain  tcyesno          iAllowCancelIfDispositionForNCRExists,
const   domain  tcyesno          iAllowCancelIfDispositionForFRACASExists,
const   domain  tcyesno          iAllowCancelIfOpenAssignmentExists,
const   domain  tcyesno          iSetRelatedCallToSolved,
const   domain  tsspc.stat       iNewPlannedActivityStatus,
const   domain  tcyesno          iCancelPurchaseOrders,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to cancel one specific service order
(tssoc200 record). See functionality when a service order
is cancelled with session Cancel Service Orders
(tssoc2204m000).
If the cancel action does not succeed for whatever reason, this
function will return a value unequal zero and the reason why
the cancel action was not successful is present in the
oExceptionMessage and oExceptionID. If cancelling succeeds then
the value zero is returned.
Note that because of the possibility that for return warehouse
orders, some warehouse activities might have been set to
automatic, the system will commit the database transactions in
this function. This means that it is not necessary to set a
db.retry.point() before calling this function and abort/commit
after this function, because that is already handled within
this function.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   If warehouse procedures have been set to automatic, then these
are executed.
Input:  iServiceOrder                                                         -
The service order.
Mandatory input.
iCancelReason                                                            -
The cancel reason. Note that only a reason code of
type Cancellation which is valid on the
iCancelLocalDate is allowed. If the cancel action is
successful then this is stored as cancel reason on
related cancelled activities and on
the service order header.
Mandatory input.
iCancelReasonText                                                            -
A valid text number. If the cancel action is successful
then it is stored as the cancel text on related
cancelled activities and on the service order header.
Not mandatory input.
iCancelLocalDate                                                            -
The date which is used as date for the cancel action.
Note that this is a local date, so it represents the
days since year 0.  If the value 0 is given as input
argument, the system will use the current date (=
date.num()). It is stored as the date of cancellation
on related cancelled activities and on the service
order header.
Not mandatory input.
iAllowCancelIfDispositionForNCRExists                                         -
Indicator whether it is allowed for the cancel process
to continue if the current service order is the
disposition of a Non                              -Conformance report in Quality
Management.
Mandatory input.
iAllowCancelIfDispositionForFRACASExists                                      -
Indicator whether it is allowed for the cancel process
to continue if the current service order is the
disposition of a FRACAS report in Quality Management.
Mandatory input.
iAllowCancelIfOpenAssignmentExists                                            -
Indicator whether it is allowed for the cancel process
to continue if related to the current service order,
open assignments exist (tssoc205).
Mandatory input.
iSetRelatedCallToSolved                                                       -
If this indicator is set to Yes and the current
service order originates from a Call and the
cancellation succeeds, the related Call will be set to
the status Solved.
Mandatory input.
iNewPlannedActivityStatus                                                     -
If the current service order originates from a Planned
Activity (tsspc200), this will be the status to which
the related planned activity will be set back.
Allowed values are tsspc.stat.free, tsspc.stat.released
and tsspc.stat.canceled.
Mandatory input.
iCancelPurchaseOrders                                                         -
If this indicator is set to Yes, then Procurement will
try to Delete/Cancel (first delete and if that is no
longer allowed cancel) related purchase orders when that
is still allowed.
Mandatory input.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation and the status of the service order was not
changed to Cancelled.
Return: 0                     -       No Error and the status of the given
service order changed to Cancelled.
<> 0                          -       The status of the service order could not be
changed to Cancelled.
```
