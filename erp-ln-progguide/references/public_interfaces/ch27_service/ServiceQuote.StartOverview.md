# ServiceQuote.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1466-1467

```baan
DLL:   tsexteppapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long ServiceQuote.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iQuote,
domain  tcpono           iRevision,
long             iViewFieldSet,
ref     domain  tcorno           oQuote,
ref     domain  tcpono           oRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Quotes Overview (tsepp1100m000).
Before calling ServiceQuote.StartOverview(), call
ProcessingOptionSet.Create() and assign the value to
iViewFieldSet.
After the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the table                              -index that is to be used. (Optional)
Supported values:
1: sort by Quote Revision
2: sort by Quote Status
3: sort by Related Order
4: sort by Sold                               -to Business Partner
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on main
table tsepp100 are supported. (Optional)
iQuote
The Quote to display at the top of the grid if present
in the chosen view. (Optional)
iRevision
The Quote Revision to display at the top of the grid if
present in the chosen view. (Optional)
iViewFieldSet
Processing Option Set to set the view fields
when the index used is not index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2       Status                  domain  tsepp.stat      tsepp.stat.free
3       RelatedOrderType        domain  tsmdm.origin
tsmdm.origin.notapp
3       RelatedOrder            domain  tcorno          empty
4       SoldToBusinessPartner   domain  tccom.bpid      empty
Output:
oQuote
oRevision
The selected Quote Revision if iStartMode is MODAL and
the session is closed by a single selection.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```
