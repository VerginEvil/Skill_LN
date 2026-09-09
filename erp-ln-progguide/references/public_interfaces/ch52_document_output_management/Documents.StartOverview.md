# Documents.StartOverview

> Chapter: Chapter 52 Public Interfaces for Document Output Management
>
> Group: Public Interfaces for Documents
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1958-1959

```baan
DLL:   ttextrpiapi
This function is available from 2025.12 (KB3636431).
Syntax: long Documents.StartOverview(
const           long             iStartMode,
const           string           iStartFilter(),
const           long             iSessionIndex,
const           string           iQueryExtend(),
const   domain  ttutc            iBatchStartDate,
const   domain  ttlong10         iBatchID,
const   domain  ttlong10         iDocument,
const   domain  ttrpi.bsta       iDocumentStatus,
const   domain  ttrpi.doct       iDocumentType,
const   domain  ttdesc40         iDocumentKeyWord1 mb,
const   domain  ttdesc40         iDocumentKeyWord2 mb,
const   domain  ttdesc40         iDocumentKeyWord3 mb,
const   domain  ttdesc40         iDocumentKeyWord4 mb,
ref     domain  ttutc            oBatchStartDate,
ref     domain  ttlong10         oBatchID,
ref     domain  ttlong10         oDocument,
ref     domain  ttdesc500        oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session "Documents (ttrpi3510m000)"
with the given input parameters.
Pre:    -
Post:   -
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Specifies the session index that is to be used.
If specific session index is to be used, below Indices
are only applicable:
iStartMode equals MODELESS:
Index 1 - Documents by Batch (default)
Index 2 - Documents by Status
Index 4 - Documents by Document Type, Keyword 1
Index 5 - Documents by Document Type, Keyword 2
Index 6 - Documents by Document Type, Keyword 3
Index 7 - Documents by Document Type, Keyword 4
Index 8 - Documents by Document Type
iStartMode equals MODAL:
Index 1 - Documents by Batch
iQueryExtend
Optional
A specific query to be used when zooming to this session.
iBatchStartDate         - The DOM batch start date.
iBatchID                - The DOM batch ID.
iDocument               - The DOM document number
iDocumentStatus         - The DOM document status
iDocumentType           - The DOM document type
iDocumentKeyWord1       - The DOM Keyword 1
iDocumentKeyWord2       - The DOM Keyword 2
iDocumentKeyWord3       - The DOM Keyword 3
iDocumentKeyWord4       - The DOM Keyword 4
Output:
For iStartMode MODAL:
oBatchStartDate         - The DOM batch start date.
oBatchID                - The DOM batch ID
oDocument               - The DOM document number
For exceptions:
oExceptionMessage       - A message if the return value is not equal
to 0. This message contains the root cause of
the method failure.
oExceptionID            - An ID that refers to all error information. Use
the functions in Exception to get the error
messages.
Return values:
0                       - Function is executed successfully
<> 0                    - Error(s) occurred
```
