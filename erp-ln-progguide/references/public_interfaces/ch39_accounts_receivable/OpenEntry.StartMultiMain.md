# OpenEntry.StartMultiMain

> Chapter: Chapter 39 Public Interfaces for Accounts Receivable
>
> Group: Public Interfaces for OpenEntry
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1806-1807

```baan
DLL:   tfextacrapi
This function is available from     2026.06 (KB3674833  ).
Syntax: long OpenEntry.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tfgld.ttyp       iTransactionType,
domain  tfgld.docn       iDocument,
domain  tfgld.lino       iDocumentLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session
Open Entry Details (tfacr2525s000).
Pre:    na
Post:   na
Input:  iStartMode                    -
Specifies the start mode for the session.
Possible values are:
MODAL                                 -       The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel sessions
that can be manipulated simultaneously.
iStartFilter                          -
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"" (Session has no start filter)
iSessionIndex                         -
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
Possible value is: 1
iQueryExtend                          -
Optional
A specific query to be used when zooming to this session.
iTransactionType                              - Transaction Type
iDocument                                     - Document
iDocumentLine                                 - Document Line
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```

## Public Interfaces for ReceiptDetails

The following functions are available: ReceiptDetails.StartOverview
