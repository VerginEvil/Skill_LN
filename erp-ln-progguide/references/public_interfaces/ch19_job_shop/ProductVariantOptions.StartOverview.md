# ProductVariantOptions.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariantOptions
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 702-702

```baan
DLL:   tiextpcfapi
This function is available from 2023.05 (KB2283720).
Syntax: long ProductVariantOptions.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccpva           iProductVariant,
domain  tcopts           iOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Product Variant Options in
overview mode (tipcf5520m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
Optional
iProductVariant
The Product Variant for which the session will be
started. Mandatory.
iOptionSet
The Option Set for which the session will be started.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
