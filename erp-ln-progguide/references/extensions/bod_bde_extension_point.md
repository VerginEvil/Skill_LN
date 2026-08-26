# BOD or BDE extension point

A BOD or BDE extension is used to publish additional fields with a BOD or BDE. You can also process additional fields that are part of an inbound BOD or BDE.

For example:

- `PurchaseOrderBOD`. To include all CDFs of the Purchase Order in the

- `PurchaseOrderBOD`. To include some standard Business Partner fields in the

- To update an own table with fields in an incoming BDE.

Those fields are added to or processed from the `UserArea` in the BOD or BDE. A BOD or BDE can have `UserAreas` on different levels. Each component, which is a part in the hierarchical structure of the BOD or BDE, can have a `UserArea`. These are examples of components: • `PurchaseOrderBOD` • `PurchaseOrderBOD.PurchaseOrderLine` • `PurchaseOrderBOD.PurchaseOrderLine.PurchaseOrderSchedule` • `PurchaseOrderBOD.PurchaseOrderLine.PurchaseOrderSchedule.ReceivedQuantityDistribution`

For the BOD or BDE extension point you have two extension types:

- BOD or BDE

- Component Extension

This diagram shows the position of the BOD or BDE extension:

## BOD or BDE

The hooks you can define on BOD or BDE level are supporting hooks for the hooks on Component level.

This table shows the available hooks:

Name Signature

Declarations

Functions

## Declarations hook

Use this hook to declare tables and variables that must be globally available in all hooks of the extension. Also, the references to include files and DLLs that are used by the extension must be coded in this hook with `#include` and `#pragma`.

Tables that are used in the field mappings of the BOD or BDE Components, are implicitly declared. Adding them to this hook is not required.

Example:

```baan
#include        <bic_text>
table   txprc100          |* Prices
```

BOD/BDE BOD/BED BOD/BDE BOD/BDE LN tables LN tables
BOD/BED
processor
BOD/BDE
implementation
BOD/BDE
Extension
BOD/BDE
document implementation Extension processor document

```baan
string  date.string(14)
boolean retb
#pragma used dll "otxprcdll0001"
```

## Functions hook

Use this hook to code (common) functions to use in the other hooks of the BOD or BDE extension. This helps you in reusing code and to keep the other hooks small and clear.

Example:

```baan
function string format.date(long i.date)
{
return(utc.to.iso(i.date, UTC_ISO_DIFF))
}
```

## Component Extension

With the properties and hooks defined for the extension type Component Extension, you can include fields from the linked tables and other fields to the UserArea of the Component. Note that you can only add fields to the UserArea and not to other structures of the BOD or BDE XML. Components that have no UserArea cannot be extended.

When you add a Component Extension, you can select one of the Components that have a UserArea.

This table shows the available properties:

Name

All Customer Defined Fields

Field List

This table shows the available hooks:

| Name | Signature |
|---|---|
| Add Calculated Fields | Not applicable. The lines of code you add in this hook are included in a function that is generated in the Extension Script. |

Process Inbound User Area Not applicable. The lines of code you add in this hook are included in a function that is generated in the Extension Script.

## All Customer Defined Fields property

If you select this property, all CDFs of the tables, that are linked to the Component, are included in the UserArea of the Component in the BOD or BDE. Click Details in the `Field List` property to see which tables are linked to the Component. If you do not select this property, you can select individual CDFs in the `Field List` property.

If you select all CDFs by selecting this property, the CDF is added to the UserArea with the technical field name as element name. For example `tdpur400.cdf_name`. For CDFs of type `List`, the constant name is used as value. You can deviate from those defaults. For example, by choosing a different element name or publishing the enum value instead of the constant. In this case, do not select all CDFs, but select the CDFs individually in the `Field List`. Within the `Field List` you can specify the deviations.

## Field List property

In the `Field List` property, you can select all fields to add to the UserArea. Click Details in the property value cell to show the list of available fields. Select the ones to add to the UserArea. If you did not select the All Customer Defined Fields check box, you also can select the CDFs in the list.

For each selected field two additional properties are available:

Name

Element Name

Use Constant Name

### Element Name property

You can specify the Element Name to be used for the field in the BOD or BDE XML. If you do not specify the Element name, the technical field name is used.

### Use Constant Name property

