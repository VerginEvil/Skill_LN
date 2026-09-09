# ProductionOrderOperation.StartMoveRejectedEndItemToQuarantine

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 803-804

```baan
DLL:   tiextsfcapi
This function is available from 2026.04 (KB3608602).
Syntax: long ProductionOrderOperation.StartMoveRejectedEndItemToQuarantine(
long             iStartMode,
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tiqep1           iQuantityToQuarantine,
domain  tccwar           iWarehouse,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Move Rejected End Item to
Quarantine(tisfc0209m000). Move Rejected End Item to Quarantine
session is used to move a quantity of end item with the status
rejected to a quarantine warehouse or a specific location in a
regular warehouse specified as the quarantine location.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dialog.
iSite                   Site.
iProductionOrder        Production Order.
iOperation              Operation.
iQuantityToQuarantine   Quantity To Quarantine.
iWarehouse              Warehouse.
iProcessingOptionSet    Processing Option Set.
If 0, then user default/session default
values are applied. A Processing Option
Set can be created via a call to
ProcessingOptionSet.Create() in DLL
tcextextapi. After the call the option
set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                            TYPE            DEFAULT
EffectivityUnit                 tcuef.effn      0
WarehouseLocation               tiloca          ""
LotCode                         tcclot          ""
NCMReport                       tcorno          ""
Text                            tcmcs.s999m     ""
DirectProcessInbound            tcyesno         tcyesno.no
PrintDocument                   tcyesno         tcyesno.no
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
