# ProductionOrderOperation.GenerateSubcontractingPurchaseDocumentV2

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 789-791

```baan
DLL:   tiextsfcapi
This function is available from 2024.03 (KB2323102).
Syntax: long ProductionOrderOperation.GenerateSubcontractingPurchaseDocumentV2(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tisfc.sdoc       iGenerateRequisitionOrOrder,
domain  tcyesno          iCheckPreviousOperations,
domain  tcyesno          iCombineOperations,
domain  tcyesno          iGenerateForBlockedOperations,
domain  tcyesno          iCheckSubcontractorStatus,
domain  tcdate           iStatusCheckDate,
domain  tcseri           iPurchaseOrderSeries,
domain  tccotp           iPurchaseOrderType,
domain  tcseri           iPurchaseRequisitionSeries,
domain  tcyesno          iAddToExistingPurchaseDocument,
domain  tcyesno          iForceAddToExistingPurchaseDocument,
domain  tcorno           iExistingPurchaseOrder,
domain  tcrqno           iExistingPurchaseRequisition,
ref     domain  tcorno           oPurchaseOrder,
ref     domain  tcrqno           oPurchaseRequisition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Use this Public Interface to generate 1 Subcontracting
Purchase Order or 1 Subcontracting Purchase Requisition
for the input production order operation. The status of
this operation must be less than completed. It must have
a subcontracting work center.
Transaction management is handled within this function.
Errors which occurred during the actual subcontracting
purchase requisition / order creation process are included
in oExceptionID.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:  iSite
Site of Production Order - mandatory when site
concept is active; must be filled with site of
production order
iProductionOrder
Production Order - mandatory; must be a valid
production order number
iOperation
Operation - mandatory; must be filled with operation
number, which exists for Production Order
iGenerateRequisitionOrOrder
Generate Requisition or Order - mandatory; must have
value 'Purchase Order' or 'Purchase Requisition'
iCheckPreviousOperations
Check Previous Operations - mandatory; when set to
'Yes', it will check if previous operations
have been completed already
iCombineOperations
Combine Operations - mandatory; when set to 'Yes',
adjacent operations, to be subcontracted to
same subcontractor, will be combined on 1
purchase order line
iGenerateForBlockedOperations
Generate for Blocked Operations - mandatory; when
set to 'No', no purchase document will be
generated for blocked operations
iCheckSubcontractorStatus
Check Subcontractor Status - mandatory; when set
to 'Yes', the status of the subcontractor
will be checked
iStatusCheckDate
Status Check Date - mandatory when Check
Subcontractor Status is set to 'Yes'
iPurchaseOrderSeries
Purchase Order Series - mandatory when Generate
Requisition or Order has been set to 'Purchase
Order'
iPurchaseOrderType
Purchase Order Type - mandatory when Generate
Requisition or Order has been set to 'Purchase
Order'
iPurchaseRequisitionSeries
Purchase Requisition Series - mandatory when
Generate Requisition or Order has been set to
'Purchase Requisition'
iAddToExistingPurchaseDocument
Add To Existing Purchase Document - mandatory;
when set to 'Yes', it is tried to add the to be
created purchase order / requisition line to
the input Existing Purchase Order or Existing
Purchase Requisition
iForceAddToExistingPurchaseDocument
Force Add To Existing Purchase Document - mandatory;
when set to 'Yes', it is mandatory to add the to be
created line to the input Existing Purchase Order
or Existing Purchase Requisition. When this is not
possible, no new order is created and an error is
returned
iExistingPurchaseOrder
Existing Purchase Order - mandatory when Add To
Existing Purchase Document is 'Yes' and Generate
Requisition Or Order is 'Purchase Order'
iExistingPurchaseRequisition
Existing Purchase Requisition - mandatory when Add
To Existing Purchase Document is 'Yes' and Generate
Requisition Or Order is 'Purchase Requistion'
Output: oPurchaseOrder
Purchase Order - number of generated purchase order
oPurchaseRequisition
Purchase Requisition - number of generated purchase
requisition
oExceptionMessage
The last message if any message is found. If more
than one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use
the functions in Exception to get all relevant
information.
Return: 0       purchase order/requisition has been generated
<> 0    order/requisition could not be generated
```
