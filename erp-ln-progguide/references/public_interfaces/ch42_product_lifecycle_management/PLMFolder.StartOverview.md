# PLMFolder.StartOverview

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMFolder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1836-1838

```baan
DLL:   pdextpdmapi
This function is available from     2024.06 (KB2330004  ).
Syntax: long PLMFolder.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  pdfld.fkey       iFolder,
domain  pdfld.revi       iFolderRevision,
domain  pdproj           iPLMProject,
ref     domain  pdfld.fkey       oFolder,
ref     domain  pdfld.revi       oFolderRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Folders (pdpdm3500m000) in
overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Mandatory
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byFolder":
data is displayed by Folder.
session will be started on index 1
"byPLMProject":
data is displayed by PLM Project By Folder.
session will be started on index 3
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
Value:  1:  Folder, Folder Revision
3:  PLM Project, Folder, Folder Revision
Determines the sort order in the session.
E.g. if iSessionIndex = 3, then Folders are sorted by
PLM Project, Folder and Revision.
iQueryExtend
A specific query to be used when starting the
session. Use this to specfiy a filter, e.g.
"pdpdm300.auth = "XYZ" "
Using the query extend may lead to a
"data not found, session not started" situation.
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

## Public Interfaces for PLMItem

The following functions are available: PLMItem.ClearChildItems PLMItem.GetChildItems PLMItem.SendToProductionBOM PLMItem.SendToReceivedJSBOM
