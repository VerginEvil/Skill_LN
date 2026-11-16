# Warehousing.GetSettings

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Warehousing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 990-992

```baan
DLL:   whextwmdapi001
This function is available from 2020.03 (KB2111387).
Syntax: long Warehousing.GetSettings(
domain  tcncmp           iLogisticCompany,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves warehousing settings. Individual fields
are retrieved, multiple fields can be retrieved in one call.
This function is Multi Site aware, and data is read from general
level (parameter tables whina000, whinh000, whinp000, whinr000,
whltc000 or whwmd000), or site level (settings table whwmd201)
depending on the specified input field(s) (mnemonic), input
argument Site and implementation phase of Multi Site.
Notes:
1. Fields that are only defined at parameter level (not
defined per site) are also retrieved.
2. Fields that are available at table whwmd201 and at the
warehouse table may not be read using this Public Interface, but
should be read from the warehouse table. The warehouse table
contains the most detailed value.
3. This function uses variable arguments, for input and
output. Data is retrieved via name value pairs: specify the
field and the field value.
Example: when warehouse order series, step size for warehouse
order lines and the first element of slow-moving percentage
are needed, the function must be called as follows:
if Warehousing.GetSettings(
|* Fixed arguments:
company,                  --> input
site,                     --> input
force.read,               --> input
context.is.master.data,   --> input
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"wosr",                         --> input
series.for.warehousing.orders,  --> output
"woss",                         --> input
step.size.for.order.lines,      --> output
"slmp(1)",                      --> input
slow.moving.percentage) <> 0 then --> output
|* Error, do something
Exception.Delete(exception.id)
endif
4. For field "psrm" (Packing Slip Mandatory on Receipts for),
an additional argument is needed: the order origin. The output
has domain tcyesno.
The function call will look like this:
if Warehousing.GetSettings(
|* Fixed arguments:
company,                  --> input
site,                     --> input
force.read,               --> input
context.is.master.data,   --> input
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"psrm"                    --> input
order.origin,             --> input
output) <> 0 then         --> output
|* Error, do something
Exception.Delete(exception.id)
endif
5. The fields "qiap" (Quarantine Inventory Available for
Planning) and "qipo" (Quarantine Inventory Available for
Planning by Origin) are related. Both fields will return the
same value. If qiap is 'No', 'Yes' or 'By Due Date', then this
value will be returned. if qiap is 'By Order Origin', the value
of "qipo" for the specified order origin is returned.
! So for these fields, an additional argument 'order origin'
is needed. This argument is described in note 4.
The domain of the return value is whinh.qipo.
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
iSite                   - Site: Not Mandatory
iForceRead              - For future use
iContextIsMasterData    - True/False:
Indicates if call is done to retrieve
data for master data or transactional
data.
...                     - The field mnemonic of the required
field.
If the field mnemonic is 'psrm', the
order origin must be passed as well.
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
<> 0                    - Error.
```
