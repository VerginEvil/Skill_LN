# btext.sli0001.invoicing.extended.validation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1972-1974

```baan
Syntax: long btext.sli0001.invoicing.extended.validation(
domain  btorno           i.invoice.fiscal.reference,
domain  btncmp           i.invoice.financial.company,
domain  btncmp           i.invoice.logistic.company )
Usage:        Expl:   Use this method to extend the invoice error validation and
define customized error messages for outbound invoices.
To create customized error checking, it is possible to query the
Invoicing table (btsli200) using the provided 'Fiscal Reference'
variable which is part of the index 1 of the 'Invoicing' table.
To get additional fields a new query is needed.
The financial and logistic companies of the fiscal reference are
also provided.
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
messages. When an invoice error message is set, it is not
possible to send it to the Brazilian Tax Authority.
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
domain  btcom.bpid      invoice.header.bp
domain  btlino          invoice.line
domain  btfrat          invoice.line.fiscal.class
boolean         error.found
long            ret.val
tt.init.vars(
invoice.header.bp,
invoice.line,
invoice.line.fiscal.class,
error.found,
ret.val)
|* Get the Business Partner field from the Invoicing table.
|* Use the index_1 fields of the table btsli200 which are
|* available.
select  btsli200.bpid:invoice.header.bp
from    btsli200
where   btsli200._index1 = {
:i.invoice.fiscal.reference}
and     btsli200._compnr = :i.invoice.financial.company
as set with 1 rows
selectdo
if trim$(invoice.header.bp) = <something> then
dal.set.error.message(
"@" &
"Line 0: " &
"Business Partner " &
trim$(invoice.header.bp) &
" is not allowed.")
error.found = true
endif
select  btsli201.line:invoice.line,
btsli201.frat:invoice.line.fiscal.class
from    btsli201
where   btsli201._index1 = {
:i.invoice.fiscal.reference}
and     btsli201._compnr = :i.invoice.financial.company
selectdo
if trim$(invoice.line.fiscal.class) =
<something> then
dal.set.error.message(
"@" &
"Line " &
str$(invoice.line) &
": " &
"NCM " &
trim$(invoice.line.fiscal.class) &
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
Input:  i.invoice.fiscal.reference                    - Invoice fiscal reference
i.invoice.financial.company                           - Invoice financial company
i.invoice.logistic.company                            - Invoice logistic company
Output: n.a.
```

## Process Extensions for BRA.WarehouseOrder

The following process extension(s) is/are available: BRA.WarehouseOrder.GetBusinessPartner
