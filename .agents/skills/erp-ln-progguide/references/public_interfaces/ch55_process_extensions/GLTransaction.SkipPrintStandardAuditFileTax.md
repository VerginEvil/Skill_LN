# GLTransaction.SkipPrintStandardAuditFileTax

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for GLTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2047-2048

```baan
Skip GL-Transactions when printing Standard Audit File Tax.
This process extension is available from 2025.04 (KB3568308).
To implement this process extension, you can use the information below:
Usage:        Process Extension GLTransaction.SkipPrintStandardAuditFileTax can be used
to skip certain GL-Transactions when Printing Standard Audit File Tax.
Sessions where this Process Extension can be implemented:
- Create Standard Audit File - Tax (SAF-T). (tftax2210m000)
- Create Standard Audit File - Tax (SAF-T v 2.00). (tftax2220m000)
- Create Standard Audit File - Tax - Portugal. (tftax2211m000)
- Create Standard Audit File - Tax - Angola. (lpago2211m000)
- Create Standard Audit File Tax (SAF-T Norway). (lpnor0210m000)
External variables that are available to be used in the Process
Extension:
- proc_ext_called_from [type: string(13)] : this variable is filled
with one of next values:
- "tftax2210m000"
- "tftax2220m000"
- "tftax2211m000"
- "lpago2211m000"
- "lpnor0210m000"
Fields that are available to be used in this Process Extension:
- Primary key fields of tfgld106:       tfgld106.otyp (Transaction Type)
tfgld106.odoc (Document)
tfgld106.olin (Line)
tfgld106.osrl (Sequence Number)
tfgld106.osrn (Background Sequence No.)
This fields can be used to read table tfgld106 (binded).
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfgld106       |* Finalized Transactions
extern          string          proc_ext_called_from(13)
Hook: ext.skip
function extern boolean ext.skip()
{
|* read data using primary key fields of tfgld106
if proc_ext_called_from = "tftax2210m000" and
<condition on the data read = true> then
return(true)
endif
if proc_ext_called_from = "tftax2220m000" and
<condition on the data read = true> then
return(true)
endif
if proc_ext_called_from = "tftax2211m000" and
<condition on the data read = true> then
return(true)
endif
if proc_ext_called_from = "lpago2211m000" and
<condition on the data read = true> then
return(true)
endif
if proc_ext_called_from = "lpnor0210m000" and
<condition on the data read = true> then
return(true)
endif
return (false)
}
```
