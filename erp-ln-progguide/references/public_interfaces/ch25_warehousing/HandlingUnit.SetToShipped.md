# HandlingUnit.SetToShipped

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1061-1062

```baan
DLL:   whextwmdapi
This function is available from 2023.02 (KB2277253).
Syntax: long HandlingUnit.SetToShipped(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will reset expected not shipped quantity
in the iHandlingUnit outbound process and related shipment line.
This handling unit will be shipped when related shipment
line is confirmed.
iHandling.Unit can be set to shipped if:
1. iHandlingUnit has status Staged;
2. Expected not shipped quantity in the iHandlingUnit outbound
process is greater than zero.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit   - Handling Unit which must be set shipped
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
