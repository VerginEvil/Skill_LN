# RentalAgreement.Cancel

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalAgreement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1579-1581

```baan
DLL:   tsextsocapi
This function is available from 2024.11 (KB3532033).
Syntax: long RentalAgreement.Cancel(
domain  tcorno           iRentalOrder fixed,
domain  tsmdm.acln       iAgreementLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to cancel one Rental Agreement
(tssoc210 record). See functionality when a Rental Agreement
is cancelled with session Cancel Rental Agreements
(tssoc2204m000).
If the cancel action does not succeed for whatever reason, this
function will return a value unequal zero and the reason why
the cancel action was not successful is present in the
oExceptionMessage and oExceptionID. If cancelling succeeds then
the value zero is returned. If in the same process the system
also sets the header to Cancelled, then this is logged as
information message and is present in the oExceptionMessage and
oExceptionID.
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
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   If the Service Order Parameter for automatic cancellation is
set, then if the current Agreement is the last Agreement which
is set to Cancelled, then also the Rental Order is set to
Cancelled.
If warehouse procedures have been set to automatic, then these
are executed.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iRentalOrder -
Rental Order
Mandatory.
iAgreementLine
Rental Agreement
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
CancelReason
domain  tccdis          ""
The cancel reason. Note that only a reason code of
type Cancellation which is valid on the
CancelLocalDate is allowed. If the cancel action is
successful then this is stored as Cancel Reason on
related Agreements and Rental Order.
CancelReasonText
domain  tsmdm.text      0
A valid text number. If the cancel action is successful
then it is stored as the cancel text on related
cancelled Agreement.
CancelLocalDate
domain  tsmdm.date      0
The date which is used as date for the cancel action.
Note that this is a local date, so it represents the
days since year 0. If the value 0 is given as input
argument, the system will use the current date (=
date.num()). It is stored as the date of cancellation
on related cancelled Agreement.
AllowCancelIfOpenAssignmentExists
domain  tcyesno         tcyesno.no
Indicator whether it is allowed for the cancel process
to continue if related to the current Rental Agreement,
open assignments exist (tssoc205).
SetRelatedCallToSolved
domain  tcyesno         tcyesno.yes
If this indicator is set to Yes and the current
Rental Agreement originates from a Call and the
cancellation succeeds, the related Call will be set to
the status Solved.
CancelPurchaseOrders
domain  tcyesno         tcyesno.yes
If this indicator is set to Yes, then Procurement will
try to Delete/Cancel (first delete and if that is no
longer allowed cancel) related purchase orders when that
is still allowed.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation and the status of the service order activity
was not changed to Cancelled.
Return: 0       -       No Error and the status of the given
service order activity changed to Cancelled.
<> 0    -       The status of the service order activity could
not be changed to Cancelled.
```
