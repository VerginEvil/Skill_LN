# Purchase.GetServicesProcurementOrderSettings

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for Purchase
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 409-410

```baan
DLL:   tdextpurapi
This function is available from 2023.04 (KB2286306).
Syntax: long Purchase.GetServicesProcurementOrderSettings(
domain  tcncmp           iLogisticCompany,
domain  tcsite           iSite,
domain  tccwoc           iPurchaseOffice,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves settings for Services Procurement Orders.
Individual fields are retrieved, multiple fields can be
retrieved in one call.
This function is Multi Site aware, and data is read from general
level (parameter table tdpur001), or site or office level
(settings table tdpur086) depending on the specified input
field(s) (mnemonic), input arguments Site and Office and
implementation phase of Multi Site.
Notes:
1. Fields that are only defined at parameter level (not
defined per office or site) are also retrieved.
2. This function uses variable arguments, for input and
output. Data is retrieved via name value pairs: specify the
field and the field value.
Example: when number group for services procurement, series for
equipment procurement orders and log financial economic
transactions are needed, the function must be
called as follows:
if Purchase.GetServicesProcurementOrderSettings(
|* Fixed arguments:
company,                  --> input
site,                     --> input
purchase office,          --> input
force.read,               --> input
context is master data    --> input
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"ngsp",                   --> input
number.group.for.services.procurement.orders, --> output
"sepo",                   --> input
series.for.equipment.procurement.orders, --> output
"lpof",                 --> input
log.financial.economic.transactions) <> 0 then --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
iSite                   - Site: Not Mandatory
iPurchaseOffice         - Purchase Office: Not Mandatory
iForceRead              - Option to force new query in stead of
using cached information
iContextIsMasterData    - True/False:
Indicates if call is done to retrieve
data for master data or transactional
data.
...                     - The field mnemonic of the required
field.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                     - The value of the required field.
Return: 0                       - Data read
<> 0                    - An error occurred
```
