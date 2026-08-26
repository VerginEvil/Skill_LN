# PLMFolder.StartMultiMain

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMFolder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1835-1836

```baan
DLL:   pdextpdmapi
This function is available from     2024.06 (KB2330004  ).
Syntax: long PLMFolder.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  pdfld.fkey       iFolder,
domain  pdfld.revi       iFolderRevision,
ref     domain  pdfld.fkey       oFolder,
ref     domain  pdfld.revi       oFolderRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the (MultiMain) session Folder (pdpdm3600m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
MODAL+START.WITH.ADD.SET                               -
Session is started in Add                                              -mode, so a new
folder can be entered directly.
The parent session is blocked until the
child session exits.
MODELESS+START.WITH.ADD.SET                               -
Session is started in Add                                              -mode, so a new
folder can be entered directly.
Parent and child are parallel sessions that
can be manipulated simultaneously.
iStartFilter
Not used
iSessionIndex
Not used
iQueryExtend
Not used
iFolder
optional
iFolderRevision
optional
iPLMProject
optional
Output: for iStartMode MODAL:
oFolder                                       - Folder of the selected record
oFolder Revision                              - Folder Revision of the selected record
oExceptionMessage                             - The last message if the return value is
not equal to 0. If more than one message
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```
