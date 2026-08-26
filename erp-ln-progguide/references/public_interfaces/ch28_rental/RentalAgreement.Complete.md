# RentalAgreement.Complete

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalAgreement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1567-1569

```baan
DLL:   tsextsocapi
This function is available from     2024.11 (KB3532033  ).
Syntax: long RentalAgreement.Complete(
domain  tcorno           iRentalOrder fixed,
domain  tsmdm.acln       iAgreementLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to complete a Rental Agreement (tssoc210
record). See functionality when a Rental Agreement is completed
with form command Set Rental Agreement to Completed in session
Rental Agreements (tssoc2110m200) or Rental Agreement
(tssoc2610m300).
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
-                       When an Electronic Signature is required for completing a
Rental Order and this is the last Agreement which
is being set to Completed and the input argument
SetRentalOrderToCompletedWhenLastAgreeementIsCompleted is set
to Yes, then the header will not be set to Completed,
because the electronic signature functionality is only
available when completing from header level.
-                       When interactive counter reading reset rules are defined for
any of the Agreements, the session for resetting
the counters is not started when this public interface is
used. Resetting these counters can be done using LN UI.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   If the order gets blocked, the blocking flag is set on header
level.
If return warehouse orders are created and warehouse activities
have been set to Automatic, these are executed.
If the current Agreement is the last Agreement which is set
to Completed and
SetRentalOrderToCompletedWhenLastAgreeementIsCompleted has the
value Yes, and the Rental Order header could also be set to
Completed, the status of the header is changed to Completed.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iRentalOrder
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
ActualRentalLocationAddress
domain  tccom.cadr      empty
If default return address of the Agreement is set to
Other Address, then this will be the actual location
address of the rental equipment.
If this address is not provided and the default return
address is set to Other Address, an error will be
returned.
SetOrderToCompletedWhenLastAgreeementIsCompleted
domain  tcyesno         tcyesno.no
Set the Rental Order to Completed when the given
Agreement is completed successfully and all other
Agreements have already been set to Completed.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation and the status of the Agreement
was not changed to Completed.
Return: 0                     -       No Error and the status of the given
Agreement changed to Completed.
<> 0                          -       The status of the Agreement could not be
changed to Completed.
```
