# WarehouseInspection.Print

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1274-1276

```baan
DLL:   whextinhapi
This function is available from 2025.06 (KB3566665).
Syntax: long WarehouseInspection.Print(
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the Warehouse Inspections for
the iInspection and iInspectionSequence using the defaults
or options as provided in the iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Pre:    N.a.
Post:   N.a.
Input:  iInspection             Optional
iInspectionSequence     Optional, ignored if iInspection is
empty.
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iInspection is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- InspectionArray
The warehouse inspections will then be printed for the given
iInspection (and specific iInspectionSequence, if filled).
In case option InspectionArray is set then the selection
range fields (From/To) of the iProcessingOptionSet will be
ignored.
The warehouse inspections will then be printed for the
inspections in the array.
Processing Options have a direct relationship with the form fields
on session Print Warehouse Inspections (whinh3422m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
InspectionFrom                  domain tcorno           Minimum Value
InspectionTo                    domain tcorno           Maximum Value
InspectionSequenceFrom          domain tcpono           Minimum Value
InspectionSequenceTo            domain tcpono           Maximum Value
OrderOriginFrom                 domain whinh.oorg       Minimum Value
OrderOriginTo                   domain whinh.oorg       Maximum Value
OrderNumberFrom                 domain tcorno           Minimum Value
OrderNumberTo                   domain tcorno           Maximum Value
OrderSetFrom                    domain tcwset           Minimum Value
OrderSetTo                      domain tcwset           Maximum Value
OrderLineFrom                   domain tcpono           Minimum Value
OrderLineTo                     domain tcpono           Maximum Value
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
LocationFrom                    domain whloca           Minimum Value
LocationTo                      domain whloca           Maximum Value
InspectionDateFrom              domain tcdate           Minimum Value
InspectionDateTo                domain tcdate           Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
InspectionStatus                domain whinh.prap       whinh.prap.tobe
InspectionType                  domain whinh.prat       whinh.prat.both
PrintInspectionLines            domain tcyesno          tcyesno.no
PrintOwnership                  domain tcyesno          tcyesno.no
PrintOrderLineTotals            domain tcyesno          tcyesno.no
PrintHandlingUnits              domain tcyesno          tcyesno.no
PrintInspectionText             domain tcyesno          tcyesno.yes
PrintInspectionInstructionText  domain tcyesno          tcyesno.no
PrintInspectionResultsText      domain tcyesno          tcyesno.no
InspectionArray                 domain ttjson           0
ReportNumber                    domain tcmcs.long       1
ReportName                      domain tcmcs.str16      Empty String
Possible values of ReportNumber are:
1 - Warehouse Inspections
JSON Object InspectionArray has the following structure:
"InspectionArray": [
{
"Inspection": "INS000006"
"InspectionSequence": 1,
},
{
"Inspection": "INS000003"
"InspectionSequence": 2,
}
]
This structure can be created with the following code:
InspectionArray = Json.newArray()
Inspection = Json.newObject()
Json.setString(Inspection, "Inspection", "INS000006")
Json.setNumber(Inspection, "InspectionSequence", 1)
Json.add(InspectionArray, Inspection)
Inspection = Json.newObject()
Json.setString(Inspection, "Inspection", "INS000003")
Json.setNumber(Inspection, "InspectionSequence", 2)
Json.add(InspectionArray, Inspection)
ReportName only needs to filled for customized reports,
otherwise the standard report is used based on the ReportNumber.
ReportName must start with an "r", e.g. "rwhinh342211001"
Output: oDataProcessed          - true:  Data Printed.
false: Nothing Printed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
