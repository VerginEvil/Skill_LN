# ciext.sli0001.define.custom.xml.data.elements

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2074-2076

```baan
Syntax: long ciext.sli0001.define.custom.xml.data.elements(
ref             long             o.number.of.elements,
ref     domain  tcfdnm.c         o.custom.element.field.names() fixed,
ref     domain  tcdscg           o.custom.element.descriptions() fixed mb,
ref     domain  tcxml.tgtp       o.custom.element.data.types(),
ref     domain  cisli.xils       o.custom.element.sections() )
Usage:        Expl:
Use this method to define extra custom XML data elements to be
used in the XML data elements.
The custom XML data elements can then be used for mapping to
an XML attribute in session XML Invoice Layouts
(cisli1151m000).
If a custom XML data element is mapped, during building the XML
invoice, a value must be retrieved for the element. For that, the
following method must be used:
ciext.sli0001.get.value.for.custom.xml.data.element
Notes:
Keep in mind that when a custom XML data element is used in a
XML layout and that XML layout is used in an invoice you should
not stop supporting that custom XML data element.
Because reprinting of an old invoice can result in a different
invoice when the custom XML data element is not available or properly
filled anymore.
Do not use the prefixes "h.", "f.", "l." or "c." for a
"custom element field name" because those prefixes are used in the
standard implementation, this excludes the risk that when in the standard
a new element field name is introduced it gets the same name as a
custom element field name.
----------------------------------------------------------------
Start of Example of Implementation
long    domain.length.tcfdnm.c
long    domain.length.tcdscg
long    dummy.convert
rdi.domain.string(      "tcfdnm.c",
domain.length.tcfdnm.c, |* ref
dummy.convert)          |* ref
rdi.domain.string(      "tcdscg",
domain.length.tcdscg,   |* ref
dummy.convert)          |* ref
o.number.of.elements = 4        |* 4 data elements wil be defined and
|* returned
if (alloc.mem(  o.custom.element.field.names,
domain.length.tcfdnm.c,
o.number.of.elements) <> 0 ) or
(alloc.mem(  o.custom.element.descriptions,
domain.length.tcdscg,
o.number.of.elements) <> 0 ) or
(alloc.mem(  o.custom.element.data.types,
o.number.of.elements) <> 0 ) or
(alloc.mem(  o.custom.element.sections,
o.number.of.elements) <> 0 ) then
dal.set.error.message(  "cislis0266")
|* Allocation of memory failure, process stopped.
return(DALHOOKERROR)
endif
|* Data elements for Invoice Header
o.custom.element.field.names(1,1) = "ext_fld_h001"
o.custom.element.descriptions(1,1) = "Extensibility h001 description"
o.custom.element.data.types(1) = tcxml.tgtp.string
o.custom.element.sections(1) = cisli.xils.header
o.custom.element.field.names(1,2) = "ext_fld_h002"
o.custom.element.descriptions(1,2) = "Extensibility h002 description"
o.custom.element.data.types(2) = tcxml.tgtp.dec.number
o.custom.element.sections(2) = cisli.xils.header
|* Data elements for Invoice Line
o.custom.element.field.names(1,3) = "ext_fld_l001"
o.custom.element.descriptions(1,3) = "Extensibility l001 description"
o.custom.element.data.types(3) = tcxml.tgtp.string
o.custom.element.sections(3) = cisli.xils.line
|* Data elements for Tax Summary
o.custom.element.field.names(1,4) = "ext_fld_s001"
o.custom.element.descriptions(1,4) = "Extensibility s001 description"
o.custom.element.data.types(4) = tcxml.tgtp.string
o.custom.element.sections(4) = cisli.xils.tax.summary
return (0)
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.number.of.elements            - Number of custom XML data elements
o.custom.element.field.names    - Array with field names
o.custom.element.descriptions   - Array with descriptions.
Maximum of 70 characters.
o.custom.element.data.types     - Array data types
Data type should be one of the
following values:
tcxml.tgtp.string
tcxml.tgtp.dec.number
tcxml.tgtp.bool
tcxml.tgtp.date
tcxml.tgtp.utc.date
tcxml.tgtp.enum
o.custom.element.sections       - Array with section
Section should be one of the
following values:
cisli.xils.header
cisli.xils.line
cisli.xils.tax.summary
Return: 0                       - Success
<> 0                    - When an error occurs in setting
custom xml data elements.
```
