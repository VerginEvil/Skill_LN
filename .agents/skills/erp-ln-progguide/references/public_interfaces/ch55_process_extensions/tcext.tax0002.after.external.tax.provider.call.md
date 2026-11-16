# tcext.tax0002.after.external.tax.provider.call

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2289-2294

```baan
Syntax: long tcext.tax0002.after.external.tax.provider.call(
domain  tcapi.prov       i.tax.interface.provider,
long             i.input.arguments.external.tax.provider,
domain  tcmcs.xml        i.tax.results.node )
Usage:        Expl:
This method is called after the External Tax Provider (EXTP)
has been called. It can be used to e.g. log the data sent to
EXTP or to log the tax results.
The i.input.arguments.external.tax.provider is for Vertex an
XML document; for Avatax, it is a JSON message.
Only Vertex and Avatax are supported.
Pre:    The tax provider interface must be present
Post:   na
Input:  i.tax.interface.provider
- EXTP which is used --> Vertex or Avatax
i.input.arguments.external.tax.provider
- XML or JSON message with input parameters.
Message contains document header data plus the
document line data from 1 or more lines
i.tax.results.node
- XML message with tax results
Result node contains tax data from 1 or more lines
Output: na
Return: 0 = ok
<> 0 otherwise
Examples:
Example of i.input.arguments.external.tax.provider:
Vertex:
<InputExternalTaxProvider>
<DocumentHeader>
›¼•  <financial.company>190</financial.company>
›¼•  <transaction.type></transaction.type>
›¼•  <invoice.number>0</invoice.number>
›¼•  <invoice.date>1760430405</invoice.date>
›¼•  <business.partner>JEN000002</business.partner>
›¼•  <financial.bp.group>JEN</financial.bp.group>
›¼•  <currency>USD</currency>
›¼•  <DocumentLines>
›¼•  <DocumentLine>
›¼•  ›¼•  <update.tax.register>2</update.tax.register>
›¼•  ›¼•  <order.number>000000155</order.number>
›¼•  ›¼•  <order.line>10</order.line>
›¼•  ›¼•  <invoice.line>0</invoice.line>
›¼•  ›¼•  <last.invoice.line>0</last.invoice.line>
›¼•  ›¼•  <order.date>1763542578</order.date>
›¼•  ›¼•  <tax.date>0</tax.date>
›¼•  ›¼•  <order.quantity>0</order.quantity>
›¼•  ›¼•  <tax.country>USA</tax.country>
›¼•  ›¼•  <tax.code>JENVT ›¼•  ›¼•  </tax.code>
›¼•  ›¼•  <wh.or.office>AO-US </wh.or.office>
›¼•  ›¼•  <customer.order></customer.order>
›¼•  ›¼•  <delivery.terms> ›¼•  </delivery.terms>
›¼•  ›¼•  <point.of.title.passage>
›¼•  ›¼•  ›¼•  ›¼•  </point.of.title.passage>
›¼•  ›¼•  <sales.service.rental.usage>1</sales.service.rental.usage>
›¼•  ›¼•  <item>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </item>
›¼•  ›¼•  <product></product>
›¼•  ›¼•  <product.class></product.class>
›¼•  ›¼•  <ship.from.country>USA</ship.from.country>
›¼•  ›¼•  <ship.from.zip.code>06101 ›¼•  ›¼•  </ship.from.zip.code>
›¼•  ›¼•  <ship.from.street>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.from.str
eet>
›¼•  ›¼•  <ship.from.state>CT </ship.from.state>
›¼•  ›¼•  <ship.from.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.from.cou
nty>
›¼•  ›¼•  <ship.from.city.name>Hartford
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.from.city.name>
›¼•  ›¼•  <ship.from.geo.code>70030200 1</ship.from.geo.code>
›¼•  ›¼•  <ship.from.latitude>0</ship.from.latitude>
›¼•  ›¼•  <ship.from.longitude>0</ship.from.longitude>
›¼•  ›¼•  <ship.from.iso.code2>US</ship.from.iso.code2>
›¼•  ›¼•  <ship.to.country>USA</ship.to.country>
›¼•  ›¼•  <ship.to.zip.code>79905 ›¼•  ›¼•  </ship.to.zip.code>
›¼•  ›¼•  <ship.to.street>1304 Wandering Way
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.to.street>
›¼•  ›¼•  <ship.to.state>TX </ship.to.state>
›¼•  ›¼•  <ship.to.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.to.count
y>
›¼•  ›¼•  <ship.to.city.name>El Paso
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </ship.to.city.name>
›¼•  ›¼•  <ship.to.geo.code>441410980 </ship.to.geo.code>
›¼•  ›¼•  <ship.to.latitude>0</ship.to.latitude>
›¼•  ›¼•  <ship.to.longitude>0</ship.to.longitude>
›¼•  ›¼•  <ship.to.iso.code2>US</ship.to.iso.code2>
›¼•  ›¼•  <admin.ship.from.country>USA</admin.ship.from.country>
›¼•  ›¼•  <admin.ship.from.zip.code>06101
›¼•  ›¼•  </admin.ship.from.zip.code>
›¼•  ›¼•  <admin.ship.from.street>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.fr
om.street>
›¼•  ›¼•  <admin.ship.from.state>CT </admin.ship.from.state>
›¼•  ›¼•  <admin.ship.from.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.fr
om.county>
›¼•  ›¼•  <admin.ship.from.city.name>Hartford
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.from.city.name>
›¼•  ›¼•  <admin.ship.from.geo.code>70030200 1</admin.ship.from.geo.code>
›¼•  ›¼•  <admin.ship.from.latitude>0</admin.ship.from.latitude>
›¼•  ›¼•  <admin.ship.from.longitude>0</admin.ship.from.longitude>
›¼•  ›¼•  <admin.ship.from.iso.code2>US</admin.ship.from.iso.code2>
›¼•  ›¼•  <admin.ship.to.country>USA</admin.ship.to.country>
›¼•  ›¼•  <admin.ship.to.zip.code>79905
›¼•  ›¼•  </admin.ship.to.zip.code>
›¼•  ›¼•  <admin.ship.to.street>1304 Wandering Way
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.to.street>
›¼•  ›¼•  <admin.ship.to.state>TX </admin.ship.to.state>
›¼•  ›¼•  <admin.ship.to.county>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.to
.county>
›¼•  ›¼•  <admin.ship.to.city.name>El Paso
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </admin.ship.to.city.name>
›¼•  ›¼•  <admin.ship.to.geo.code>441410980 </admin.ship.to.geo.code>
›¼•  ›¼•  <admin.ship.to.latitude>0</admin.ship.to.latitude>
›¼•  ›¼•  <admin.ship.to.longitude>0</admin.ship.to.longitude>
›¼•  ›¼•  <admin.ship.to.iso.code2>US</admin.ship.to.iso.code2>
›¼•  ›¼•  <exempt.certificate>
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  </exempt.certificate>
›¼•  ›¼•  <exempt.reason> ›¼•  ›¼•  ›¼•  </exempt.reason>
›¼•  ›¼•  <taxable.amount>500</taxable.amount>
›¼•  ›¼•  <tax.included>0</tax.included>
›¼•  ›¼•  <carrier></carrier>
›¼•  ›¼•  <invoice.type>0</invoice.type>
›¼•  </DocumentLine>
›¼•  </DocumentLines>
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
Example of i.tax.results.node:
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
StreetAddress="
›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  ›¼•  "
State="CT "
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
