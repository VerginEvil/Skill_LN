# tcext.tax0002.before.external.tax.provider.call

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2294-2301

```baan
Syntax: long tcext.tax0002.before.external.tax.provider.call(
domain  tcapi.prov       i.tax.interface.provider,
ref             long             io.input.arguments.external.tax.provider,
ref             boolean          o.skip.external.tax.provider.call,
ref     domain  tcmcs.xml        o.tax.results.node )
Usage:        Expl:
Use this method to:
1. Change the data which is send to the External Tax Provider (EXTP).
This can be done by changing the content of the
io.input.arguments.external.tax.provider argument.
For Vertex, this argument is an XML document;
for Avatax, it is a JSON message.
2. Skip the call to the External Tax Provider (EXTP).
If the tax calculation must be skipped,
e.g. if this tax calculation call is coming from
Sales Order Lines session to prevent too high number of calls,
the o.skip.external.tax.provider.call must be set to TRUE.
Note that a valid XML tax results node must be returned
via o.tax.results.node.
Only Vertex and Avatax are supported.
NOTE:
This method is called for every document line.
Outside Central Invoicing, the calls to the EXTP are always per
document line. So if a Sales Order has 5 order lines,
this method is called 5 times; for each call,
the input parameters can be changed or the call to the EXTP can
be skipped.
In Central Invoicing, the calls to the EXTP can be per invoice
line or per entire invoice. Even if the EXTP call is per entire
invoice, this method is called per invoice line to be able to
change the input parameters of that line. To skip the call to
the EXTP in this case, the output parameter
o.skip.external.tax.provider.call must be set to true at the
moment the variable ›¼Àœlast.invoice.line›¼À• is set in
io.input.arguments.external.tax.provider.
The variable ›¼Àœcall.tax.provider.per.invoice" in
io.input.arguments.external.tax.provider indicates that the call
to EXTP is done per entire invoice.
Pre:    The tax provider interface must be present and this method
cannot be used in combination with method
"Tax.FlexibleFieldsVertex".
Post:   na
Input:  i.tax.interface.provider
- EXTP which is used --> Vertex or Avatax
Output: io.input.arguments.external.tax.provider
- XML or JSON message with input parameters for call to EXTP
This message contains the info of the document header
and 1 document line.
The next fields are informational and are ignored when
changed by this method:
- update tax register
- last invoice line
- call tax provider per invoice
- For Vertex a flexible fields node can be added to the
document line in the XML message, like:
<FlexibleFields>
<FlexibleCodeField fieldId="1">ABC</FlexibleCodeField>
<!--String(40) occurs 0-25 fieldId 1-25 -->
<FlexibleNumericField
fieldId="1">100.0</FlexibleNumericField>
<!--Double occurs 0-10 fieldId 1-10 -->
<FlexibleDateField fieldId="1"></FlexibleDateField>
<!--Date(Format yyyy-mm-ddThh:mm:ss) occurs 0-5
fieldId 1-5 -->
</FlexibleFields>
- For Avatax de "userDefinedFields": [] array in the
JSON message can be populated for document header or
document line like:
"userDefinedFields": [
{
"name": "UDF01",
"value": "Hardware"
},
],
o.skip.external.tax.provider.call
- TRUE or FALSE
o.tax.results.node
- XML message with tax results. To be returned when
o.skip.external.tax.provider.call = TRUE
Return: 0 = OK
<> 0 Otherwise
Examples:
Example of io.input.arguments.external.tax.provider:
Vertex:
<InputExternalTaxProvider
InputMode="SingleLine">
<DocumentHeader>
›¼•  <financial.company>190</financial.company>
›¼•  <transaction.type></transaction.type>
<call.tax.provider.per.invoice>1</call.tax.provider.per.invoice>
›¼•  <invoice.number>0</invoice.number>
›¼•  <invoice.date>1760430405</invoice.date>
›¼•  <business.partner>JEN000002</business.partner>
›¼•  <financial.bp.group>JEN</financial.bp.group>
›¼•  <currency>USD</currency>
›¼•  <DocumentLine>
›¼•  <update.tax.register>2</update.tax.register>
›¼•  <order.number>000000155</order.number>
›¼•  <order.line>10</order.line>
›¼•  <invoice.line>0</invoice.line>
›¼•  <last.invoice.line>0</last.invoice.line>
›¼•  <order.date>1763542578</order.date>
›¼•  <tax.date>0</tax.date>
›¼•  <order.quantity>0</order.quantity>
›¼•  <tax.country>USA</tax.country>
›¼•  <tax.code>JENVT ›¼•  ›¼•  </tax.code>
›¼•  <wh.or.office>AO-US </wh.or.office>
›¼•  <customer.order></customer.order>
›¼•  <delivery.terms> ›¼•  </delivery.terms>
›¼•  <point.of.title.passage>
›¼•  ›¼•  ›¼•  ›¼•  </point.of.title.passage>
›¼•  <sales.service.rental.usage>1</sales.service.rental.usage>
›¼•  <item>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </item>
›¼•  <product></product>
›¼•  <product.class></product.class>
›¼•  <ship.from.country>USA</ship.from.country>
›¼•  <ship.from.zip.code>06101 ›¼•  ›¼•  </ship.from.zip.code>
›¼•  <ship.from.street>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.from.str
eet>
›¼•  <ship.from.state>CT </ship.from.state>
›¼•  <ship.from.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.from.cou
nty>
›¼•  <ship.from.city.name>Hartford
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.from.city.name>
›¼•  <ship.from.geo.code>70030200 1</ship.from.geo.code>
›¼•  <ship.from.latitude>0</ship.from.latitude>
›¼•  <ship.from.longitude>0</ship.from.longitude>
›¼•  <ship.from.iso.code2>US</ship.from.iso.code2>
›¼•  <ship.to.country>USA</ship.to.country>
›¼•  <ship.to.zip.code>79905 ›¼•  ›¼•  </ship.to.zip.code>
›¼•  <ship.to.street>1304 Wandering Way
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.to.street>
›¼•  <ship.to.state>TX </ship.to.state>
›¼•  <ship.to.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.to.count
y>
›¼•  <ship.to.city.name>El Paso
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.to.city.name>
›¼•  <ship.to.geo.code>441410980 </ship.to.geo.code>
›¼•  <ship.to.latitude>0</ship.to.latitude>
›¼•  <ship.to.longitude>0</ship.to.longitude>
›¼•  <ship.to.iso.code2>US</ship.to.iso.code2>
›¼•  <admin.ship.from.country>USA</admin.ship.from.country>
›¼•  <admin.ship.from.zip.code>06101 ›¼•  ›¼•  </admin.ship.from.zip.code>
›¼•  <admin.ship.from.street>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.fr
om.street>
›¼•  <admin.ship.from.state>CT </admin.ship.from.state>
›¼•  <admin.ship.from.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.fr
om.county>
›¼•  <admin.ship.from.city.name>Hartford
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.from.city.name>
›¼•  <admin.ship.from.geo.code>70030200 1</admin.ship.from.geo.code>
›¼•  <admin.ship.from.latitude>0</admin.ship.from.latitude>
›¼•  <admin.ship.from.longitude>0</admin.ship.from.longitude>
›¼•  <admin.ship.from.iso.code2>US</admin.ship.from.iso.code2>
›¼•  <admin.ship.to.country>USA</admin.ship.to.country>
›¼•  <admin.ship.to.zip.code>79905 ›¼•  ›¼•  </admin.ship.to.zip.code>
›¼•  <admin.ship.to.street>1304 Wandering Way
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.to.street>
›¼•  <admin.ship.to.state>TX </admin.ship.to.state>
›¼•  <admin.ship.to.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.to
.county>
›¼•  <admin.ship.to.city.name>El Paso
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.to.city.name>
›¼•  <admin.ship.to.geo.code>441410980 </admin.ship.to.geo.code>
›¼•  <admin.ship.to.latitude>0</admin.ship.to.latitude>
›¼•  <admin.ship.to.longitude>0</admin.ship.to.longitude>
›¼•  <admin.ship.to.iso.code2>US</admin.ship.to.iso.code2>
›¼•  <exempt.certificate>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </exempt.certificate>
›¼•  <exempt.reason> ›¼•  ›¼•  ›¼•  </exempt.reason>
›¼•  <taxable.amount>500</taxable.amount>
›¼•  <tax.included>0</tax.included>
›¼•  <carrier></carrier>
›¼•  <invoice.type>0</invoice.type>
›¼•  </DocumentLine>
</DocumentHeader>
</InputExternalTaxProvider>
Avatax:
{
›¼•  "documentHeader": {
›¼•  ›¼•  "updateTaxRegister": 2,
›¼•  ›¼•  "callTaxProviderPerInvoice": false,
›¼•  ›¼•  "financialCompany": 1190,
›¼•  ›¼•  "transactionType": "",
›¼•  ›¼•  "invoiceNumber": 0,
›¼•  ›¼•  "invoiceDate": "2025-10-14T10:29:20",
›¼•  ›¼•  "businessPartner": "AVA000032",
›¼•  ›¼•  "warehouseOrOffice": "AO-US",
›¼•  ›¼•  "userDefinedFields": [],
›¼•  ›¼•  "documentLines": [
›¼•  ›¼•  ›¼•  {
›¼•  ›¼•  ›¼•  ›¼•  "invoiceLine": 0,
›¼•  ›¼•  ›¼•  ›¼•  "orderNumber": "RH0000050",
›¼•  ›¼•  ›¼•  ›¼•  "orderLine": 10,
›¼•  ›¼•  ›¼•  ›¼•  "lastInvoiceLine": false,
›¼•  ›¼•  ›¼•  ›¼•  "orderDate": "2025-11-19T11:20:35",
›¼•  ›¼•  ›¼•  ›¼•  "taxDate": "1970-01-01T01:00:00",
›¼•  ›¼•  ›¼•  ›¼•  "orderQuantity": 0,
›¼•  ›¼•  ›¼•  ›¼•  "taxCountry": "USA",
›¼•  ›¼•  ›¼•  ›¼•  "taxCode": "JENVT",
›¼•  ›¼•  ›¼•  ›¼•  "customerOrder": "",
›¼•  ›¼•  ›¼•  ›¼•  "deliveryTerms": "",
›¼•  ›¼•  ›¼•  ›¼•  "pointOfTitlePassage": "",
›¼•  ›¼•  ›¼•  ›¼•  "salesServiceRentalUsage": 1,
›¼•  ›¼•  ›¼•  ›¼•  "item": "",
›¼•  ›¼•  ›¼•  ›¼•  "product": "",
›¼•  ›¼•  ›¼•  ›¼•  "productClass": "",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromCountry": "USA",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromZipCode": "92615",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromStreet": "123 main street",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromState": "CA",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromCounty": "",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromCityName": "IRVINE",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromGeoCode": "",
›¼•  ›¼•  ›¼•  ›¼•  "shipFromLatitude": 33.657808,
›¼•  ›¼•  ›¼•  ›¼•  "shipFromLongitude": -117.968489,
›¼•  ›¼•  ›¼•  ›¼•  "shipFromIsoCode2": "US",
›¼•  ›¼•  ›¼•  ›¼•  "shipToCountry": "USA",
›¼•  ›¼•  ›¼•  ›¼•  "shipToZipCode": "92615",
›¼•  ›¼•  ›¼•  ›¼•  "shipToStreet": "123 main street",
›¼•  ›¼•  ›¼•  ›¼•  "shipToState": "CA",
›¼•  ›¼•  ›¼•  ›¼•  "shipToCounty": "",
›¼•  ›¼•  ›¼•  ›¼•  "shipToCityName": "IRVINE",
›¼•  ›¼•  ›¼•  ›¼•  "shipToGeoCode": "",
›¼•  ›¼•  ›¼•  ›¼•  "shipToLatitude": 33.657808,
›¼•  ›¼•  ›¼•  ›¼•  "shipToLongitude": -117.968489,
›¼•  ›¼•  ›¼•  ›¼•  "shipToIsoCode2": "US",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromCountry": "USA",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromZipCode": "92615",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromStreet": "123 main street",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromState": "CA",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromCounty": "",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromCityName": "IRVINE",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromGeoCode": "",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromLatitude": 33.657808,
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromLongitude": -117.968489,
›¼•  ›¼•  ›¼•  ›¼•  "adminShipFromIsoCode2": "US",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToCountry": "USA",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToZipCode": "92615",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToStreet": "123 main street",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToState": "CA",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToCounty": "",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToCityName": "IRVINE",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToGeoCode": "",
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToLatitude": 33.657808,
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToLongitude": -117.968489,
›¼•  ›¼•  ›¼•  ›¼•  "adminShipToIsoCode2": "US",
›¼•  ›¼•  ›¼•  ›¼•  "exemptCertificate": "",
›¼•  ›¼•  ›¼•  ›¼•  "exemptReason": "",
›¼•  ›¼•  ›¼•  ›¼•  "taxableAmount": 1000,
›¼•  ›¼•  ›¼•  ›¼•  "taxIncluded": false,
›¼•  ›¼•  ›¼•  ›¼•  "carrier": "",
›¼•  ›¼•  ›¼•  ›¼•  "invoiceType": 0,
›¼•  ›¼•  ›¼•  ›¼•  "currency": "USD",
›¼•  ›¼•  ›¼•  ›¼•  "userDefinedFields": []
›¼•  ›¼•  ›¼•  }
›¼•  ›¼•  ]
›¼•  }
}
Example of o.tax.results.node:
<TaxCalcResults
FinancialCompany="190"
TaxCountry="USA"
TaxCode="JENVT ›¼•  ›¼•  "
InternalTax="2"
ExternalTax="1"
LocalizationTax="2"
TotalTaxAmount="82.5"
TotalClaimableTaxAmount="82.5"
TotalNonClaimableTaxAmount="0"
TotalTaxPercentage="8.25">
<InternalTaxCalcResults>
›¼•  <TaxSequence
›¼•  TaxSequenceNumber="1"
›¼•  />
</InternalTaxCalcResults>
<ExternalTaxCalcResults
›¼•  NoTax="2"
›¼•  PrimaryJurisdiction="50">
›¼•  <AddressInformation>
›¼•  <ShipFrom
›¼•  ›¼•  Country="USA"
›¼•  ›¼•  ZipCode="06101 ›¼•  ›¼•  "
›¼•  ›¼•  StreetAddress="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  State="CT "
›¼•  ›¼•  County="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  CityName="Hartford
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  GeoCode="70030200 1"
›¼•  />
›¼•  <ShipTo
›¼•  ›¼•  Country="USA"
›¼•  ›¼•  ZipCode="79905 ›¼•  ›¼•  "
›¼•  ›¼•  StreetAddress="1304 Wandering Way
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  State="TX "
›¼•  ›¼•  County="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  CityName="El Paso
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  GeoCode="441410980 "
›¼•  />
›¼•  <AdminShipFrom
›¼•  ›¼•  Country="USA"
›¼•  ›¼•  ZipCode="06101 ›¼•  ›¼•  "
›¼•  ›¼•  StreetAddress="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  State="CT "
›¼•  ›¼•  County="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  CityName="Hartford
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  GeoCode="70030200 1"
›¼•  />
›¼•  <AdminShipTo
›¼•  ›¼•  Country="USA"
›¼•  ›¼•  ZipCode="79905 ›¼•  ›¼•  "
›¼•  ›¼•  StreetAddress="1304 Wandering Way
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  State="TX "
›¼•  ›¼•  County="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  CityName="El Paso
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
›¼•  ›¼•  GeoCode="441410980 "
›¼•  />
›¼•  </AddressInformation>
›¼•  <Country
›¼•  JurisdictionCode=""
›¼•  CertificateNumber=""
›¼•  TaxableAmount="0"
›¼•  NonTaxableAmount="0"
›¼•  ExemptAmount="0"
›¼•  TaxAmount="0"
›¼•  TaxPercentage="0"
›¼•  />
›¼•  <State
›¼•  JurisdictionCode="TEXAS"
›¼•  CertificateNumber=""
›¼•  TaxableAmount="1000"
›¼•  NonTaxableAmount="0"
›¼•  ExemptAmount="0"
›¼•  TaxAmount="62.5"
›¼•  TaxPercentage="6.25"
›¼•  />
›¼•  <County
›¼•  JurisdictionCode="EL PASO"
›¼•  CertificateNumber=""
›¼•  TaxableAmount="1000"
›¼•  NonTaxableAmount="0"
›¼•  ExemptAmount="0"
›¼•  TaxAmount="5"
›¼•  TaxPercentage="0.5"
›¼•  />
›¼•  <City
›¼•  JurisdictionCode="EL PASO"
›¼•  CertificateNumber=""
›¼•  TaxableAmount="1000"
›¼•  NonTaxableAmount="0"
›¼•  ExemptAmount="0"
›¼•  TaxAmount="10"
›¼•  TaxPercentage="1"
›¼•  />
›¼•  <District
›¼•  JurisdictionCode="EL PASO CITY TRANSIT DEPARTMEN"
›¼•  CertificateNumber=""
›¼•  TaxableAmount="1000"
›¼•  NonTaxableAmount="0"
›¼•  ExemptAmount="0"
›¼•  TaxAmount="5"
›¼•  TaxPercentage="0.5"
›¼•  />
</ExternalTaxCalcResults>
<LocalizationTaxCalcResults>
›¼•  <TaxResult>
›¼•  <TaxSequence/>
›¼•  </TaxResult>
</LocalizationTaxCalcResults>
</TaxCalcResults>
```
