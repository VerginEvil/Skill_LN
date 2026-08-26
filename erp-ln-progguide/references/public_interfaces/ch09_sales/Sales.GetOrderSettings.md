# Sales.GetOrderSettings

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 280-281

```baan
DLL:   tdextslsapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long Sales.GetOrderSettings(
domain  tcncmp           iLogisticCompany,
domain  tccwoc           iSalesOffice,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves settings for sales orders. Individual
fields are retrieved, multiple fields can be retrieved
in one call.
This function is Multi Site aware, and data is read from general
level (parameter table tdsls000), or office or site level
(settings table tdsls084) depending on the specified input
field(s) (mnemonic), input arguments Site and Office and
implementation phase of Multi Site.
Notes:
1. Fields that are only defined at parameter level (not
defined per office or site) are also retrieved.
2. This function uses variable arguments, for input and
output. Data is retrieved via name value pairs: specify the
field and the field value.
Example: when sales order series and step size for sales order
lines are needed, the function must be called as follows:
if Sales.GetOrderSettings(
|* Fixed arguments:
company,                                                --> input
sales office,                                           --> input
site,                                                   --> input
force.read,                                             --> input
context is master data                                  --> input
exception.message,                                      --> output
exception.id,                                           --> output
|* Variable arguments:
"seso",                                                 --> input
series.for.sales.orders,                                --> output
"ssso",                                                 --> input
step.size.for.sales.order.lines) <> 0 then                               --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Alternatively, the function can also be called with "seso.4"
and "ssso.4", respectively, which refers to the mnemonics at
parameter level.
Pre:    None
Post:   None
Input:
iLogisticCompany                              - Logistic Company: Mandatory
iSite                                         - Site: Not Mandatory
iSalesOffice                                  - Sales Office: Not Mandatory
iForceRead                                    - Option to force new query in stead of
using cached information
iContextIsMasterData                          - True/False:
Indicates if call is done to retrieve
data for master data or transactional
data.
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
<> 0                                          - An error occurred
```