This property is available for enumerated fields only. If you select this property, the constant name of the enum is published in the BOD or BDE XML. For example, for the Sales Order status field the string `closed` is published. If you do not select this property, the numeric value is published.

## Add Calculated Fields hook

Use this hook to add additional fields to the UserArea. Examples:

- A concatenation of table fields

- Table fields that are not part of the table(s) which is/are linked to the component

- A result that is returned by calling a DLL function

- An XML tree built up with data from any source

The lines of code in this hook are included in the function that the runtime BOD or BDE processor calls to fill the UserArea. The structure of this generated function is:

```baan
function extern long get.additional.elements(
const   stringi.component,
ref     long        o.xml)
{
...
on case i.component
case "component1":
|* Generated code for selected fields for component1
|* Hook code for Add Calculated Fields for component1
break
case "component2":
|* Generated code for selected fields for component2
|* Hook code for Add Calculated Fields for component2
break
default:
break
endcase
...
return(0)
}
```

In the Add Calculated Fields hook you can use these macros to add fields to the UserArea:

- addValue

- addAmountValue

- addCodeValue

- addMasterDataReferenceValue

- addQuantityValue

- addDescription

- addEffectiveTimePeriod

- addXML

Note: Those macros only work in the hook itself. You cannot use them in a function you call from the hook.

In the Add Calculated Fields hook you cannot use directly the table fields of the linked table(s) of the Component. The actual values of the table fields are undefined. With some additional macros, you have access to the identifying attributes of the current Component and with those attributes you can query the database to get additional values. These macros are available:

- (for each component with a UserArea) `getTableIdentifiers.<Component>`

• `getIdentifierValueFromIdentifierStructure` • `getIdentifierDataTypeFromIdentifierStructure`

### addValue macro

Use this macro to add a simple value to the UserArea. A simple value has a Name, a Value and a Data Type. `addValue(string name, string value, string datatype)` This table shows the arguments:

| Argument | Description |
|---|---|
| Name | The element name the field needs to get in the BOD or BDE XML |
| Value | The value of the field; this is always a string |
| Data Type | See the table that shows the supported data types. |
| This table shows the supported data types: |  |
| Data Type | Remark |
| String | Single byte or multibyte string |
| Integer | Integer number (long) |
| Numeric | Numeric number (float or double) |
| Date | Date in the format |

"yyyy-mm-ddThh:mm:ssZ" (GMT) "yyyy-mm-ddThh:mm:ss+hh:mm" (local time later than GMT) Example: "yyyy-mm-ddThh:mm:ss-hh:mm" (local time earlier than GMT) For more information on those date formats, see function utc.to.iso() in the Infor ES Programmers Manual.

Check box “true” or “false”

```baan
Example:        addValue("StringElement", "stringValue", "String")
addValue("IntegerElement", "1", "Integer")
addValue("NumericElement", "123.45", "Numeric")
addValue("DateElement", utc.to.iso(utc.num(), UTC_ISO_Z), "Date")
addValue("CheckboxElement", "true", "Checkbox")
```

### addAmountValue macro

Use this macro to add an amount value to the UserArea. An amount value has a Name, a Value and a currency. The data type “amount” is implied. `addAmountValue(string name, string value, string currency)`

This table shows the arguments:

| Argument | Description |
|---|---|
| Name | The element name the field requires to get in the BOD or BDE XML |
| Value | The value of the field; the amount value must be converted to string |
| Currency Example: | The currency in which the amount is represented |

```baan
addAmountValue("PurchaseOrderAmount",
str$(tdpur400.amnt), tdpur400.ccur)
```

### addCodeValue macro

Use this macro to add a code value to the UserArea. A code value has a Name, a Value, a List Identification which the code is part of and an Accounting Entity. The data type `code` is implied.

```baan
addCodeValue(string name, string value, string listId,
string accountingEntity)
```

This table shows the arguments:

| Argument | Description |
|---|---|
| Name | The element name the field needs to get in the BOD or BDE XML |
| Value | The value of the field; this is always a string |
| ListId | The list to which the code belongs |
| AccountingEntity | The accounting entity of the list |

Example:

```baan
addCodeValue("Country", tccom130.ccnt, "CountryCodes",
str$(get.compnr()))
```

### addMasterDataReferenceValue macro

Use this macro to add a master data reference value to the UserArea. A master data reference value value has a Name, a Value, a Noun and an Accounting Entity. The data type `masterDataReference` is implied.

