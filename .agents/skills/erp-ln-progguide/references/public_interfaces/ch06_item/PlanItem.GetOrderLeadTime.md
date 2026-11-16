# PlanItem.GetOrderLeadTime

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 220-220

```baan
DLL:   cpextrpdapi
This function is available from 2026.08 (KB3651697).
Syntax: long PlanItem.GetOrderLeadTime(
domain  tcncmp           iCompany,
domain  cpitem           iPlanItem,
domain  tcsite           iSite,
domain  tcdate           iDate,
ref     domain  tcwttm           oOrderLeadTime,
ref     domain  tctope           oOrderLeadTimeUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will Calculate Order Lead Time and Order
Lead Time Unit for Plan Item.
Pre:    None
Post:   None
Input:
iCompany                - Company (Mandatory).
iPlanItem               - Plan Item (Mandatory). The value must
exist in Items-Planning.
iSite                   - Site(Mandatory when the Site concept
is active).
iDate                   - Date (Mandatory).
Output:
oOrderLeadTime          - Order Lead Time.
oOrderLeadTimeUnit      - Order Lead Time Unit.
oExceptionMessage       - The last error message found during
the execution of public interface.
If multiple error messages are found,
by using "oExceptionID", messages can
be retrieved.
oExceptionID            - An ID that refers to the exception
information. Use "Exception" related
functions to retrieve related
information.
Return: 0                       - Success.
<>0                     - Error occurred during Calculation of
Order Lead Time
```
