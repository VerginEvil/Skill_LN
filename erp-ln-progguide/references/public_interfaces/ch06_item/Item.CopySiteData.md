# Item.CopySiteData

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 167-168

```baan
DLL:   tcextibdapi
This function is available from     2023.11 (KB2302509  ).
Syntax: long Item.CopySiteData(
domain  tcitem           iSourceItem,
domain  tcsite           iSourceSite,
domain  tcitem           iTargetItem,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Copy the Item by Site data from the  Source Item to the
Target Item.
Pre:    db.retry.point() must have been set.
Post:   Commit or abort the transaction.
Input:  iSourceItem             Mandatory, item to copy Site Data from
iSourceSite             Mandatory, Site data to copy
iTargetItem             Mandatory, item to copy Site Data to
iProcessingOptionSet    Optional, if 0, the default copy options
are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
This parameter is for future use, so
currently no processing options
are available for this Public Interface.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Site Data was copied.
<> 0                                          - Otherwise.
```
