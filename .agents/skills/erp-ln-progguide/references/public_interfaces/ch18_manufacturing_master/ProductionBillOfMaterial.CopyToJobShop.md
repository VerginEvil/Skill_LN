# ProductionBillOfMaterial.CopyToJobShop

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 625-626

```baan
DLL:   tiextmfcapi
This function is available from 2021.01 (KB2155728).
Syntax: long ProductionBillOfMaterial.CopyToJobShop(
domain  tcitem           iProduct,
domain  tibmrv           iRevision,
domain  tcsite           iToSite,
domain  tcyesno          iCreateNewBillOfMaterial,
domain  tibmdl           iBillOfMaterialCode,
domain  tcseri           iSeries,
domain  tcyesno          iResetLogisticFields,
domain  tcyesno          iCopyManualMaterialLines,
ref     domain  tibmdl           oGeneratedModel,
ref     domain  tibmrv           oGeneratedRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface generates a job shop bill of material
from the given source production BOM.
Pre:    Multi Site setting 'Job Shop by Site' must be In Preparation or
Active.
Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iProduct                - Main item (mandatory).
iRevision               - Revision (mandatory).
iToSite                 - Site (mandatory).
iCreateNewBillOfMaterial
- yes means create new BOM model,
no is to add a revision to the current
BOM.
iBillOfMaterialCode     - BOM Model, mandatory if
iCreateNewBillOfMaterial is no.
iSeries                 - BOM Model Series, mandatory if
iCreateNewBillOfMaterial is yes.
iResetLogisticFields    - yes means logistic fields are reset
to the default value, no means that
the value is taken from the previous
Job Shop BOM revision (this is about
fields that are not present in the
Production BOM). This applies only
when iCreateNewBillOfMaterial is no.
iCopyManualMaterialLines
- Copy material lines that were added
manually in the previous Job Shop BOM
revision (which are not present in the
Production BOM). This applies only
when iCreateNewBillOfMaterial is no.
Output: oGeneratedModel         - The generated BOM model
oGeneratedRevision      - The generated BOM revision
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - PBOM copied succesfully
<> 0                    - PBOM could not be copied
```
