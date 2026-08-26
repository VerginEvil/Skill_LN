# Service.GetWorkOrderSettings

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Service
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1339-1341

```baan
DLL:   tsextwcsapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long Service.GetWorkOrderSettings(
domain  tcncmp           iLogisticCompany,
domain  tccwoc           iServiceOffice,
domain  tcsite           iSite,
boolean          iForceRead,
boolean          iContextIsMasterData,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function retrieves work order settings. Individual
fields are retrieved, multiple fields can be retrieved
in one call.
This function is Multi Site aware, and data is read from general
level (parameter table tswcs000), or office or site level
(settings table tswcs003) depending on the specified input
field(s) (mnemonic), input arguments Site and Office and
implementation phase of Multi Site.
Notes:
1. Fields that are only defined at parameter level (not
defined per office or site) are also retrieved.
2. This function uses variable arguments, for input and
output. Data is retrieved via name value pairs: specify the
field and the field value.
Example: when commitment required and default labor type
are needed, the function must be called as follows:
if service.GetWorkOrderSettings(
|* Fixed arguments:
company,                                                --> input
service office,                                         --> input
site,                                                   --> input
force.read,                                             --> input
context is master data                                  --> input
exception.message,                                      --> output
exception.id,                                           --> output
|* Variable arguments:
"ccrl",                                                 --> input
commitment.required,                                    --> output
"chlt",                                                 --> input
default.labor.type) <> 0 then                               --> output
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
<> 0                                          - Otherwise.
```

## Public Interfaces for BlockingReason

The following functions are available: BlockingReason.Release
