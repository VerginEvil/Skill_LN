# ProductVariant.AddToCPQConfiguration

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2171-2171

```baan
Execute additional logic directly after finishing the configuration process of a CPQ product variant.
This process extension is available from 2020.09 (KB2143379).
Technical information for this process extension:
Usage:                This extension method is called after finishing the
configuration process for a product variant configuration
by CPQ. This is after the product variant is updated with
engineering options, price structures and status.
It applies for the interactive configuration (raised from the
Configure option in various sessions) as well as for the
background configuration of sales options (either directly via
SalesOrderBOD processing, or via tipcf5205m000).
It allows the implementor to add logic for creating or updating
related order line data and/or other related data in LN. This can be
based on additional data elements or rules in the related CPQ
ruleset.
To implement this process extension, you need to implement the following method(s):
```
