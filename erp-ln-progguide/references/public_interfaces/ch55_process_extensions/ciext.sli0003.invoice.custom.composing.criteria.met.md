# ciext.sli0003.invoice.custom.composing.criteria.met

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2052-2054

```baan
Syntax: long ciext.sli0003.invoice.custom.composing.criteria.met(
ref             boolean          o.custom.composing.criteria.met )
Usage:        Expl:
Use this method to check your own defined composing criteria,
whether the current billable line should be composed in the
current invoice number or not.
At the time of composing of billable lines together, LN performs
its own check to determine whether the lines can be composed
together based on the standard composing criteria logic.
Only when standard logic in LN allows the current billable line
to be composed together in the current invoice, this method in
the Process Extension is called.
Default value of "o.custom.composing.criteria.met" is True.
In this method, own checks can be implemented and the variable
o.custom.composing.criteria.met can be set. If the variable is
set to false, then the current billable line will not be
composed in the current invoice but then it will look for the
next available invoice number and if available then this process
extension is called again. If no invoice number is available
then a new invoice number will be created and this process
extenstion will not be called again.
If the variable is set to true then the current billable
line will be added in the current invoice number.
Fields that are available to be used in this Process Extension:
-                       All fields of table: Billable lines (cisli810)
-                       All fields of table: Although the Invoice is not yet
committed, the Invoice Header (cisli305)
fields are already available. The Invoice
header key fields can be used to read
other tables like Invoice Lines
(cisli310) or Invoice Lines                                              - Additional
Fields (cisli311).
Note:
1) Dal messages set in this function will be ignored by
the standard.
2) User must use bind variables when they read data,
otherwise the standard flow may be affected.
3) External variables that are available to be used in this
Process.
----------------------------------------------------------------
Start of Example of Implementation
Requirement                       -   Each Packing slip should be composed separately
in a new invoice number.
Solution                          -   Packing slip is not available in the invoicing
method to make it one of the standard composing
criteria. So Customer can use this process
extension to make it one of the custom composing
criteria.
Packing slip is available on the Billale line
and is available in the Invoice line Additional
Fields (cisli311).
Pseudocode                        -
Hook: Declarations
table   tcisli305       |* Invoice Header
table   tcisli810       |* Billable Lines
Hook: ciext.sli0003.invoice.custom.composing.criteria.met
function extern long
ciext.sli0003.invoice.custom.composing.criteria.met(
ref boolean o.custom.composing.criteria.met)
{
domain  cisli.fldv2     field.value     fixed
domain  cisli.fldc      field.code      fixed
field.code = "PKSP"
|* Default value is set to True.
o.custom.composing.criteria.met = true
select  cisli311.fldv:field.value
from    cisli311
where   cisli311._index1 =
{:cisli305.sfcp,
:cisli305.tran,
:cisli305.idoc}
and     cisli311.fldc = :field.code
and     cisli311.fldv <> :cisli810.pksp
as set with 1 rows
selectdo
|**************************************
|* If different Packing Slip is
|* available in  the invoice then the
|* current billable line should not be
|* inserted into given invoice number
|* so the composing criteria does not
|* meet here.
|**************************************
o.custom.composing.criteria.met = false
endselect
return (0)
}
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.custom.composing.criteria.met               -
Determines whether current billable line
should be composed in the current
invoice or not.
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs during checking;
the invoice will not be composed
together.
```
