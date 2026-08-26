# BRA.Department.GetEstablishmentCode

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.Department
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1918-1919

```baan
DLL:   lpextbraapi
This function is available from     2026.05 (KB3655446  ).
Syntax: long BRA.Department.GetEstablishmentCode(
domain  btncmp           iLogisticCompany,
domain  tccwoc           iDepartment,
domain  tccom.cadr       iAddress,
ref     domain  lpbra.estb       oEstablishmentCode,
ref     domain  btmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will get the establishment code for a given
department.
Pre:    n.a.
Post:   n.a.
Input:  iLogisticCompany                      - Logistic company. This is a mandatory
argument.
iDepartment                                   - Department. This is a mandatory
argument.
iAddress                                      - Address code. If empty the department
address will be used.
Output: oEstablishmentCode                    - Establishment code
Return: 0/DALHOOKERROR
```

## Public Interfaces for POL.BusinessPartner

The following functions are available: POL.BusinessPartner.StartVerifyOnline
