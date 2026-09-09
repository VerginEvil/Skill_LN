# HandlingUnit.SetToNotShipped

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1061-1061

```baan
DLL:   whextwmdapi
This function is available from 2023.02 (KB2277253).
Syntax: long HandlingUnit.SetToNotShipped(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will set expected not shipped quantity
in the iHandlingUnit outbound process and related shipment line.
This handling unit will remain in stock when related shipment
line is confirmed.
iHandling.Unit can be set to not shipped if:
1. iHandlingUnit has status Staged;
2. Expected not shipped quantity in the iHandlingUnit outbound
process is zero.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit   - Handling Unit which must be set not shipped
(Mandatory)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - iHandlingUnit is set to not shipped.
<> 0    - Error
```