```baan
addMasterDataReferenceValue(string name, string value, string noun,
string accountingEntity)
```

This table shows the arguments:

| Argument | Description |
|---|---|
| Name | The element name the field needs to get in the BOD or BDE XML |
| Value | The value of the field; this is always a string |
| Noun | The noun of the master data entity |
| AccountingEntity Example: | The accounting entity of the noun |

```baan
addMasterDataReferenceValue("Item", tcibd001.item, "ItemMaster",
str$(get.compnr()))
```

### addQuantityValue macro

Use this macro to add a quantity value to the UserArea. A quantity value has a Name, a Value and a unit. The data type “quantity” is implied. `addQuantity(string name, string value, string unit)`

This table shows the arguments:

| Argument | Description |
|---|---|
| Name | The element name the field needs to get in the BOD or BDE XML |
| Value | The value of the field; the quantity value must be converted to string |
| Currency | The unit in which the amount is represented |

Example:

```baan
addQuantityValue("StockQuantity",
str$(total.stock), "pcs")
```

### addDescription macro

Use this macro to add a description value to an element that was added before to the UserArea. The call of this macro must immediately follow the call of the macro to add the value because the description is added to the latest element that was added. `addDescription(string description)`

This table shows the argument:

| Argument | Description |
|---|---|
| Description | The description that must be added to the element added previously |

Example:

```baan
addQuantityValue("StockQuantity",
str$(total.stock), "pcs")
addDescription("The total stock of the item")
```

### addEffectiveTimePeriod macro

Use this macro to add an effective time periode to an element that was added before to the UserArea. The call of this macro must immediately follow the call of the macro to add the value because the timeperiod is added to the latest element that was added. `addEffectiveTimePeriod(string startDateTime, string endDateTime)`

This table shows the arguments:

Argument Description

Start Date Time The start date time that must be added to the element added previously. This field must be in the format:

- "yyyy-mm-ddThh:mm:ssZ" (GMT)

- "yyyy-mm-ddThh:mm:ss+hh:mm" (local time later than GMT)

- "yyyy-mm-ddThh:mm:ss-hh:mm" (local time earlier than GMT) See function `utc.to.iso()` in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

End Date Time The end date time that must be added to the element added previously. Format see Start Date Time.

Example:

```baan
addQuantityValue("StockQuantity",
str$(total.stock), "pcs")
addEffectiveTimePeriod(utc.to.iso(utc.num(), UTC_ISO_Z),
utc.to.iso(utc.num()+24*60*60, UTC_ISO_Z))
```

### addXML macro

Use this macro to add an XML node to the UserArea. The UserArea can only contain `Property` elements, so an XML node to be added must represent a `Property` element. `addXml(long xmlnode)`

This table shows the arguments:

| Argument | Description |
|---|---|
| XML node | The XML node that contains the XML tree to be added to the BOD or BDE XML. This XML tree must have the following structure (all non-italic words must be added as shown): |

```baan
<Property>
<NameValue name="anyName" type="AnyType">
<myElement>
<mySubElement>value</mySubElement>
</myElement>
</NameValue>
</Property>
```

Example:

```baan
long property.node
long name.node
long xml.node
long child.node
property.node = xmlNewNode("Property")
name.node = xmlNewNode("NameValue", XML_ELEMENT, property.node)
xmlSetAttribute(name.node, "name", "BusinessPartnerData")
xmlSetAttribute(name.node, "type", "AnyType")
xml.node = xmlNewNode("BPElements", XML_ELEMENT, name.node)
child.node = xmlNewDataElement("LongName", tccom100.cdf_lnam,
xml.node)
child.node = xmlNewDataElement("Name", tccom100.nama, xml.node)
addXML(property.node)
```

### getTableIdentifiers.<Component> macro

Use this macro to retrieve the identifying attributes of the current Component that is being processed.

The <Component> for the getTableIdentifiers is not the full component name, but only the last segment. For example: for component `PurchaseOrderBOD.PurchaseOrderLine.PurchaseOrderSchedule` the generated macro

| has the name: `getTableIdentifiers.PurchaseOrderSchedule`. |  |
|---|---|
| `long getTableIdentifiers.<Component>(ref long xmlnode)` |  |
| This table shows the arguments: |  |
| Argument | Description |
| XML node | XML node that contains the table identifiers after the call |

