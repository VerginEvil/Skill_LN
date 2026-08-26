# PriceBookLine.SkipGlobalUpdatePricesViaPriceBooks

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PriceBookLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2111-2112

Skips Price Book Line when global updating Prices via Price Books. This process extension is available from 2023.04 ( KB2272981 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PriceBookLine.SkipGlobalUpdatePricesViaPriceBooks can
be used to skip specific Price Book Lines when doing a
Global Update of Prices via Price Books.
Sessions where this Process Extension can be implemented:
-               Global Update of Prices via Price Books (tdpcg0231m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Price Book Lines (tdpcg031)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdpcg031       |* Price Book Lines
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdpcg031 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for Pricing

The following process extension(s) is/are available: Pricing.DefaultPriceDateType Pricing.HandleInputOverruling Pricing.RetrievePriceAndDiscounts
