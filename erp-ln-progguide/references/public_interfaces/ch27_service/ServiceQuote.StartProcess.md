# ServiceQuote.StartProcess

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1482-1486

```baan
DLL:   tsexteppapi
This function is available from 2025.04 (KB3568308).
Syntax: long ServiceQuote.StartProcess(
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Process Quotes (tsepp1203m000).
Pre     : -
Post    : -
Input:  iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
StartMode
long                    MODAL
Specifies the start mode for the session.
Possible values:
MODAL
MODELESS
MODELESS_ALWAYS
IgnoreSelectionFields
boolean                 false
If true, the session defaults are used.
FromSoldToBusinessPartner
tccom.bpid              ""
From Sold-to Business Partner selection field is filled
with this value, unless IgnoreSelectionFields is False.
FromServiceOffice
domain  tccwoc          ""
From Service Office selection field is filled
with this value, unless IgnoreSelectionFields is False.
FromQuote
domain  tcorno          ""
From Quote selection field is filled with this value,
unless IgnoreSelectionFields is False.
FromQuoteLine
domain  tcpono          0
From Quote Line selection field is filled with
this value, unless IgnoreSelectionFields is False.
ToSoldToBusinessPartner
tccom.bpid              ""
To Sold-to Business Partner selection field is filled
with this value, unless IgnoreSelectionFields is False.
When not filled, it is defaulted with the max value of
the domain.
ToServiceOffice
domain  tccwoc          ""
To Service Office selection field is filled
with this value, unless IgnoreSelectionFields is False.
When not filled, it is defaulted with the max value of
the domain.
ToQuote
domain  tcorno          ""
To Quote selection field is filled with this value,
unless IgnoreSelectionFields is False.
When not filled, it is defaulted with the max value of
the domain.
ToQuoteLine
domain  tcpono          999999
To Quote Line selection field is filled with
this value, unless IgnoreSelectionFields is False.
When not filled, it is defaulted with the max value of
the domain.
ServiceOrderSeries
domain  tcseri          ""
Service Order Series.
Field is ignored when IgnoreSelectionFields is True.
AddToServiceOrder
domain  tcorno          ""
Add to Service Order.
Field is ignored when IgnoreSelectionFields is True.
MaintenanceSalesOrderSeries
domain  tcseri          ""
Maintenance Sales Order Series
Field is ignored when IgnoreSelectionFields is True.
CreateWorkOrderForPartMaintenanceLinesA
domain  tcyesno         tcyesno.no
Create Work Order for Part Maintenance Lines.
When in the MSC Parameters the Create Work Order for
Part Maintenance Line is Automatic, this argument is
ignored.
Field is ignored when IgnoreSelectionFields is True.
CreateWorkOrderForPartMaintenanceLinesB
domain  tcgen.ynds      tcgen.ynds.use.dfs
Create Work Order for Part Maintenance Lines.
When in the MSC Parameters the Create Work Order for
Part Maintenance Line is Automatic, this argument is
ignored.
Field is ignored when IgnoreSelectionFields is True.
PerformATPCheck
domain  tcyesno         tcyesno.no
Indicator whether the ATP check is performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
Field is ignored when IgnoreSelectionFields is True.
PerformPlannedAvailableCheck
domain  tcyesno         tcyesno.no
Indicator whether the Planned Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
Field is ignored when IgnoreSelectionFields is True.
PerformOnHandAvailableCheck
domain  tcyesno         tcyesno.no
Indicator whether the On Hand Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
Field is ignored when IgnoreSelectionFields is True.
SkipBlockedInventory
domain  tcyesno         tcyesno.no
Indicator whether Blocked Inventory has to be considered
during the various material availability checks.
Note: value Yes only allowed if material availability
is present in the Service Order Parameters
(or site specific record, if the Sites-concept has
been implemented). Furthermore, at least one of the
input arguments PerformPlannedAvailableCheck or
PerformOnHandAvailableCheck should have the value
Yes.
Field is ignored when IgnoreSelectionFields is True.
BlockProcess
domain  tcyesno         tcyesno.no
If set to Yes, then the processing of the Quote
will not be successful if one of the material
availability checks reports a shortage.
Note: value Yes only allowed if at least one of the
material availability checks is being executed, which
means that either PerformATPCheck,
PerformPlannedAvailableCheck or
PerformOnHandAvailableCheck should have the value Yes.
Field is ignored when IgnoreSelectionFields is True.
InventoryScope
domain  tsmdm.scin      tsmdm.scin.curr.warehouse
Indicator if during the various material availability
checks only the current warehouse should be considered
or the whole warehouse cluster.
Possible values:
Current Warehouse Only
Checks if the material is available in the
warehouse defined on the Material Line.
All Warehouses in Planning Cluster
Checks if the material is available in one of
the warehouses in the same cluster as the
warehouse defined on the Material Line.
Field is ignored when IgnoreSelectionFields is True.
UpdatePlannedDeliveryTimeOfMaterialLines
domain  tcyesno         tcyesno.no
Indicator whether the material availability checks
should update the planned delivery time of related
material lines.
Note: value Yes only allowed if at least one of the
input arguments PerformATPCheck or
PerformPlannedAvailableCheck has the value Yes.
Field is ignored when IgnoreSelectionFields is True.
UpdateQuoteAndLinesWithLatestPlannedMaterialLine
domain  tcyesno         tcyesno.no
Indicator whether the material availability checks
should update the Agreement and Order with the time of
the latest planned material line.
Note: value Yes only allowed if at least one of the
input arguments PerformATPCheck or
PerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
UpdatePlannedDeliveryTimeOfMaterialLines is Yes.
Field is ignored when IgnoreSelectionFields is True.
SynchronizeMaterialsWithLatestPlannedMaterialLine
domain  tcyesno         tcyesno.no
Indicator whether the material availability checks
should synchronize material lines with the latest
planned material line.
Note: value Yes only allowed if at least one of the
input arguments PerformATPCheck or
PerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
UpdatePlannedDeliveryTimeOfMaterialLines is Yes.
Field is ignored when IgnoreSelectionFields is True.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
