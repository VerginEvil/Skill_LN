# ProductStructure.SkipCopyComponent

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2167-2168

```baan
Skips insert of the Components.
This process extension is available from 2025.07 (KB3536528).
To implement this process extension, you can use the information below:
Usage:
Process Extension ProductStructure.SkipCopyComponent can be used to
skip inserting components in the bill of materials when copying a
standard product structure.
Sessions where this Process Extension can be implemented:
- Copy Standard Product Structure to Customized Structure (tipcs2230m000)
- Copy Customized Product Structure to Customized Structure (tipcs2231m000)
- Copy Customized Product Structure to Standard Structure (tipcs2232m000)
- Copy Product Subcontracting Model (tisub1200m100)
Fields that are available to be used in this Process Extension:
- All fields of table: Job Shop List of Material (tibom310) or
- All fields of table: Bill of Material (tibom010) or
- All fields of table: Product Subcontractor Bill of Material (tisub110)
Note: tables must also be declared in the Process Extension.
Site is restricting the scope of the copy
Extern Variables used in this process extension
proc_ext_skip_copycomp_table
proc_ext_skip_copycomp_copy.method (Possible values)
STANDARD.TO.CUST        1 (Standard to Customized)
CUST.TO.STANDARD        2 (Customized to Standard)
CUST.TO.CUST            3 (Customized to Customized)
proc_ext_skip_copycomp_site
These Below fields are the source and target item as they were specified
on the session.
proc_ext_skip_copycomp_source_item
proc_ext_skip_copycomp_target_item
Pseudocode:
Below you can find an example.
Hook: Declarations
table ttibom310
Hook: ext.skip
function extern boolean ext.skip()
{
if is.customized(proc_ext_skip_source_item) then
if proc_ext_skip_copycomp_table = "tibom310" then
if not
allow.use.in.customized.product.structure(tibom310.sitm) then
return(true)
endif
endif
endif
return(false)
}
```
