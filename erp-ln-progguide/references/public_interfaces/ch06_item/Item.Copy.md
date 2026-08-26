# Item.Copy

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 166-167

```baan
DLL:   tcextibdapi
This function is available from     2023.11 (KB2302509  ).
Syntax: long Item.Copy(
domain  tcitem           iSourceItem,
domain  tcitem           iTargetItem,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Copy the Source Item to the Target Item using the defaults or
copy options as provided in the input Processing Option Set.
By default, transaction management is executed within the
function, so no pending transactions should be present before
calling this function.
Processing Option 'transactionManagementByCaller' is available
to have the transaction management under control of the caller.
Pre:                  -
Post:                 -
Input:  iSourceItem             Mandatory
iTargetItem             Mandatory
iProcessingOptionSet    Optional, if 0, the default copy options
are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Copy Item Data (tcibd0205m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
Copy Item Data options which are not available as Processing Options
will get defaulted in accordance with the session logic.
Processing Options that are set while a required Implemented
Software Component is not available are ignored.
NAME                               TYPE          DEFAULT
targetItemDescription                   string    <from source item>
copyAlternativeItems                    domain tcyesno  tcyesno.yes
copyBillOfMaterial                      domain tcyesno  tcyesno.yes
copyRouting                             domain tcyesno  tcyesno.yes
copyEItemRelations                      domain tcyesno  tcyesno.yes
copySupplyingRelationships              domain tcyesno  tcyesno.yes
copyTradeManagement                     domain tcyesno  tcyesno.yes
copyItemText                            domain tcyesno  tcyesno.yes
copyBusinessPartnersByItem              domain tcyesno  tcyesno.yes
copyDocuments                           domain tcyesno  tcyesno.no
copyDocumentLinks                       domain tcyesno  tcyesno.yes
copyProjectActivities                   domain tcyesno  tcyesno.yes
copyReferenceDesignators                domain tcyesno  tcyesno.yes
copyRequirementsByItem                  domain tcyesno  tcyesno.yes
copyAttributeSets                       domain tcyesno  tcyesno.yes
copyItemsBySiteAndItemsByOffice         domain tcyesno  tcyesno.yes
copyConstraints                         domain tcyesno  tcyesno.yes
copyFeaturesAndOptions                  domain tcyesno  tcyesno.yes
copyItemGenerationSettings              domain tcyesno  tcyesno.yes
copyGenericRouting                      domain tcyesno  tcyesno.yes
copyGenericBillsOfMaterial              domain tcyesno  tcyesno.yes
copyGenericPriceLists                   domain tcyesno  tcyesno.yes
projectPartQuantity                     double          0.0
approveConversionFactors                domain tcyesno  tcyesno.yes
transactionManagementByCaller           domain tcyesno  tcyesno.no
Note: The session option to Calculate Standard Cost and Valuation Price
is not included in the set and therefore this action is not
supported. StandardCosts.CalculateForNewItem() should be used
instead.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The item was copied.
<> 0                                          - Otherwise.
```
