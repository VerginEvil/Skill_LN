# InspectionOrder.Print

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for InspectionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1759-1761

```baan
DLL:   qmextptcapi
This function is available from     2021.12 (KB2217770  ).
Syntax: long InspectionOrder.Print(
domain  qmptc.orgn       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  qmptc.pono       iOrderPosition,
domain  tcopno           iOperation,
domain  qmrpt.wstt       iWorkStation,
domain  tcpono           iOrderSequence,
domain  tcorno           iInspection,
domain  tcpono           iInspectionLine,
domain  qmptc.iorn       iInspectionOrder,
domain  tcitem           iItem,
domain  tcyesno          iPrintPrintedLines,
domain  tcyesno          iPrintStorageInspInv,
domain  tcmcs.str15      iPrintDevice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function prints the given inspection order and this can
be called for all origins except Service, Maintenance Sales,
Batch Repair, Maintenance Work and Not Applicable.And this
function must not be called within a logical transaction as
this function will have its own transaction handling.
Pre:    NA
Post:   NA
Input:
iOrderOrigin                                  - Order Origin: Mandatory when Inspection
Order is not given
iOrderNumber                                  - Order Number: Mandatory for all origins
other than Inventory Inspection and
when Inspection Order is not given
iOrderPosition                                - Order Position: Mandatory for all Origins
other than Routing, Production,
Production Repetitive & Inventory Inspection
and when Inspection Order is not given
iOperation                                    - Operation: Mandatory for Origin Routing
when Inspection Order is not given
iWorkStation                                  - Work Station: Mandatory for Origin
Repetitive Routing and when
Inspection Order is not given
iOrderSequence                                - Order Sequence: Mandatory for all Origins
other than Inventory Inspection and
when Inspection Order is not given
iInspection                                   - Inspection: Mandatory for all Origins
other than Routing & Repetitive Routing
and when Inspection Order is not given
iInspectionLine                               - Inspection Line: Mandatory for Origins
other than Routing & Repetitive Routing
and when Inspection Order is not given
iInspectionOrder                              - QM Inspection Order: Mandatory when
Order details are not given
iItem                                         - Item: Mandatory when Origin is
Storage Inspection and Inspection Order
is not given
iPrintPrintedLines                            - Print Already Printed Lines Indicator: Mandatory
iPrintStorageInspInv                          - Print Storage Inspection Inventory Lines:
Mandatory
iPrintDevice                                  - Printing Device: Not Mandatory If not
Provided asked for device when report
is opened.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Order has been printed succesfully
<> 0                                          - Error
```
