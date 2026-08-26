# TaxDeclaration.GetXMLTextTagContent

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TaxDeclaration
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2278-2278

Get content for an XML Text Tag for the Tax Declaration. This process extension is available from 2025.08 ( KB3572604 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible for the extender to
re              -determine and fill the Tag Content (field tfgld121.tcon)
for a specified XML Tag Name (field tfgld121.xmlt) based on the
parameters passed to the Process Extension method.
E.g. for tax country Slovenia the tag TaxPeriodStart
must be filled with the start date of the tax declaration period.
-                       i.xml.tag.name = "TaxPeriodStart"
-                       io.tag.content = "2025-05-01"
E.g. for tax country Slovenia the tag TaxPeriodEnd
must be filled with the end date of the tax declaration period.
-                       i.xml.tag.name = "TaxPeriodEnd"
-                       io.tag.content = "2025-05-31"
```

To implement this process extension, you need to implement the following method(s):
