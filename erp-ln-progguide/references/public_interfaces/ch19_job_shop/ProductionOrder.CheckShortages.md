# ProductionOrder.CheckShortages

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 709-710

```baan
DLL:   tiextsfcapi
This function is available from     2021.03 (KB2165373  ).
Syntax: long ProductionOrder.CheckShortages(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tisfc.stck       iShortageCheckType,
domain  tisfc.scin       iShortageCheckScope,
domain  tcyesno          iShortageCheckSkipBlockedInventory,
domain  tcyesno          iShortageCheckCriticalItemsOnly,
ref             boolean          oShortageDetected,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to check for material
shortages prior to releasing the production order.
Pre:    None
Post:   None
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iShortageCheckType      Type of Shortage Check (mandatory)
iShortageCheckScope     Scope of Shortage Check (mandatory)
iShortageCheckSkipBlockedInventory
Exclude blocked inventory from Shortage
Check (mandatory)
iShortageCheckCriticalItemsOnly
Check Critical Items only during Shortage
Check (mandatory)
Output: oShortageDetected       Indicates if a shortage was detected.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Check Shortages executed successfully.
<> 0                    An error encountered during check for
shortages.
```
