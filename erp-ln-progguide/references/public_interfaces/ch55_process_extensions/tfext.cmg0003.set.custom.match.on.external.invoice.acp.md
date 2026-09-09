# tfext.cmg0003.set.custom.match.on.external.invoice.acp

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BankStatement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1971-1971

```baan
Syntax: long tfext.cmg0003.set.custom.match.on.external.invoice.acp(
ref     domain  tcfieldname      o.match.external.invoice.field )
Usage:     Expl: Use this method to return the code of a string field of table tfacp500.
This string field can be used for matching with the external invoice.
Standard tfacp500.isup (Supplier›¼À™s invoice number) is used for this purpose
but
by means of this method other string fields of table tfacp500 can be used like:
tfacp500.vrsm (Variable Symbol)
NOTE: If the returned field is not a part of an index the use of this
process extension migth have a negative effect on the performance.
This method is used in session: Match Bank Statements (tfcmg5210m000)
Example:
o.match.external.invoice.field = ›¼Àœtfacp500.vrsm›¼À•
return(0)
Pre:       na
Post:      na
Input:
Output:    o.match.external.invoice.field
- The string field of tfacp500 which must be used
to match with the external invoice.
Return:    0               - succes
DALHOOKERROR         - otherwise
```
