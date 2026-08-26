# tfext.cmg0001.define.custom.payment.elements

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2097-2099

```baan
Syntax: long tfext.cmg0001.define.custom.payment.elements(
ref             long             o.number.of.elements,
ref     domain  tcmcs.st12       o.custom.element.codes() fixed,
ref     domain  tcmcs.str132m    o.custom.element.descriptions() fixed mb,
ref     domain  tfcmg.xttp       o.custom.element.data.types() )
Usage:        Expl:
Use this method to define extra custom defined elements to be
used in the XML Payment layout and file. These custom element
codes must start with "8" or "9"; other defined element codes
will be ignored.
Mapping a custom element to a Remittance Related XML Tag, only
the custom elements starting with "8" can be used.
The custom elements starting with "9" can only be used for
mapping to non                      -remittance related XML Tags.
The custom defined elements can then be used for mapping to
an XML attribute in session XML Payment/Receipt Layout Lines
(tfcmg0125m000).
If a custom defined element is mapped, during building the XML
file, a value must be retrieved for the element. For that, the
following method must be used:
tfext.cmg0001.get.value.for.custom.payment.element
----------------------------------------------------------------
Start of Example of Implementation
long    length.element.code
long    length.element.description
long    elem.nr
long    dummy.long
dummy.long = rdi.domain.string(
domainof(o.custom.element.codes),
length.element.code,
dummy.long)
dummy.long = rdi.domain.string(
domainof(o.custom.element.descriptions),
length.element.description,
dummy.long)
elem.nr = 0
|***************************************************************
|* We will add 2 custom elements.
|***************************************************************
o.number.of.elements = 2
if alloc.mem(   o.custom.element.codes,
length.element.code,
o.number.of.elements) +
alloc.mem(   o.custom.element.descriptions,
length.element.description,
o.number.of.elements) +
alloc.mem(   o.custom.element.data.types,
o.number.of.elements) <> 0 then
return(DALHOOKERROR)
endif
|***************************************************************
|* Add the element Name for the Pay                      -to BP
|***************************************************************
elem.nr = elem.nr + 1
o.custom.element.codes(1, elem.nr) = "910210000000"
o.custom.element.descriptions(1, elem.nr) =
"Composed Payments/Pay                              -to Business Partner/Name"
o.custom.element.data.types(elem.nr) = tfcmg.xttp.string
|***************************************************************
|* Add the element Transaction Amount Positive
|***************************************************************
elem.nr = elem.nr + 1
o.custom.element.codes(1, elem.nr) = "911200000000"
o.custom.element.descriptions(1, elem.nr) =
"Composed Payments/Transaction Amount Positive"
o.custom.element.data.types(elem.nr) = tfcmg.xttp.decimal
return(0)
End of Example of Implementation
----------------------------------------------------------------
In above example, a custom element is added to
influence the transaction amount in the file (i.e. making the
transaction amount positive); note that this impacts the control
amount in the file and thus a custom element is needed as well
to determine the control amount in the extension.
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.number.of.elements                  - Number of additional custom payment
elements
o.custom.element.codes                        - Array with element codes. The element
code must start with a "8" or "9".
Maximum of 12 characters.
E.g. "910100000000".
o.custom.element.descriptions
-                                               Array with descriptions of the
element codes.
Maximum of 132 characters.
o.custom.element.data.types
-                                               Array with data types of the
element code.
Data type should be one of the
following values:
tfcmg.xttp.string     (String)
tfcmg.xttp.date       (Date)
tfcmg.xttp.utc        (UTC Date)
tfcmg.xttp.decimal    (Decimal Number)
tfcmg.xttp.bool       (Boolean)
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in defining
the custom elements.
```
