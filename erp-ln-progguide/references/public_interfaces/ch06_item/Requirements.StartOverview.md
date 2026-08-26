# Requirements.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Requirements
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 247-249

```baan
DLL:   tcextuefapi
This function is available from     2026.09 (KB3654371  ).
Syntax: long Requirements.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcuef.eopt       iRequirement,
domain  tcuef.catg       iCategory,
ref     domain  tcuef.eopt       oRequirement,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Requirements (tcuef0106m000)
in overview mode.
All function arguments are mandatory unless specified.
Pre:    None
Post:   None
Input:  iStartMode                            - Specifies the start mode for the
session.
Possible values are:
MODAL                                         - The parent session is blocked until
the child session exits. The session
will be started as a zoom session.
MODELESS                                      - Parent and child are parallel sessions
that can be manipulated simultaneously.
iStartFilter                                  - Not Used.(not mandatory)
iSessionIndex                                 - The index that will be used.
Supported values:
1: sort by requirement
2: sort by category
iQueryExtend                                  - A specific query to be used when
zooming to this session.(not mandatory)
iRequirement                                  - Requirement (not mandatory)
iCategory                                     - Category (not mandatory)
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oRequirement                                  - Requirement
oExceptionMessage                             - The last error message found during
the execution of public interface.
If multiple error messages are found,
by using "oExceptionID", messages can
be retrieved.
oExceptionID                                  - An ID that refers to the exception
information. Use "Exception" related
functions to retrieve related
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```

## Chapter 7 Public Interfaces for Engineering Data

## Management

## Public Interfaces for EngineeringItemRevision

The following functions are available: EngineeringItemRevision.ApproveByEngineering EngineeringItemRevision.ApproveByProduction EngineeringItemRevision.CopyToItem EngineeringItemRevision.Finalize EngineeringItemRevision.GenerateEBomCopyData EngineeringItemRevision.StartMultiMain
