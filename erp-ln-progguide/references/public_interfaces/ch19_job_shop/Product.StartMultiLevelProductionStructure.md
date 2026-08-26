# Product.StartMultiLevelProductionStructure

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for Product
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 653-656

```baan
DLL:   tiextbomapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long Product.StartMultiLevelProductionStructure(
long             iStartMode,
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tcdate           iReferenceDate,
domain  tcsrce           iSupplySource,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iBillOfMaterialRevision,
domain  tirpt.prmd       iProductionModel,
domain  tirpt.revi       iProductionModelRevision,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tirpt.revi       iSubcontractingModelRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the View Multilevel Product
Structure browser for the Product.
The top level object that will be shown is based on the
actual supply source.
Without exact specification of the top level object, an approved
and effective top level object on the reference date will be
selected. If no reference date is given, the current date and
time is assumed.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSite
Site (Mandatory when concept Job Shop by Site is active).
The site for which the browser is started.
iProduct
Product (Mandatory).
The product for which the browser is started.
iReferenceDate (Optional).
Reference date for top                              -level selection. Only used when
no specific model is given as top level object.
iSupplySource (Optional).
Supply Source can be either of the following:
tcsrce.shopfloor                                      - Job Shop
tcsrce.repetitive                                     - Repetitive
tcsrce.subcontract                                    - Subcontract
If no value is given, the product's actual supply source
is used.
iBillOfMaterialCode
BOM Model  (Optional).
Relevant when supply source is Job Shop.
Only when Job Shop by Site concept is active.
iBillOfMaterialRevision
BOM Model revision (Optional).
Relevant when supply source is Job Shop.
Only when Job Shop by Site concept is active.
Mandatory if iBillOfMaterialCode is provided.
Only when Job Shop by Site concept is active.
iProductionModel
Production Model (Optional).
Relevant when supply source is Repetitive.
iProductionModelRevision
Production Model Revision (Optional).
Relevant when supply source is Repetitive.
Mandatory if iProductionModel is provided.
iSubcontractor
Subcontractor (Optional).
Relevant when supply source is Subcontract.
iSubcontractorSite
Subcontractor Site (Optional).
Relevant when supply source is Subcontract.
Mandatory if iSubcontractor is provided.
iShipFromBusinessPartner
Ship From Business Partner (Optional)
Derived from iSubcontractorSite when the Resource by
Site concept is active.
Relevant when supply source is Subcontract.
Mandatory if iSubcontractor is provided.
iSubcontractingModelRevision
Subcontracting Model Revision (Optional)
Relevant when supply source is Subcontract.
Mandatory if iSubcontractor is provided.
Output:
oExceptionMessage
The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               -     Session started.
<> 0                       -  Otherwise.
```

## Public Interfaces for JobShopRouting

The following functions are available: JobShopRouting.ApproveRevision JobShopRouting.ClearUseForPlanning JobShopRouting.Copy JobShopRouting.CopyOperations JobShopRouting.CopyV2 JobShopRouting.CreateNewRevision JobShopRouting.ExpireRevision JobShopRouting.SetUseForCosting JobShopRouting.SetUseForPlanning JobShopRouting.StartMultiMain
