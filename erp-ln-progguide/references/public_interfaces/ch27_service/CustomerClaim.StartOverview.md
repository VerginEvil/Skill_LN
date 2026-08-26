# CustomerClaim.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaim
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1525-1526

```baan
DLL:   tsextcmmapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long CustomerClaim.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iCustomerClaim,
long             iViewFieldSet,
ref     domain  tcorno           oCustomerClaim,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Customer Claims Overview
(tscmm1100m000).
Before calling CustomerClaim.StartOverview(), call
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
1: sort by Customer Claim
2: sort by Sold                               -to Business Partner
3: sort by (Serialized) Item
4: sort by Service Department
5: sort by Project
6: sort by Sales Document
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on main
table tscmm100 are supported. (Optional)
iCustomerClaim
The Customer Claim to display at the top of the grid if
present in the chosen view. (Optional)
iViewFieldSet
Processing Option Set to set the view fields
when the index used is not index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2       SoldToBusinessPartner   domain  tccom.bpid      empty
3       Item                    domain  tcitem          empty
3       SerialNumber            domain  tcibd.sern      empty
4       ServiceDepartment       domain  tccwoc          empty
5       Project                 domain  tccprj          empty
6       SalesReferenceSystem    domain  tscmm.oosy
tscmm.oosy.not.applicable
6       SalesDocumentNumber     domain  tcorno          empty
Output:
oCustomerClaim
The selected Customer Claim if iStartMode is MODAL and
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
