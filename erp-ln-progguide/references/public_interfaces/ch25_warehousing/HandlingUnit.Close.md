# HandlingUnit.Close

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1043-1043

```baan
DLL:   whextwmdapi
This function is available from 2021.12 (KB2213967).
Syntax: long HandlingUnit.Close(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will set the status of a handling unit and
all handling unit childs if any to Closed.
iHandling unit can be closed if:
1. iHandlingUnit is not blocked;
2. iHandlingUnit has status Inactive or
3. iHandlingUnit has status Shipped and related shipment line
is already confirmed or
4. iHandlingUnit has status InStock and
- Ownership registration or allocation registration in the
Item Data by Warehouse (see session whwmd2110s000) are not
defined at a Physical Item Level.
- iHandlingUnit is not under location change (session
whwmd3105m000);
- iHandlingUnit is not present with an active or proposed
stock in the Prepacking Advice (sessions whwmd5640m000).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit   - Handling Unit which must be closed (Mandatory)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - iHandlingUnit is closed.
<> 0    - Error
```
