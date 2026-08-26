# tfext.cmg0001.get.value.for.custom.receipt.element

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2102-2103

```baan
Syntax: domain tcmcs.s999m tfext.cmg0001.get.value.for.custom.receipt.element(
domain  tcncmp           i.receipt.company,
domain  tcmcs.st12       i.custom.element.code,
domain  tccwoc           i.accounting.office )
Usage:        Expl:
Use this method to get a value for the defined custom receipt
element code during the creation of the Direct Debit XML File.
The custom elements must be defined with the following method:
tfext.cmg0001.define.custom.receipt.elements
Following tables are current when this extension is triggered
(during creation of the XML Bank File):
tccom000        Implemented Software Components (Companies)
tccom100        Business Partners
tccom115        Bank Accounts by Pay                      -by Business Partner
tccom125        Bank Accounts by Pay                      -to Business Partner
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
tfcmg027        Direct Debit Mandates
tfcmg403        Composed Direct Debits
tfcmg025        Payment/Receipt XML Layout Details
The below table is current only for Remittance Related elements:
tfcmg401        Direct Debit Advice
An example implementation is given in the method
tfext.cmg0001.get.value.for.custom.payment.element, which is
likely same.
Pre:    N.A.
Post:   N.A.
Input:  i.receipt.company                     - Receipt Company
i.custom.element.code                         - The custom element code mapped to
an XML attribute.
i.accounting.office                           - Accounting Office.
Output: N.A.
Return: String with the value of the custom receipt element.
```

## Process Extensions for PerformInventoryValuation

The following process extension(s) is/are available: PerformInventoryValuation.SkipItem
