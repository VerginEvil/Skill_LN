# Inventory.GetTimePhasedAvailabilityV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 957-958

```baan
DLL:   whextinpapi
This function is available from 2021.08 (KB2196679).
Syntax: long Inventory.GetTimePhasedAvailabilityV2(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  tcdate           iDate,
boolean          iIncludeOnOrderTransactions,
boolean          iIncludeIssueTransactions,
boolean          iAllowNegativeAvailableQuantity,
ref     domain  tcqiv1           oAvailableQuantity,
ref     domain  tccuni           oInventoryUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the available inventory on the given
date for the given item and warehouse, based on the current
inventory and the planned receipt/issue transactions.
Inventory of a financial warehouse is not taken into account
and will return zero for the available quantity.
Reasoning Version 2:
With the introduction of the input variables
iIncludeOnOrderTransactions, iIncludeIssueTransactions and
iAllowNegativeAvailableQuantity the user is now much more in
control on how the available inventory must be calculated.
Input:  iItem                   - Item          (Mandatory)
iWarehouse              - Warehouse     (Mandatory)
iDate                   - Date          (Mandatory)
iIncludeOnOrderTransactions
- Include On Order Transactions
(Mandatory)
True - Planned receipt transactions
are taken into account.
False - Planned receipt transactions
are not taken into account.
iIncludeIssueTransactions
- Include Issue Transactions
(Mandatory)
True - Planned issue transactions
are taken into account.
False - Planned issue transactions
are not taken into account.
iAllowNegativeAvailableQuantity
- Allow Negative Available Quantity
(Mandatory)
True - If available quantity is
negative then this value
will be returned.
False - If available quantity is
negative then the value
zero will be returned.
Output: oAvailableQuantity      - Available Quantity on the given date
expressed in the inventory unit.
oInventoryUnit          - Inventory unit.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Available Inventory retrieved
<> 0                    - Error
```
