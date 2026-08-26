# ItemPurchaseBusinessPartner.GetSafetyTime

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchaseBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 202-203

```baan
DLL:   tdextipuapi
This function is available from     2024.08 (KB3514344  ).
Syntax: long ItemPurchaseBusinessPartner.GetSafetyTime(
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcdate           iEffectiveDate,
domain  tcsite           iSite,
ref     domain  tcwttm           oSafetyTime,
ref     domain  tctope           oSafetyTimeUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns the safety time and safety time unit for
the specified Buy                      -from/Ship-from Business Partner and Item
combination.
Pre:    Not Applicable.
Post:   Not Applicable.
Input : iItemGroup                            - Item Group (Mandatory if Item is
not filled)
iItem                                         - Item (Mandatory if Item Group is
not filled)
iBuyFromBusinessPartner                       - Buy-from Business Partner (Mandatory)
iShipFromBusinessPartner
-                                               Ship-from Business Partner (Optional)
iEffectiveDate                                - Effective Date (Mandatory, use utc.num()
if the current date is needed)
iSite                                         - Site (Optional)
Output: oSafetyTime                           - Safety Time
oSafetyTimeUnit                               - Safety Time Unit
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Data read
<> 0                                          - An error occurred
```
