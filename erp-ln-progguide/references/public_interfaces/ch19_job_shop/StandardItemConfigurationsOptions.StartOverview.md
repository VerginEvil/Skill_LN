# StandardItemConfigurationsOptions.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for StandardItemConfigurationsOptions
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 701-702

```baan
DLL:   tiextpcfapi
This function is available from     2023.04 (KB2247487  ).
Syntax: long StandardItemConfigurationsOptions.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session Standard Item -
Configurations Options (tipcf5160m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Not used.
iQueryExtend
Not used.
iItem
The Standard Item for which the session will be
started. Mandatory.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started.
<> 0                                          - Otherwise.
```

## Public Interfaces for ProductVariantOptions

The following functions are available: ProductVariantOptions.StartOverview
