# tiext.pcs0002.product.variant.skip.delete.or.expire.jsbom

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2174-2174

```baan
Syntax: long tiext.pcs0002.product.variant.skip.delete.or.expire.jsbom(
domain  tccpva           i.product.variant,
domain  tcitem           i.parent.item,
domain  tcsite           i.site,
domain  tibmdl           i.bill.of.material,
domain  tibmrv           i.revision,
domain  tibmst           i.status,
ref             boolean          o.skip.delete.or.expire.jsbom )
Usage:        Expl:   This function is used to skip delete/expire of the job shop bill
of materials when generating the project structure for a product
variant, provided the 'regenerate existing product variant'
option is selected. This public interface only works when the
Sites concept is active.
Implementation Example:
Intention:
For a specific Parent Item (SLO), when Regenerate
Product Variant Structure is requested, Delete or Expire
Job Shop Bill Materials is not allowed.
Hook Declarations:
Hook tiext.pcs0002.product.variant.skip.delete.or.expire.jsbom:
function extern long tiext.pcs0002...
...
{
if      str.startswith(i.parent.item, "SLO")
then
o.skip.delete.or.expire.jsbom = true
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.product.variant       - Product Variant
i.parent.item           - Parent Item
i.site                  - Site
i.bill.of.material      - Bill of Material
i.revision              - Revision
i.status                - Status
Output: o.skip.delete.or.expire.jsbom
- Skip Delete or Expire Job Shop Bill of
materials.
Return: 0                       - Success.
DALHOOKERROR            - When an error occurs in determination
of the skip job shop bill of
materials.
```
