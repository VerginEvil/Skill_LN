# InventoryCommitment.CreateAllocationBuffer

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 959-960

```baan
DLL:   whextinpapi
This function is available from     2023.01 (KB2272147  ).
Syntax: long InventoryCommitment.CreateAllocationBuffer(
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tcalbt           iAllocationBusinessObjectType,
domain  tcboid           iAllocationBusinessObject,
domain  tcborf           iAllocationBusinessObjectReference,
domain  tcrefa           iAllocationReference mb,
domain  tccpva           iProductVariant,
domain  tcolid           iOptionList,
domain  tcqiv1           iQuantityToAllocate,
ref     domain  tcqiv1           oQuantityAllocated,
ref     domain  tccuni           oInventoryUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates an allocation buffer. If an allocation
buffer already exists for the specification then this buffer
will be updated.
Input:  iWarehouse                            - Warehouse             (Mandatory)
iItem                                         - Item                  (Mandatory)
iEffectivityUnit                              - Effectivity Unit
The following input fields are referred to the specification
(tcibd420)
iSoldToBusinessPartner                        - Sold-To Business Partner (tcibd420.albp)
iShipToBusinessPartner                        - Ship-To Business Partner (tcibd420.alst)
iAllocationBusinessObjectType
-                                               Allocation Business Object Type
(tcibd420.albt)
iAllocationBusinessObject
-                                               Allocation Business Object
(tcibd420.albo)
iAllocationBusinessObjectReference
-                                               Allocation Business Object Reference
(tcibd420.abor)
iAllocationReference                          - Allocation Reference (tcibd420.alrf)
iProductVariant                               - Product Variant (tcibd420.cpva)
iOptionList                                   - Option List (tcibd420.olid)
iQuantityToAllocate                           - Quantity to Allocate expressed in
inventory unit (Mandatory)
Output: oQuantityAllocated                    - Allocated Quantity expressed in
inventory unit
oInventoryUnit                                - Inventory Unit
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No error has been detected. Allocation
Buffer has been created, a part has
been created of nothing has been
created.
<> 0                                          - An Error is detected.
```
