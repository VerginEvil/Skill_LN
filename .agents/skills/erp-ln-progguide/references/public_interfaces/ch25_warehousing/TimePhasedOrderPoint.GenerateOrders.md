# TimePhasedOrderPoint.GenerateOrders

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for TimePhasedOrderPoint
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1300-1301

```baan
DLL:   whextinhapi
This function is available from 2024.12 (KB3533941).
Syntax: long TimePhasedOrderPoint.GenerateOrders(
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates warehouse, production, purchase and/or
sales orders based on the Time Phased Order Point principle.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Orders (TPOP) (whinh2201m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
ItemFrom                domain tcitem           Minimum Value
ItemTo                  domain tcitem           Maximum Value
ItemTypeFrom            domain tckitm           Minimum Value
ItemTypeTo              domain tckitm           Maximum Value
ItemGroupFrom           domain tccitg           Minimum Value
ItemGroupTo             domain tccitg           Maximum Value
SiteFrom                domain tcsite           Minimum Value
SiteTo                  domain tcsite           Maximum Value
WarehouseFrom           domain tccwar           Minimum Value
WarehouseTo             domain tccwar           Maximum Value
LocationFrom            domain whloca           Minimum Value
LocationTo              domain whloca           Maximum Value
WarehouseTypeFrom       domain tctypw           Minimum Value
WarehouseTypeTo         domain tctypw           Maximum Value
ABCFrom                 domain tcabcc           Minimum Value
ABCTo                   domain tcabcc           Maximum Value
SlowMovingPercFrom      domain tcprct           Minimum Value
SlowMovingPercTo        domain tcprct           Maximum Value
BuyFromPartnerFrom      domain tccom.bpid       Minimum Value
BuyFromPartnerTo        domain tccom.bpid       Maximum Value
OrderSystemFrom         domain tcosys           Minimum Value
OrderSystemTo           domain tcosys           Maximum Value
OrderMethodFrom         domain tcomth           Minimum Value
OrderMethodTo           domain tcomth           Maximum Value
Factor                  domain tcfacr           0
Constant                domain tcwttm           0
Unit                    domain tctope           tctope.days
IncludeSpecification    domain tcyesno          tcyesno.no
MaxOrders               domain tcffno           1
CombineInterval         domain tcyesno          tcyesno.no
CombineOrders           domain tcyesno          tcyesno.no
ActivateOrders          domain tcyesno          tcyesno.no
DirectProcess           domain tcyesno          tcyesno.no
SeriesWarehousing       domain tcseri           Empty String
OrderTypeWarehousing    domain tccotp           Empty String
SeriesProduction        domain tcseri           Empty String
SeriesPurchase          domain tcseri           Empty String
OrderTypePurchase       domain tccotp           Empty String
SeriesSales             domain tcseri           Empty String
OrderTypeSales          domain tccotp           Empty String
Output: N.a.
Return: 0 - Order(s) have been created successfully.
DALHOOKERROR - Order could not be created.
```
