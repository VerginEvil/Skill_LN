# Item.GetWarehousingData

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 183-184

```baan
DLL:   whextwmdapi
Syntax: long Item.GetWarehousingData(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tcsite           iSite,
boolean          iForceRead,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves data from Item - Warehousing.
Individual fields are retrieved, multiple fields can be
retrieved in one call.
This function is Multi Site aware, data is read from general
level or site level, depending on the input argument Site
and implementation phase of Multi Site.
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example: when the indication 'Cross-docking', Minimum
Cross-dock quantity and Maximum Cross-dock quantity are needed,
the function must be called as follows:
if Item.GetWarehousingData(
|* Fixed arguments:
company,                        --> input
item,                           --> input
site,                           --> input
force.read,                     --> input
exception.message,              --> output
exception.id,                   --> output
|* Variable arguments:
"dycd",                         --> input
dynamic.cross.docking,          --> output
"qcmi",                         --> input
minimum.cross.dock.quantity,    --> output
"qcma",                         --> input
maximum.cross.dock.quantity)    --> output
<> 0 then
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
iItem   -               - Item: Mandatory
iSite   -               - Site: Optional
iForceRead              - Option to force new query in stead of
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
...                     - The value of the required field.
Return: 0                       - Data read
<> 0                    - Error
```
