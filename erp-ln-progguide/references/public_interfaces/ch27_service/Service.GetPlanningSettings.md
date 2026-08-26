# Service.GetPlanningSettings

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Service
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1334-1335

```baan
DLL:   tsextspcapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long Service.GetPlanningSettings(
domain  tcncmp           iLogisticCompany,
domain  tccwoc           iServiceOffice,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves planning settings. Individual
fields are retrieved, multiple fields can be retrieved
in one call.
This function is Multi Site aware, and data is read from general
level (parameter table tsspc000), or office or site level
(settings table tsspc003) depending on the specified input
field(s) (mnemonic), input arguments Site and Office and
implementation phase of Multi Site.
Notes:
1. Fields that are only defined at parameter level (not
defined per office or site) are also retrieved.
2. This function uses variable arguments, for input and
output. Data is retrieved via name value pairs: specify the
field and the field value.
Example: when step size for activities and unit for day
are needed, the function must be called as follows:
if service.GetPlanningSettings(
|* Fixed arguments:
company,                                                --> input
service office,                                         --> input
site,                                                   --> input
force.read,                                             --> input
context is master data                                  --> input
exception.message,                                      --> output
exception.id,                                           --> output
|* Variable arguments:
"ssac",                                                 --> input
step.size.for.activities,                               --> output
"undy",                                                 --> input
unit.for.day) <> 0 then                                 --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany                              - Logistic Company: Mandatory
iSite                                         - Site: Not Mandatory
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
