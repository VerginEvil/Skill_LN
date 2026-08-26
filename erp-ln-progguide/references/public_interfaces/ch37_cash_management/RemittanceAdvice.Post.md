# RemittanceAdvice.Post

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for RemittanceAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1791-1793

```baan
DLL:   tfextcmgapi
This function is available from     2025.04 (KB3568308  ).
Syntax: long RemittanceAdvice.Post(
domain  tcncmp           iFinancialCompany,
domain  tfgld.date       iTransactionEntryDate,
const   domain  tfgld.desc       iBatchReference mb,
domain  tfgld.date       iDocumentDate,
long             iNumberOfRemittances,
const   domain  tfcmg.rcod       iRemittanceArray() fixed,
ref             long             oNumberOfHandledRemittances,
ref     domain  tfcmg.rcod       oHandledRemittanceArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will post the given Remittances by creating a
Receipt Transaction.
Remittances belonging to the same Bank will be created
in a separate Batch and Document.
Per Bank, a (modifiable) Financial Batch is created; the
Fiscal, Reporting and Tax Period of the Batch and the Bank
Transaction will be determined/defaulted based on the
given Transaction Entry Date.
Within the Financial Batch, a Bank Document is created for the
Transaction Type linked to the Bank. Within this Bank Document,
for all the Remittances passed (having this same Bank),
a Bank Transaction line is created with Type of Transaction
'Receipt Transaction' for the Remittance.
Note: via this function, it is not possible to add Sundry Costs
or Factoring Commission to the Bank Transaction.
Pre:    None.
Post:   This function sets a retry              -point and will commit or abort
the transaction.
Note that always a batch is created and committed.
Input:
iFinancialCompany                             - Financial Company in which batch(es)
and bank transactions will be created.
Mandatory.
iTransactionEntryDate                         - Transaction Entry Date of the batch(es).
Mandatory.
iBatchReference                               - Reference of the batch(es).
Optional.
iDocumentDate                                 - Document Date of the Bank Transaction(s).
Mandatory.
iNumberOfRemittances                          - Number of Remittances to be handled.
Mandatory
iRemittanceArray                              - Array with Remittances.
Mandatory.
Output:
oNumberOfHandledRemittances
-                                               The number of successfully handled
Remittances.
oHandledRemittanceArray                       - The successfully handled Remittances
Return: 0                                     - All Remittances are successfully
handled for which Bank Transactions
are created.
<> 0                                          - Error occurred during Bank
Transaction creation of one of the
Remittances. Note that some are
possibly handled correct (see the
oHandledRemittanceArray).
```

## Public Interfaces for BankTransaction

The following functions are available: BankTransaction.CreateBankReconciliation
