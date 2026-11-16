# SerializedItem.Supersede

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1361-1363

```baan
DLL:   tsextcfgapi
This function is available from 2023.05 (KB2281129).
Syntax: long SerializedItem.Supersede(
domain  tcitem           iSourceItem fixed,
domain  tcibd.sern       iSourceSerialNumber fixed,
domain  tcitem           iTargetItem fixed,
domain  tcibd.sern       iTargetSerialNumber fixed,
domain  tcedm.revi       iRevision fixed,
domain  tcclot           iLotCode fixed,
domain  tcseri           iWarehouseOrderSeries fixed,
domain  tcyesno          iSetPrice,
domain  tcpric           iNewPrice,
domain  tcccur           iCurrencyNewPrice fixed,
domain  tcyesno          iCopySourceSerializedItemData,
domain  tcyesno          iCopyLogisticalAndOperationalData,
domain  tcyesno          iCopyText,
domain  tcyesno          iCopyCounterReadings,
domain  tcyesno          iCopyWarranty,
domain  tstdm.wrtp       iWarrantyType,
domain  tscfg.cwte       iWarrantyTemplate fixed,
domain  tsmdm.date       iWarrantyStartDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function handles the process of superseding a
Serialized Item. It offers the same functionality as session
Supersede Serialized Item (tscfg2240m000).
Superseding is only possible when there is a Physical
Breakdown Change (PBC) present for the Source Item. When
no PBC exists it will be created first.
To have Physical Breakdown Changes, the Configuration
Management Parameter Physical Breakdown Changes must be Yes.
First it is checked if superseding of the Source Item is
allowed.
Superseding is allowed when:
- the Source Item has not been superseded already;
- there are no open Service Orders, Maintenance Sales Orders,
Maintenance Work Orders, Field Change Orders, Calls,
Quotes, Planned Activities, Contracts, Inspections,
Maintenance Notifications, Subcontract Agreements,
or Claims for the Source Item;
- there is no Part Maintenance Line present for the
Source Item based on which the new Serialized Item
will be returned to the customer, or the related warehouse
issue order can be changed.
When superseding is allowed the following actions are
performed:
- a new Serialized Item is created when it does not exist yet;
when Copy Source Serialized Item Data is Yes, and Copy
Logistical and Operational Data  is Yes, logistical and
operational data is copied as well.
When Copy Logistical and Operational Data is No, the
field values will be defaulted from the item master data.
When Copy Text is Yes, the three Text fields are copied;
- warranty data is copied when Copy Warranty indicates to do
so. Otherwise warranty is controlled by the warranty
settings which are passed as input arguments;
- warranty is not copied when the warranty of the Source
Item has been expired or terminated;
- warranty is not copied when the Target Item already exists,
having its own warranty;
- when Copy Counter Readings is Yes, the Counter Readings and
Reset Rules are copied between the Source Item and Target
Item;
- counter readings are not copied when the Target Item
already exists, having its own counter readings;
- when the Source Item is in a Warehouse, an Item Transfer
is created and processed automatically;
- the Physical Breakdown of the Source Item is copied to
the Target Item;
- the Serialized Item Status of the Source Item is
set to Superseded, and the relation between the two items
is stored in table Superseded Items (tscfg204);
- finally, the existing Physical Breakdown Change for the
Source Item is updated. The Item Superseded flag is
set and the Target Item and Target Serial Number are
updated.
Pre     : No open database transaction should be present (so before
calling this function the existing database transactions
should either have been aborted or committed).
Post    : -
Input   : iSourceItem
Serialized Item to supersede: Mandatory
iSourceSerialNumber
Serial Number of Serialized Item to supersede: Mandatory
iTargetItem
New Serialized Item: Mandatory
iTargetSerialNumber
Serial Number of New Serialized Item: Mandatory
iRevision
Revision of the  New Serialized Item: Not mandatory
iLotCode
Lot Code of New Serialized Item: Not mandatory
iWarehouseOrderSeries
Warehouse Order Series: Not mandatory
iSetPrice
Set Price: Mandatory; Yes/No
iNewPrice
New Price: Not mandatory
iCurrencyNewPrice
Currency New Price: Mandatory when iSetPrice = Yes
iCopySourceSerializedItemData
Copy Source Serialized Item Data: Mandatory; Yes/No
iCopyLogisticalAndOperationalData
Copy Logistical and Operational Data: Mandatory; Yes/No
iCopyText
Copy Text: Mandatory; Yes/No
iCopyCounterReadings
Copy Counter Readings: Mandatory; Yes/No
iCopyWarranty
Copy Warranty: Mandatory; Yes/No
iWarrantyType
Warranty Type: Not mandatory
iWarrantyTemplate
Warranty Template: Not mandatory
iWarrantyStartDate
Warranty Start Date: Not mandatory
Output  : ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0             - No error
<> 0          - An error occurred
```
