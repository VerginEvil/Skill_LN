# ServiceOrderActivity.Cost

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1441-1444

```baan
DLL:   tsextsocapi
This function is available from     2022.06 (KB2239580  ).
Syntax: long ServiceOrderActivity.Cost(
const   domain  tcorno           iServiceOrder fixed,
const   domain  tsmdm.acln       iActivityLine,
const   domain  tcyesno          iIncludeReleasedOrdersAndActivities,
const   domain  tcyesno
iSetServiceOrderToCostedWhenAllActivitiesAreCosted,
const   domain  tcyesno          iCheckUnconsumedItems,
const   domain  tcyesno          iRemoveSubsequentDeliveryQuantity,
const   domain  tcyesno          iInvoiceFreightLinesinFreightManagement,
const   domain  tcyesno          iIgnoreUnapprovedInvoices,
const   domain  tcyesno          iCostZeroQuantityForOtherCosts,
const   domain  tcyesno          iDoNotCostIfOpenInspectionsExist,
const   domain  tcyesno          iSetOpenInspectionsToNotMeasured,
const   domain  tcyesno          iDeleteOpenInspections,
const   domain  tcccur           iCurrency fixed,
const   domain  tcamnt           iMaximumLimitForInvoiceAmount,
const   domain  tcamnt           iMaximumLimitForOtherAmount,
const   domain  tcprcg           iLowerMargin,
const   domain  tcprcg           iUpperMargin,
const   domain  tcsli.stat       iInvoiceLineStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to cost one specific service order activity (
tssoc210).
See functionality in the costing session (tssoc2290m000) when
the Selection Criteria Level is set to Activity.
All options available in the costing session tssoc2290m000 are
available as input arguments. The labels of the options from the
session tssoc2290m000 are taken over to the input variables,
so that also the help from this session can be used to get more
information.
If setting the activity to status Costed does not succeed
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
Post:
Input:  iServiceOrder               -
The service order.
Mandatory input.
iActivityLine                       -
The activity line number.
Mandatory input.
iIncludeReleasedOrdersAndActivities                       -
If this option is set to Yes, then also if the
status of the activity is Released, it is considered
for costing.
Mandatory input.
iSetServiceOrderToCostedWhenAllActivitiesAreCosted                            -
If this option is set to Yes, the system will also
set the service order header to Costed if all related
activities are Costed and all related cost lines are
Costed.
Mandatory input.
iCheckUnconsumedItems                       -
If a material line is being costed, which is related to
the given activity line, and this parameter is set to
Yes, then if not all unconsumed items have been
returned, the costing will not proceed.
If set to No, then the system will continue the
costing even if there is still unconsumed quantity
available.
Mandatory input.
iRemoveSubsequentDeliveryQuantity                       -
If a material line is being costed, which is related to
the given activity line, and the subsequent delivery
quantity is unequal zero, then with this option set to
Yes, the system will automatically set the subsequent
delivery quantity on the material line to zero.
Mandatory input.
InvoiceFreightLinesinFreightManagement                       -
If this option is set to Yes, are there are
freight invoice lines in Freight Management which
have not been sent to Central Invoicing, then these
are automatically released to Central Invoicing.
Mandatory input.
iIgnoreUnapprovedInvoices                       -
If this option is set to Yes and if a subcontracting
other cost line is being costed and not all purchase
invoices related to the related purchase order line
have been approved, then costing will still proceed.
Mandatory input.
iCostZeroQuantityForOtherCosts                       -
If this option is set to No and if another cost
line is being costed (tssoc240) and the actual quantity
is still zero, then costing will not proceed. Note that
a Total Travel Line is excluded from this check, because
the actual quantity for a Total Travel Line is always
zero.
Mandatory input.
iDoNotCostIfOpenInspectionsExist                       -
If this option is set to Yes and if the related
activity can also be set to Costed and open inspections
exist (tscfg300) related to that activity, then costing
will not succeed. If also the the related order header
can be set to Costed and open inspections exist
related to the order, then costing will not succeed.
Mandatory input.
iSetOpenInspectionsToNotMeasured                       -
If the input argument iDoNotCostIfOpenInspectionsExist is
set to No, this input can be set to Yes.
If set to Yes, then any open inspection will get the
status Not Measured.
Mandatory input.
iDeleteOpenInspections                       -
If the input argument iDoNotCostIfOpenInspectionsExist is
set to No and the input argument
iSetOpenInspectionsToNotMeasured is set to No, this
input argument can be set to Yes. If set to Yes, then
any open inspection will be deleted.
Mandatory input.
iCurrency                       -
The currency in which the input arguments
iMaximumLimitForInvoiceAmount and
iMaximumLimitForOtherAmount are expressed.
Mandatory input.
iMaximumLimitForInvoiceAmount                       -
The maximum net invoice amount of the activity line
which is allowed to be costed.
iMaximumLimitForOtherAmount                       -
The maximum other amount (is actually the goodwill
amount) which is allowed to be costed.
iLowerMargin                       -
If margin control is applicable in the service order
parameters (or in the settings by service office if
the Sites                              -concept has been activated), then this
is the lowest margin for which it is allowed to cost the
given activity line.
iUpperMargin                       -
If margin control is applicable in the service order
parameters (or in the settings by service office if the
Sites                              -concept has been activated), then this is the
highest margin for which it is allowed to cost the
given activity line.
iInvoiceLineStatus                       -
The line status with which the billable line in Central
Invoicing is created.
Allowed values are:
tcsli.stat.on.hold
tcsli.stat.confirmed
tcsli.stat.not.appl
If the status is set to tcsli.stat.not.appl then this
will mean that the system will default it again from
either the service order parameters or from the
settings per office, if the Sites                              -concept has been
activated.
Mandatory input.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then the status of the activity line is
not changed to Costed.
Return: 0                     -       No Error and the status of the given
service order activity changed to Costed.
<> 0                          -       The status of the service order activity could
not be changed to Costed.
```
