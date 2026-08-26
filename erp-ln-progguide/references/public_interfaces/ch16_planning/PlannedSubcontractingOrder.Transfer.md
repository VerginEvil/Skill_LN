# PlannedSubcontractingOrder.Transfer

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedSubcontractingOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 587-589

```baan
DLL:   cpextrrpapi
This function is available from     2026.10 (KB3643773  ).
Syntax: long PlannedSubcontractingOrder.Transfer(
domain  cpcom.plnc       iScenario,
domain  cprrp.orno       iPlannedSubcontractingOrder,
domain  tccotp           iSubcontractingOrderType,
domain  tcseri           iSubcontractingOrderSeries,
boolean          iRetainBuyer,
long             iProcessingOptionSet,
ref     domain  tckoor           oCreatedOrderType,
ref     domain  tcorno           oCreatedOrder,
ref     domain  tcpono           oCreatedOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface transfers a Planned Subcontracting Order
into a Purchase Order or Request For Quotation. This function
makes use of a Processing
Option Set, which can be created via a call to
ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete(). Transaction Handling is
done inside the function.
Pre:    N.A.
Post:   N.A.
Input:  iScenario
-                                       (Mandatory) The Planning Scenario
iPlannedSubcontractingOrder
-                                       (Mandatory) The Planned Subcontracting Order
to be transferred.
iSubcontractingOrderType
-                                       (Optional) The Subcontracting Order Type. If
the user does not provide a value, then the
value is retrieved from the user purchase
profile.
iSubcontractingOrderSeries
-                                       (Optional) The Subcontracting Order Series.
If the user does not provide a value, then the
value is retrieved from the user purchase
profile.
iRetainBuyer
-                                       Control to force that generated order is
linked to the same Buyer (Optional).
iProcessingOptionSet
-                                       Processing Option Set which can be used to
pass additional parameters. This parameter is
optional, when zero (0) is passed, the options
get their defined default values (Optional).
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create() in DLL
tcextextapi. After the call, the option set
can be deleted by calling
ProcessingOptionSet.Delete().
NAME                    TYPE                    DEFAULT
Contract                domain tccono           ""
ContractLine            domain tcpono           0
ContractSequence        domain tcpono           0
ContractPurchaseOffice  domain tccwoc           ""
ContractIgnored         domain tcyesno          tcyesno.no
TransferText            boolean                 false
Default Values:
Contract
-                                       If the contract is selected, it will be used
as the default value, otherwise it will be
defaulted with empty string.
ContractLine
-                                       If the contract is selected, its Contract Line
will be as the default value, otherwise it
will be defaulted with 0.
ContractSequence
-                                       If the contract is selected, its sequence
number will be used as the default value,
otherwise it will be defaulted with 0.
ContractPurchaseOffice
-                                       If the contract is selected, its Purchase
Office will be used as the default value,
otherwise it will be defaulted with empty
string.
ContractIgnored
-                                       If the contract is selected, it will be used
as the default value, otherwise it will be
defaulted with tcyesno.no.
TransferText
-                                       If true, the text of Planned Subcontracting
Order will be transferred. Default value is
false (Optional).
Output:
oCreatedOrderType
-                                       Transferred to Order Type.
Possible values are:
Purchase Order (tckoor.act.pur) or
Request for Quotation (tckoor.pur.rfq).
oCreatedOrder
-                                       The Order that was created.
oCreatedOrderLine
-                                       The Order Line number of the created Order.
oExceptionMessage
-                                       The last message if any message is found. If
more than one message is found, these are
present in the oExceptionID.
oExceptionID
-                                       An ID that refers to the exception information.
Use the functions in Exception to get all
relevant information.
Return: 0                             - Planned Order successfully transferred.
<> 0                                  - Error occurred during Transfer Planned Order.
```

## Public Interfaces for SpecialDemandByItem

The following functions are available: SpecialDemandByItem.StartPrint
