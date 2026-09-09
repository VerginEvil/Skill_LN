# tfext.cmg0001.get.value.for.custom.payment.element

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2123-2125

```baan
Syntax: domain tcmcs.s999m tfext.cmg0001.get.value.for.custom.payment.element(
domain  tcncmp           i.payment.company,
domain  tcmcs.st12       i.custom.element.code,
domain  tccwoc           i.accounting.office )
Usage:        Expl:
Use this method to get a value for the defined custom payment
element code during the creation of the Payment XML File.
The custom elements must be defined with the following method:
tfext.cmg0001.define.custom.payment.elements
Following tables are current when this extension is triggered
(during creation of the XML Bank File):
tccom000        Implemented Software Components (Companies)
tccom100        Business Partners
tccom115        Bank Accounts by Pay-by Business Partner
tccom125        Bank Accounts by Pay-to Business Partner
tccom130        Addresses
tccom139        Cities by Country
tcmcs002        Currencies
tcmcs010        Countries
tcmcs029        Business Partner Types
tcmcs046        Languages
tcmcs143        States/Provinces
tfcmg001        Bank Relations
tfcmg003        Payment/Receipt Methods
tfcmg009        Financial Institutions
tfcmg011        Bank Branches
tfcmg103        Composed Payments
tfcmg002        Reasons for Payment
tfcmg025        Payment/Receipt XML Layout Details
The below table is current only for Remittance Related elements:
tfcmg101        Payment/Trade Notes Payable Advice
----------------------------------------------------------------
Start of Example of Implementation
domain  tcnama          name.of.bp
domain  tfgld.amnt      composed.amount
name.of.bp      = ""
composed.amount = 0.0
on case i.custom.element.code
case "910210000000":
|* Name of Composed Pay-to BP
get.var(pid, "tccom100.nama", name.of.bp)
return(name.of.bp)
case "911200000000":
|* Transaction Amount Composed Payment (Positive)
|* Return always a POSITIVE value of the Amount field
get.var(pid, "tfcmg103.amnt", composed.amount)
return( trim$(
sprintf$("%@ZZZZZZZZZZZZZZ9V.99@" ,
abs(composed.amount) )))
default:
break
endcase
return("")
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  i.payment.company       - Payment Company
i.custom.element.code   - The custom element code mapped to
an XML attribute.
i.accounting.office     - Accounting Office.
Output: N.A.
Return: String with the value of the custom payment element.
```
