# btext.rec0001.fiscal.receipt.extended.validation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BRA.BrazilianFiscalReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1966-1969

```baan
Syntax: long btext.rec0001.fiscal.receipt.extended.validation(
domain  btorno           i.fiscal.receipt.fiscal.reference,
domain  btncmp           i.fiscal.receipt.financial.company,
domain  btncmp           i.fiscal.receipt.logistic.company )
Usage:        Expl:   Use this method to extend the invoice error validation and
define customized error messages for inbound invoices (fiscal
receipts).
To create customized error checking, it is possible to query the
Fiscal Receipt table (btrec200) using the provided 'Fiscal
Reference' variable which is part of the index 1 of the 'Fiscal
Receipt' table.
To get additional fields a new query is needed.
The financial company of the fiscal reference is provided.
To set a custom error it is needed to set a DAL error message
in the DAL buffer using the function dal.set.error.message.
Then the program will get all the data from the DAL error buffer
and print the error report containing the original and/or the
customized error messages.
It is advised to also include in the error message, the line
where the error occurs so it is easier for the user to fix
the error. Use 0 if the error occurs in the invoice header.
When setting the DAL error message, use the construction using
the "@" before the message string, to allow custom messages.
Example: dal.set.error.message("@" & "Data not allowed").
When setting the error message there is no need to set in
English. Set it in the desired language.
At the end of the function, if an error is found, the function
should return DALHOOKERROR.
To use the error return DALHOOKERROR and/or the function
'dal.set.error.message' declare the library 'bic_dam'
in the 'Declarations' section of the extension modeler:
#include <bic_dam>
!!!!!! DO NOT use .* to select table fields. This will probably
generate errors.
*************************** WARNING ***************************
*** Warning: if this extension sets an error message, it will
be displayed in the error report and it won't be possible to
send the invoice to the Brazilian tax authority until the
error is fixed.
*** Warning 2: be careful when creating customized error
messages. When a receipt error message is set, it is not
possible to approve it.
Infor is not responsible for custom messages which will be
defined by this extension.
*************************** WARNING ***************************
----------------------------------------------------------------
Start of Example of Implementation
Pseudocode:
In the code below the error message will be triggered if the
Business Partner in the invoice header is <something> and/or
the NCM Fiscal Classification of the invoice lines are
<something>.
Hook: Declarations
#include <bic_dam>
domain  btfovn          fiscal.rec.header.fiscal.id
domain  btlino          fiscal.rec.line
domain  btfrat          fiscal.rec.line.fiscal.class
boolean         error.found
long            ret.val
tt.init.vars(
fiscal.rec.header.fiscal.id,
fiscal.rec.line,
fiscal.rec.line.fiscal.class,
error.found,
ret.val)
|* Get the Business Partner field from the Invoicing table.
|* Use the index_1 fields of the table btsli200 which are
|* available.
select  btrec200.fovn:fiscal.rec.header.fiscal.id
from    btrec200
where   btrec200._index1 = {
:i.fiscal.receipt.fiscal.reference}
as set with 1 rows
selectdo
if trim$(fiscal.rec.header.fiscal.id) = <something> then
dal.set.error.message(
"@" &
"Line 0: " &
"The fiscal ID " &
trim$(fiscal.rec.header.fiscal.id) &
" is not allowed.")
error.found = true
endif
select  btrec201.line:fiscal.rec.line,
btrec201.frat:fiscal.rec.line.fiscal.class
from    btrec201
where   btrec201._index1 = {
:i.fiscal.receipt.fiscal.reference}
selectdo
if trim$(fiscal.rec.line.fiscal.class) =
<something> then
dal.set.error.message(
"@" &
"Line " &
str$(fiscal.rec.line) &
": " &
"NCM " &
trim$(fiscal.rec.line.fiscal.class) &
" is not allowed.")
error.found = true
endif
endselect
endselect
if error.found then
return(DALHOOKERROR)
endif
return(0)
End of Example of Implementation
----------------------------------------------------------------
Pre:    n.a.
Post:   n.a.
Input:  i.fiscal.receipt.fiscal.reference                     - Fiscal receipt fiscal
reference
i.fiscal.receipt.financial.company                            - Fiscal receipt
financial company
i.fiscal.receipt.logistic.company                             - Fiscal receipt
logistic company
Output: n.a.
```

## Process Extensions for BRA.BrazilianInvoice

The following process extension(s) is/are available: BRA.BrazilianInvoice.DirectProcessCriteria BRA.BrazilianInvoice.Validate
