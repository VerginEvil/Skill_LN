# JobShop.GetOrderSettings

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShop
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 641-642

```baan
DLL:   tiextsfcapi
This function is available from 2020.07 (KB2135398).
Syntax: long JobShop.GetOrderSettings(
domain  tcncmp           iLogisticCompany,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves settings for job shop orders
(table tisfc000 / tisfc080).
One or more settings fields can be retrieved in one call.
This function is Multi Site aware, and data is read from general level
(parameter table tisfc000), or site level (settings table tisfc080),
depending on:
- implementation phase of Multi Site,
- input argument iSite,
- the specified input field(s) (mnemonic).
Note:
This function uses variable arguments, for input and
output. Data is retrieved via name-value pairs: specify the
field (input) and a variable for the field value (output).
Example: when the settings 'production order series for ep' (psep) and
'step size for renumbering operations' (svro) are needed,
the function must be called with the following arguments:
JobShop.GetOrderSettings(
|* Fixed arguments:
company,                  --> input
site,                     --> input
force.read,               --> input
context is master data    --> input
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"psep",                   --> input
prod.ord.series.ep,       --> output
"svro",                   --> input
step.size.renum.ops)      --> output
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
