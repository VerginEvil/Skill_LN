# PurchaseOrderAdvice.Confirm

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PurchaseOrderAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1291-1293

```baan
DLL:   whextinaapi
This function is available from     2025.11 (KB3628779  ).
Syntax: long PurchaseOrderAdvice.Confirm(
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function confirms purchase order advice.
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
on session Confirm Purchase Order Advice (whina3211m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
AdviceFrom              domain tcorno           Minimum Value
AdviceTo                domain tcorno           Maximum Value
EffectivityUnitFrom     domain tcuef.effn       Minimum Value
EffectivityUnitTo       domain tcuef.effn       Maximum Value
ItemGroupFrom           domain tccitg           Minimum Value
ItemGroupTo             domain tccitg           Maximum Value
SiteFrom                domain tcsite           Minimum Value
SiteTo                  domain tcsite           Maximum Value
WarehouseFrom           domain tccwar           Minimum Value
WarehouseTo             domain tccwar           Maximum Value
BuyFromPartnerFrom      domain tccom.bpid       Minimum Value
BuyFromPartnerTo        domain tccom.bpid       Maximum Value
ShipFromPartnerFrom     domain tccom.bpid       Minimum Value
ShipFromPartnerTo       domain tccom.bpid       Maximum Value
BuyerFrom               domain tcemno           Minimum Value
BuyerTo                 domain tcemno           Maximum Value
PlannerFrom             domain tcemno           Minimum Value
PlannerTo               domain tcemno           Maximum Value
RelatedOrderFrom        domain tcorno           Minimum Value
RelatedOrderTo          domain tcorno           Maximum Value
ItemFrom                domain tcitem           Minimum Value
ItemTo                  domain tcitem           Maximum Value
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - Purchase order advice have been confirmed successfully.
<> 0                       - Error. Purchase order advice could not be confirmed.
```
