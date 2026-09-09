# EngineeringItem.GenerateByMBC

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 267-268

```baan
DLL:   tiextedmapi
This function is available from 2026.08 (KB3638118).
Syntax: long EngineeringItem.GenerateByMBC(
domain  tcorno           iMBCNumber,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to Generate Engineering Items by MBC.
If the E-item does not have a revision yet, one will be created
by the MBC. If the E-item does have a revision, the revision is
linked to the MBC as old revision (which will expire when new
revisions are created). New revisions will be generated only
when the EBOM is processed, and these items are the basis for
generating engineering BOMs in the Process EBOM Changes
(tiedm3205m000) session for revisions defined with MBCs.
This Public Interface only uses MBCs which have a status In Design.
Pre:    db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iMBCNumber              MBC Number (Mandatory)
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields on
session Generate Engineering Items by MBC(tiedm3201m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
NAME                            TYPE                    DEFAULT
MBCNumberFrom                   tcorno (string)         ""
MBCNumberTo                     tcorno (string)         "ZZZZZZZZZ"
PrintErrorReport                tcyesno                 tcyesno.no
PrintingDeviceErrorReport       tcmcs.str14             ""
PrintingFileoutPathAndNameErrorReport
tcmcs.str100            ""
If PrintErrorReport is tcyesno.yes then the error report will be printed.
If it is tcyesno.no then errors will be logged in exception structure.
Output:
oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Successfully Generated Engineering Items
by MBC.
<> 0                    Errors occurred during Generating
Engineering Items by MBC.
```
