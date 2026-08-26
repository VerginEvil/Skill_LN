# PLMItem.GetChildItems

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1838-1839

```baan
DLL:   pdextpdmapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long PLMItem.GetChildItems(
domain  pdikey           iKey,
domain  pdirev           iRevision,
domain  pdintr           iLevels,
domain  pddate           iEffectiveDate,
domain  pdyesno          iSendPurchasedBOM,
ref     domain  tcguid.extend    oItemStructureId,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is for getting child items in the structure to
cache tables pderp201 and pderp202.
All the parameters are mandatory.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:                -        None
Input:  iKey                                  - Item Key
iRevision                                     - Revision
iLevels                                       - Number of Levels
iEffective Date                               - Effective Date
iSendPurchasedBOM                             - Send Purchased BOM
Output: oItemStructureId                      - output GUID
oExceptionMessage                       - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                                       - An ID that refers to all error information.
Use
the functions in Exception to get all relevant
information.
Return: long                          - 0      if success
-                                       <> 0  if fail
```
