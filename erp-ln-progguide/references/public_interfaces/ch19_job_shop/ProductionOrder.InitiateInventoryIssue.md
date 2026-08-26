# ProductionOrder.InitiateInventoryIssue

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 715-716

```baan
DLL:   tiextsfcapi
This function is available from     2020.07 (KB2135601  ).
Syntax: long ProductionOrder.InitiateInventoryIssue(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tisfc.wybf       iOperationSelectionMethod,
domain  tcopno           iOperation,
domain  tcutcs           iActualDate,
domain  tcyesno          iProcessSerialUsingAsBuilt,
domain  tcyesno          iProcessSerialNotInAsBuilt,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   *** Warning ***
This public interface is deprecated.
use:    ProductionOrder.InitiateInventoryIssueV2
This function executes the Initiate Inventory Issue functionality,
as in session tisfc0207m000, for 1 production order.
NB.
-                       retrypoint and commit / rollback is done in the function
-                       no reports are printed
Input:  iSite                   Site (mandatory when the Site concept
is active)
iProductionOrder        Production Order (mandatory and must be
in iSite)
iOperationSelectionMethod
Operation(s) to handle:
all
upto
one
empty (= all)
iOperation              Operation (mandatory in case
iOperationSelectionMethod = tisfc.wybf.one)
iActualDate             Actual Date (0 = current date):
date used on warehouse transactions
iProcessSerialUsingAsBuilt
Process Serialized Materials In Inventory
according to the As Built structure
iProcessSerialNotInAsBuilt
Process Serialized Materials In Inventory
which are not in the As Built structure
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Initiate Inventory Issue completed
succesfully.
<> 0                    Initiate Inventory Issue was not
completed succesfully.
```
