# Lot.Delete

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Lot
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1103-1105

```baan
DLL:   whextltcapi
This function is available from     2026.04 (KB3665487  ).
Syntax: long Lot.Delete(
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  whltc.klot       iLotType,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function deletes lots and lot-related data within a
certain range, including dependent tables (if there is
no stock on hand, blocked or allocated).
Optionally, the lot tracking can be deleted as well.
Pre:    The transaction handling is done within this function,
so there is no need to set retry point.
Post:   The transaction handling is done within this function,
so there is no need to commit or abort the process.
Input:  iItem                   Item (optional).
iLot                    Lot number (optional).
iLotType                Lot Type (mandatory).
(Purchase, Production, Maintenance, All).
iDevice                 Device for printing reports.
Mandatory if the processed lots and/or
errors must be printed.
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Archive/Delete Lots (whltc1200m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
Dates are in ISO 8601 format, e.g. YYYY              -MM-DDTHH:MM:SSZ
NAME                            TYPE                    DEFAULT
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
LotFrom                         domain tcclot           Minimum Value
LotTo                           domain tcclot           Maximum Value
BusinessPartnerFrom             domain tccom.bpid       Minimum Value
BusinessPartnerTo               domain tccom.bpid       Maximum Value
LotDateFrom                     domain tcinvt.date      Minimum Value
LotDateTo                       domain tcinvt.date      Maximum Value
DeleteLotTracking               domain tcyesno          tcyesno.yes
PrintProcessedLots              domain tcyesno          tcyesno.yes
PrintLotText                    domain tcyesno          tcyesno.yes
PrintErrors                     domain tcyesno          tcyesno.no
LotReportName                   domain tcmcs.str16      Empty String
ErrorReportName                 domain tcmcs.str16      Empty String
In case iItem/iLot/ is filled then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
LotReportName/ErrorReportName only needs to filled for customized
reports, otherwise the default report is automatically used.
Report name must start with an "r", e.g. "rwhinh423011001"
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - OK
<> 0                                          - Error.
```
