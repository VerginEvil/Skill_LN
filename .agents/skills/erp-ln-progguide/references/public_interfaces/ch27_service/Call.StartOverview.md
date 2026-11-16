# Call.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1379-1381

```baan
DLL:   tsextclmapi
This function is available from 2024.10 (KB3532922).
Syntax: long Call.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iCall,
long             iViewFieldSet,
ref     domain  tcorno           oCall,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Calls Overview (tsclm1509m000).
Before calling Call.StartOverview(), call
ProcessingOptionSet.Create() and assign the value to
iViewFieldSet.
After the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
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
Specifies the table-index that is to be used. (Optional)
Supported values:
1: sort by Call
2: sort by Call Status
4: sort by Actual Time Left
5: sort by Reaction Time
8: sort by Support Department and Actual Time Left
9: sort by Sold-to Business Partner and Project
10: sort by Support Engineer
11: sort by (Serialized) Item
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on main
table tsclm100 are supported. (Optional)
iCall
The Call to display at the top of the grid if present in
the chosen view. (Optional)
iViewFieldSet
Processing Option Set to set the view fields
when the index used is not index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2       Status                  domain  tsclm.stat      empty
4*      ActualTimeLeft          domain  tsclm.tmd1      0.0
5       ReactionTime            domain  tsmdm.utct      0
8       SupportDepartment       domain  tccwoc          empty
8*      ActualTimeLeft          domain  tsclm.tmd1      0.0
9       SoldToBusinessPartner   domain  tccom.bpid      empty
9       Project                 domain  tccprj          empty
10      SupportEngineer         domain  tcemno          empty
11      Item                    domain  tcitem          empty
11      SerialNumber            domain  tcibd.sern      empty
* The ActualTimeLeft property is used for indices 4 and 8.
Output:
oCall
The selected Call if iStartMode is MODAL and the
session is closed by a single selection.
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
