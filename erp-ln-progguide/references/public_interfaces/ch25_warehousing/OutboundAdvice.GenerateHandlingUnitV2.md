# OutboundAdvice.GenerateHandlingUnitV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1181-1182

```baan
DLL:   whextinhapi
This function is available from     2023.11 (KB2303552  ).
Syntax: long OutboundAdvice.GenerateHandlingUnitV2(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
domain  whhuid           iHandlingUnit,
ref     domain  whhuid           oGeneratedHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates handling unit structure for outbound
advice.
Handling unit will NOT be generated if one of these situations
is found:
-                       Outbound advice already contains handling unit;
-                       Outbound Advice has been already picked;
-                       Handling units are not in use in inventory for the combination
of warehouse and item;
-                       There is no sufficient anonymous stock to be packed in
handling units. It can occur when outbound advice is
(partially) created for negative inventory.
Pre:    db.retry.point()
Post:   commit/abort transaction.
Input:  Primary key fields of outbound advice:
iOrderOrigin                          - order origin (Mandatory)
iOrderNumber                          - order number (Mandatory)
iOrderSet                             - order set
iOrderLine                            - order line
iOrderSequence                        - order sequence
iAdvice                               - advice number (Mandatory)
The primary key fields must refer to an existing Outbound Advice
iHandlingUnit                         - Handling Unit Id (optional)
Handling unit with this code cannot exists.
Output: oGeneratedHandlingUnit                - Generated Handling Unit.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     - Handling Unit generated
<> 0                          - Generating Handling Unit failed
```
