# BusinessPartner.GetPayToData

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 125-126

```baan
DLL:   tcextcomapi
This function is available from 2021.12 (KB2201372).
Syntax: long BusinessPartner.GetPayToData(
domain  tcncmp           iFinancialCompany,
domain  tccom.bpid       iPayToBusinessPartner,
domain  tccwoc           iDepartment,
boolean          iForceRead,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves data from Pay-to Business Partners.
Individual fields are retrieved, multiple fields can be
retrieved in one call.
Data is read from general level or department level. Depending
on the input argument iDepartment
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example:
if BusinessPartner.GetPayToData(
|* Fixed arguments:
575,                            --> input
"RLX000002",                    --> input
"",                             --> input
true,                           --> input
oExceptionMessage,              --> output
oExceptionID,                   --> output
|* Variable arguments:
"cadr",                         --> input
l.tccom124.cadr,                --> output
"ccnt",                         --> input
l.tccom124.ccnt) <> 0 then      --> output
|* Error, do something
Exception.Delete(exception.id)
Pre:    none
Post:   none
Input:  iFinancialCompany       - Financial Company (mandatory)
iPayToBusinessPartner   - Pay-to Business Partner (mandatory)
iDepartment             - Department
iForceRead              - True/False:
Option to force new query instead of
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
<> 0                    - An error occurred
```
