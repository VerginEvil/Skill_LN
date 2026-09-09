# lpext.tur0001.get.etransport.data.by.shipment

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TUR.eTransport
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2313-2313

```baan
Syntax: long lpext.tur0001.get.etransport.data.by.shipment(
domain  tcshpm           i.shipment,
ref     domain  tcivrc           o.vehicle.plate.number.country,
ref     domain  tcdsca           o.vehicle.plate.number mb,
ref     domain  tccom.name       o.driver.name mb,
ref     domain  tccom.name       o.driver.surname mb,
ref     domain  tccom.fidn       o.driver.fiscal.id,
ref     domain  tccfrw           o.carrier.lsp,
ref     domain  tctax.txnb       o.carrier.tax.id )
Usage:        Expl:   Use this method to determine e-Transport data in case the data
cannot be retrieved from the E-Transport Data by Shipment
(lptur0130m000) or from Freight.
Pre:    na
Post:   na
Input:  i.shipment              - Shipment
Output: o.vehicle.plate.number.country
- Vehicle Plate Number Country
o.vehicle.plate.number  - Vehicle Plate Number
o.driver.name           - Driver Name
o.driver.surname        - Driver Surname
o.driver.fiscal.id      - Driver Fiscal ID
o.carrier.lsp           - Carrier/LSP
o.carrier.tax.id        - Carrier TAX ID
Return: 0                       - Succes
<> 0                    - When an error occurs
```
