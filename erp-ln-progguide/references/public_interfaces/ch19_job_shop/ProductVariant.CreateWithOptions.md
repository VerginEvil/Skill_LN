# ProductVariant.CreateWithOptions

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 670-674

```baan
DLL:   tiextpcfapi
This function is available from     2025.03 (KB3540107  ).
Syntax: long ProductVariant.CreateWithOptions(
domain  tcitem           iGenericItem,
domain  tcreft           iReferenceType,
long             iItemConfigurationStructure,
long             iProcessingOptions,
ref     domain  tccpva           oCreatedProductVariant,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to create a Product Variant
with a set of sales options. The set of options created
will serve as input for (background) processing on
CPQ. Therefore, this function will only work for items that
have the setting Configured by CPQ Configurator active in
session CPQ Configurator Settings (tipcf0111m000).
This function makes use of a Processing Option Set, which
can be created via a call to ProcessingOptionSet.Create(),
and cleaned up after use, via a call to
ProcessingOptionSet.Delete().
Item Configuration Structure can be created by using XML
related functions xmlNewNode(), xmlNewDataElement(),
xmlSetAttribute(),etc.
Example: Create iItemConfigurationStructure Node.
A car with color red(r) and 1 seat of color brown(b).
<ItemConfiguration>
<ConfigurationComponent>
<Name>Car</Name>
<Sequence>1</Sequence>
<ParentComponent></ParentComponent>
<Feature>
<Sequence>1</Sequence>
<OptionClass type="StringType">Color
</OptionClass>
<OptionClassDescription/>
<Option>r</Option>
<OptionDescription/>
<Note/>
</Feature>
<Feature>
<Sequence>2</Sequence>
<OptionClass type="StringType">
NumberOfSeats</OptionClass>
<OptionClassDescription/>
<Option>1</Option>
<OptionDescription/>
<Note/>
</Feature>
</ConfigurationComponent>
<ConfigurationComponent>
<Name>Seat</Name>
<Sequence>2</Sequence>
<ParentComponent>1</ParentComponent>
<Feature>
<Sequence>1</Sequence>
<OptionClass type="StringType">Color
</OptionClass>
<OptionClassDescription/>
<Option>b</Option>
<OptionDescription/>
<Note/>
</Feature>
</ConfigurationComponent>
</ItemConfiguration>
Code Snippet:
***************************************************************
long            iItemConfigurationStructure
long            cc.id
long            req.id
iItemConfigurationStructure = xmlNewNode("ItemConfiguration")
|* Configuration Component 1
cc.id = xmlNewNode("ConfigurationComponent",XML_ELEMENT,
iItemConfigurationStructure)
req.id = xmlNewDataElement("Name","Car",cc.id)
req.id = xmlNewDataElement("Sequence","1",cc.id)
req.id = xmlNewNode("ParentComponent",XML_ELEMENT,cc.id)
|* Feature 1
add.feature.to.item.configuration.structure(
cc.id,
"1",
"Color",
"",
"r",
"",
"")
|* Feature 2
add.feature.to.item.configuration.structure(
cc.id,
"2",
"NumberOfSeats",
"",
"1",
"",
"")
|* Configuration Component 2
cc.id = xmlNewNode("ConfigurationComponent",XML_ELEMENT,
iItemConfigurationStructure)
req.id = xmlNewDataElement("Name","Seat",cc.id)
req.id = xmlNewDataElement("Sequence","2",cc.id)
req.id = xmlNewDataElement("ParentComponent","1",cc.id)
|* Feature 1
add.feature.to.item.configuration.structure(
cc.id,
"1",
"Color",
"",
"b",
"",
"")
***************************************************************
function void add.feature.to.item.configuration.structure(
long            i.cc.id,
string          i.seq(3),
string          i.opt.cls(15),
string          i.opt.cls.dsca(30),
string          i.option(15),
string          i.opt.dsca(30),
string          i.note(256))
{
long            req.id
long            feature
long            opt.cls
feature = xmlNewNode("Feature",XML_ELEMENT,i.cc.id)
req.id = xmlNewDataElement("Sequence",i.seq,feature)
opt.cls = xmlNewDataElement("OptionClass",i.opt.cls,
feature)
req.id = xmlSetAttribute(opt.cls,"type","StringType")
req.id = xmlNewDataElement("OptionClassDescription",
i.opt.cls.dsca,feature)
req.id = xmlNewDataElement("Option",i.option,feature)
req.id = xmlNewDataElement("OptionDescription",
i.opt.dsca,feature)
req.id = xmlNewDataElement("Note",i.note,feature)
}
***************************************************************
Pre:    db.retry point must be set.
Post:   Transaction must be aborted or committed.
Input:  iGenericItem                          - Generic Item. (Mandatory).
iReferenceType                                - Reference Type of Product Variant
to be created.
iItemConfigurationStructure
-                                               XML Structure with Sales Options
for Product Variant to be created.
iProcessingOptionSet                          - A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
If 0, then default values are
applied (Optional).
Processing Options are used for detailed specification of product
variant settings.
Order                                         - Sales Order Number of Item.
OrderPosition                                 - Sales Order Position of Item.
AlternativeSalesQuotation
-                                               Alternative Sales Quotation of
Item.
BusinessPartner                               - Business Partner of Sales Order.
SalesCurrency                                 - Sales Currency of Sales Order.
Quantity                                      - Quantity Ordered of Item.
SalesPriceUnit                                - Sales Price Unit of Sales Order.
ShipFromWarehouse                             - Warehouse from where the Item
will be shipped.
ShipToAddress                                 - Address to which the Item will
be shipped.
ReferenceDate                                 - Reference Date of Sales Order.
Processing Options which are not provided will be filled with default
value.
NAME                            TYPE                    DEFAULT
Order                           domain  tcorno          ""
OrderPosition                   domain  tcpono          0
AlternativeSalesQuotation       domain  tcpono          0
BusinessPartner                 domain  tccom.bpid      ""
SalesCurrency                   domain  tcccur          ""
Quantity                        domain  tcqsl1          0.0
SalesPriceUnit                  domain  tccuni          ""
ShipFromWarehouse               domain  tccwar          ""
ShipToAddress                   domain  tccom.cadr      ""
ReferenceDate                   domain  tiutcs          0
Output: oCreatedProductVariant                - The created Product Variant.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Product Variant is created.
<> 0                                          - Otherwise.
```
