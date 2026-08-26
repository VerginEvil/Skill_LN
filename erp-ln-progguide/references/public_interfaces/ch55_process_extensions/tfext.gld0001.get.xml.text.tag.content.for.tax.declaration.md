# tfext.gld0001.get.xml.text.tag.content.for.tax.declaration

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TaxDeclaration
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2278-2280

```baan
Syntax: long tfext.gld0001.get.xml.text.tag.content.for.tax.declaration(
domain  tcncmp           i.financial.company,
domain  tfgld.txdt       i.tax.declaration.type,
domain  tctax.txcg       i.tax.category,
domain  tccom.bpid       i.collection.office,
domain  tfgld.tdvs       i.tax.declaration.version,
domain  tfgld.year       i.declaration.year,
domain  tfgld.prod       i.declaration.period,
domain  tfgld.srno       i.correction.number,
domain  tcccty           i.tax.country,
domain  tcmcs.str132m    i.xml.tag.name mb,
ref     domain  tcmcs.str50m     io.tag.content mb )
Usage:        Expl:
Use this Process Extension method to re                      -determine and fill
the Tag Content (field tfgld121.tcon) for a specified
XML Tag Name (field tfgld121.xmlt) based on the
parameters passed to the Process Extension method.
Only if an implementation is done for this Process Extension
and the Process Extension method is returning 0,
the Tag Content (field tfgld121.tcon) is filled with the
custom defined tag content (io.tag.content).
(1)     This Process Extension is called from session
(tfgld1620m000) 'Tax Declaration Master' with satellite session
(tfgld1121m000) 'Tax Positions by Tax Declaration Master'
via form command 'Show file'.
(2)     This Process Extension is called from session
(tfgld1625m000) 'Tax Declaration'
via form command 'Show file'.
(3)     This Process Extension is called from session
(tfgld1625m000) 'Tax Declaration'
via form command 'Show ASCII as XML'.
(4)     This Process Extension is called from session
(tfgld1625m000) 'Tax Declaration'
via form command 'Transfer Tax Declaration'.
Pre:    N.A.
Post:   N.A.
Input:  i.financial.company                   - Financial Company.
i.tax.declaration.type                        - Tax Declaration Type. (Only VAT is appl.)
i.tax.category                                - Tax Category.
i.collection.office                           - Collection Office.
i.tax.declaration.version
-                                               Tax Declaration Version.
i.declaration.year                            - Tax Declaration Year.
Filled with 0 if called from session
(tfgld1620m000) 'Tax Declaration Master'.
Filled with tfgld125.vyer if called from session
(tfgld1625m000) 'Tax Declaration'.
i.declaration.period                          - Tax Declaration Period.
Filled with 0 if called from session
(tfgld1620m000) 'Tax Declaration Master'.
Filled with tfgld125.vprd if called from session
(tfgld1625m000) 'Tax Declaration'.
i.correction.number                           - Correction Number.
Filled with 0 if called from session
(tfgld1620m000) 'Tax Declaration Master'.
Filled with tfgld125.crno if called from session
(tfgld1625m000) 'Tax Declaration'.
i.tax.country                                 - Tax Country.
Filled with tfgld120.ccty.
i.xml.tag.name                                - XML Tag Name.
Filled with tfgld121.xmlt.
IO:     io.tag.content                        - Tag Content.
Filled with tfgld121.tcon.
This field can be influenced by the
process extension based on own logic
e.g. see the example code below.
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in getting the
XML Text Tag content for the Tax Declaration.
Example:
if trim$(i.tax.country) = "SVN" and
trim$(i.xml.tag.name) = "TaxPeriodStart" then
|* Determine the start date of the given declaration year & period.
io.tag.content = "2025                      -05-01"
endif
```

## Process Extensions for Tools

The following process extension(s) is/are available: Tools.SkipScrap
