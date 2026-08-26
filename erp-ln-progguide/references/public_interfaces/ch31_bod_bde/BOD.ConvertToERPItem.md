# BOD.ConvertToERPItem

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1638-1639

```baan
DLL:   tcextbodapi
This function is available from     2019.04 (KB2044306  ).
Syntax: long BOD.ConvertToERPItem(
domain  tcmcs.str50      iBODItem,
ref     domain  tcitem           oERPItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function sets the ERP LN item, using the item as received
from other product.  (e.g. WMS)
Process:  Dynamic translation by project lookup.
The first 9 characters of the item (or less dependent on item
segmentation) are taken, and looked up as project code in
the project table. If this code exists, the item code is
assumed to represent a customized item and not converted.
Otherwise it is treated as standard item and leading spaces
are added.
EXAMPLES:
CBO item string         ERP item
-----------------------------------------
"PR0000001BIKE"         "PR0000001BIKE"
Project = PR0000001
"PR1      BIKE"         "PR1      BIKE"
Project = PR1
"         BIKE"         "         BIKE"
"BIKE"                  "         BIKE"
Project = ""
Pre     :               -
Post    :               -
Input   : iBODItem                            - CBO item (e.g. "BIKE"). Mandatory.
Output  : oERPItem                            - LN item
(e.g. "         BIKE              ")
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                                   - iBODItem converted to oERPItem
<> 0                                          - Otherwise.
```
