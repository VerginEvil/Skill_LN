# PLMObject.CheckOut

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMObject
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1827-1828

```baan
DLL:   pdextpdmapi
This function is available from     2022.08 (KB2254143  ).
Syntax: long PLMObject.CheckOut(
domain  pdobjt           iObjectType,
domain  pdokey           iKey,
domain  pdrevi           iRevision,
domain  pdrevi           iManualRevision,
domain  pdyesno          iIsMajor,
domain  pdproj           iProject,
domain  pdyesno          iIgnoreProjectConfig,
domain  pdyesno          iLockFilesOnCheckOut,
ref     domain  tcguid.extend    oTransactionGUID,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is for Check-Out Action.
All the parameters are mandatory except Manual Revision.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iObjectType                   - Object Type
Possible values are:
-                                               pdobjt.item (Item)
-                                               pdobjt.document (Document)
-                                               pdobjt.folder (Folder)
iKey                                  - Object Key
iRevision                             - Object Revision
iManualRevision                       - Object Manual Revision
iIsMajor                              - Major Check-Out
iProject                              - Project
iIgnoreProjectConfig                          - Ignore ›¼ÀœProject Configuration Parameters›¼À
when the Object is Check                                              -Out.
iLockFilesOnCheckOut                          - Indicates if files shall be automatically
locked as part of Check                                              -Out operation
Output: oTransactionGUID              - Transaction GUID. The Revision Control Mechanism
processing objects will be inserted into the
tables pdcom013                                      - Revision Control Objects and
pdcom023                                      - Revision Control Validations with the
oTransaction as guid. The calling method gets
the objects and it's validations information using
this field.
oExceptionMessage                             - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                          - An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long               - 0        if success
-                            <> 0     if fail
```
