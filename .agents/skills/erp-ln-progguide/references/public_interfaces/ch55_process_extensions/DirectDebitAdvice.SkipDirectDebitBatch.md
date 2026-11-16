# DirectDebitAdvice.SkipDirectDebitBatch

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for DirectDebitAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2024-2024

```baan
Skips processing of a direct debit batch.
This process extension is available from 2024.04 (KB2322586).
To implement this process extension, you can use the information below:
Usage:        DirectDebitAdvice.SkipDirectDebitBatch can be used to skip a direct
debit batch during Process Direct Debits(tfcmg4240m000).
Fields that are available to be used in this Process Extension:
- Key field of tfcmg409 - tfcmg409.btno (Direct Debit Batch)
This field can be used to read table tfcmg409 (binded)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfcmg409       |* Direct Debit Batches
domain tfgld.user               user.id
Hook: ext.skip
function extern boolean ext.skip()
{
|* function skips the batch if tfcmg409.user = "dummy"
user.id = ""
select  tfcmg409.user:user.id
from    tfcmg409
where   tfcmg409._index1 = {:tfcmg409.btno}
as set with 1 rows
selectdo
if trim$(user.id) = "dummy" then
return(true)
endif
endselect
return (false)
}
```
