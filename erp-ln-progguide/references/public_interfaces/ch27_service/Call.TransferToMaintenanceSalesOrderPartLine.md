# Call.TransferToMaintenanceSalesOrderPartLine

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1370-1373

```baan
DLL:   tsextclmapi
This function is available from     2024.08 (KB3506889  ).
Syntax: long Call.TransferToMaintenanceSalesOrderPartLine(
domain  tcorno           iCall,
long             iProcessingOptionSet,
ref     domain  tcyesno          oCallIsBlocked,
ref     domain  tcorno           oMaintenanceSalesOrder,
ref     domain  tcpono           oPartLine,
ref     domain  tcpono           oPartDeliveryLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to:
-                       Transfer a Call to a new Maintenance Sales Order Part Line:
Part Delivery, Part Receipt, Part Loan or Part Maintenance
-                       Transfer a Call to a pair of new Maintenance Sales Order
Part Receipt and Delivery Lines.
-                       Transfer a Call to an existing Maintenance Sales Order
Part Maintenance Line.
-                       Any of the above under an existing or a new Maintenance Sales
Order.
Via the Processing Option Set several options can be passed to
control the type(s) of the Part Line(s) to be created, the
Maintenance Sales Order to reuse, the Part Maintenance Line to
reuse and the answer to several questions that could be asked in
the UI                      -based equivalent of this Public Interface.
Note that when Call Management parameter 'Matching Maintenance
Sales Order Numbers' is set to Yes, always a new Maintenance
Sales Order and Part Lines are generated.
Before transferring the call, based on the blocking settings
defined in the Call Management parameters, it is checked if the
call must be blocked. When the call is set to blocked, the call
cannot be transferred and output argument oCallIsBlocked
will be set to Yes.
This function sets a retry                      -point and will commit and/or abort
the transaction.
Pre:    Call ProcessingOptionSet.Create() to obtain iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete()
Input:  iCall
Call Number: Mandatory
iProcessingOptionSet
Processing Option Set: Mandatory, a processing option
set number referring to a processing option set
containing at least one valid option.
Processing Options which are set while they do not apply in
context of the given Line Procedure, Order Number or Part
Maintenance Line number are ignored.
NAME                           TYPE            DEFAULT
================================================================
LineProcedure                                   long    8
This defines to which type of Part Line(s) the Call should be
transferred. When not provided, the default value is 8; "Part
Maintenance Line".
Allowed values:
1 : Part Receipt Line
2 : Part Delivery Line
3 : Part Receipt and Part Delivery Line
4 : Part Loan Line
8 : Part Maintenance Line
10: Part Maintenance and Part Delivery Line
12: Part Maintenance and Part Loan Line
MaintenanceSalesOrder                   domain  tcorno  empty
When provided, the Call will be transferred to a Part Line
under this existing Maintenance Sales Order.
If the Maintenance Sales Order does not exist, transferring
the Call will fail.
PartMaintenanceLine                     domain  tcpono  zero
Only applies if LineProcedure is 8; "Part Maintenance Line",
10 or 12 and MaintenanceSalesOrder is given.
When provided, the Call will be transferred to the existing
Part Maintenance Line with this line number.
If this Part Line does not exists or it is not a Part
Maintenance Line, transferring the Call will fail.
ContinueWhenFcoWillBeUnlinked           domain  tcyesno tcyesno.no
Continue transfer when a Field Change Order is linked to the
call and an anonymous item is set on the call? This transfer
would remove the link between the FCO and the Call.
ContinueWhenStartOrFinishTimesNotSet    domain  tcyesno tcyesno.no
Continue transfer when the Earliest Start Time and Latest
Finish Time are not set on the call?
CreatePartLineUnderExistingOrder        domain  tcyesno tcyesno.no
Only applies if MaintenanceSalesOrder is not given.
If this is YES, and exactly one existing Maintenance Sales
Order can be found for the Call, the new Part Line will be
created under this order.
CreateNewOrderWhenMultipleOpenOrdersPresent
domain  tcyesno tcyesno.no
Only applies if CreatePartLineUnderExistingOrder is YES.
If this is YES and multiple existing Maintenance Sales Orders
are found for the Call, the Call will be transferred to a
Part Line under a new Maintenance Sales Order.
Otherwise transferring the call will fail.
LinkToExistingPartMaintenanceLine       domain  tcyesno tcyesno.no
Only applies if LineProcedure is 8; "Part Maintenance Line",
10 or 12 and PartMaintenanceLine is not given.
If this is YES and a single existing Part Maintenance Line is
found for the Call, the Call will be linked to this Part
Line.
CreateNewPartMaintenanceLineWhenMultipleLinesPresent
domain  tcyesno tcyesno.no
Only applies if LinkToExistingPartMaintenanceLine is YES.
If this is YES and multiple existing Part Maintenance Lines
are found for the Call, the Call will be transferred to a new
Part Line.
Otherwise transferring the call will fail.
CreateWorkOrderForPartMaintenanceLine   domain  tcyesno tcyesno.no
Only applies if LineProcedure is 8; "Part Maintenance Line",
10 or 12. If this is YES, a Work Order will be created for the
Part Line if it does not already exist.
CopySerializedItemToMSOHeader           domain  tcyesno tcyesno.yes
Only applies if LineProcedure is 8; "Part Maintenance Line",
10 or 12. If this is YES, the serialized item will be copied
to the Maintenance Sales Order header.
================================================================
Output: oCallIsBlocked
Indicates if the Call is set to blocked.
If the Call is blocked, the Call will not be
transferred.
oMaintenanceSalesOrder
The new or existing maintenance sales order number to
which the call is transferred.
oPartLine
The new or existing maintenance sales order part line
number to which the call is transferred/linked.
If LineProcedure is 3, Part Receipt and Part Delivery,
then this will be the line number of the Part Receipt
Line.
If LineProcedure is 10 or 12, Part Maintenance and Part
Delivery or Loan, then this will be the line number of
the Part Maintenance Line.
oPartDeliveryLine
If LineProcedure is 3 or 10, Part Receipt or Part
Maintenance and Part Delivery, then this will be the
line number of the Part Delivery Line.
If LineProcedure is 12, Part Maintenance and Part Loan,
then this will be the line number of the Part Loan Line.
Otherwise this will be 0.
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
