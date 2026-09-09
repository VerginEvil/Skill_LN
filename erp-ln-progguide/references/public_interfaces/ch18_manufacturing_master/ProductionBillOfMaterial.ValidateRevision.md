# ProductionBillOfMaterial.ValidateRevision

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 631-631

```baan
DLL:   tiextmfcapi
This function is available from 2021.06 (KB2189918).
Syntax: long ProductionBillOfMaterial.ValidateRevision(
domain  tcitem           iProduct,
domain  tibmrv           iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to validate the specified Production
Bill of Material Revision.
Pre:    Multi Site setting 'Job Shop by Site' must be In Preparation or
Active.
Input:  iProduct                Product ID (Mandatory).
iRevision               Revision Number (Mandatory).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       PBOM Revision passed all the validation checks.
<> 0    PBOM Revision did not pass all the validation checks.
```
