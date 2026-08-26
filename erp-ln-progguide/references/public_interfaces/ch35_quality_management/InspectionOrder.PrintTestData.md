# InspectionOrder.PrintTestData

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for InspectionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1762-1764

```baan
DLL:   qmextptcapi
This function is available from     2024.09 (KB3505946  ).
Syntax: long InspectionOrder.PrintTestData(
domain  qmptc.orgn       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  qmptc.pono       iOrderPosition,
domain  tcopno           iOperation,
domain  qmrpt.wstt       iWorkStation,
domain  tcpono           iOrderSequence,
domain  tcorno           iWarehouseInspection,
domain  tcpono           iWarehouseInspectionLine,
domain  qmptc.iorn       iInspectionOrder,
domain  tcpono           iInspectionOrderLine,
domain  qmptc.saml       iSample,
domain  qmptc.sait       iSampleIteration,
domain  qmptc.srno       iSamplePart,
domain  tcitem           iItem,
domain  qmptc.metd       iPrintReportBy,
domain  tcmcs.str15      iPrintDevice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function prints the inspection order test data
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
iOrderPosition                                - Order Position: Mandatory for all Origins
other than Routing, Production,
Production Repetitive & Inventory Inspection
and when Inspection Order is not given.
iOperation                                    - Operation: Mandatory for Origin Routing
when Inspection Order is not given.
iWorkStation                                  - Work Station: Mandatory for Origin
Repetitive Routing and when
Inspection Order is not given.
iOrderSequence                                - Order Sequence: Mandatory for all Origins
other than Inventory Inspection and
when Inspection Order is not given.
iWarehouseInspection                          - Warehouse Inspection: Mandatory for all
Origins other than Routing & Repetitive Routing
and when Inspection Order is not given.
iWarehouseInspectionLine
-                                               Warehouse Inspection Line: Mandatory for
Origins other than Routing & Repetitive Routing
and when Inspection Order is not given.
iInspectionOrder                              - QM Inspection Order: Mandatory when
Order details are not given.
iInspectionOrderLine                          - QM Inspection Order Line: Not Mandatory.
iSample                                       - Inspection Order Sample: Not Mandatory.
iSampleIteration                              - Inspection Order Sample Iteration:
Not Mandatory.
iSamplePart                                   - Inspection Order Sample Part:
Not Mandatory.
iItem                                         - Item: Mandatory when Origin is
Storage Inspection and Inspection Order
is not given
iPrintReportBy                                - Print report by (Mandatory).
Possible values are:
1) Characteristic
2) Sample Part
3) Sequence
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
