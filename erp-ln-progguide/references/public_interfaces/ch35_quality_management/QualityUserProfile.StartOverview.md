# QualityUserProfile.StartOverview

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for QualityUserProfile
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1803-1803

```baan
DLL:   qmextptcapi
This function is available from 2025.04 (KB3541341).
Syntax: long QualityUserProfile.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tclogn           iLoginCode,
ref     domain  tclogn           oLoginCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Overview session "Quality User
Profiles"(qmptc0130m000).
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
Optional
A specific query to be used when zooming to this session.
iLoginCode
Login code (Not Mandatory)
Output: For iStartMode MODAL:
oLoginCode      - Login code selected by user
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
