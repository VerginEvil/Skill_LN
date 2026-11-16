# JobShop.GetMasterDataSettings

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShop
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 640-641

```baan
DLL:   tiextrouapi
This function is available from 2020.07 (KB2135398).
Syntax: long JobShop.GetMasterDataSettings(
domain  tcncmp           iLogisticCompany,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves master data settings for job shop
(table tirou000 / tirou080).
One or more setting fields can be retrieved in one call.
This function is Multi Site aware, and data is read from general level
(parameter table tirou000), or site level (settings table tirou080),
depending on:
- implementation phase of Job Shop by Site,
- input argument iSite,
- the specified input field(s) (mnemonic).
Note:
This function uses variable arguments, for input and
output. Data is retrieved via name-value pairs: specify the
field (input) and a variable for the field value (output).
Example: when the settings 'default routing' (dfrt) and
'use production rate' (uprr) are needed,
the function must be called with the following arguments:
JobShop.GetMasterDataSettings(
|* Fixed arguments:
company,                  --> input
site,                     --> input
force.read,               --> input
context is master data    --> input
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"dfrt",                   --> input
default.routing,          --> output
"uprr",                   --> input
use.production.rates)     --> output
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
iSite                   - Site: Not Mandatory
iForceRead              - Option to force reading new data in stead of
using cached information
iContextIsMasterData    - True/False (not used)
...                     - The field mnemonic of the required
field(s)
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                     - The value of the required field(s).
Return: 0                       - Data read
<> 0                    - Otherwise.
```
