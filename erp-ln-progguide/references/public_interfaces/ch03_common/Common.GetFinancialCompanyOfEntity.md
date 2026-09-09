# Common.GetFinancialCompanyOfEntity

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 109-110

```baan
DLL:   tcextemmapi
Syntax: long Common.GetFinancialCompanyOfEntity(
domain  tcncmp           iLogisticCompany,
domain  tcemm.enty       iEntityType,
domain  tcemm.enio       iEntity,
ref     domain  tcncmp           oFinancialCompany,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function gets the financial company of the logistic
company linked to entity.
Pre:
Post:
Input:  i.logistic.company      - Logistic Company: Mandatory
i.entity.type           - Entity Type: Mandatory
i.entity                - Entity: Mandatory
Output:
oFinancialCompany       - Financial company of the enterprise
unit linked to the entity.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Financial company is found.
<> 0                    - Otherwise.
```
