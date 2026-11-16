# Common.GetAdditionalEntityInfo

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 107-107

```baan
DLL:   tcextemmapi
This function is available from 2022.02 (KB2200687).
Syntax: long Common.GetAdditionalEntityInfo(
domain  tcemm.enty       iEntityType,
domain  tcemm.enio       iEntity,
ref     domain  tcncmp           oOperationalCompany,
ref     domain  tcsite           oSite,
ref     domain  tcemm.grid       oEnterpriseUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function determines the Operational Company, Site and
Enterprise Unit for a department, warehouse or project
Entity Type/Entity combination.
Pre     : -
Post    : -
Input   : iEntityType           - Entity type (Mandatory). Entity types
'Not Applicable' and 'Contract' are
not valid.
iEntity               - Entity (Mandatory)- a department,
warehouse or project code.
Output  : oOperationalCompany   - Operational Company
oSite                 - Site, for entity type 'Project' Site is
not applicable and returns always empty.
oEnterpriseUnit       - Enterprise Unit
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0                       - Additional entity information read
<> 0                    - Otherwise
```
