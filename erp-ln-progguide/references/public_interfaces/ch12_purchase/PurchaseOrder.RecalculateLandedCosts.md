# PurchaseOrder.RecalculateLandedCosts

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 445-447

```baan
DLL:   tdextpurapi
This function is available from     2025.12 (KB3634332  ).
Syntax: long PurchaseOrder.RecalculateLandedCosts(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
domain  tcpono           iPurchaseOrderSequence,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the recalculation of Landed Costs
for a Purchase Order or for a Purchase Order Line.
-                       Recalculation of Landed Cost for a Purchase Order:
If i.purchase.order.line IS NOT PROVIDED (i.e., equals 0),
the landed cost recalculation will be performed at the
Purchase Order header level for the specified Purchase Order.
In this situation the optional input arguments
OrderHeaderLandedCosts and OrderLinesLandedCosts, if
provided, can be set to value 'tcyesno.yes' or 'tcyesno.no'.
-                       Recalculation of Landed Cost for a Purchase Order Line:
If i.purchase.order.line IS PROVIDED, the recalculation
will be executed at the Purchase Order Line level for
the specified Purchase Order Line.
In this situation the optional input arguments
OrderHeaderLandedCosts and OrderLinesLandedCosts, if
provided, must be set to value 'tcyesno.no'.
Supported Processing Options and their defaults:
NAME                                    TYPE            DEFAULT
OrderHeaderLandedCosts                  domain tcyesno  If
i.purchase.order.line = 0 the
default is set to
'tcyesno.yes',
otherwise to
'tcyesno.no'
OrderLinesLandedCosts                   domain tcyesno  If
i.purchase.order.line = 0 the
default is set to
'tcyesno.yes',
otherwise to
'tcyesno.no'
OverwriteManualAndModifiedLandedCosts   domain tcyesno  The default is set
to 'tcyesno.no'
Supported Processing Options and their meaning:
OrderHeaderLandedCosts                       - This option is only considered
in case i.purchase.order.line IS NOT
PROVIDED (meaning; acting on header
level). If it is set to tcyesno.yes,
the system will execute a recalculation
of all Landed Cost Lines related to
the specified Purchase Order header.
Otherwise this is not done.
OrderLinesLandedCosts                       -   This option is only considered
in case i.purchase.order.line IS NOT
PROVIDED (meaning; acting on header
level). If it is set to tcyesno.yes,
the system will execute a recalculation
of all Landed Cost Lines related to
all Purchase Order Lines of the
specified Purchase Order header.
Otherwise this is not done.
OverwriteManualAndModifiedLandedCosts                       - This option indicates
wheteher manual and modified Landed
Costs are allowed to be overwritten
during recalculation.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder                        - Purchase Order (Mandatory)
iPurchaseOrderLine                            - Purchase Order Line (Optional)
iPurchaseOrderSequence                        - Purchase Sequence number (Optional)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default recalculate options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       Recalculation was successful, or no recalculation needs
to be done.
<> 0    An error occurred
```
