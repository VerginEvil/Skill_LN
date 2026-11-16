# Item.GetProductionData

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 175-177

```baan
DLL:   tiextipdapi
This function is available from 2020.03 (KB2111387).
Syntax: long Item.GetProductionData(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tcsite           iSite,
boolean          iForceRead,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves data from Item - Production Data
Individual fields are retrieved, multiple fields can be retrieved
in one call.
Two levels of data exist, global - which is the relevant scope
unless site specific data exists.
When the Job Shop by Site or the Sites concept is active,
some fields have modified relevance or scope.
STANDARD:
Fields are always read from global data or the specified Site.
When the Sites concept is not active, the iSite parameter is
ignored:
cpha - Phantom
cick - Critical for Inventory
iimf - Receipt Inspection
iima - Outbound Inspection
cncd - Conformance Reporting
rgrp - Routing Group
txta - Item Production Text
Ignore-Site:
Fields are always read from global data.
seak - Search Key
jsst - Job Shop Site
Site-NA:
Fields cannot be read when the Sites concept is active.
repi - Repetitive Item
scdl - Schedule Code
pcrp - Rate Factor for Planning
JSBS-NA:
Fields cannot be read when the Job Shop by Site concept is
active.
oqdr - Quantity-Dependent Routing
phst - Use Phantom Inventory
swoc - Warehouse is Mandatory on BOM line
JSBS-Site-Required:
Fields must be read with iSite specified when the Job Shop by
Site concept is active.
iuma - Turn operation 0 into First of
bfcp - Backflush if Material
bfep - Backflush Materials
bfhr - Backflush Hours
drin - Direct Initiate Inventory Issue
dris - Direct Proc. Wareh. Order Line
nsfc - Net Change JSC
sfpl - Shop Floor Planner
psfv - Production Site for Variant
arpm - Assembly Report Material
JSBS-NA-for-Product:
Field cannot be read when Job Shop by Site concept is active
and the item is of type Product. For other item-types, the
field may only be read when iSite is not specified.
unom - BOM Quantity
runi - Routing Quantity
scpf - Scrap Percentage
scpq - Scrap Quantity
oltm - Order Lead Time
oltu - Order Lead Time Unit
smfs - Subcontracting with Material Flow
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example: when Shop Floor Planner and the Critical for Inventory
fields are needed, the function must be called as follows:
if Item.GetProductionData(
|* Fixed Arguments
company,                        --> input
item,                           --> input
site,                           --> input
force.read,                     --> input
exception.message,              --> output
exception.id,                   --> output
|* Variable arguments:
"sfpl",                         --> input
sfc.planner,                    --> output
"cick",                         --> input
critical.for.inventory) <> 0    --> output
then
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
iItem                   - Item: Mandatory
iSite                   - Site - not mandatory
iForceRead              - Option to force new query instead of
using cached information
...                     - The field mnemonic of the required
field.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                     - The value of the requested field.
Return: 0                       - Data read
<> 0                    - Otherwise.
```
