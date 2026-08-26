# ItemLotSerialTransactions.Get

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemLotSerialTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1119-1120

```baan
DLL:   whextltcapi
This function is available from     2025.12 (KB3599334  ).
Syntax: long ItemLotSerialTransactions.Get(
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tcltc.boty       iBusinessObjectType,
domain  tcprbo           iBusinessObject,
domain  tcborf           iBusinessObjectReference,
ref             long             oTransactions,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns the transaction details as shown in the
bottom Transactions pane of session "Item, Lot and Serial 360"
(whltc3600m100), for a combination of item, lot and serial.
It could e.g. be called for each Item, Lot and/or serial level
of a 'where supplied / where used' structure as retrieved with
function ItemLotSerialTracking.GetChildren().
The transactions can be filtered by business object type,
business object and/or business object reference.
The output is in json format.
Input:  iItem
The item code (mandatory)
e.g. "         RLX FRONT COMP 360"
iLot
The lot code (optional)
e.g. "LOT                              -2017-01-18-03242"
iSerial
The serial number (optional)
e.g. "SER                              -2017-01-18-51788"
iBusinessObjectType
Business Object Type (optional), to filter the
transactions to be retrieved. This could be an order
origin.
e.g. tcltc.boty.production
iBusinessObject
Business Object (optional), to filter the transactions
to be retrieved. This could be an order number.
e.g. "SFC003560"
iBusinessObjectReference
Business Object Reference (optional), to filter the
transactions to be retrieved. This could be an order line.
e.g. ""
Output: oTransactions
A json array containing the item, lot and serial
transactions (whltc310) for the given input selection.
e.g:
{
"Item": "                 RLX FRONT COMP 360",
"Lot": "LOT                        -2017-01-18-03242",
"Serial": "SER                        -2017-01-18-51788",
"Transactions": [
{
"TransactionDate": 1709714921,
"BusinessObjectType": 25,
"BusinessObject": "SFC003560",
"BusinessObjectReference": "",
"Event": "Receipt in Warehouse",
"BusinessPartner": "",
"BusinessPartnerName": "",
"Warehouse": "RLXWH3",
"WarehouseDescription": "No locations",
"SerialStatus": 1,
"OriginalLot": "",
"Receipt": "WR0029613",
"ReceiptLine": 10,
"Shipment": "",
"ShipmentLine": 0,
"QuantityInInventoryUnit": 1,
"InventoryUnit": "pcs",
"User": "jsmith",
"UserName": "John Smith"
},
{
etc..
}
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK
<> 0: error
```
