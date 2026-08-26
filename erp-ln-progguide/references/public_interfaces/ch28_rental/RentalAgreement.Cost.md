# RentalAgreement.Cost

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalAgreement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1569-1572

```baan
DLL:   tsextsocapi
This function is available from     2024.11 (KB3532033  ).
Syntax: long RentalAgreement.Cost(
domain  tcorno           iRentalOrder fixed,
domain  tsmdm.acln       iAgreementLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to cost a Rental Agreement (tssoc210).
See functionality in the costing session (tssoc2290m000) when
the Selection Criteria Level is set to Activity.
All options available in the costing session tssoc2290m000 are
available as input arguments. The labels of the options from the
session tssoc2290m000 are taken over to the input variables,
so that also the help from this session can be used to get more
information.
If setting the Agreement to status Costed does not succeed
for whatever reason, this function will return a value unequal
zero and the reason why the costing was not successful is
present in the oExceptionMessage and oExceptionID. If costing
succeeds then the value zero is returned.
This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iRentalOrder               -
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
SetOrderToCostedWhenAllAgreementsAreCosted
domain  tcyesno         tcyesno.no
If this option is set to Yes, the system will also
set the Rental Order to Costed if all related
Agreements are Costed and all related cost lines are
Costed.
CheckUnconsumedItems
domain  tcyesno         tcyesno.yes
If a material line is being costed, which is related to
the given Agreement, and this parameter is set to
Yes, then if not all unconsumed items have been
returned, the costing will not proceed.
If set to No, then the system will continue the
costing even if there is still unconsumed quantity
available.
InvoiceFreightLinesinFreightManagement
domain  tcyesno         tcyesno.yes
If this option is set to Yes, and there are
freight invoice lines in Freight Management which
have not been sent to Central Invoicing, then these
are automatically released to Central Invoicing.
IgnoreUnapprovedInvoices
domain  tcyesno         tcyesno.no
If this option is set to Yes and if a subcontracting
other cost line is being costed and not all purchase
invoices related to the related purchase order line
have been approved, then costing will still proceed.
IncludeReleasedOrdersAndAgreements
domain  tcyesno         tcyesno.no
If this option is set to Yes, then also if the
status of the activity is Released, it is considered
for costing.
RemoveSubsequentDeliveryQuantity
domain  tcyesno         tcyesno.no
If a material line is being costed, which is related to
the given Agreement, and the subsequent delivery
quantity is unequal zero, then with this option set to
Yes, the system will automatically set the subsequent
delivery quantity on the material line to zero.
CostZeroQuantityForOtherCosts
domain  tcyesno         tcyesno.yes
If this option is set to No and if another cost
line is being costed (tssoc240) and the actual quantity
is still zero, then costing will not proceed. Note that
a Total Travel Line is excluded from this check, because
the actual quantity for a Total Travel Line is always
zero.
DoNotCostIfOpenInspectionsExist
domain  tcyesno         tcyesno.yes
If this option is set to Yes and if the related
Agreement can also be set to Costed and open inspections
exist (tscfg300) related to that Agreement, then costing
will not succeed. If also the related Rental Order
can be set to Costed and open inspections exist
related to the order, then costing will not succeed.
SetOpenInspectionsToNotMeasured
domain  tcyesno         tcyesno.no
If the input argument DoNotCostIfOpenInspectionsExist is
set to No, this input can be set to Yes.
If set to Yes, then any open inspection will get the
status Not Measured.
DeleteOpenInspections
domain  tcyesno         tcyesno.no
If the input argument DoNotCostIfOpenInspectionsExist is
set to No and the input argument
SetOpenInspectionsToNotMeasured is set to No, this
input argument can be set to Yes. If set to Yes, then
any open inspection will be deleted.
Currency
domain  tcccur          ""
The currency in which the input arguments
MaximumLimitForInvoiceAmount and
MaximumLimitForOtherAmount are expressed.
MaximumLimitForInvoiceAmount
domain  tcamnt          99999.0
The maximum net invoice amount of the Agreement
which is allowed to be costed.
MaximumLimitForOtherAmount
domain  tcamnt          99999.0
The maximum other amount (is actually the goodwill
amount) which is allowed to be costed.
LowerMargin
domain  tcprcg          0.0
If margin control is applicable in the Service Order
Parameters (or in the settings by service office if
the Sites                              -concept has been activated), then this
is the lowest margin for which it is allowed to cost the
given activity line.
UpperMargin
domain  tcprcg          0.0
If margin control is applicable in the Service Order
Parameters (or in the settings by service office if the
Sites                              -concept has been activated), then this is the
highest margin for which it is allowed to cost the
given activity line.
InvoiceLineStatus
domain  tcsli.stat      tcsli.stat.on.hold
The line status with which the billable line in Central
Invoicing is created.
Allowed values are:
tcsli.stat.on.hold
tcsli.stat.confirmed
tcsli.stat.not.appl
If the status is set to tcsli.stat.not.appl then this
will mean that the system will default it again from
either the Service Order Parameters or from the
settings per office, if the Sites                              -concept has been
activated.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then the status of the Agreement is
not changed to Costed.
Return: 0                     -       No Error and the status of the given
Agreement changed to Costed.
<> 0                          -       The status of the Agreement could not be
changed to Costed.
```
