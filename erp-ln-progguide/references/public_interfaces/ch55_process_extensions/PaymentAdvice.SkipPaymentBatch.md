# PaymentAdvice.SkipPaymentBatch

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2095-2096

Skips processing of a payment batch. This process extension is available from 2023.06 ( KB2280730 ). To implement this process extension, you can use the information below:

```baan
Usage:        PaymentAdvice.SkipPaymentBatch can be used to skip a payment batch
during Process Payments(tfcmg1240m000).
Fields that are available to be used in this Process Extension:
-               Key field of tfcmg109 - tfcmg109.btno (Payment Batch)
This field can be used to read table tfcmg109 (binded)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfcmg109       |* Payment Batches
domain tfgld.user               user.id
Hook: ext.skip
function extern boolean ext.skip()
{
|* function skips the batch if tfcmg109.user = "dummy"
user.id = ""
select  tfcmg109.user:user.id
from    tfcmg109
where   tfcmg109._index1 = {:tfcmg109.btno}
as set with 1 rows
selectdo
if trim$(user.id) = "dummy" then
return(true)
endif
endselect
return (false)
}
```
