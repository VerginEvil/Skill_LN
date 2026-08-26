# EngineeringBillOfMaterial.Copy

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 256-257

```baan
DLL:   tiextedmapi
This function is available from     2024.07 (KB2313152  ).
Syntax: long EngineeringBillOfMaterial.Copy(
domain  tcitem           iSourceEngineeringItem,
domain  tiedm.revi       iSourceRevision,
domain  tcitem           iTargetEngineeringItem,
domain  tiedm.revi       iTargetRevision,
domain  tiedm.optn       iCopyMethod,
domain  tcyesno          iCopyReferenceDesignators,
domain  tcyesno          iCopyAlternativeMaterials,
domain  tcyesno          iCopyUseUpMaterials,
domain  tcyesno          iCopyLinkedDocuments,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to copy the EBOM of a previous revision
to a new revision of the same E                      -item, or to copy the EBOM
(defined for a specific revision) of one E                      -item to a different
E                      -item revision.
For example: The EBOM of an E                      -item TIRE for revision 1 can be
copied to revision 2. Likewise, the EBOM of an E                      -item TIRE that
is in revision 1 can be copied to the EBOM of an E                      -Item TIRE2
revision 4.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSourceEngineeringItem                - Engineering Item from which the
Engineering BOM must be copied
(Mandatory).
iSourceRevision                               - Engineering Item Revision from which
the Engineering BOM must be copied
(Mandatory).
iTargetEngineeringItem                        - Engineering Item to which the
Engineering BOM must be copied
(Mandatory).
iTargetRevision                               - Engineering Item Revision to which
the Engineering BOM must be copied
(Mandatory).
iCopyMethod                                   - Method used for copying (Mandatory).
Below are valid values:
1) Create                                                 - tiedm.optn.napp
2) Overwrite                                                 - tiedm.optn.ovrt
3) Append                                                 - tiedm.optn.apnd
iCopyReferenceDesignators
-                                               Control for copying Reference
Designators.
iCopyAlternativeMaterials
-                                               Control for copying Alternative
Materials.
iCopyUseUpMaterials                           - Control for copying Use Up Materials.
iCopyLinkedDocuments                          - Control for copying Linked Documents.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Copy Engineering BOM is successful.
<> 0                                          - Copy Engineering BOM is not
successful.
```
