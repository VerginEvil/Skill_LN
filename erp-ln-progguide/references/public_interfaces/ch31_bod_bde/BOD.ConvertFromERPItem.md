# BOD.ConvertFromERPItem

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1635-1636

```baan
DLL:   tcextbodapi
This function is available from     2019.04 (KB2044306  ).
Syntax: long BOD.ConvertFromERPItem(
domain  tcitem           iERPItem,
ref     domain  tcmcs.str50      oBODItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function converts the ERP item
to the external item used in the BODs.
Pre     :               -
Post    :               -
Input   : iERPItem                            -  Mandatory.
Output  : oBODItem
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                                   - iERPItem converted to oBODItem
<> 0                                          - Otherwise.
```
