# ProductionOrder.InitiateInventoryIssueV2

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 716-717

```baan
DLL:   tiextsfcapi
This function is available from 2022.06 (KB2222932).
Syntax: long ProductionOrder.InitiateInventoryIssueV2(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tisfc.wybf       iOperationSelectionMethod,
domain  tcopno           iOperation,
domain  tcdate           iUpToDate,
domain  tcutcs           iActualDate,
domain  tcyesno          iProcessSerialUsingAsBuilt,
domain  tcyesno          iProcessSerialNotInAsBuilt,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes the Initiate Inventory Issue functionality,
as in session tisfc0207m000, for 1 production order.
NB.
- retrypoint and commit / rollback is done in the function
- no reports are printed
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iOperationSelectionMethod
Operation(s) to handle:
all
upto
one
empty (= all)
iOperation              Operation (mandatory in case
iOperationSelectionMethod = tisfc.wybf.one).
iUpToDate               Select materials with requirement date
up to the specified date (if 0, all
materials will be selected).
iActualDate             Actual Date, date used on warehouse
transactions. If 0, the actual date will
be empty.
iProcessSerialUsingAsBuilt
Process Serialized Materials In Inventory
according to the As Built structure.
iProcessSerialNotInAsBuilt
Process Serialized Materials In Inventory
which are not in the As Built structure.
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
