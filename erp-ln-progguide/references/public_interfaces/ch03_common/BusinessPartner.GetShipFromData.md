# BusinessPartner.GetShipFromData

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 125-127

```baan
DLL:   tcextcomapi
This function is available from     2021.12 (KB2201372  ).
Syntax: long BusinessPartner.GetShipFromData(
domain  tcncmp           iLogisticCompany,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves data from Ship-from Business Partners.
Individual fields are retrieved, multiple fields can be
retrieved in one call.
Data is read from general level or site level. Depending
on the input argument iSite
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example:
if BusinessPartner.GetShipFromData(
|* Fixed arguments:
575,                                                            --              > input
"RLX000002",                                                            --      > input
"",                                                            --               > input
"",                                                            --               > input
true,                                                            --             > input
false                                                            --             > input
oExceptionMessage,                                                            --> output
oExceptionID,                                                            --     > output
|* Variable arguments:
"cadr",                                                            --           > input
l.tccom121.cadr,                                                            --  > output
"ccnt",                                                            --           > input
l.tccom121.ccnt) <> 0 then                                                    --> output
|* Error, do something
Exception.Delete(exception.id)
Pre:    none
Post:   none
Input:  iLogisticCompany                      - Logistic Company (mandatory)
iShipFromBusinessPartner                      - Ship-from Business Partner (mandatory)
iBuyFromBusinessPartner                       - Buy-from Business Partner
This input field is only used for
reading the fields:
"Delivery Terms"(cdec),
"Point of Title Passage"(ptpa) and
"Return Delivery Terms"(rdec).
If those are empty for the given
Ship                                                -from Business Partner the
system will try to retrieve the data
from the Buy                                                -from Business Partner
iSite                                         - Site
iForceRead                                    - True/False:
Option to force new query instead of
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
