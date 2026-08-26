# InspectionOrder.PrintSamples

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for InspectionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1761-1762

```baan
DLL:   qmextptcapi
This function is available from     2026.02 (KB3644636  ).
Syntax: long InspectionOrder.PrintSamples(
domain  qmptc.orgn       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  qmptc.pono       iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcopno           iOperation,
domain  qmrpt.wstt       iWorkStation,
domain  tcorno           iWarehouseInspection,
domain  tcpono           iWarehouseInspectionSequence,
domain  qmptc.iorn       iInspectionOrder,
domain  qmptc.saml       iSample,
domain  qmptc.sait       iSampleIteration,
domain  tcitem           iItem,
domain  tcmcs.str15      iPrintDevice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function prints the inspection order samples
and this can be called for all origins except:
-                               Service
-                               Maintenance Sales
-                               Batch Repair
-                               Maintenance Work
-                               Not Applicable
Pre:    NA
Post:   NA
Input:
iOrderOrigin                                  - Order Origin: Mandatory when Inspection
Order is not given.
iOrderNumber                                  - Order Number: Mandatory for all origins
other than Inventory Inspection and
when Inspection Order is not given.
iOrderLine                                    - Order Line: Mandatory for all Origins
other than Routing, Production,
Production Repetitive & Inventory Inspection
and when Inspection Order is not given.
iOrderSequence                                - Order Sequence: Mandatory for all Origins
other than Inventory Inspection and
when Inspection Order is not given.
iOperation                                    - Operation: Mandatory for Origin Routing
when Inspection Order is not given.
iWorkStation                                  - Work Station: Mandatory for Origin
Repetitive Routing and when
Inspection Order is not given.
iWarehouseInspection                          - Warehouse Inspection: Mandatory for all
Origins other than Routing & Repetitive Routing
and when Inspection Order is not given.
iWarehouseInspectionSequence
-                                               Warehouse Inspection Sequence : Mandatory for
Origins other than Routing & Repetitive Routing
and when Inspection Order is not given.
iInspectionOrder                              - QM Inspection Order: Mandatory when
Order details are not given.
iSample                                       - Inspection Order Sample: Not Mandatory.
iSampleIteration                              - Inspection Order Sample Iteration:
Not Mandatory.
iItem                                         - Item: Mandatory when Origin is
Storage Inspection and Inspection Order
is not given
iPrintDevice                                  - Mandatory.
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
