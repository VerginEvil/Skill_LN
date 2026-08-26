# SalesContract.StartWorkbench

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 300-301

```baan
DLL:   tdextslsapi
This function is available from     2023.09 (KB2301023  ).
Syntax: long SalesContract.StartWorkbench(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwoc           iSalesOffice,
domain  tcemno           iInternalSalesRepresentative,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the workbench session Sales Contracts
(tdsls8330m000).
Input:  iStartMode                            - Specifies the start mode for the
session  (Mandatory)
Possible values are:
MODAL                                                 -    The parent session is
blocked until the child
session exits, in case of
a multi                                                           -occurrence the
session will be started
as a zoom session.
MODELESS                                                 - Parent and child are
parallel sessions that
can be manipulated
simultaneously.
iStartFilter                                  - Not Used
iSessionIndex                                 - Not Used
iQueryExtend                                  - Not Used
Following input variables form the filtering fields, these
fields are not mandatory:
iSalesOffice                                  - Sales Office (Optional)
iInternalSalesRepresentative                       - Internal Sales Representative (Optional)
iSoldToBusinessPartner                        - Sold-to Business Partner (Optional)
iItem                                         - Item (Optional)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - An error occurred
```
