# Opportunities.StartOverview

> Chapter: Chapter 8 Public Interfaces for CRM
>
> Group: Public Interfaces for Opportunity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 270-271

```baan
DLL:   tdextsmiapi
This function is available from 2024.08 (KB3522389).
Syntax: long Opportunities.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcopty           iOpportunity,
domain  tcemno           iAssignedTo,
domain  tccom.bpid       iSoldToBusinessPartner,
ref     domain  tcopty           oOpportunity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Opportunities Overview
(tdsmi1110m000).
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
Not Used
iSessionIndex
Specifies the table-index that is to be used.
Supported values:
1: sort by Opportunity (default)
5: sort by Assigned to
6: sort by Sold-to Business Partner
iQueryExtend
A specific query to be used when zooming to this session.
iOpportunity
Opportunity (Optional)
iAssignedTo
Assigned to (Optional)
iSoldToBusinessPartner
Sold-to Business Partner (Optional)
Output:         for iStartMode MODAL:
oOpportunity    The selected Opportunity
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
