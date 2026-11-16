# FinancialIntegration.GetDefaultLedgerAccountAndDimensions

> Chapter: Chapter 36 Public Interfaces for FinancialIntegration
>
> Group: Public Interfaces for FinancialIntegration
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1804-1805

```baan
DLL:   tcextfinapi
This function is available from 2023.09 (KB2300216).
Syntax: long FinancialIntegration.GetDefaultLedgerAccountAndDimensions(
domain  tcncmp           iBusinessObjectCompany,
domain  tcbona           iBusinessObjectName,
domain  tcboid           iBusinessObjectID,
domain  tcborf           iBusinessObjectReference,
domain  tcguid           iBusinessObjectReferenceGuid,
domain  tcncmp           iInvoiceFinancialCompany,
domain  tcttyp           iInvoiceTransactionType,
domain  tcinvn           iInvoiceDocument,
domain  tciseq           iInvoiceLine,
domain  tcncmp           iTradeOrderCompany,
domain  tcorno           iTradeOrder,
domain  tcpono           iTradeOrderLine,
domain  tcncmp           iFinancialCompany,
domain  tctror           iTransactionOrigin,
domain  tcfitr           iFinancialTransaction,
domain  tcyesno          iCustomerOwned,
domain  tcdecr           iDebitCredit,
domain  tccpcp           iCostComponent,
ref     domain  tfgld.leac       oLedgerAccount,
ref     domain  tfgld.dimx       oDimension1,
ref     domain  tfgld.dimx       oDimension2,
ref     domain  tfgld.dimx       oDimension3,
ref     domain  tfgld.dimx       oDimension4,
ref     domain  tfgld.dimx       oDimension5,
ref     domain  tfgld.dimx       oDimension6,
ref     domain  tfgld.dimx       oDimension7,
ref     domain  tfgld.dimx       oDimension8,
ref     domain  tfgld.dimx       oDimension9,
ref     domain  tfgld.dimx       oDimension10,
ref     domain  tfgld.dimx       oDimension11,
ref     domain  tfgld.dimx       oDimension12,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface determines the ledger account and
dimensions in the actual mapping scheme, based on a given
business object and Transaction Origin/Financial Transaction/
Customer Owned combination.
Pre:    NA
Post:   NA
Input:  iBusinessObjectCompany          - Business Object Company (Mandatory)
iBusinessObjectName             - Business Object Name (Mandatory)
iBusinessObjectID               - Business Object ID (Mandatory)
iBusinessObjectReference        - Business Object Reference
iBusinessObjectReferenceGuid    - Business Object Reference Guid
iInvoiceFinancialCompany        - Invoice Financial Company
iInvoiceTransactionType         - Invoice Transaction Type
iInvoiceDocument                - Invoice Document
iInvoiceLine                    - Invoice Line
iTradeOrderCompany              - Trade Order Company
iTradeOrder                     - Trade Order
iTradeOrderLine                 - Trade Order Line
iFinancialCompany               - Financial Company
iTransactionOrigin              - Transaction Origin (Mandatory)
iFinancialTransaction           - Financial Transaction (Mandatory)
iCustomerOwned                  - Customer Owned (Mandatory)
iDebitCredit                    - Debit Credit (Mandatory)
iCostComponent                  - Cost Component
Output: oLedgerAccount                  - Ledger account
oDimension1                     - Dimension 1
oDimension2                     - Dimension 2
oDimension3                     - Dimension 3
oDimension4                     - Dimension 4
oDimension5                     - Dimension 5
oDimension6                     - Dimension 6
oDimension7                     - Dimension 7
oDimension8                     - Dimension 8
oDimension9                     - Dimension 9
oDimension10                    - Dimension 10
oDimension11                    - Dimension 11
oDimension12                    - Dimension 12
oExceptionMessage               - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                    - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Ledger account and dimensions determined
<> 0                    otherwise
```
