# BOD.ComposeLocationId

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1653-1653

```baan
DLL:   tcextbodapi
This function is available from 2023.03 (KB2275062).
Syntax: long BOD.ComposeLocationId(
domain  tcmcs.str20      iType,
domain  tcncmp           iOperationalCompany,
domain  tcbod.lctn       iLocation,
ref     domain  tcmcs.str50      oLocationIdentifier,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function composes the location identifier to be used in
the LocationBOD or in any Location/ID elements that reference
the LocationBOD.
Pre:    NA
Post:   NA
Input : iType                   - The type of the location. Mandatory.
The type should be one of following values:
"Department"
"Project"
"Warehouse"
"Company"
"Site"
iOperationalCompany     - The operational company to which the
location belongs. Only used for location
type Site. If not supplied, the
current company is assumed.
iLocation               - The location (department, project,
warehouse, company or site) in LN.
Mandatory.
Output: oLocationIdentifier     - The composed location identifier used
in the BODs.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK.
<> 0                    - Error occurred.
```
