# OutboundAdvice.RemoveHandlingUnit

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1195-1196

```baan
DLL:   whextinhapi
This function is available from 2023.06 (KB2289726).
Syntax: long OutboundAdvice.RemoveHandlingUnit(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function removed handling unit structure from outbound
advice.
Handling unit will NOT be removed if one of these situations
is found:
- Outbound advice does not contain handling unit;
- Outbound Advice have been already picked;
- Handling unit is multi-stock point handling unit;
- Keeping handling units in stock is mandatory;
This is a case when:
1. Outbound advice is created for the warehouse transfer with
specific handling unit filled in the warehousing order
header;
2. Ownership registration level in Item Data by Warehouse is
Physical Item;
3. Allocation registration level in Item Data by Warehouse is
Physical Item;
4. Item is configurable purchase item;
Pre:    db.retry.point()
Post:   commit/abort transaction.
Input:  Primary key fields of outbound advice:
iOrderOrigin    - order origin (Mandatory)
iOrderNumber    - order number (Mandatory)
iOrderSet       - order set
iOrderLine      - order line
iOrderSequence  - order sequence
iAdvice         - advice number (Mandatory)
The primary key fields must refer to an existing Outbound Advice
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Handling Unit removed
<> 0    - Removing Handling Unit failed
```
