# Batch.SkipSelectForAuditBatches

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Batch
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1972-1973

```baan
Skips Batch selection during Audit Batches.
This process extension is available from 2025.10 (KB3629872).
Technical information for this process extension:
Usage:        Batch.SkipSelectForAuditBatches can be used to skip a
Batch during Audit Batches.
This process extension is called twice per Batch during the
Audit Batch proces.
First call - During selection of Batch (tfgld100) (Batch Level = 1)
Second call- During selection of Transaction Type Batch Status(tfgld101)
of the selected batch.     (Batch Level = 2)
A message may be filled, to present information about the skip
decision on the report. This message can have max 70 characters.
Session where this Process Extension can be implemented:
-  Audit Batches (tfgld1211s000)
Fields that are available to be used in this Process Extension:
- proc_ext_batch_level                  - indicates if batch is selected(1)
- or batch line(2).
- Primary key fields of tfgld100        -       tfgld100.year
-       tfgld100.btno
- Primary key fields of tfgld101        -       tfgld101.year
-       tfgld101.btno
-       tfgld101.ttyp
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfgld100       |* Financial Batch
table   ttfgld101       |* Transaction Type Batch Status
extern          long            proc_ext_batch_level
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if proc_ext_batch_level = 1 then
|* During selecting a batch in tfgld1211s000
read tfgld100 (binded!)
if <condition on tfgld100 = true> then
o.reason = "Batch skipped because ....."
return(true)
endif
endif
if proc_ext_batch_level = 2 then
|* During selecting a Transaction Type Batch
|* Status of a selected batch in tfgld1211s000
read tfgld101 (binded!)
if <condition on tfgld101 = true> then
o.reason = "Batch skipped because...."
return(true)
endif
endif
return (false)
}
```