Example:

```baan
long                    ret
long                    header.xml
domain  tcorno          orno
domain  tccom.bpid      otbp
ret = getTableIdentifiers.PurchaseOrderBOD(header.xml)
orno = getIdentifierValueFromIdentifierStructure(
header.xml, "tdpur400", "orno")
select  tdpur400.otbp:otbp
from    tdpur400
where   tdpur400.orno = :orno
selectdo
select  tccom100.*
from    tccom100
where   tccom100.bpid = :tdpur400.otbp
selectdo
addValue("LongBpName", tccom100.cdf_lnam, "String")
endselect
endselect
```

In this example the identifying attribute of the current Component `PurchaseOrderBOD` are stored in `header.` `xml`. With the macro `getIdentifierValueFromIdentifierStructure` the individual table field values can be retrieved. Those values can be used in subsequent queries or function calls.

### getIdentifierValueFromIdentifierStructure macro

Use this macro to retrieve the values of the individual identifying attributes.

```baan
string getIdentifierValueFromIdentifierStructure(
long xmlnode, string table, string field)
```

This table shows the arguments:

| Argument | Description |
|---|---|
| XML node | XML node that contains the table identifiers (retrieved with macro `getTableIdentifiers` `.<Component>()`) |
| Table | The table to retrieve the identifying attribute of |
| Field | The field name of the identifying attribute to retrieve |

Example:

```baan
ret = getTableIdentifiers.PurchaseOrderBOD(header.xml)
orno = getIdentifierValueFromIdentifierStructure(
header.xml, "tdpur400", "orno")
```

### getIdentifierDataTypeFromIdentifierStructure

Use this macro to retrieve the data types of the individual identifying attributes.

```baan
string getIdentifierDataTypeFromIdentifierStructure(
long xmlnode, string table, string field)
```

This table shows the arguments:

| Argument | Description |
|---|---|
| XML node | XML node that contains the table identifiers (retrieved with macro `getTableIdentifiers` `.<Component>()`) |
| Table | The table to retrieve the data type of the identifying attribute |
| Field | The field name of the identifying attribute to retrieve the data type |

Example:

```baan
ret = getTableIdentifiers.PurchaseOrderBOD(header.xml)
datatype = getIdentifierDataTypeFromIdentifierStructure(
header.xml, "tdpur400", "orno")
```

### UserArea example

This section shows an example of a UserArea:

- The first codeblock shows the XML structure of the UserArea, which is created by the BOD or BDE extension.

- The second codeblock shows the Add Calculated Fields hook that built this User Area.

UserArea

```baan
<UserArea>
<Property><NameValuename="NegotiationDate"
type="DateTimeType">2013-05-16T07:46:37Z</NameValue>
</Property>
<Property><NameValuename="NegotiationLevel"
type="EnumerationType">hard</NameValue>
</Property>
<Property><NameValuename="StringElement"
type="StringType">stringValue</NameValue>
</Property>
<Property><NameValuename="IntegerElement"
type="IntegerNumericType">1</NameValue>
</Property>
<Property><NameValuename="NumericElement"
type="NumericType">123.45</NameValue>
</Property>
<Property><NameValuename="DateElement"
type="DateTimeType">2016-07-08T07:38:28Z</NameValue>
</Property>
<Property><NameValuename="CheckboxElement"
type="IndicatorType">true</NameValue>
</Property>
.<Property><NameValuename="LongBpName"
type="StringType">LONG BP NAME</NameValue>
</Property>
<Property><NameValuename="Name"
type="StringType">BP Name</NameValue>
</Property>
<Property><NameValuename="DatatypeOfOrno"
type="StringType">DB.STRING</NameValue>
</Property>
<MyOwnUserAreaExtension>
<LongName>LONG BP NAME</LongName>
<Name>BP Name</Name>
</MyOwnUserAreaExtension>
</UserArea>
```

Add Calculated Fields hook

```baan
Negotiation Date and Negotiation Level are
selected in the Field List of the
PurchaseOrderBOD Component
longret, header.xml
longxmlnode
longchildnode
domain  tcorno          orno
domain  tccom.bpid      otbp
addValue("StringElement","stringValue","String")
addValue("IntegerElement","1","Integer")
addValue("NumericElement","123.45","Numeric")
addValue("DateElement",
```

