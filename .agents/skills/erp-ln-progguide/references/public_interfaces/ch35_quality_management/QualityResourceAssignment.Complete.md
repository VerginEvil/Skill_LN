# QualityResourceAssignment.Complete

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for QualityResourceAssignment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1796-1797

```baan
DLL:   qmextptcapi
This function is available from 2024.04 (KB2328014).
Syntax: long QualityResourceAssignment.Complete(
domain  qmptc.dtyp       iDocumentType,
domain  tcorno           iBusinessObject,
domain  qmncm.type       iType,
domain  qmpono           iLine,
domain  qmpono           iSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function performs the Complete action which updates the status
of the resource assignment to Completed for the given document type
and business object.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iDocumentType           - Document Type: Mandatory
iBusinessObject         - Business Object: Mandatory
iType                   - Non Conformance Type: Mandatory,
For all the document types other than
Non Conformance Report, pass the value
as 'Material'.
iLine                   - Line: Mandatory
iSequence               - Sequence: Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Resource Assignment status changed to completed.
<> 0                    - Error
```
