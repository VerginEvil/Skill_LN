# Inventory.ChangeMAUC

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 940-942

```baan
DLL:   whextinaapi
This function is available from 2024.04 (KB2327731).
Syntax: long Inventory.ChangeMAUC(
domain  whina.mcby       iMAUCCorrectionBy,
domain  tccwar           iWarehouse,
domain  whina.valg       iWarehouseValuationGroup,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
domain  tccprj           iProject,
domain  tccdis           iReason,
domain  tcccur           iReportCurrency,
domain  tcrtyp           iExchangeRateType,
domain  whina.uort       iUsageOfRates,
boolean          iSetNewMAUC,
domain  tccopr           iNewMAUCInReportCurrency,
boolean          iSetNewMAUH,
domain  tcphrs           iNewMAUH,
domain  tcyesno          iOnlyByWarehouseValuationGroup,
domain  tcyesno          iOnlyWithMethodMAUC,
domain  tcyesno          iIncludeServiceRejectWarehouses,
ref             boolean          oDataProcessed,
ref     domain  tcccur           oReportCurrency,
ref     domain  tcccur           oHomeCurrencyArray() fixed,
ref     domain  tccopr           oOldMAUC,
ref     domain  tccopr           oOldHomeMAUCArray(),
ref     domain  tcphrs           oOldMAUH,
ref     domain  tccopr           oNewMAUC,
ref     domain  tccopr           oNewHomeMAUCArray(),
ref     domain  tcphrs           oNewMAUH,
ref             long             oNumberOfCostComponents,
ref     domain  tccpcp           oCostCompArray() fixed,
ref     domain  tccopr           oOldCostCompMAUCReportCurrencyArray(),
ref     domain  tccopr           oOldCostCompMAUCHomeCurrency1Array(),
ref     domain  tccopr           oOldCostCompMAUCHomeCurrency2Array(),
ref     domain  tccopr           oOldCostCompMAUCHomeCurrency3Array(),
ref     domain  tcphrs           oOldCostCompMAUHArray(),
ref     domain  tccopr           oNewCostCompMAUCReportCurrencyArray(),
ref     domain  tccopr           oNewCostCompMAUCHomeCurrency1Array(),
ref     domain  tccopr           oNewCostCompMAUCHomeCurrency2Array(),
ref     domain  tccopr           oNewCostCompMAUCHomeCurrency3Array(),
ref     domain  tcphrs           oNewCostCompMAUHArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will change the MAUC for the given
selection.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Output arrays will be allocated, so a free.mem() must be used
to free the memory which is used by these arrays.
Input:  iMAUCCorrectionBy               Mandatory
iWarehouse                      Mandatory, if iMAUCCorrectionBy
is by Warehouse else ignored.
iWarehouseValuationGroup        Mandatory, if iMAUCCorrectionBy
is by Warehouse Valuation Group
else ignored.
iItem                           Mandatory
iEnterpriseUnit                 Mandatory if standard cost per
enterprise unit for iItem is
set.
Otherwise it should be empty.
iProject                        Optional
iReason                         Mandatory
iReportCurrency                 Mandatory
iExchangeRateType               Mandatory
iUsageOfRates                   Mandatory
iSetNewMAUC                     Mandatory
iNewMAUCInReportCurrency        Used when iSetNewMAUC is True
iSetNewMAUC                     Mandatory
iNewMAUH                        Used when iSetNewMAUH is True
iOnlyByWarehouseValuationGroup  Mandatory
iOnlyWithMethodMAUC             Mandatory
iIncludeServiceRejectWarehouses Mandatory
Output: oDataProcessed          - true:  MAUC has changed.
false: MAUC is not changed.
oReportCurrency
oHomeCurrencyArray
oOldMAUC                - MAUC value before correction in
home or option set currency.
oOldHomeMAUCArray       - MAUC values per home currency before
correction.
oOldMAUH                - MAUH value before correction.
oNewMAUC                - MAUC value after correction in
home or option set currency.
oNewHomeMAUCArray       - MAUC values per home currency after
correction.
oNewMAUH                - MAUH value after correction.
oNumberOfCostComponents
oCostCompArray
oOldCostCompMAUCReportCurrencyArray
oOldCostCompMAUCHomeCurrency1Array
oOldCostCompMAUCHomeCurrency2Array
oOldCostCompMAUCHomeCurrency3Array
oOldCostCompMAUHArray
oNewCostCompMAUCReportCurrencyArray
oNewCostCompMAUCHomeCurrency1Array
oNewCostCompMAUCHomeCurrency2Array
oNewCostCompMAUCHomeCurrency3Array
oNewCostCompMAUHArray
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
