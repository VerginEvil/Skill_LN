# Item.GetCostingData

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 169-170

```baan
DLL:   tiextcprapi
This function is available from     2019.08 (KB2066826  ).
Syntax: long Item.GetCostingData(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
boolean          iForceRead,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves data from Item - Costing Data.
Individual fields are retrieved, multiple fields can be retrieved
in one call.
The enterprise.unit argument is only used when the parameter
Standard Cost by Enterprise Unit is set to Active in Implemented
Software Components. In that case it is necessary to supply an
Enterprise Unit when the item                      -type requires this. For item types
Cost or Service, no Enterprise Unit is expected.
The set of supported fields for retrieval is limited. The ones
marked with EU only have relevance when Standard Cost by
Enterprise Unit is Active.
Mnemonic                              -    Description                -   Scope
type                                  - Item Costing Type             - EU
base                                  - Standard Cost Base            - EU
cwar                                  - Warehouse                     - EU
cofc                                  - Supplying Purchase Office     - EU
scos                                  - Costing Source                - EU
sueu                                  - Supplying Enterprise Unit     - EU
spit                                  - Surcharges by Item            -
vpwh                                  - Surcharges by Warehouse       -
ccur                                  - Item Costing Currency         -
ltcp                                  - Last Calculation Date         -
chrt                                  - Standard Cost Component Scheme-
coyn                                  - Combined Ownership Allowed    -
inlc                                  - Included Landed Costs         -
lcst                                  - Landed Costs Set              -
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example: when item costing warehouse and currency are needed,
the function must be called as follows:
if Item.GetCostingData(
|* Fixed arguments:
company,                                                            --    > input
item,                                                            --       > input
enterprise.unit,                                                        --> input
force.read,                                                            -- > input
exception.message,                                                      --> output
exception.id,                                                           --> output
|* Variable arguments:
"cwar",                                                            --     > input
warehouse,                                                            --  > output
"ccur",                                                            --     > input
currency) <> 0 then                                                     --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany                              - Logistic Company: Mandatory
iItem                         -               - Item: Mandatory
iEnterpriseUnit                               - Enterprise Unit - not mandatory
iForceRead                                    - Option to force new query instead of
using cached information
...                                           - The field mnemonic of the required
field.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                                           - The value of the required field.
Return: 0                                     - Data read
<> 0                                          - Otherwise.
```
