# DeliveryNote.Print

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for DeliveryNote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1136-1139

```baan
DLL:   whextinhapi
This function is available from     2025.03 (KB3540150  ).
Syntax: long DeliveryNote.Print(
domain  tcdeln           iDeliveryNote,
domain  whinh.shpm       iPreliminaryDeliveryNote,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the delivery note for the
iDeliveryNote/iPreliminaryDeliveryNote using the defaults or
options as provided in the iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iDeliveryNote           Optional
iPreliminaryDeliveryNote Optional
iDevice                 Mandatory
iProcessingOptionSet Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iDeliveryNote is filled then field
iPreliminaryDeliveryNote and the following options of the
iProcessingOptionSet will be ignored:
-                       selection range fields (From/To)
-                       DeliveryNoteArray
-                       PreliminaryDeliveryNoteArray
The Delivery Note will then be printed for the given
iDeliveryNote.
In case iPreliminaryDeliveryNote is filled then the following
options of the iProcessingOptionSet will be ignored:
-                       selection range fields (From/To)
-                       DeliveryNoteArray
-                       PreliminaryDeliveryNoteArray
The Delivery Note will then be printed for the given
iPreliminaryDeliveryNote.
In case option DeliveryNoteArray is set then the selection range
fields (From/To) and PreliminaryDeliveryNoteArray of the
iProcessingOptionSet will be ignored.
The Delivery Note will then be printed for the delivery notes
in the array.
In case option PreliminaryDeliveryNoteArray is set then the
selection range fields (From/To) of the iProcessingOptionSet
will be ignored.
The Delivery Note will then be printed for the preliminairy
delivery notes in the array.
Processing Options have a direct relationship with the form fields
on session Print Delivery Notes (whinh4477m000) and are not explained
in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
DeliveryNoteFrom                domain tcdeln           Minimum Value
DeliveryNoteTo                  domain tcdeln           Maximum Value
PreliminaryDeliveryNoteFrom     domain whinh.shpm       Minimum Value
PreliminaryDeliveryNoteTo       domain whinh.shpm       Maximum Value
YearFrom                        domain tcyrno           Minimum Value
YearTo                          domain tcyrno           Maximum Value
ShipmentFrom                    domain whinh.shpm       Minimum Value
ShipmentTo                      domain whinh.shpm       Maximum Value
LoadFrom                        domain whinh.load       Minimum Value
LoadTo                          domain whinh.load       Maximum Value
ShipFromTypeFrom                domain tctyps           Minimum Value
ShipFromTypeTo                  domain tctyps           Maximum Value
ShipFromCodeFrom                domain tcshpm           Minimum Value
ShipFromCodeTo                  domain tcshpm           Maximum Value
ShipToTypeFrom                  domain tctyps           Minimum Value
ShipToTypeTo                    domain tctyps           Maximum Value
ShipToCodeFrom                  domain tcshpm           Minimum Value
ShipToCodeTo                    domain tcshpm           Maximum Value
CarrierFrom                     domain tccfrw           Minimum Value
CarrierTo                       domain tccfrw           Maximum Value
RouteFrom                       domain tccrte           Minimum Value
RouteTo                         domain tccrte           Maximum Value
ShipmentConfirmDateFrom         domain tcdate           Minimum Value
ShipmentConfirmDateTo           domain tcdate           Current Date/Time
CashOnDeliveryType              domain tckofn           tckofn.both
OpenDeliveryNotes               domain tcyesno          tcyesno.no
UseOrderLanguage                domain tcyesno          tcyesno.yes
ManualDeliveryNotes             domain tcyesno          tcyesno.yes
DeliveryNoteAction              domain whinh.dnac       whinh.dnac.preview
PrintDetailedReport             domain tcyesno          tcyesno.no
PrintOwnership                  domain tcyesno          tcyesno.no
NumberOfCopies                  domain tcsrno           0
DeliveryNoteArray               domain ttjson           0
PreliminaryDeliveryNoteArray    domain ttjson           0
ReportName                      domain tcmcs.str16      Empty String
JSON Object DeliveryNoteArray has the following structure:
"DeliveryNoteArray": [
{
"DeliveryNote": "DLN008448"
},
{
"DeliveryNote": "DLN008428"
}
]
This structure can be created with the following code:
DeliveryNoteArray = Json.newArray()
DeliveryNote = Json.newObject()
Json.setString(DeliveryNote, "deliverynote", "DLN008448")
Json.add(DeliveryNoteArray, DeliveryNote)
DeliveryNote = Json.newObject()
Json.setString(DeliveryNote, "deliverynote", "DLN008428")
Json.add(DeliveryNoteArray, DeliveryNote)
In a similar way the PreliminairyNoteArray can be set.
ReportName only needs to filled for customized reports, otherwise
the standard report is automatically used.
ReportName must start with an "r", e.g. "rwhinh447701001"
Output: oDataProcessed                        - true:  Delivery Note Printed.
false: Nothing Printed.
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
