# ProjectPCS.PrintActualStandardCost

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 896-898

```baan
DLL:   tiextpcsapi
This function is available from 2024.11 (KB3519652).
Syntax: long ProjectPCS.PrintActualStandardCost(
domain  tccprj           iProject,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to print Actual Standard Cost
for a range of PCS Projects. This Public Interface is similar to
session tipcs3462m000.
Pre:    -
Post:   -
Input:  iProject                - Project for which the report must be
printed. Optional.
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default printing options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Print Actual Standard Cost by Project" (tipcs3462m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Print options which are not available as Processing Options
will get defaulted in accordance with the session logic.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
Turnig off category processing options will also turn off and disable
their sub category processing options.
Example : If we set "Project" processing option as tcyesno.no then
its sub processing options ProjectGeneralCosts,ProjectGeneralHours,
ProjectSurcharges will also be set to tcyesno.no.
NAME                                    TYPE                    DEFAULT
ProjectFrom                     domain  tccprj          iProject
ProjectTo                       domain  tccprj          ProjectFrom when
set. Otherwise max
domain value.
CurrencyForDetails              domain  tiusec          tiusec.home.ref
CurrencyForTotals               domain  tcccur          Reference currency
of the company.
ExchangeRateType                domain  tcemm.expu      Internal exchange
rate of the company.
Project                         domain  tcyesno         tcyesno.yes
ProjectGeneralCosts             domain  tcyesno         tcyesno.yes
ProjectGeneralHours             domain  tcyesno         tcyesno.yes
ProjectSurcharges               domain  tcyesno         tcyesno.yes
Purchasing                      domain  tcyesno         tcyesno.yes
PurchasingGeneralCosts          domain  tcyesno         tcyesno.yes
PurchaseCosts                   domain  tcyesno         tcyesno.yes
PurchaseVariances               domain  tcyesno         tcyesno.yes
PurchaseSurcharges              domain  tcyesno         tcyesno.yes
Production                      domain  tcyesno         tcyesno.yes
ProductionMaterialCosts         domain  tcyesno         tcyesno.yes
ProductionOperationCosts        domain  tcyesno         tcyesno.yes
ProductionSubcontractingCosts   domain  tcyesno         tcyesno.yes
ProductionSurcharges            domain  tcyesno         tcyesno.yes
Sales                           domain  tcyesno         tcyesno.yes
SalesGeneralCosts               domain  tcyesno         tcyesno.yes
SalesStandardItemDeliveries     domain  tcyesno         tcyesno.yes
SalesSrurcharges                domain  tcyesno         tcyesno.yes
Service                         domain  tcyesno         tcyesno.yes
ServiceGeneralCosts             domain  tcyesno         tcyesno.yes
ServiceItemDeliveries           domain  tcyesno         tcyesno.yes
OperationCosts                  domain  tcyesno         tcyesno.yes
ServiceSubcontractingCosts      domain  tcyesno         tcyesno.yes
ServiceSurcharges               domain  tcyesno         tcyesno.yes
Warehousing                     domain  tcyesno         tcyesno.yes
TransferCosts                   domain  tcyesno         tcyesno.yes
WarehouseSurcharges             domain  tcyesno         tcyesno.yes
DetailsPerOrder                 domain  tcyesno         tcyesno.yes
DetailsPerCostComponent         domain  tcyesno         tcyesno.no
PrintingDevice                  domain  tcmcs.str14     ""
PrintingFileoutPathAndName      domain  tcmcs.str100    ""
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Print Actual Standard Cost by Project
is succesfull.
<> 0                    - Otherwise.
```
