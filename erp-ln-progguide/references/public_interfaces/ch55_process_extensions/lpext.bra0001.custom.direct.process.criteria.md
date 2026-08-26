# lpext.bra0001.custom.direct.process.criteria

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1969-1971

```baan
Syntax: long lpext.bra0001.custom.direct.process.criteria(
boolean          i.direct.process.allowed,
ref             boolean          o.custom.direct.process.allowed )
Usage:        Expl:   Use this method to define additional direct process criteria to
determine if Brazilian invoices can be directly printed and
posted or the invoicess need to be sent the external system.
All the Brazilian invoices should be sent to the external
system, except in three scenarios:
1                       - A fixed criteria - currently debit or credit invoices.
2                       - The direct process matrix - defined by the user in the
session lpbra0114m000.
3                       - The custom direct process rules defined by this process
extension.
To create custom rules, it is possible to query the billable
lines using the provided variables which are part of the
index 1 of the 'Billable Lines' table (cisli810). To use the
index 1 variables, the table cisli810 should be declared. Only
the fields from the index 1 are available. To get other fields
a query is needed.
Then, it is possible to get all data needed to customize the
rules for which the direct process of Brazilian invoices can
be used.
To use the error return DALHOOKERROR and/or the function
'dal.set.error.message' declare the library 'bic_dam'
in the 'Declarations' section of the extension modeler:
#include <bic_dam>
!!!!!! DO NOT use .* to select table fields. This will probably
generate errors.
*************************** WARNING ***************************
*** Warning: if this function returns TRUE then LN
will understand that the DIRECT PROCESS is enabled and the
option 'Submit to the External System' won't be available for
composed invoices and it can be composed/printed/posted
directly.
*** Warning 2: if this function returns FALSE and there is
an direct process criteria defined in the matrix (set on session
lpbra0114m000) this function will overrule the criteria defined
in the matrix.
*** Warning 3: this function won't affect the fixed criteria.
This means that, this process extension won't be executed
by LN when a fixed criteria is found, therefore, the results
set by this extension won't create or prevent the need for the
direct process.
*** Warning 4: be careful when modifying the conditions of the
direct process for the Brazilian invoices.
Infor is not responsible for custom criteria which will be
defined by this extension.
*************************** WARNING ***************************
----------------------------------------------------------------
Start of Example of Implementation
Pseudocode:
In de code below the direct process will be allowed if the
Invoice                      -to Business Partner is "<something>".
Hook: Declarations
table tcisli810         |* Billable Lines
domain  tccom.bpid      invoice.to.bp
long            ret.val
tt.init.vars(
o.custom.direct.process.allowed,
invoice.to.bp,
ret.val)
o.custom.direct.process.allowed = i.direct.process.allowed
|* Get the Invoice                      -to Business Partner field from the
|* billable lines table. Use the index_1 fields of the table
|* cisli810 which are available.
select  cisli810.itbp:invoice.to.bp
from    cisli810
where   cisli810._index1 = {
:cisli810.srcp,
:cisli810.srtp,
:cisli810.orno,
:cisli810.pono,
:cisli810.oref,
:cisli810.tref,
:cisli810.bseq}
as set with 1 rows
selectdo
selectempty
dal.set.error.message(
"@" &
"Billable Line not found.")
return(DALHOOKERROR)
endselect
|* If the business partner is one for which the direct process
|* should be used for Brazilian invoices then set the
|* return as true. Otherwise, use the value from the matrix,
|* which is already set in the beggining of the function.
if invoice.to.bp = "<something>" then
o.custom.direct.process.allowed = true
endif
return(0)
End of Example of Implementation
----------------------------------------------------------------
Pre:    n.a.
Post:   n.a.
Input:  i.source.company                              - Source company
i.direct.process.allowed                              - Return of the Direct Process
Matrix from the session
lpbra0114m000. If TRUE an
criteria exsits in the
matrix. If FALSE no criteria
exists.
Output: o.custom.direct.process.allowed               - If TRUE the invoice will be
applicable for direct process.
If FALSE the invoice won't be
applicable for direct process.
Return: long                                          - If not zero, the results of
this process extension
will not be used.
```
