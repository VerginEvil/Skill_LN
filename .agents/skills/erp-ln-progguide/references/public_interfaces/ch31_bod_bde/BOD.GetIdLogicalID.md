# BOD.GetIdLogicalID

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1670-1671

```baan
DLL:   tcextbodapi
Syntax: long BOD.GetIdLogicalID(
domain  tcncmp           iCompany,
domain  tcbod.name       iNoun,
long             iEntityType,
domain  tcmcs.str30      iEntityCode,
domain  tcmcs.tabl       iRootTable,
ref     domain  tcbod.loid       oLogicalID,
ref             boolean          oLogicalIDisSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the Logical ID.
Pre:    NA
Post:   NA
Input:  iCompany        - company for which the logical Id
is determined. Mandatory
iNoun           - Noun: Mandatory
iEntityType     - Entity Type: Mandatory for transactional data BODs
Possible values: 1 (Warehouse), 2 (Department),
3 (Project)
iEntityCode     - Entity Code: Mandatory for transactional data BODs
Possible values: The warehouse, department or
project.
The Entity Type and Entity Code are used to
determine the Tenant, AccountingEntity and
Location.
iRootTable      - Root Table: Mandatory for master data BODs
Output: oLogicalID              - LogicalID
oLogicalIDisSet         - LogicalID set (true or false).
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - LogicalId is determined.
<> 0                    - Otherwise.
```
