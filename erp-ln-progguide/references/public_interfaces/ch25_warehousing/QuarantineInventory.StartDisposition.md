# QuarantineInventory.StartDisposition

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1204-1206

```baan
DLL:   whextwmdapi
This function is available from     2025.12 (KB3623004  ).
Syntax: long QuarantineInventory.StartDisposition(
long             iStartMode,
domain  tcorno           iQuarantineIdentifier,
domain  tcmcs.long       iDispositionLine,
domain  whhuid           iHandlingUnit,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Quarantine Inventory
Disposition (whwmd2272m200) in Detail Mode.
Input:  iStartMode                            - Not used
Session is always started in MODAL
mode.
iQuarantineIdentifier                         - Mandatory
iDispositionLine                              - Optional, if 0, then all disposition
lines will be processed.
But will be ignored when
DispositionLineArray or
HandlingUnitArray of
iProcessingOptionSet is filled.
iHandlingUnit                                 - Optional, will be ignored when
iDispositionLine is filled and when
DispositionLineArray or
HandlingUnitArray of
iProcessingOptionSet is filled.
iProcessingOptionSet Optional, if 0, the default options
are applied.
Processing Options have a direct relationship with the form
fields on session Disposition (whwmd2272m200) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented
Software Component is not available are ignored.
NAME                    TYPE            DEFAULT
Disposition             whwmd.disp      whwmd.disp.awaiting
Reason                  tccdis          Empty String
ToItem                  tcitem          Empty String
ToLot                   tcclot          Empty String
Responsibility          whwmd.resp      whwmd.resp.not.appl
NonConformanceReference tcrefa          Empty String
DispositionQuantity     tcqst1          0.0
DispositionUnit         tccuni          Empty String
OrderSeries             tcseri          Empty String
OrderType               tccotp          Empty String
BuyFromBP               tccom.bpid      Empty String
ShipFromBP              tccom.bpid      Empty String
DispositionLineArray    domain ttjson   0
HandlingUnitArray       domain ttjson   0
JSON Object DispositionLineArray has the following structure:
"DispositionLineArray": [
{
"Line": 10
},
{
"Line": 30
}
]
This structure can be created with the following code:
DispositionLineArray = Json.newArray()
DispositionLine = Json.newObject()
Json.setNumber(DispositionLine, "Line", 10)
Json.add(DispositionLineArray, DispositionLine)
DispositionLine = Json.newObject()
Json.setNumber(DispositionLine, "Line", 30)
Json.add(DispositionLineArray, DispositionLine)
HandlingUnitArray will be ignored when DispositionLineArray is
filled.
JSON Object HandlingUnitArray has the following structure:
"HandlingUnitArray": [
{
"HandlingUnit": "HU100"
},
{
"HandlingUnit": "HU200"
}
]
This structure can be created with the following code:
HandlingUnitArray = Json.newArray()
HandlingUnit = Json.newObject()
Json.setString(HandlingUnit, "HandlingUnit", "HU100")
Json.add(HandlingUnitArray, HandlingUnit)
HandlingUnit = Json.newObject()
Json.setString(HandlingUnit, "HandlingUnit", "HU200")
Json.add(HandlingUnitArray, HandlingUnit)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```
