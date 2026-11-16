# ServiceOrderActivity.Complete

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1452-1454

```baan
DLL:   tsextsocapi
This function is available from 2022.04 (KB2233573).
Syntax: long ServiceOrderActivity.Complete(
const   domain  tcorno           iServiceOrder fixed,
const   domain  tsmdm.acln       iActivityLine,
const   domain  tcyesno          iAllowCompletingWithEmptyProblemCode,
const   domain  tcyesno          iAllowCompletingWithEmptySolutionCode,
const   domain  tssoc2207.upd    iUpdateMethodForRentalPeriod,
const   domain  tccom.cadr       iActualRentalLocationAddress fixed,
const   domain  tcyesno
iSetServiceOrderToCompleteWhenLastActivityIsCompleted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to complete one specific service order activity
(tssoc210 record). See functionality when a service order
activity is completed with form command Set Activity to
Completed in session Service Order Activities (tssoc2110m000)
or Service Order Activity (tssoc2110m100).
If the complete action does not succeed for whatever reason,
this function will return a value unequal zero and the reason
why the complete action was not successful is present in the
oExceptionMessage and oExceptionID. If completing succeeds then
the value zero is returned.
This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
This is necessary because the system will execute the blocking
checks and if the order gets blocked, the blocking flag on
header level is set and committed and the complete action will
fail.
If return warehouse orders are created, then the system will
at the end also process the warehouse activities which are set
to automatic.
Note:
- When an Electronic Signature is required for completing a
service order and this is the last activity which
is being set to Completed and the input argument
iSetServiceOrderToCompleteWhenLastActivityIsCompleted is set
to Yes, then the header will not be set to Completed,
because the electronic signature functionality is only
available when completing from header level.
- When interactive counter reading reset rules are defined for
any of the service order activities, the session for resetting
the counters is not started when this public interface is
used. Resetting these counters can be done using LN UI.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   If the order gets blocked, the blocking flag is set on header
level.
If return warehouse orders are created and warehouse activities
have been set to Automatic, these are executed.
If the current activity is the last activity which is set
to Completed and
iSetServiceOrderToCompleteWhenLastActivityIsCompleted has the
value Yes, and the service order header could also be set to
Completed, the status of the header is changed to Completed.
Input:  iServiceOrder                                           -
The service order.
Mandatory input.
iActivityLine
The activity line number.
Mandatory input.
iAllowCompletingWithEmptyProblemCode                    -
With this input argument the user can indicate that the
complete action should continue if the problem code
on the activity is empty and either on the user template
or service type, it is indicated that this check should
result in a warning.
Note: this situation would result in LN UI in a question
for the user.
Mandatory input.
iAllowCompletingWithEmptySolutionCode                   -
With this input argument the user can indicate that the
complete action should continue if the solution code
on the activity is empty and either on the user template
or service type, it is indicated that this check should
result in a warning.
Note: this situation would result in LN UI in a question
for the user.
Mandatory input.
iActualRentalLocationAddress                            -
If the activity is related to Rental and the default
return address is set to Other Address, then this will
be the actual location address of the rental equipment.
If this address is not provided and the activity is
related to Rental and the default return address is set
to Other Address, an error will be returned.
Optional input.
iUpdateMethodForRentalPeriod                            -
If a related activity is set to Completed which is
related to Rental, then with this indicator the user
can indicate how the rental period should be updated
for the related Rental Cost line (tssoc240).
Allowed values are:
tssoc2207.upd.copy.planned
- Use Agreed Time
tssoc2207.upd.use.actual
- Use Actual Time
tssoc2207.upd.none
- No update
Mandatory input.
iSetServiceOrderToCompleteWhenLastActivityIsCompleted   -
Set the service order header status to Complete when
the given service order activity line is completed
successfully and all other service order activity lines
are already set to Completed.
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
situation and the status of the service order activity
was not changed to Completed.
Return: 0       -       No Error and the status of the given
service order activity changed to Completed.
<> 0    -       The status of the service order activity could
not be changed to Completed.
```
