# BillOfLading.SkipShipmentLine

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BillOfLading
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1956-1957

Skips Shipment Lines when Printing Bill of Lading. This process extension is available from 2020.05 ( KB2120253 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension BillOfLading.SkipShipmentLine can be used
to skip Shipment Lines when Printing the Bill of Lading.
Sessions where this Process Extension can be implemented:
-               Print Bills of Lading (whinh4470m000)
-               Automatic Processing of Shipping Documents when Shipment is Confirmed
and the Print Bills of Lading is an automatic step.
Fields that are available to be used in this Process Extension:
-               All fields of tables
Shipment (whinh430)
Shipment Lines (whinh431)
Load (whinh440)
Addresses (tccom130)
Carriers/LSP (tcmcs080)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table twhinh430
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on whinh430 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for

## BlockedSalesOrderOrSalesOrderLine

The following process extension(s) is/are available: BlockedSalesOrderOrSalesOrderLine.SkipFirmRelease BlockedSalesOrderOrSalesOrderLine.SkipSoftRelease
