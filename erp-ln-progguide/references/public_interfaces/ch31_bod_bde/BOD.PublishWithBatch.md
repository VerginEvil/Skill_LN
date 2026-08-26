# BOD.PublishWithBatch

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1660-1661

```baan
DLL:   tcextbodapi
This function is available from     2025.10 (KB3621405  ).
Syntax: long BOD.PublishWithBatch(
domain  tcbod.name       iNoun,
domain  tcmcs.tabl       iRootTable,
domain  tcmcs.str30      iActionCode,
long             iEntityType,
domain  tcmcs.str30      iEntityCode,
domain  tcmcs.str100     iDocumentId,
domain  tcmcs.str32      iBatch,
domain  tcmcs.long       iBatchSequence,
domain  tcmcs.long       iBatchSize,
domain  tcmcs.str30      iProcessingAction,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function publishes any BOD that is part of a Batch with BODs.
Pre:    Transaction handling is needed.
Post:   Transaction handling is needed: A commit or abort must be done.
Input:  iNoun                         - The (protected) Noun. Examples:
XXXCustomBOD, ItemMasterCommonBOD. Mandatory
iRootTable                            - Root Table: Mandatory for master data BODs
iActionCode                           - Action Code: Mandatory
Possible values: "Add", "Change", "Delete",
"Replace", "Canceled".
iEntityType                           - Entity Type: Mandatory for transactional data BODs
Possible values: 1 (Warehouse), 2 (Department),
3 (Project)
iEntityCode                           - Entity Code: Mandatory for transactional data BODs
Possible values: The warehouse, department or
project.
The Entity Type and Entity Code are used to
determine the Tenant, AccountingEntity and
Location.
iDocumentId                           - Document ID: Mandatory
iBatch                                - Batch to which the BOD belongs. Mandatory
iBatchSequence                        - The sequence number in the batch. Mandatory
iBatchSize                            - The size (total number of BODs) of the batch.
This must be provided in one of the BODs in the
batch; normally with the last BOD of the batch.
iProcessingAction                       - Processing Action: Mandatory
Possible values: "OnlyStage", "StageOrPublish",
"OnlyPublish".
Variable arguments are Identifiers
-                                       The first Identifier is Mandatory
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - BOD is published.
<> 0                                          - BOD could not be published
```
