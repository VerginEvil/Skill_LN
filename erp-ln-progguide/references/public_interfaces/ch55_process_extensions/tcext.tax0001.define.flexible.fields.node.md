# tcext.tax0001.define.flexible.fields.node

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2273-2278

```baan
Syntax: long tcext.tax0001.define.flexible.fields.node(
domain  tcmcs.xml        i.input.arguments.node,
ref     domain  tcmcs.xml        o.flexible.fields.node )
Usage:        Expl:
Use this method to define a 'flexible fields node' to be
added to the main xml which is used by the External Tax Provider
(Vertex). This 'flexible fields node' will be used in Vertex to
customize the tax determination.
NOTE:   This process extension will be called when the external tax
is determined at moments which are defined by the logic in LN.
Keep in mind when defining logic in the extension
and Vertex that you do not have control over the moment
the tax will be determined.
Example: Business Partner Balances inclusive tax gives
problems when tax determination becomes dependent on a
value change of a field other than known in LN Logic.
Pre:    na
Post:   na
Input:  i.input.arguments.node                - xml node with all the fields used to
compile the xml message to the
External Tax Provider.
Output: o.flexible.fields.node                - xml node with flexible fields
example i.input.arguments.node:
<InputExternalTaxProvider
InputMode="SingleLine">
<DocumentHeader>
<financial.company>300</financial.company>
<!                                      --domain is: tcncmp -->
<transaction.type>SLS</transaction.type>
<!                                      --domain is: tcgld.ttyp -->
<invoice.number>123456</invoice.number>
<!                                      --domain is: tcinvn -->
<invoice.date>1623669699</invoice.date>
<!                                      --domain is: tcdate -->
<business.partner>RLX_BP</business.partner>
<!                                      --domain is: tccom.bpid -->
<financial.bp.group>AAA</financial.bp.group>
<!                                      --domain is: tcficu -->
<currency>NLG</currency>
<!                                      --domain is: tcccur -->
<DocumentLine>
<update.tax.register>2</update.tax.register>
<!                                              --domain is: tcyesno -->
<order.number>SLS000075</order.number>
<!                                              --domain is: tcorno -->
<order.line>10</order.line>
<!                                              --domain is: tcpono -->
<invoice.line>10</invoice.line>
<!                                              --domain is: tcmcs.long -->
<last.invoice.line>0</last.invoice.line>
<!                                              -- boolean -->
<order.date>1623669699</order.date>
<!                                              --domain is: tcdate -->
<tax.date>1623669699</tax.date>
<!                                              --domain is: tcdate -->
<order.quantity>10.22</order.quantity>
<!                                              --domain is: tcqdhc -->
<tax.country>NLD</tax.country>
<!                                              --domain is: tcccty -->
<tax.code>HIGH</tax.code>
<!                                              --domain is: tccvat -->
<wh.or.office>ABCDEF</wh.or.office>
<!                                              --domain is: tccwoc -->
<customer.order>ABCDEFGHIJK</customer.order>
<!                                              --domain is: tcmcs.st30m -->
<delivery.terms>DEL</delivery.terms>
<!                                              --domain is: tccdec -->
<point.of.title.passage>ABCDEFGHI</point.of.title.passage>
<!                                              --domain is: tcptpa -->
<sales.service.rental.usage>1</sales.service.rental.usage>
<!                                              --domain is: tctxin -->
<item>         ITEM                                      -SALES</item>
<!                                              --domain is: tcitem -->
<product>PRODUCT A</product>
<!                                              --domain is: tcpcat -->
<product.class>PRODUCT CLASS</product.class>
<!                                              --domain is: tcpcat -->
<ship.from.country>NLD</ship.from.country>
<!                                              --domain is: tcccty -->
<ship.from.zip.code>3904 KT</ship.from.zip.code>
<!                                              --domain is: tcpstc -->
<ship.from.street>Green street</ship.from.street>
<!                                              --domain is: tcnamc -->
<ship.from.state>UTR</ship.from.state>
<!                                              --domain is: tcmcs.cste -->
<ship.from.county>The Netherlands</ship.from.county>
<!                                              --domain is: tcname -->
<ship.from.city.name>Ede</ship.from.city.name>
<!                                              --domain is: tcdsca -->
<ship.from.geo.code>GEOCODE</ship.from.geo.code>
<!                                              --domain is: tcgeoc -->
<ship.from.latitude>123.123456</ship.from.latitude>
<!                                              --domain is: tcglat -->
<ship.from.longitude>123.654321</ship.from.longitude>
<!                                              --domain is: tcglon -->
<ship.from.iso.code2>NL</ship.from.iso.code2>
<!                                              --domain is: tcict2 -->
<ship.to.country>NLD</ship.to.country>
<!                                              --domain is: tcccty -->
<ship.to.zip.code>2941BL</ship.to.zip.code>
<!                                              --domain is: tcpstc -->
<ship.to.street>Kerkweg</ship.to.street>
<!                                              --domain is: tcnamc -->
<ship.to.state>ZH</ship.to.state>
<!                                              --domain is: tcmcs.cste -->
<ship.to.county>County</ship.to.county>
<!                                              --domain is: tcname -->
<ship.to.city.name>Nederlek</ship.to.city.name>
<!                                              --domain is: tcdsca -->
<ship.to.geo.code>ABC</ship.to.geo.code>
<!                                              --domain is: tcgeoc -->
<ship.to.latitude>123.123456</ship.to.latitude>
<!                                              --domain is: tcglat -->
<ship.to.longitude>123.654321</ship.to.longitude>
<!                                              --domain is: tcglon -->
<ship.to.iso.code2>NL</ship.to.iso.code2>
<!                                              --domain is: tcict2 -->
<admin.ship.from.country>GER</admin.ship.from.country>
<!                                              --domain is: tcccty -->
<admin.ship.from.zip.code>ZIP123</admin.ship.from.zip.code>
<!                                              --domain is: tcpstc -->
<admin.ship.from.street>Street</admin.ship.from.street>
<!                                              --domain is: tcnamc -->
<admin.ship.from.state>OB</admin.ship.from.state>
<!                                              --domain is: tcmcs.cste -->
<admin.ship.from.county>County</admin.ship.from.county>
<!                                              --domain is: tcname -->
<admin.ship.from.city.name>City
Name</admin.ship.from.city.name>
<!                                              --domain is: tcdsca -->
<admin.ship.from.geo.code>GEO</admin.ship.from.geo.code>
<!                                              --domain is: tcgoec -->
<admin.ship.from.latitude>123.123456</admin.ship.from.latitude>
<!                                              --domain is: tcglat -->
<admin.ship.from.longitude>123.654321</admin.ship.from.longitude>
<!                                              --domain is: tcglon -->
<admin.ship.from.iso.code2>IN</admin.ship.from.iso.code2>
<!                                              --domain is: tcict2 -->
<admin.ship.to.country>IND</admin.ship.to.country>
<!                                              --domain is: tcccty -->
<admin.ship.to.zip.code>ZIP1234</admin.ship.to.zip.code>
<!                                              --domain is: tcpstc -->
<admin.ship.to.street>Street 34</admin.ship.to.street>
<!                                              --domain is: tcnamc -->
<admin.ship.to.state>AP</admin.ship.to.state>
<!                                              --domain is: tcmcs.cste -->
<admin.ship.to.county>County Name</admin.ship.to.county>
<!                                              --domain is: tcname -->
<admin.ship.to.city.name>City name
2</admin.ship.to.city.name>
<!                                              --domain is: tcdsca -->
<admin.ship.to.geo.code>GEO</admin.ship.to.geo.code>
<!                                              --domain is: tcgoec -->
<admin.ship.to.latitude>456.123456</admin.ship.to.latitude>
<!                                              --domain is: tcglat -->
<admin.ship.to.longitude>123.654321</admin.ship.to.longitude>
<!                                              --domain is: tcglon -->
<admin.ship.to.iso.code2>RU</admin.ship.to.iso.code2>
<!                                              --domain is: tcict2 -->
<exempt.certificate>exemption
certificate</exempt.certificate>
<!                                              --domain is: tcfovn -->
<exempt.reason>REASON</exempt.reason>
<!                                              --domain is: tccdis -->
<taxable.amount>123.78</taxable.amount>
<!                                              --domain is: tcamnt -->
<tax.included>1</tax.included>
<!                                              --boolean -->
<carrier>ABC</carrier>
<!                                              --domain is: tccrfw -->
<invoice.type>2</invoice.type>
<!                                              --domain is: tcinvt -->
</DocumentLine>
</DocumentHeader>
</InputExternalTaxProvider>
example flexible.fields.node:
<FlexibleFields>
<FlexibleCodeField fieldId="1">ABC</FlexibleCodeField>
<!                                      --String(40) occurs 0-25 fieldId 1-25 -->
<FlexibleNumericField fieldId="1">100.0</FlexibleNumericField>
<!                                      --Double occurs 0-10 fieldId 1-10 -->
<FlexibleDateField fieldId="1"></FlexibleDateField>
<!                                      --Date(Format yyyy-mm-ddThh:mm:ss) occurs 0-5 fieldId 1-
5       -->
</FlexibleFields>
example program:
domain  tcmcs.xml       document.line.node
domain  tcmcs.xml       flex.field.node
domain  tccfrw          carrier
long            ret.val
ret.val = 0
o.flexible.fields.node = 0
document.line.node = xmlFindFirst("DocumentLine", i.input.argument.node)
carrier = xmlDataElement$(document.line.node, "carrier")
if not isspace(carrier) then
|* top node     :FlexibleFields
o.flexible.fields.node = xmlNewNode("FlexibleFields")
|* data element :FlexibleCodeField
flex.field.node = xmlNewDataElement("FlexibleCodeField",
carrier,
o.flexible.fields.node)
|* Attribute fieldID
ret.val = xmlSetAttribute(
flex.field.node,
"fieldId",
10)
endif
return(0)
Return: 0                                     - Succes
<> 0                                          - When an error occurs in defining
o.flexible.fields.node
```

## Process Extensions for TaxDeclaration

The following process extension(s) is/are available: TaxDeclaration.GetXMLTextTagContent
