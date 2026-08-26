# OrderInspection.Process

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for OrderInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1757-1758

```baan
DLL:   qmextptcapi
This function is available from     2021.01 (KB2150475  ).
Syntax: long OrderInspection.Process(
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
Usage:        Expl:   This function processes the given order inspection and this can
be called for all origins except Storage Inspections, Service,
Maintenance Sales, Batch Repair, Maintenance Work and
Not Applicable. And this function must not be called within
a logical transaction as this function will have its own
transaction handling.
Pre:    NA
Post:   NA
Input:
iOrderOrigin                                  - Order Origin: Mandatory
iOrderNumber                                  - Order Number: Mandatory for all origins
other than Inventory Inspection
iOrderPosition                                - Order Position: Mandatory for all Origins
other than Routing, Production, Purchase
Schedule,
Production Repetitive & Inventory Inspection
iOperation                                    - Operation: Mandatory for Origin Routing
iWorkStation                                  - Work Station: Mandatory for Origin
Repetitive Routing
iOrderSequence                                - Order Sequence: Mandatory for all Origins
other than Purchase Schedule & Inventory
Inspection
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
Return: 0                                     - Order has been processed succesfully
<> 0                                          - Error
```

## Public Interfaces for ReinspectionOrder

The following functions are available: ReinspectionOrder.Create
