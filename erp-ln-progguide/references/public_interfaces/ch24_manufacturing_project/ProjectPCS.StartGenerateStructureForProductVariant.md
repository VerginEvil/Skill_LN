# ProjectPCS.StartGenerateStructureForProductVariant

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 894-896

```baan
DLL:   tiextpcsapi
This function is available from     2024.07 (KB2329993  ).
Syntax: long ProjectPCS.StartGenerateStructureForProductVariant(
long             iStartMode,
domain  tcitem           iGeneratedItem,
domain  tcitem           iGenericItem,
domain  tccpva           iProductVariant,
domain  tccprj           iProject,
domain  tiutcd           iReferenceDate,
domain  tcyesno          iUpdateProjectReferenceDate,
domain  tccpge           iGenerationMethod,
domain  tcyesno          iCheckStandardItemInventory,
domain  tcyesno          iUpdatePricesQuotationLines,
domain  tcyesno          iUpdatePricesSalesOrderLines,
domain  tcyesno          iApproveConversionFactors,
domain  tcyesno          iPrintWarnings,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to start session Generate (Project)
Structure for Product Variant (tipcs2220m000). This session is
used to generate a product structure from a generic item, or to
regenerate a product variant structure of an existing project.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode                            - Specifies the start mode for the
session (Mandatory). Possible values:
MODAL                                                 - The parent session is blocked
until the child session exits. The
session will be started as a zoom
session.
MODELESS_ALWAYS                                                 - Parent and child are
parallel sessions that can be
manipulated simultaneously, even if
the session is a Dialog.
iGeneratedItem                                - The (customized) Item for which the
structure will be (re)generated.
iGenericItem                                  - The Generic Item from which the
customized item structure will be
generated.
iProductVariant                               - The Product Variant from which the
customized item structure will be
generated.
iProject                                      - The PCS Project for which the
structure must be generated.
iReferenceDate                                - Reference Date for the project
structure.
iUpdateProjectReferenceDate
-                                               Control for updating of the Project's
Reference Date.
iGenerationMethod                             - Generation method for the structure.
Below are the valid options:
1) tccpge.sto: Standard                                                -to-Order.
2) tccpge.eto: Engineer                                                -to-Order.
iCheckStandardItemInventory
-                                               Control for checking Standard Item
Inventory Level.
iUpdatePricesQuotationLines
-                                               Control for updating prices in
existing quotation lines.
iUpdatePricesSalesOrderLines
-                                               Control for updating prices in
existing sales order lines.
iApproveConversionFactors
-                                               Control for approving conversion
factors.
iPrintWarnings                                - Control for printing warnings.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Generate (Project) Structure for
Product Variant is started
successfully.
<> 0                                          - Generate (Project) Structure for
Product Variant is not started
successfully.
```

## Chapter 25 Public Interfaces for Warehousing

## Public Interfaces for AdjustmentOrder

The following functions are available: AdjustmentOrder.GenerateHandlingUnits AdjustmentOrder.GenerateHandlingUnitsV2 AdjustmentOrder.Process AdjustmentOrder.StartDetail AdjustmentOrder.StartMultiMain AdjustmentOrder.StartOverview
