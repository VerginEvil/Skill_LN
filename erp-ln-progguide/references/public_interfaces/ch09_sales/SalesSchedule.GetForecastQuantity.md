# SalesSchedule.GetForecastQuantity

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesSchedule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 305-306

```baan
DLL:   tdextslsapi
This function is available from     2021.08 (KB2198627  ).
Syntax: long SalesSchedule.GetForecastQuantity(
domain  tcemm.clus       iCluster,
domain  tcitem           iItem,
domain  tcdate           iRequestedStartDate,
domain  tcdate           iRequestedEndDate,
ref     domain  tcqsl2           oForecastQuantity,
ref     domain  tccuni           oInventoryUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the forecast quantity with regards to
sales schedules for the given item in the given date range.
Forecast quantity comes from the planned requirements of
a Material Release with Release Capability and from the
recalculated planned requirements of a Material Release (MR)
followed by a (Sequence) Shipping  Schedule ((S)SHP).
For all schedules found for the input item, the forecast is
determined. If the Item                       - Sold-to Business Partner information
is not present for a certain sales schedule, the schedule is
skipped.
Date handling:
Input arguments iRequestedStartDate and iRequestedEndDate are
used to select the proper schedule lines. A sales schedule line
falls within the requested date                      -range if the period between
its start date (tdsls307.sdat) and end date (tdsls307.edat) is
partly or entirely within the requested date range.
|     [     307     ]
[     307 |   ]
|               [     307 |   ]
legend:
[]                        -> start/end date of tdsls307
|                         -> requested start/ end date
Handling of overlapping periods:
For a Material Release followed by a Shipping Schedule or a
Sequence Shipping Schedule, correction must be done in case
(Sequence) Shipping periods overlap with Material Release
periods.
For a Material Release Only no correction is needed.
Planning Cluster handling:
If iCluster is passed as empty, all schedule lines linked to
nettable warehouses are selected independent of the cluster
linked to the warehouse.
If iCluster is filled, all schedules linked to nettable or
non                      -nettable warehouses are selected but only if these
warehouses are linked to iCluster.
Pre:    NA
Post:   NA
Input:  iCluster                              - Cluster (Optional)
iItem                                         - Item (Mandatory)
iRequestedStartDate                           - Requested Start Date
iRequestedEndDate                             - Requested End Date (Mandatory)
must be after iRequestedStartDate
Output: oForecastQuantity                     - Total approved forecast quantity.
expressed in inventory unit
oInventoryUnit                                - The inventory unit of the item.
Return: 0                                     - Function executed successfully
<> 0                                          - An error occurred
```
