# ProductVariant.CreateWithFeaturesOptions

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 667-670

```baan
DLL:   tiextpcfapi
This function is available from     2026.09 (KB3626749  ).
Syntax: long ProductVariant.CreateWithFeaturesOptions(
domain  tcitem           iGenericItem,
domain  tcreft           iReferenceType,
long             iItemConfigurationStructure,
long             iProcessingOptionSet,
ref     domain  tccpva           oCreatedProductVariant,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to create a Product Variant with
a set of features/options. This function will work for items
that do not have the setting Configured by CPQ Configurator
active in session CPQ Configurator Settings (tipcf0111m000) and
items which are not enabled for CPQ.
This function makes use of a Processing Option Set, which can be
created via a call to ProcessingOptionSet.Create(), and cleaned
up after use, via a call to ProcessingOptionSet.Delete(). The
Item Configuration Structure can be created by using XML related
functions xmlNewNode(), xmlNewDataElement(),xmlSetAttribute(),
etc.
Pre:    db.retry point must be set.
Post:   Transaction must be aborted or committed.
Input:  iGenericItem
-                               Generic Item. (Mandatory).
iReferenceType
-                               Reference Type of Product Variant to be created.
Standard reference type will be used as default value
if the input value is empty.
iItemConfigurationStructure
-                               XML Structure with features and options for Product
Variant to be created.
iProcessingOptionSet
-                               Processing Option Set (Optional). If 0, then user
default/session default values are applied.
A Processing Option Set can be created via a call to
ProcessingOptionSet.Create() in DLL tcextextapi. After
the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options are used for detailed specification of product
variant settings.
Order                                         - Sales Order Number of Item.
OrderPosition                                 - Sales Order Position of Item.
AlternativeSalesQuotation
-                                               Alternative Sales Quotation of
Item.
BusinessPartner                               - Business Partner of Sales Order.
SalesCurrency                                 - Sales Currency of Sales Order.
ReferenceDate                                 - Reference Date of Sales Order.
Processing Options which are not provided will be filled with default
value.
NAME                            TYPE                    DEFAULT
Order                           domain  tcorno          ""
OrderPosition                   domain  tcpono          0
AlternativeSalesQuotation       domain  tcpono          0
BusinessPartner                 domain  tccom.bpid      ""
SalesCurrency                   domain  tcccur          ""
ReferenceDate                   domain  tiutcs          0
XML Structure for creating variant for Non                      -cpq:
<ItemConfiguration>
<ConfigurationComponent>
<Sequence>1</Sequence>
<ParentComponent/>      |* This is empty for TOP Item
<ItemID>
<ID>ITEM_CODE_001</ID>
</ItemID>
<Note>Optional text note for this component</Note>
<UnitPrice>
<Amount>150.00</Amount>
</UnitPrice>
<Feature>
<OptionClass type="StringType">FEATURE_CODE</OptionClass>
<!                                  -- type: "NumericType", "IndicatorType", or "StringType" -->
<Sequence>1</Sequence>
<OptionClassDescription>Feature
Description</OptionClassDescription>
<Option>OPTION_VALUE</Option>
<OptionDescription>Option Description</OptionDescription>
<Note>Optional feature                                  -level note text</Note>
</Feature>
<Feature>
<OptionClass type="NumericType">WEIGHT</OptionClass>
<Sequence>2</Sequence>
<OptionClassDescription>Weight</OptionClassDescription>
<Option>25.5</Option>
<OptionDescription>25.5 kg</OptionDescription>
</Feature>
<!                              -- ... more Feature siblings ... -->
</ConfigurationComponent>
<!                          -- Subsequent ConfigurationComponents = child/sub items -->
<ConfigurationComponent>
<Sequence>2</Sequence>
<ParentComponent>1</ParentComponent>  <!                              -- Sequence nr of parent -
-      >
<ItemID>
<ID>CHILD_ITEM_001</ID>
</ItemID>
<Note>Optional note</Note>
<Feature>
<OptionClass type="StringType">COLOR</OptionClass>
<Sequence>1</Sequence>
<OptionClassDescription>Color</OptionClassDescription>
<Option>RED</Option>
<OptionDescription>Red</OptionDescription>
</Feature>
<!                              -- ... more Features ... -->
</ConfigurationComponent>
<!                          -- Deeper nesting via ParentComponent referencing any prior Sequence
--      >
<ConfigurationComponent>
<Sequence>3</Sequence>
<ParentComponent>2</ParentComponent>  <!                              -- Child of sequence 2 -->
<ItemID>
<ID>SUB_CHILD_ITEM</ID>
</ItemID>
<Feature>
<!                                  -- ... -->
</Feature>
</ConfigurationComponent>
<!                          -- ... more ConfigurationComponent siblings ... -->
</ItemConfiguration>
Code Snippet:
long            iItemConfigurationStructure
long            cc.id
long            req.id
long            item.id
long            unit.price.id
iItemConfigurationStructure = xmlNewNode("ItemConfiguration")
|* Configuration Component 1
cc.id = xmlNewNode("ConfigurationComponent",XML_ELEMENT,
iItemConfigurationStructure)
req.id = xmlNewDataElement("Sequence","1",cc.id)
req.id = xmlNewNode("ParentComponent",XML_ELEMENT,cc.id)
item.id = xmlNewNode("ItemID",XML_ELEMENT, cc.id)
req.id = xmlNewDataElement("ID"," ITEM_CODE_001",item.id)
req.id = xmlNewDataElement("Note"," ",cc.id)
unit.price.id = xmlNewNode("UnitPrice ",XML_ELEMENT,cc.id)
req.id = xmlNewDataElement("Amount",.150.00.,unit.price.id)
|* Feature 1
add.feature.to.item.configuration.structure(
cc.id,
"1",
" WEIGHT ",
"",
"25.5 kg",
"",
"")
|* For subsequent features, the argument sequence has to be
|* send accordingly which is 2nd argument in above function.
|* Configuration Component 2
cc.id = xmlNewNode("ConfigurationComponent",XML_ELEMENT,
iItemConfigurationStructure)
req.id = xmlNewDataElement("Sequence","2",cc.id)
req.id = xmlNewDataElement("ParentComponent","1",cc.id)
item.id = xmlNewNode("ItemID",XML_ELEMENT, cc.id)
req.id = xmlNewDataElement("ID"," CHILD_ITEM_001",item.id)
req.id = xmlNewDataElement("Note"," ",cc.id)
|* Feature 1
add.feature.to.item.configuration.structure(
cc.id,
"1",
"COLOR",
"",
"RED",
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
Output:
oCreatedProductVariant                        - Product Variant Created
Return:
0                                     - Success. Product Variant Created with Features
<> 0
-                                       Error occurred during creating Product Variant.
```
