# ciext.sli0001.get.value.for.custom.xml.data.element

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2057-2059

```baan
Syntax: long ciext.sli0001.get.value.for.custom.xml.data.element(
domain  tcxml.layd       i.xml.layout,
domain  tcxml.tgtp       i.xml.tag.type,
domain  tcxml.tgid       i.xml.tag.id,
domain  tcxml.tag        i.xml.tag mb,
domain  cisli.xils       i.xml.section,
long             i.section.key.object,
domain  tcfdnm.c         i.custom.element.field.name,
ref             string           o.custom.element.value(),
ref             long             o.custom.element.type )
Usage:        Expl:   Use this method to get a value and type for the given custom
XML data element field.
----------------------------------------------------------------
Start of Example of Implementation
table   tcisli315
#define NO_FIELD_TYPE           0
#define AMOUNT_FIELD            10
#define UTC_DATE_FIELD          20
#define BOOLEAN_FIELD           70
#define QUANTITY_FIELD          80
#define PRICE_PERCENTAGE_FIELD  90
#include        <bic_dam>
#include        <bic_ext>       |* For Process Extensions
o.custom.element.type = NO_FIELD_TYPE
on case strip$(i.custom.element.field.name)
case "ext_fld_h001":
o.custom.element.value = "This is the string value of field ext_fld_h001"
o.custom.element.type = NO_FIELD_TYPE
break
case "ext_fld_h002":
o.custom.element.value = "8.8"
o.custom.element.type = AMOUNT_FIELD
break
case "ext_fld_h003":
o.custom.element.value = "1"                    |* = true
o.custom.element.type = BOOLEAN_FIELD
break
case "ext_fld_h004":
o.custom.element.value = enum.descr$(
"tcinvt",
tcinvt.travel,
"2")
o.custom.element.type = NO_FIELD_TYPE
break
case "ext_fld_h005":
o.custom.element.value = str$(utc.num())
o.custom.element.type = UTC_DATE_FIELD
break
case "ext_fld_h007":
o.custom.element.value = "12.43"
o.custom.element.type = QUANTITY_FIELD
break
case "ext_fld_h008":
o.custom.element.value = "1.1"
o.custom.element.type = PRICE_PERCENTAGE_FIELD
break
case "ext_fld_l001":
o.custom.element.value = "This is the string value of ext_fld_l001"
o.custom.element.type = NO_FIELD_TYPE
break
case "ext_fld_s001":
object.to.keyfields(i.section.key.object)
o.custom.element.value =        concat$("/",
"Custom TaxSummary Field: ",
cisli315.sfcp,
cisli315.tran,
cisli315.idoc,
cisli315.ccty,
cisli315.cvat)
o.custom.element.type = NO_FIELD_TYPE   |* other field
break
endcase
return(0)
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  i.xml.layout                  - The xml invoice layout code
i.xml.tag.type                        - type of the xml.tag
i.xml.tag.id                          - xml tag id
i.xml.tag                             - xml tag name
i.xml.section                         - section where the tag is used for:
cixils.header                                         -       invoice header
cixils.line                                         -         invoice line
cixils.tax.summary    invoice tax summary
-                                       The above xml fields are indicating in which (part of)
XML layout  "i.custom.element.field.name" is used.
i.section.key.object
-                                       This field contains the current value of the key fields
Those key fields can be used when the value of
the i.custom.element.field.name is stored in
one of the tables mentioned below.
Those keyfields can be restored by using
"object.to.keyfields".
In case i.xml.section reads: cixils.header the
keyvalues of cisli305 are restored
In case i.xml.section reads: cixils.line the
keyvalues of cisli310 are restored
In case i.xml.section reads: cixils.tax.summary the
keyvalues of cisli315 are restored
If other then the keyfields are needed a query
must be done.
i.custom.element.field.name                       - Custom XML data element for which
a value must be retrieved.
Output: o.custom.element.value                - The value of the custom element field
o.custom.element.type                         - The element type of the custom element field,
the "o.custom.element.value" will be formatted
or converted according the element type value.
-                                       The next element types are supported:
#define AMOUNT_FIELD          10
-                                               o.custom.element.value is assumed to be
in Invoice header currency, and formatted
according (manual) amount format of the XML
layout.
#define UTC_DATE_FIELD        20
-                                               o.custom.element.value will be formatted
according format settings of the XML layout
#define BOOLEAN_FIELD         70
-                                               o.custom.element.value contains a long
and will be converted as follows
0 = "false", >0 = "true"
#define QUANTITY_FIELD        80
-                                               o.custom.element.value will be reformatted
according decimal and group signs defined
on the XML layout and domain "tcqsl1"
definition.
(Example 10000.00                                                  --> 10.000,00)
#define PRICE_PERCENTAGE_FIELD 90
-                                               o.custom.element.value will be reformatted
according decimal and group signs defined
on the XML layout and domain "tcpric"
definition.
(Example 10.00                                                --> 10,00)
#define NO_FIELD_TYPE 0
-                                               o.custom.element.value will be used without
formatting or conversion.
Use this type for strings or when you want
to deviate from the element types above.
Return: 0                                     - Success
<> 0                                          - When an error occurs in getting
a value for custom xml data element.
```
