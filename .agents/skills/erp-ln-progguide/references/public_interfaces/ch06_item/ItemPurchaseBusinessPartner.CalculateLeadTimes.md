# ItemPurchaseBusinessPartner.CalculateLeadTimes

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchaseBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 202-203

```baan
DLL:   tdextipuapi
This function is available from 2021.03 (KB2172211).
Syntax: long ItemPurchaseBusinessPartner.CalculateLeadTimes(
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tccom.cadr       iShipFromAddress,
domain  tccom.cadr       iShipToAddress,
domain  tcitem           iItem,
domain  tcncmp           iLogisticCompany,
domain  tcsite           iSite,
domain  tcwttm           iSupplyTime,
domain  tctope           iSupplyTimeUnit,
domain  tcwttm           iFullSupplyTime,
domain  tctope           iFullSupplyTimeUnit,
domain  tcwttm           iInternalProcessTime,
domain  tctope           iInternalProcessTimeUnit,
domain  tcwttm           iSafetyTime,
domain  tctope           iSafetyTimeUnit,
domain  tccfrw           iCarrier,
domain  tcmcs.long6      iLeadTime,
domain  tcmcs.long6      iFullLeadTime,
ref     domain  tcmcs.long6      oLeadTime,
ref     domain  tcmcs.long6      oFullLeadTime,
ref     domain  tcmcs.long6      oTransportationTime,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the lead times (normal lead time and
full lead time) and transportation time in days for the given
combination of purchased item and business partner.
Pre:    Not Applicable.
Post:   Not Applicable.
Input:  iBuyFromBusinessPartner - Buy-from Business Partner (Mandatory)
iShipFromBusinessPartner- Ship-from Business Partner (not Mandatory)
iShipFromAddress        - Ship-from Address.
If filled this address will be used in
transportation time calculation.
iShipToAddress          - Ship-to Address.
If filled this address will be used in
transportation time calculation.
iItem                   - Item (Mandatory)
iLogisticCompany        - Logistic company (Mandatory)
iSite                   - Site (not Mandatory)
iSupplyTime             - Supply Time (not Mandatory)
iSupplyTimeUnit         - Supply Time Unit (Mandatory)
Possible values:
- Hours
- Days
iFullSupplyTime         - Full Supply Time (not Mandatory)
iFullSupplyTimeUnit     - Full Supply Time Unit (Mandatory)
Possible values:
- Hours
- Days
iInternalProcessTime    - Internal Process Time (not Mandatory)
iInternalProcessTimeUnit- Internal Process Time Unit (Mandatory)
Possible values:
- Hours
- Days
iSafetyTime             - Safety Time (not Mandatory)
iSafetyTimeUnit         - Safety Time Unit (Mandatory)
Possible values:
- Hours
- Days
iCarrier                - Carrier  (not Mandatory)
iLeadTime               - Current Lead Time (not Mandatory)
iFullLeadTime           - Current Full Lead Time (not Mandatory)
Output: oLeadTime               - Calculated Lead Time
oFullLeadTime           - Calculated Full Lead Time
oTransportationTime     - Calculated Transit Time
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Calculate Leadtimes finished
<> 0                    - Not all mandatory input arguments are
filled.
```
