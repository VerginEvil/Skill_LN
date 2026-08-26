# EngineeringItemRevision.Finalize

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItemRevision
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 252-252

```baan
DLL:   tiextedmapi
This function is available from     2024.11 (KB3512821  ).
Syntax: long EngineeringItemRevision.Finalize(
domain  tcitem           iEngineeringItem,
domain  tiedm.revi       iRevision,
domain  tcitem           iFromMainItem,
domain  tcitem           iToMainItem,
domain  tiedm.updm       iProductionBOMUpdateMethod,
domain  tcyesno          iFinalizeMultilevel,
domain  tcyesno          iOverwriteExistingPBOM,
domain  tcyesno          iOverwriteDescription,
domain  tcyesno          iCopyDocumentLinks,
domain  tcyesno          iCopyAttachedDocuments,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to Finalize the Engineering Item Revision.
Transaction management is handled by this Public Interface.
Pre:    N.A.
Post:   N.A.
Input:  iEngineeringItem                      - Engineering Item (Mandatory).
iRevision                                     - Revision (Mandatory).
iFromMainItem                                 - From Main Item.
iToMainItem                                   - To Main Item.
iProductionBOMUpdateMethod
-                                               Production BOM Update Method.
iFinalizeMultilevel                           - Finalize Multilevel.
iOverwriteExistingPBOM                        - Overwrite Existing PBOM.
iOverwriteDescription                         - Overwrite Item Description and Search
Keys.
iCopyDocumentLinks                            - Copy Document Links.
iCopyAttachedDocuments                        - Copy Attached Documents.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Engineering Item Revision is
Finalized.
<> 0                                          - Engineering Item Revision is not
Finalized.
```
