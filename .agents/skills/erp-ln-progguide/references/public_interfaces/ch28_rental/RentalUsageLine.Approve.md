# RentalUsageLine.Approve

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalUsageLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1601-1602

```baan
DLL:   tsextsocapi
This function is available from 2024.11 (KB3534561).
Syntax: long RentalUsageLine.Approve(
domain  tcorno           iRentalOrder fixed,
domain  tsmdm.cotp       iCostType,
domain  tcpono           iCostLine,
domain  tcpono           iActualResourceSequence,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to approve a specific Rental Usage Line.
If setting the Usage Line to status Approved does not succeed
for whatever reason, this function will return a value unequal
zero. The reason why the approval was not successful is
present in the oExceptionMessage and oExceptionID. If approval
succeeds then the value zero is returned.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iRentalOrder
Rental Order
Mandatory.
iCostType
Cost Type
Mandatory.
iCostLine
The Cost Line number
Mandatory.
iActualResourceSequence
The actual resource line number
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
NAME                    TYPE                    DEFAULT
================================================================
CreateSubsequentUsageLineForBillingSchedule
domain  tcyesno         tcyesno.yes
If this option is set to Yes and the Rental Agreement
has a Billing Schedule linked to it, the system will
create the succeeding usage line record based on the
schedule.
ApproveZeroQuantityUsageLine
domain  tcyesno         tcyesno.yes
If this option is set to No and if the actual usage
is still zero, then approval will not proceed.
UpdateEmptyActualOnHireDateWithUsagePeriodStartDate
domain  tcyesno         tcyesno.yes
If this option is set to Yes and the Actual On Hire Date
of the Cost Line is empty, it will be updated with
Usage Period End Date of the approved Usage Line.
================================================================
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
