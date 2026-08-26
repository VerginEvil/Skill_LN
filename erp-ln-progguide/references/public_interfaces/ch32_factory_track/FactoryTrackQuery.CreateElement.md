# FactoryTrackQuery.CreateElement

> Chapter: Chapter 32 Public Interfaces for Factory Track
>
> Group: Public Interfaces for FactoryTrackQuery
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1666-1667

```baan
DLL:   brextqryapi
This function is available from     2020.09 (KB2143379  ).
Syntax: long FactoryTrackQuery.CreateElement(
const           string           iElementID(),
const           string           iDomain(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Use this public interface to create a custom element in the
current query output row.
This public interface can only be used in the context of process
extension 'FactoryTrackQuery.QueryExtend'.
If this public interface is used in the context of an extension
on a standard query, the attribute EXT="yes" is linked to the
custom element.
Example:
long            ReturnValue
ReturnValue = FactoryTrackQuery.CreateElement(
"InventoryOnHand",
"tcqiv1",
ExceptionMessage,
ExceptionID,
whinr140.qhnd)
This will add the Element Node (assuming whinr140.qhnd = 10.5)
<InventoryOnHand
Type="Double"
Domain="tcqiv1"
EXT="yes">10.5</InventoryOnHand>
Example:
domain  tcmcs.str20     InventoryDate
long            ReturnValue
InventoryDate = sprintf$(
"%u(%04Y/%02m/%02d)",
whinr140.idat)
ReturnValue = FactoryTrackQuery.CreateElement(
"InventoryDate",
"tcmcs.str20",
ExceptionMessage,
ExceptionID,
InventoryDate,
whinr140.idat)
This will add the Element Node (assuming whinr140.idat contains
date 04/25/2018 13:51:40 in UTC                      -long format)
<InventoryDate
Type="String"
Domain="tcmcs.str20"
Date="04/25/2018"
Time="13:51:40"
EXT="yes">2018/04/25</InventoryDate>
Pre:    N.A.
Post:   N.A.
Input:
iElementID                                    - The name of the custom element:
Mandatory. Dots are truncated.
iDomain                                       - The domain of the custom element:
Mandatory.
... (1 or 2 arguments)                        - The value of the custom element and
optionally the date and time in long
format.
If the date and time argument is
present, then date and time attributes
will be added to the element. If the
date and time argument equals zero,
the date and time attributes will be
empty.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0                                             - Success
<> 0                                          - Failure
```
