# AdditionalFile.Upload

> Chapter: Chapter 53 Public Interfaces for Application Development
>
> Group: Public Interfaces for AdditionalFile
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1961-1961

```baan
DLL:   ttextadvapi
This function is available from 2025.12 (KB3641415).
Syntax: long AdditionalFile.Upload(
domain  ttscm.sofc       iAdditionalFile mb,
domain  ttdesc60         iDescription mb,
boolean          iEditable,
domain  ttst255m         iFile mb,
domain  ttst255m         iRevisionText mb,
ref             string           oExceptionMessage() mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface uploads an additional file.
The following rules apply for the upload action.
- The upload action can only handle additional files in package tx
- The current user should have development authorization for package tx
- The current user should have a current Package VRC for development
in package tx
- The additional file argument (iAdditionalFile) consists of package,
module and additional file name, where package and module
should already exist
- The additional file will be created or updated in the package VRC of
package tx of the current package combination of the user
- If SCM is on, the additional file will be checked out and checked in.
Revision text will be used as checkin text.
Pre:    db.retry.point() must have been set.
Post:   abort.transaction() or commit.transaction() must be done.
Input:  iAdditionalFile - The additional file to be uploaded. Including package,
module, additional file and extension. Mandatory
iDescription    - The description of the additional file
iEditable       - Indicates if this additional file is editable
(true/false)
iFile           - Complete path of the file to be uploaded. Mandatory
iRevisionText   - Revision text to be used as checkin text
Output: oExceptionMessage       - A message if the return value is not equal
to 0. This message contains the root cause of
the method failure.
oExceptionID            - An ID that refers to all error information. Use
the functions in Exception to get the error
messages.
Return values:
0               - Function is executed successfully
<> 0            - Error(s) occurred
```