`utc.to.iso(utc.num(), UTC_ISO_Z),` `"Date"` `)`

```baan
addValue("CheckboxElement","true","Checkbox")
ret = getTableIdentifiers.PurchaseOrderBOD(
header.xml)
orno =
getIdentifierValueFromIdentifierStructure(
```

`header.xml,` `"tdpur400"` `,` `"orno"` `)`

```baan
select  tdpur400.otbp:otbp
from    tdpur400
where   tdpur400.orno = :orno
selectdo
select  tccom100.*
from    tccom100
where   tccom100.bpid = :tdpur400.otbp
selectdo
```

`addValue(` `"LongBpName"` `, tccom100.cdf_lnam,` `"String"` `)` `addValue(` `"Name"` `, tccom100.nama,` `"String"` `)`

```baan
endselect
endselect
addValue("DatatypeOfOrno",
getIdentifierDataTypeFromIdentifierStructure(
header.xml,"tdpur400","orno"),"String")
xmlnode = xmlNewNode(
"MyOwnUserAreaExtension")
childnode = xmlNewDataElement("LongName",
tccom100.cdf_lnam, xmlnode)
childnode = xmlNewDataElement("Name",
tccom100.nama, xmlnode)
addXML(xmlnode)
```

## Process Inbound User Area hook

Use this hook to execute additional actions when the BOD or BDE is processed. Examples:

- Update another table based on fields in the UserArea

- Update the linked tables with results of expressions

- The inbound processing is based on the presence of the UserArea but is not limited to fields in the UserArea.

- This processing of the UserArea is executed when the BOD or BDE component is completely processed by the BOD or BDE handler. The standard fields and the fields of the UserArea that are mapped to fields of the linked tables are processed already. The database records are updated, although not committed yet. To update the linked tables, select the current record again before updating the fields.

The lines of code in this hook are included in the function that the runtime BOD or BDE processor calls to process the UserArea. The structure of this generated function is:

```baan
function extern long process.inbound.user.area(
const   string   i.component,
long     i.xml)
{
...
on case i.component
case "component1":
|* Hook code for Process Inbound User Area for component1
break
case "component2":
|* Hook code for Process Inbound User Area for component2
break
default:
break
endcase
...
return(0)
}
```

You can report errors by calling function `dal.set.error.message()` and do an early return(DALHOOKERROR).

In the Process Inbound User Area hook you can use these macros to find the fields and their values in the UserArea:

- getFirstProperty

- getNextProperty

- getNrProperties

- getPropertyNr

- getNamedProperty

- getPropertyName

- getPropertyType

- getPropertyValue

- getAccountingEntity

- getCurrencyID

- getListID

- getNounName

- getUnitCode

- getDescription

- getStartDateTime

- getEndDateTime

- getUserAreaParent

Note: Those macros only work in the hook itself. You cannot use them in a function you call from the hook. There are basically three ways to process the properties in the UserArea:

- `getNamedProperty()` Get the required properties by their names with

- `getNrProperties()` and process them one by one with `getPropertyNr()` Get the number of properties with

- `getFirstProperty()` and the next ones with `getNextProperty()` Get the first property with

The examples used in the descriptions of the macros assume a UserArea in the PersonInBOD with this content:

```baan
<UserArea>
<Property>
<NameValue name="salary" type="AmountType"
currencyID="USD">43000</NameValue>
<EffectiveTimePeriod>
<StartDateTime>2017-07-21T06:05:13Z</StartDateTime>
<EndDateTime>2017-08-20T23:59:59Z</EndDateTime>
</EffectiveTimePeriod>
</Property>
<Property>
<NameValue name="oldWorkCenter"
type="MasterDataReferenceType"
nounName="WorkCenter"
accountingEntity="AE1000">WC1</NameValue>
</Property>
<Property>
<NameValue name="country" type="CodeType"
listID="Countries"
accountingEntity="AE1000">US</NameValue>
<Description>United States</Description>
</Property>
<Property>
<NameValue name="skill_01" type="StringType">S00</NameValue>
</Property>
<Property>
<NameValue name="skill_02" type="StringType">S01</NameValue>
</Property>
<Property>
<NameValue name="skill_03" type="StringType">S02</NameValue>
</Property>
<Property>
<NameValue name="contract" type="QuantityType"
unitCode="hrs">40</NameValue>
</Property>
</UserArea>
```

