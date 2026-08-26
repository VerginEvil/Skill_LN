# ItemLotSerialTracking.GetChildren

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemLotSerialTracking
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1122-1124

```baan
DLL:   whextltcapi
This function is available from     2025.12 (KB3599334  ).
Syntax: long ItemLotSerialTracking.GetChildren(
long             iMode,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
ref             long             oChildren,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns the next level items, lots and/or serials
for the combination of (parent) item, lot and serial passed.
The output is in json format.
By calling this function for each child for which the HasChildren
variable in the oChildren output reads 'True', the complete
breakdown structure can be retrieved as it is shown in the
Tracking pane of session "Item, Lot and Serial 360" (whltc3600m100).
To get the details of the Transactions pane of this session,
function ItemLotSerialTransactions.Get()
can be called for a combination of Item, Lot and/or Serial.
Input:  iMode   Mandatory.
The mode determines the way the tracking data will be
retrieved. The following options are possible:
10      Where Supplied / As                              -built
20      Where Used / As                              -built
30      Where Supplied / As                              -maintained
40      Where Used / As                              -maintained
iItem   The item code (mandatory)
e.g. "         RLX CHAIR 360"
iLot    The lot code (optional)
e.g. ""
iSerial
The serial number (optional)
e.g. "SER                              -2017-01-18-51792"
Output: oChildren
This is a json array containing the children wich are
found for the combination of parent item, lot and serial
which are passed as input.
The json contains the parent key itself and a json array
of children. Each child lists a combination of item, lot
and serial, including an 'HasChildren' field which
indicates whether this node is also a parent which has
children of its own.
e.g:
{
"Item": "         RLX CHAIR 360",
"Lot": "",
"Serial": "SER                              -2017-01-18-51790",
"Children": [
{
"Item": "         RLX FRONT COMP 360",
"Lot": "LOT                                      -2017-01-18-03242",
"Serial": "SER                                      -2017-01-18-51788",
"HasChildren": "true"
},
{
"Item": "         RLX BACK COMP 360",
"Lot": "LOT                                      -2017-01-18-03243",
"Serial": "SER                                      -2017-01-18-51790",
"HasChildren": "true"
},
{
"Item": "         RLX SEAT 360",
"Lot": "LOT                                      -2017-01-18-03241",
"Serial": "",
"HasChildren": "false"
}
]
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
