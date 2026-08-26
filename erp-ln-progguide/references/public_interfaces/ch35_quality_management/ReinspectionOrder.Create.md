# ReinspectionOrder.Create

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for ReinspectionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1758-1759

```baan
DLL:   qmextptcapi
This function is available from     2024.01 (KB2311311  ).
Syntax: long ReinspectionOrder.Create(
domain  qmptc.orgn       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  qmptc.pono       iOrderPosition,
domain  tcopno           iOperation,
domain  qmrpt.wstt       iWorkStation,
domain  tcpono           iOrderSequence,
domain  tcorno           iInspection,
domain  tcpono           iInspectionLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates reinspection order for the given order
inspection and can be called for all origins except
Storage Inspections, Service, Maintenance Sales, Batch Repair,
Maintenance Work and Not Applicable.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:
iOrderOrigin                                  - Order Origin: Mandatory
iOrderNumber                                  - Order Number: Mandatory for all origins
other than Inventory Inspection
iOrderPosition                                - Order Position: Mandatory for all Origins
other than Routing, Production,
Production Repetitive & Inventory Inspection
iOperation                                    - Operation: Mandatory for Origin Routing
iWorkStation                                  - Work Station: Mandatory for Origin
Repetitive Routing
iOrderSequence                                - Order Sequence: Mandatory for all Origins
other than Inventory Inspection
iInspection                                   - Inspection: Mandatory for all Origins
other than Routing & Repetitive Routing
iInspectionLine                               - Inspection Line: Mandatory for Origins
other than Routing & Repetitive Routing
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Order has been closed successfully
<> 0                                          - Error
```

## Public Interfaces for InspectionOrder

The following functions are available: InspectionOrder.Print InspectionOrder.PrintSamples InspectionOrder.PrintTestData InspectionOrder.StartMultiMain
