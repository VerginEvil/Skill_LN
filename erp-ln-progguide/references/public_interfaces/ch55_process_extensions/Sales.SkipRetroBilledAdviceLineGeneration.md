# Sales.SkipRetroBilledAdviceLineGeneration

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2212-2214

Skips Delivery Lines when Generating Advice Lines. This process extension is available from 2025.11 ( KB3626008 ). To implement this process extension, you can use the information below:

```baan
Usage:        The Sales.SkipRetroBilledAdviceLineGeneration process extension can be
used to skip Delivery Lines during the generation of retro              -billed advice
lines.
Session where this Process Extension can be implemented:
-               Generate Retro-Billed Price Change Advice (tdsls3270d000)
-               Generate Retro-Billed Price Change Advice (tdsls3270m100)
External variable that is available to be used in this Process Extension:
-               proc_ext_skip_sales_advice_line_generation_based_on [ domain: tctabl.c ]
Supported values are:
-                 "tdsls357"
-                 "tdsls456"
-                 "tdsls340"
-                 "tdsls406"
The fields accessible within this process extension depend on the
context, which is determined by the external variable:
"proc_ext_skip_sales_advice_line_generation_based_on".
Accessible fields:
(Please note that in some contexts, all fields are accessible, while in
other contexts, only the primary key fields are accessible).
-               "tdsls357" - All fields of table "Sales Schedule Actual Delivery Lines
History" (tdsls357)
-               "tdsls456" - All fields of table "Sales Order Actual Delivery Lines
History" (tdsls456)
-               "tdsls340" - Primary key fields of table "Sales Schedule Actual
Delivery Lines" (tdsls340)
-               "tdsls406" - Primary key fields of table "Sales Order Actual Delivery
Lines" (tdsls406)
Note: tables and external variable must also be declared in the
Process Extension.
Pseudocode:
Below you can find an example how to handle the conditions for the
various contexts when LN is in the process of generating retro              -billed
advice lines.
Hook: Declarations
table   ttdsls357       |* Sales Schedule Actual Delivery Lines History
table   ttdsls456       |* Sales Order Actual Delivery Lines History
table   ttdsls340       |* Sales Schedule Actual Delivery Lines
table   ttdsls406       |* Sales Order Actual Delivery Lines
extern  domain  tctabl.c
proc_ext_skip_sales_advice_line_generation_based_on
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_skip_sales_advice_line_generation_based_on
case "tdsls357":
if <condition on tdsls357 = true> then
return(true)
endif
break
case "tdsls456":
if <condition on tdsls456 = true> then
return(true)
endif
break
case "tdsls340":
read data using:
-                                         tdsls340.schn
-                                         tdsls340.sctp
-                                         tdsls340.revn
-                                         tdsls340.spon
-                                         tdsls340.wpon
-                                         tdsls340.wsqn
-                                         tdsls340.seqn
-                                         tdsls340.invl
if <condition on the data read = true> then
return(true)
endif
break
case "tdsls406":
read data using:
-                                       tdsls406.orno
-                                       tdsls406.pono
-                                       tdsls406.sqnb
-                                       tdsls406.dsqn
-                                       tdsls406.invl
if <condition on the data read = true> then
return(true)
endif
break
default:
break
endcase
return (false)
}
```

## Process Extensions for SalesCheckInventory

The following process extension(s) is/are available: SalesCheckInventory.CustomSorting SalesCheckInventory.DefaultInventoryShortageOption SalesCheckInventory.SkipShortageLine
