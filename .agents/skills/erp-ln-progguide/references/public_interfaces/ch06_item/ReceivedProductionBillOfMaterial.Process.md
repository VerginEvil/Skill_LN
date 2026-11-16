# ReceivedProductionBillOfMaterial.Process

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ReceivedProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 247-248

```baan
DLL:   tiextmfcapi
This function is available from 2026.06 (KB3624417).
Syntax: long ReceivedProductionBillOfMaterial.Process(
domain  tcitem           iProduct,
domain  tibmrv           iRevision,
domain  tcyesno          iApprove,
long             iProcessingOptionSet,
ref             boolean          oSomeReceivedProductionBOMProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface functions in a manner similar to the
Process option found in the Session
"Process Received Production Bill of Material (timfc3250m100)"
Use this session to process the production bill of materials(PBOM)
received from PLM.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iProduct                Product.
iRevision               Revision.
iApprove                Approve.
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields on
session Process Received Production Bill of Material (timfc3250m100)
and are not explained in further detail here. Please refer to the
session help for additional information.
NAME                            TYPE                    DEFAULT
ProductFrom                     tcitem (string)         ""
ProductTo                       tcitem (string)         "ZZZZZZZZZ"
RevisionFrom                    tibmrv(string)          ""
RevisionTo                      tibmrv(string)          "ZZZZZZZZZ"
ProcessReport                   tcyesno                 tcyesno.no
PrintingDevice                  tcmcs.str14             ""
PrintingFileoutPathAndName      tcmcs.str100            ""
PrintErrorReport                tcyesno                 tcyesno.no
PrintingDeviceErrorReport       tcmcs.str14             ""
PrintingFileoutPathAndNameErrorReport
tcmcs.str100            ""
Output:
oSomeReceivedProductionBOMProcessed
- True, Some of the received production
bill of material are processed.
False, Otherwise.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Received PBOM has successfully processed.
<> 0                    - Error occurred.
```
