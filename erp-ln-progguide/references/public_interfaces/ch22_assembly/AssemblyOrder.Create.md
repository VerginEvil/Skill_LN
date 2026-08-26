# AssemblyOrder.Create

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 846-847

```baan
DLL:   tiextascapi
This function is available from     2022.07 (KB2236593  ).
Syntax: long AssemblyOrder.Create(
domain  tcitem           iAssemblyItem,
domain  tccpva           iProductVariant,
domain  tiutcd           iPlannedOfflineDate,
domain  tiasc.ardt.typ   iReferenceDateType,
domain  tcseri           iAssemblyOrderSeries,
ref     domain  tcorno           oAssemblyOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Use this Public interface to create 1 Assembly Order
for the specified Product Variant. The Product Variant
must exist for the specified Assembly Item.
The specified Planned Offline Date is only used for
a sell                      -multiple Product Variant.
The Assembly Order Series is optional. If not specified,
the standard logic for determination of order series is used.
This PI is not suitable for sell                      -multiple Product Variants.
PI 'AssemblyOrder.CreateV2' can be used for such variants.
Transaction management is handled within the Public Interface.
Errors which occurred during the actual assembly order
creation process are logged in the Assembly Messages table
(session tiasc0501m000), but also included in oExceptionID.
oExceptionMessage and oExceptionID will also indicate if
messages are logged.
*** Warning ***
This public interface is deprecated.
use:    AssemblyOrder.CreateV2
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:  iAssemblyItem                         - configurable assembly item
mandatory; must exist in session
tiapl2500m000
iProductVariant                               - product variant
mandatory; must have Assembly Item
iPlannedOfflineDate                           - planned offline date
mandatory for sell                                                -multiple variants
iReferenceDateType                            - assembly reference date type
mandatory; it must have one of the
values as can be specified in
session tiapl3201m000
iAssemblyOrderSeries                          - assembly order series
not mandatory; but must be valid
if filled: must exist in session
tcmcs0150m000 as series for the
Assembly Order Number Group parameter
Output: oAssemblyOrder                        - order number of the created
assembly order
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - assembly order has been generated
<> 0                                          - order could not be generated
Use session Assembly Messages
(tiasc0501m000) to view the messages.
```
