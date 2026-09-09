# SalesOrder.CopyBOM

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 318-319

```baan
DLL:   tdextslsapi
This function is available from 2024.04 (KB2328014).
Syntax: long SalesOrder.CopyBOM(
domain  tcorno           iSalesOrder,
domain  tcitem           iMainItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tcqsl1           iOrderQuantityInInventoryUnit,
domain  tdnbol           iMaximumNumberOfPhantomLevelsToSkip,
domain  tccprj           iProject,
domain  tccspa           iElement,
domain  tccact           iActivity,
domain  tcyesno          iIgnoreWarehouseFromBOM,
domain  tcyesno          iCombineIdenticalComponents,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function copies the Bill of Material (BOM) to the given
sales order. Note that the transaction management must be
performed by the caller. If the function returns a non-zero
value, then the entire transaction must be aborted by the
caller.
Pre:    The Sales Order must exist
Pre:    Caller must set retry-point
Post:   Caller must commit/abort the transaction
Input:  iSalesOrder             - Sales Order (Mandatory)
iMainItem               - Main Item (Mandatory)
The item-code of which the BOM
components are copied to the sales
order lines.
iEffectivityUnit        - Effectivity Unit (Optional)
iOrderQuantityInInventoryUnit
- Order Quantity in inventory unit
(Mandatory).
iMaximumNumberOfPhantomLevelsToSkip
- The number of BOM-levels that are
summarized when you use phantoms.
Must be greater or equal to 1.
iProject                - Project (Optional)
iElement                - Element (Optional)
iActivity               - Activity (Optional)
iIgnoreWarehouseFromBOM
- Ignore the warehouse from the BOM.
Yes: LN uses the standard warehouse
defaulting logic
No:  LN uses the warehouse from the
BOM (if present)
Note that if Job Shop by Site is
active, LN will always ignore the
warehouse from the BOM.
iCombineIdenticalComponents
- Combine Identical components.
Yes: If a particular component occurs
in the BOM multiple times, then
these are aggregated into a
single sales order line.
No:  Combining of identical components
is not done.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Sales order line(s) have been inserted
<> 0                    An error occurred. Caller must
abort the transaction.
```
