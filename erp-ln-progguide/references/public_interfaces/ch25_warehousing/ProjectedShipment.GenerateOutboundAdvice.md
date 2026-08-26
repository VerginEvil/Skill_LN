# ProjectedShipment.GenerateOutboundAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectedShipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1177-1178

```baan
DLL:   whextinhapi
This function is available from     2023.10 (KB2302540  ).
Syntax: long ProjectedShipment.GenerateOutboundAdvice(
domain  whinh.shpm       iShipment,
boolean          iCrossDock,
domain  tcyesno          iAlternativeItems,
domain  tcyesno          iAdviceDespiteShortage,
domain  tcyesno          iRecalculateExcessATT,
domain  tcyesno          iOverdeliveryAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate an outbound advice for the
projected shipment.
No data is printed.
No automatic outbound process is triggered.
Be aware that transaction management is handled within this
function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iShipment                             - Shipment (Mandatory)
iCrossDock                                    - Create cross dock order for
shortage (True/False)
iAlternativeItems                             - Alternative items handling (Yes/No)
iAdviceDespiteShortage                        - Advice despite shortage (Yes/No)
iRecalculateExcessATT                         - Recalculate excess ATT (Yes/No)
iOverdeliveryAllowed                          - Overdelivery allowed (Yes/No)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
