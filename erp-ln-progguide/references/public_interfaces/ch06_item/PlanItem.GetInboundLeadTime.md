# PlanItem.GetInboundLeadTime

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 218-219

```baan
DLL:   cpextrpdapi
This function is available from     2026.08 (KB3651697  ).
Syntax: long PlanItem.GetInboundLeadTime(
domain  cpitem           iPlanItem,
domain  tccwar           iWarehouse,
ref     domain  tcwttm           oInboundLeadTime,
ref     domain  tctope           oInboundLeadTimeUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will Calculate Inbound Lead Time and
Inbound Lead Time Unit for Plan Item and Warehouse.
Pre:    None
Post:   None
Input:
iPlanItem                                     - Plan Item (Mandatory). The value must
exist in Items                                                -Planning.
iWarehouse                                    - Warehouse (Mandatory). The value must
exist in Warehouses.
Output:
oInboundLeadTime                              - Inbound Lead Time.
oInboundLeadTimeUnit                          - Inbound Lead Time Unit.
oExceptionMessage                             - The last error message found during
the execution of public interface. If
multiple error messages are found, by
using "oExceptionID", messages can be
retrieved.
oExceptionID                                  - An ID that refers to the exception
information. Use "Exception" related
functions to retrieve related
information.
Return: 0                                     - Success.
<>0                                           - Error occurred during Calculation of
Inbound Lead Time for Plan Item and
Warehouse.
```
