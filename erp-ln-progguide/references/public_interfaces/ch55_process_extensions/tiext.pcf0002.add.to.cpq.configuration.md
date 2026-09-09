# tiext.pcf0002.add.to.cpq.configuration

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2171-2172

```baan
Syntax: long tiext.pcf0002.add.to.cpq.configuration(
long             i.service.node,
long             i.request.node,
long             i.response.node,
domain  tipcf.acfs       i.cpq.result.status,
domain  tccpva           i.product.variant,
domain  tccpva           i.reused.product.variant,
domain  tcqsl1           i.config.qty,
domain  tcolid           i.option.list.id )
Usage:        Expl:   This extension method is called after finishing the
configuration process for a product variant configuration
by CPQ. This is after the product variant is updated with
engineering options, price structures and status.
It applies for the interactive onfiguration (raised from the
Configure option in various sessions) as well as for the
background configuration of sales options (either directly via
SalesOrderBOD processing, or via tipcf5205m000).
It allows the implementor to add logic for creating or updating
related order line data and/or other related data in LN. This can be
based on additional data elements or rules in the related CPQ
ruleset.
The implementation of the method must contain its own
transaction management (db.retry.point, commmit or abort
transaction).
Pre:
Post:
Input:  i.service.node - Service Node (XML Structure)
i.request.node - Request Node (XML Structure)
i.response.node - CPQ configuration (XML Structure)
i.cpq.result.status - CPQ Configurator Status
i.product.variant - Product Variant
i.reused.product.variant - Reused Product Variant:
an existing product variant (<> i.product.variant)
or zero when no product variant is reused
i.config.qty - Configured quantity
i.option.list.id - Option List ID
Output:
Return: 0                       - Success
DALHOOKERROR            - When an error occurs in the
added logic
```