### getFirstProperty macro

Use this macro to get the first Property the UserArea. `long getFirstProperty()`

Return value: the xml node of the first property in the UserArea or 0 if the UserArea is empty.

Example:

```baan
domain  tcskll  skill.code
long    property.node
string  property.name(50)
long    ret
property.node = getFirstProperty()
while property.node <> 0
property.name = getPropertyName(property.node)
if property.name(1;5) = "skill" then
skill.code = getPropertyValue(property.node)
if not isspace(skill.code) then
|* Assign skill to employee
select  tcppl020.skll
from    tcppl020
where   tcppl020.emno = :bpmdm001.emno
and     tcppl020.skll = :skill.code
as set with 1 rows
selectdo
selectempty
ret = dal.new.object("tcppl020")
dal.set.field( "tcppl020.emno" , bpmdm001.emno )
dal.set.field( "tcppl020.skll" , skill.code )
ret = dal.save.object("tcppl020")
if ret <> 0 then
dal.set.error.message(sprintf$(
"@Cannot add skill %s to employee %s",
skill.code, bpmdm001.emno))
return(DALHOOKERROR)
endif
endselect
endif
endif
property.node = getNextProperty(property.node)
endwhile
```

### getNextProperty macro

Use this macro to get the next Property the UserArea. `long getNextProperty(long property.node)`

This table shows the argument:

Argument Description

Property Node The node of the previously retrieved property. Note that if the given node is not a prop- erty, the result is unpredictable; just the next right sibling of the given node will be re- turned. Return value: the xml node of the next property in the UserArea or 0 if the given property node is already the last one.

Example: See the example given for `getFirstProperty()`.

### getNrProperties macro

Use this macro to get the number of properties in the UserArea. `long getNrProperties()`

Return value: the number of properties in the UserArea.

Example:

```baan
domain  tcskll  skill.code
long    property.node
string  property.name(50)
long    ret, i
for i = 1 to getNrProperties()
property.node = getPropertyNr(i)
property.name = getPropertyName(property.node)
if property.name(1;5) = "skill" then
skill.code = getPropertyValue(property.node)
if not isspace(skill.code) then
|* Assign skill to employee
select  tcppl020.skll
from    tcppl020
where   tcppl020.emno = :bpmdm001.emno
and     tcppl020.skll = :skill.code
as set with 1 rows
selectdo
selectempty
ret = dal.new.object("tcppl020")
dal.set.field( "tcppl020.emno" , bpmdm001.emno )
dal.set.field( "tcppl020.skll" , skill.code )
ret = dal.save.object("tcppl020")
if ret <> 0 then
dal.set.error.message(sprintf$(
"@Cannot add skill %s to employee %s",
skill.code, bpmdm001.emno))
return(DALHOOKERROR)
endif
endselect
endif
endif
endfor
```

### getPropertyNr macro

Use this macro to get a Property from the UserArea by its index. `long getPropertyNr(long index)`

This table shows the argument:

| Argument | Description |
|---|---|
| Index | The index of the property. |

Return value: the xml node of the property with the given index in the UserArea or 0 if the given index is outside the range of properties.

Example: See the example given for `getNrProperties()`.

### getNamedProperty macro

Use this macro to get a Property the UserArea by its name. `long getNamedProperty(string name)`

Return value: the xml node of the property in the UserArea or 0 if the property with the given name is not present.

Example:

```baan
domain  tcamnt  salary
long    property.node
long    ret
ret = 0
property.node = getNamedProperty("salary")
if property.node <> 0 then
salary = val(getPropertyValue(property.node))
|* Create/update salary record
select  txppl001.*
from    txppl001 for update
where   txppl001.emno = :bpmdm001.emno
as set with 1 rows
selectdo
ret = dal.change.object("txppl001")
dal.set.field("txppl001.sala", salary)
selectempty
ret = dal.new.object("txppl001")
dal.set.field("txppl001.emno", bpmdm001.emno )
dal.set.field("txppl001.sala", salary)
endselect
ret = dal.save.object("txppl001")
if ret <> 0 then
dal.set.error.message(sprintf$(
"@Cannot store salary for employee %s; error %d",
bpmdm001.emno, ret))
return(DALHOOKERROR)
endif
endif
```

