# Item.GetServiceData

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 180-181

```baan
DLL:   tsextmdmapi
Syntax: long Item.GetServiceData(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tccwoc           iServiceOffice,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves data from Item - Service. Individual
fields are retrieved, multiple fields can be retrieved
in one call.
This function is Multi Site aware, data is read from general
level, or office, or site level, depending on the input
arguments Site and Office and implementation phase of
Multi Site.
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example: when item sales price and currency are needed, the
function must be called as follows:
if Item.GetServiceData(
|* Fixed arguments:
company,                                                            --    > input
item,                                                            --       > input
site,                                                            --       > input
service.office,                                                         --> input
force.read,                                                            -- > input
context is master data                                                  --> input
exception.message,                                                      --> output
exception.id,                                                           --> output
|* Variable arguments:
"ccur",                                                            --     > input
currency,                                                            --   > output
"pris",                                                            --     > input
sales.price) <> 0 then                                               --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany                              - Logistic Company: Mandatory
iItem                         -               - Item: Mandatory
iSite                         -               - Site: Not Mandatory
iServiceOffice                                - Service Office: Not Mandatory
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
