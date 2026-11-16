# ProductionBillOfMaterial.GenerateProductSubcontractingModel

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 629-630

```baan
DLL:   tiextmfcapi
This function is available from 2023.07 (KB2292734).
Syntax: long ProductionBillOfMaterial.GenerateProductSubcontractingModel(
domain  tcitem           iProduct,
domain  tibmrv           iRevision,
domain  tcsite           iProductionSite,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccwar           iSubcontractorWarehouse,
domain  tccom.bpid       iShipFromBusinessPartner,
ref     domain  tirpt.revi       oGeneratedRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface generates a Product Subcontracting Model
from the given source production BOM.
Pre:    Multi Site setting 'Job Shop by Site' must be In Preparation or
Active.
Retry point must be set.
Post:   Commit or Abort the transaction.
Input:  iProduct                - Main item in Production BOM
(Mandatory).
iRevision               - Revision in Production BOM
(Mandatory).
iProductionSite         - Production Site Subcontracting Model
(Mandatory).
iSubcontractor          - The subcontractor.
iSubcontractorSite      - Subcontractor Site (Mandatory
if Resource by Site is active).
iSubcontractorWarehouse - Subcontractor Warehouse (Mandatory).
iShipFromBusinessPartner
- Ship From Business Partner (Mandatory
if Resource by Site is not active,
derived from iSubcontractorSite
otherwise).
Output: oGeneratedRevision      - The generated Product Subcontracting
Model Revision.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Product Subcontracting Model Revision
succesfully generated.
<> 0                    - Generate failed.
```