### getPropertyName macro

Use this macro to get the name of a Property the UserArea. `string getPropertyName(long property.node)` Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, the result is unpredictable.

Return value: The name of the given property.

Example: See the example given for `getFirstProperty()`.

### getPropertyType macro

Use this macro to get the type of a Property the UserArea. `string getPropertyType(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, the result is unpredictable.

Return value: The type of the given property.

Example:

```baan
long    property.node
string  property.type(50)
property.node = getNamedProperty("salary")
if property.node <> 0 then
property.type = getPropertyType(property.node)
if property.type <> "AmountType" then
dal.set.error.message(sprintf$(
"@Property type %s is invalid for salary property",
property.type))
return(DALHOOKERROR)
endif
|* Handling for salary ...
endif
```

### getPropertyValue macro

Use this macro to get the value of a Property the UserArea. `string getPropertyName(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, the result is unpredictable.

Return value: The value of the given property. Note that this value is always a string. To assign it to table fields the correct casting or conversion must be done. Example: See the example given for `getNamedProperty()`.

### getAccountingEntity macro

Use this macro to get the accounting entity of a Property the UserArea. This only applies to Properties of type `CodeType` or `MasterDataReferenceType` `string getAccountingEntity(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, or of a type for which the accounting entity attribute is not applicable, the result is unpre- dictable.

Return value: The accounting entity of the given property.

Example:

```baan
domain  tccwoc old.wc
long    property.node
string  accounting.entity(20)
property.node = getNamedProperty("oldWorkCenter")
if property.node <> 0 then
old.wc = getPropertyValue(property.node)
accounting.entity = getAccountingEntity(property.node)
txppldll0001.process.old.wc(old.wc, accounting.entity)
endif
```

### getCurrencyID macro

Use this macro to get the currency ID of a Property the UserArea. This only applies to Properties of type `AmountType` `string getCurrencyID(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, or of a type for which the currency ID attribute is not applicable, the result is unpredictable.

Return value: The currency ID of the given property.

Example:

```baan
domain  tcccur currency
domain  tcamnt salary
long    property.node
property.node = getNamedProperty("salary")
if property.node <> 0 then
salary = val(getPropertyValue(property.node))
currency = getCurrencyID(property.node)
if currency <> "USD" then
txppldll0002.convert.salary(currency, salary)
endif
|* Handling for salary ...
endif
```

### getListID macro

Use this macro to get the list ID of a Property the UserArea. This only applies to Properties of type `CodeType` `string getListID(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, or of a type for which the list ID attribute is not applicable, the result is unpredictable.

Return value: The list ID of the given property.

Example:

```baan
long    property.node
string  property.type(50)
string  list.id(20)
string  list.value(100) mb
string  description(100) mb
property.node = getFirstProperty()
while property.node <> 0
property.type = getPropertyType(property.node)
if property.type = "CodeType" then
list.id = getlistID(property.node)
list.value = getPropertyValue(property.node)
description = getDescription(property.node)
txppldll0003.update.code.lists(list.id, list.value, description)
endif
property.node = getNextProperty(property.node)
endwhile
```

### getNounName macro

Use this macro to get the noun name of a Property the UserArea. This only applies to Properties of type `Mas` `terDataReferenceType` `string getNounName(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, or of a type for which the noun name attribute is not applicable, the result is unpredictable.

Return value: The noun name of the given property. Example:

```baan
long    property.node
string  property.type(50)
string  noun.name(50)
string  property.value(100) mb
string  l.message(200) mb
property.node = getFirstProperty()
while property.node <> 0
property.type = getPropertyType(property.node)
if property.type = "MasterDataReferenceType" then
noun.name = getNounName(property.node)
property.value = getPropertyValue(property.node)
if txppldll0003.check.reference(noun.name,
property.value, l.message) <> 0 then
dal.set.error.message("@" & l.message)
return(DALHOOKERROR)
endif
endif
property.node = getNextProperty(property.node)
endwhile
```

### getUnitCode macro

Use this macro to get the unit code of a Property the UserArea. This only applies to Properties of type `Quanti` `tyType` `string getUnitCode(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, or of a type for which the unit code attribute is not applicable, the result is unpredictable.

Return value: The unit code of the given property.

Example:

```baan
long    contract
long    property.node
long    ret
string  unit.code(10)
property.node = getNamedProperty("contract")
if property.node <> 0 then
contract = lval(getPropertyValue(property.node))
unit.code = getUnitCode(property.node)
|* Update salary record
select  txppl001.*
from    txppl001 for update
where   txppl001.emno = :bpmdm001.emno
as set with 1 rows
selectdo
ret = dal.change.object("txppl001")
dal.set.field("txppl001.cont", contract)
dal.set.field("txppl001.unit", unit.code)
ret = dal.save.object("txppl001")
if ret <> 0 then
dal.set.error.message(sprintf$(
"@Cannot update contract for employee %s; error %d",
bpmdm001.emno, ret))
return(DALHOOKERROR)
endif
endselect
endif
```

### getDescription macro

Use this macro to get the description of a Property the UserArea. `string getDescription(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, the result is unpredictable.

Return value: The description of the given property.

Example: See the example given for `getListID()`.

### getStartDateTime macro

Use this macro to get the start date of a Property the UserArea. `string getStartDateTime(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, the result is unpredictable.

Return value: The start date of the given property. This is a string in ISO format. If it must be stored in a table field with a datetime domain, it should be converted with function iso.to.utc().

Example:

```baan
long    property.node
long    ret
property.node = getNamedProperty("salary")
if property.node <> 0 then
|* Update salary record
select  txppl001.*
from    txppl001 for update
where   txppl001.emno = :bpmdm001.emno
as set with 1 rows
selectdo
ret = dal.change.object("txppl001")
dal.set.field("txppl001.sala",
val(getPropertyValue(property.node)))
dal.set.field("txppl001.stdt",
iso.to.utc(getStartDateTime(property.node)))
dal.set.field("txppl001.endt",
iso.to.utc(getEndDateTime(property.node)))
ret = dal.save.object("txppl001")
if ret <> 0 then
dal.set.error.message(sprintf$(
"@Cannot update salary for employee %s; error %d",
bpmdm001.emno, ret))
return(DALHOOKERROR)
endif
endselect
endif
```

### getEndDateTime macro

Use this macro to get the end date of a Property the UserArea. `string getEndDateTime(long property.node)`

Argument Description

Property Node The node of a previously retrieved property. Note that if the given node is not a property, the result is unpredictable.

Return value: The end date of the given property. This is a string in ISO format. If it must be stored in a table field with a `datetime` domain, it must be converted with function `iso.to.utc()`.

Example: See the example given for `getStartDateTime()`.

### getUserAreaParent macro

Note: This macro is only available after KB 1924843 is applied.

Use this macro to get the parent node the UserArea. Through this node you have access to other data in the BOD or BDE. `long getUserAreaParent()`

Return value: The node of the parent of the User Area.

Example:

```baan
string  name(100) mb
|* Get the name of the employee from the PersonInBOD
name = xmlData$(xmlFindFirst("Name", getUserAreaParent()))
```

## Functions

In the hooks of a BOD or BDE extension you can use all trusted functions to do string manipulation, calculations, comparisons, etc.

See the Trusted / Untrusted concept on page 155. Embedded SQL and the `sql.*` functions are available to read additional data from the LN database.

Calling (own) DLL functions is also possible.

## Limitations and restrictions

- Transactions Transactions in a BOD or BDE extension are not supported. Updates for the new fields in the `UserArea` are done in the context of the already started transaction for the BOD or BDE itself. Calling `commit.trans` `action(), abort.transaction()` or `db.retry.point()` from within one of the extension hooks is not allowed. It can lead to fatal applications errors, or data corruption in the database.

- UI A BOD or BDE extension has no access to the UI. You cannot start sessions or reports.

- BOD/BDE extensions are supported only for the standard methods of BODs/BDEs, such as Create, List, Show. Specific methods cannot be extended.

- `UserAreas` implemented can be extended. The BODs have `UserAreas` since July BODs or BDEs that have 2016. For BDEs that have `UserAreas` implemented, see Infor Customer Portal KB 2062874.

## CC-library

Older versions of Infor LN had the concept of CC-libraries for BODs and BDEs. CC-libraries are similar to the BOD or BDE extension script, but more complex to construct. CC-libraries are still supported, but do not comply with cloud-ready extensions.

If a BOD or BDE extension is present, the CC-library is ignored. If no BOD or BDE extension is present, the CC-library is executed.
