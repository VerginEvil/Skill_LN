# RentalOrder.Complete

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1558-1559

```baan
DLL:   tsextsocapi
This function is available from 2024.11 (KB3532033).
Syntax: long RentalOrder.Complete(
domain  tcorno           iRentalOrder fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to complete one specific Rental Order
(tssoc200 record). See functionality when a Rental Order
is completed with form command Complete in session
Rental Orders (tssoc2100m200) or Rental Order
(tssoc2600m300).
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
Rental Order, this public interface can only be used when
called in an LN UI component. Only in that case the
signature request dialog can be started.
- When interactive counter reading reset rules are defined for
any of the Rental Order activities, the session for resetting
the counters is not started when this public interface is
used. Resetting these counters can be done using LN UI.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   If the order gets blocked, the blocking flag is set on header
level.
If return warehouse orders are created and warehouse activities
have been set to Automatic, these are executed.
Input:  iRentalOrder                                            -
Rental Order.
Mandatory.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation and the status of the Rental Order was not
changed to Completed.
Return: 0       -       No Error and the status of the given
Rental Order changed to Completed.
<> 0    -       The status of the Rental Order could not be
changed to Completed.
```
