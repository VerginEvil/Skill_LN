# Pricing.GetGeneralSettings

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 496-497

```baan
DLL:   tdextpcgapi
This function is available from 2020.03 (KB2111387).
Syntax: long Pricing.GetGeneralSettings(
domain  tcncmp           iLogisticCompany,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves general pricing settings.
Individual fields are retrieved, multiple fields can be
retrieved in one call.
Data is always read from parameter level (parameter table tdpcg000).
Notes:
1. This function uses variable arguments, for input and
output. Data is retrieved via name value pairs: specify the
field and the field value.
Example: when number of discount levels and price book number group
are needed, the function must be called as follows:
if Pricing.GetGeneralSettings(
|* Fixed arguments:
company,                  --> input
force.read,               --> input
context is master data    --> input
exception.message,        --> output
exception.id,             --> output
|* Variable arguments:
"nmdl",                   --> input
number.of.discount.levels,--> output
"ngpb",                 --> input
price.book.number.group) <> 0 then --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
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
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                     - The value of the required field.
Return: 0                       - Data read
<> 0                    - An error occurred
```
