# FreightPlanning.ActualizePlan

> Chapter: Chapter 26 Public Interfaces for Freight
>
> Group: Public Interfaces for FreightPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1330-1331

```baan
DLL:   fmextlbdapi
This function is available from 2019.08 (KB2070843).
Syntax: long FreightPlanning.ActualizePlan(
domain  tcorno           iPlan,
boolean          iReplanAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will actualize the given plan
Pre:    db.retry.point is set
Post:   transaction handling (abort/commit)
exception handling can be done when applicable
Input:  iPlan                   - Plan which must be actualized:
Mandatory
iReplanAllowed          - Should potential freight order lines
in the plan which must be replanned
be replanned before actualization
takes place, true or false.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
