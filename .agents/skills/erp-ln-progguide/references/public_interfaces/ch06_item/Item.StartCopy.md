# Item.StartCopy

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 186-187

```baan
DLL:   tcextibdapi
This function is available from 2020.12 (KB2158993).
Syntax: long Item.StartCopy(
long             iStartMode,
domain  tcitem           iSourceItem,
ref     domain  tcitem           oTargetItem,
ref     domain  tcitm.dscr       oTargetItemDescription mb,
ref             boolean          oItemCopied,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Starts the session Copy Item Data (tcibd0205m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItem
Mandatory
...
Additional input, specifies the option
in a string, followed by the required
value in the proper format.
Possible options are:
targetItem      A string containing the item code of
the to be created item
targetItemDescription
A string containing the item
description of the to be created item
approveConversionFactors
A boolean for the copy option
approve conversion factors
calculateStandardCost
A boolean for the Calculate Standard
Cost of Item
projectPartQuantity
A double containing Project Part
Quantity
Note:
This function uses variable arguments, for input and
output. Data is retrieved via name-value pairs: specify the
field and a variable for the field value.
Example: when the session Copy Item Data has to be started with
the new item code and description filled and approve
conversion factors checked 'yes', you use the following
arguments:
Item.StartCopy(
|* Fixed arguments:
start.mode,               --> input
item,                     --> input
target.item,              --> output
target.item.description   --> output
item.copied               --> output
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"targetItem",             --> input
target.item,              --> input
"targetItemDescription",  --> input
target.item.description,  --> input
"approveConversionFactors",
--> input
true                      --> input
"calculateStandardCost",  --> input
true,                     --> input
"projectPartQuantity",    --> input
project.part.quantity)    --> input
Output:
oTargetItem             - The Item Code of the created Item
oTargetItemDescription  - The Item Decription of the created
Item
oItemCopied             - True,  if the item has been copied
- False, otherwise
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
