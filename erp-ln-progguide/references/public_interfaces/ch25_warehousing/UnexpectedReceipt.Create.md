# UnexpectedReceipt.Create

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for UnexpectedReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1281-1284

```baan
DLL:   whextinhapi
This function is available from     2022.04 (KB2232686  ).
Syntax: long UnexpectedReceipt.Create(
domain  tccwar           iWarehouse,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipmentNotice,
domain  tcpono           iShipmentNoticeSequence,
domain  whinh.load       iFreightLoad,
domain  whinh.shpm       iFreightShipment,
domain  tccfrw           iCarrier,
domain  tcpksp           iPackingSlip mb,
domain  tcyesno          iFinalReceipt,
domain  tcyesno          iConfirmReceipt,
domain  tcmcs.long       iNumberOfItems,
ref     domain  tcitem           iItemArray() fixed,
ref     domain  tcclot           iLotArray() fixed,
ref     domain  tcibd.sern       iSerialArray() fixed,
ref     domain  tcqst1           iReceivedQuantityArray(),
ref     domain  tccuni           iReceivedUnitArray() fixed,
ref     domain  tcdate           iActualReceiptDateArray(),
ref     domain  tcmcs.long       iNumberOfStockPointDetailsArray(),
ref     domain  tcclot           iStockPointLotArray(,) fixed,
ref     domain  tcibd.sern       iStockPointSerialArray(,) fixed,
ref     domain  tcinvt.date      iStockPointInvDateArray(,),
ref     domain  tcuef.effn       iStockPointEffUnitArray(,),
ref     domain  tcqst1           iStockPointQuantityArray(,),
ref     domain  tccuni           iStockPointUnitArray(,) fixed,
ref     domain  tcpono           iStockPointOwnSequenceArray(,),
ref     domain  whinh.shpm       oReceipt,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports creation and confirmation of the
unexpected receipt lines (receipt lines which are not linked to
an inbound order line).
The following steps will be executed by this Public Interface:
1. Create unexpected receipt lines for each item in array
iItemArray().
2. Set final receipt for all created unexpected receipt lines
if parameter iFinalReceipt = tcyesno.yes.
3. If iConfirmReceipt = tcyesno.yes then
-                          Generate purchase order. To facilitate this step
the option Generate Order for unexpected warehousing
receipt in the Items                            - Purchase Business Partner (session
tdipu0110m000) must be enabled for items present in
iItemArray() in combination with a
iShipFromBusinessPartner.
-                          Create new open receipt lines to replace unexpected receipt
lines which are created in step 1.
-                          Confirm the created open receipt lines.
Note: if for some reason like insufficient stock point data
found confirm receipt fails the unexpected receipt lines
will be present and can be confirmed manually later on.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iWarehouse                            - Warehouse; Mandatory
iShipFromBusinessPartner                      - Ship From Business Partner; Mandatory
iShipmentNotice                               - Shipment Notice; Optional
iShipmentNoticeSequence                       - Shipment Notice Sequence; Optional
iFreightLoad                                  - Freight Load; Optional
iFreightShipment                              - Freight Shipment; Optional
iCarrier                                      - Carrier; Optional
iPackingSlip                                  - Packing Slip; Optional
iFinalReceipt                                 - Final Receipt; Mandatory
iConfirmReceipt                               - Confirm Receipt; Mandatory.
iNumberOfItems                                - Number of Items; Mandatory
iItemArray                                    - Array of Items; Mandatory
iLotArray                                     - Array of Lots; Optional
iSerialArray                                  - Array of Serials; Optional
iReceivedQuantityArray                        - Array of quantities; Mandatory
iReceivedUnitArray                            - Array of units; Mandatory
iActualReceiptDateArray                       - Actual Receipt Date; Optional
iNumberOfStockPointDetailsArray                       -
Number stock point details per receipt
line; Optional
iStockPointLotArray                           - Stock point detail Lot; Optional
iStockPointSerialArray                        - Stock point detail Serial; Optional
iStockPointInvDateArray                       - Stock point detail Inventory Date;
Optional
iStockPointEffUnitArray                       - Stock point detail Effectivity Unit;
Optional
iStockPointQuantityArray                      - Stock point detail Quantity; Optional
iStockPointUnitArray                          - Stock point detail Storage Unit;
Optional
iStockPointOwnSequenceArray
-                                               Stock point detail Ownership Sequence;
Optional
Output: oReceipt                              - Created Receipt Number
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```

## Public Interfaces for WarehouseOrderLine

The following functions are available: WarehouseOrderLine.Activate WarehouseOrderLine.ActivityIsApplicable WarehouseOrderLine.ActivityIsMandatory WarehouseOrderLine.UpdatePlannedDates
