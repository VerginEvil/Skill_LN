# ProductionOrder.InitiateMaterialInventoryIssue

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 718-718

```baan
DLL:   tiextsfcapi
This function is available from     2022.04 (KB2235599  ).
Syntax: long ProductionOrder.InitiateMaterialInventoryIssue(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcpono           iMaterialPosition,
domain  tcutcs           iIssueDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will initiate Material Inventory issue for
a Production Order. Transaction management is handled by this
Public Interface.
Pre:                  -
Post:                 -
Input:  iSite                   Site (mandatory if active).
iProductionOrder        Production Order (mandatory).
iMaterialPosition       Material Position (mandatory).
iIssueDate              The Issue Date (optional). If 0, then
the Planned Dates will not be updated.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Material Inventory Issue has been
initiated.
<> 0                                          - Otherwise.
```
