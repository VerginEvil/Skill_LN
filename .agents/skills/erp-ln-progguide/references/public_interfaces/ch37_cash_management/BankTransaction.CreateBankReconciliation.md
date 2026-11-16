# BankTransaction.CreateBankReconciliation

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for BankTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1812-1814

```baan
DLL:   tfextcmgapi
This function is available from 2023.04 (KB2286306).
Syntax: long BankTransaction.CreateBankReconciliation(
domain  tcncmp           iFinancialCompany,
const   domain  tfcmg.bank       iBank,
domain  tfgld.date       iTransactionEntryDate,
const   domain  tfgld.user       iUser,
const   domain  tfgld.desc       iBatchReference mb,
domain  tfgld.date       iDocumentDate,
long             iNumberOfTransactions,
const   domain  tfcmg.tran       iTypeOfTransactionArray(),
const   domain  tcccur           iBankCurrencyArray() fixed,
const   domain  tcratc           iBankRateArray(),
const   domain  tfgld.ttyp       iAnticipatedTransactionTypeArray() fixed,
const   domain  tfgld.ninv       iAnticipatedDocumentArray(),
const   domain  tfgld.schn       iAnticipatedScheduleLineNumberArray(),
const   domain  tfgld.sern       iSerialNumberComposedAnticipatedDocumentArray(),
const   domain  tfcmg.stpd       iPaymentDocumentStatusArray(),
ref     domain  tfgld.ttyp       oBankTransactionType,
ref     domain  tfgld.docn       oBankDocument,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will create a Bank Reconciliation.
It creates a Bank Transaction of the given Type of Transaction
which can only be of type Payment Reconciliation or Receipt
Reconciliation.
The function first creates a (modifiable) Financial Batch; the
Fiscal, Reporting and Tax Period of the Batch and the Bank
Transaction will be determined/defaulted based on the
given Transaction Entry Date.
Within the Financial Batch, a Bank Document is created for the
Transaction Type linked to the given Bank. Within this Bank
Document, one ore more Bank Transactions (iNumberOfTransactions)
are created with Payment or Receipt Reconciliation.
Note: via this function, it is not possible to add Sundry Costs
to the Bank Reconciliation Transaction.
Pre:    None.
Post:   This function sets a retry-point and will commit or abort
the transaction.
Note that always a batch and document is created and committed.
Input:
iFinancialCompany       - Financial Company in which the batch
and bank transaction will be created.
Mandatory.
iBank                   - Bank Relation for which the
Reconciliation must be done.
Mandatory.
iTransactionEntryDate   - Transaction Entry Date of the batch.
Mandatory.
iUser                   - The user to be used on the batch. If
not filled, the current logged on
user will be used.
Optional.
iBatchReference         - Reference of the Financial Batch.
Optional.
iDocumentDate           - Document Date of the Bank Transaction.
Mandatory.
iNumberOfTransactions   - Number of Reconciliation Transactions
to be handled.
Mandatory
iTypeOfTransactionArray - Array with Type of Bank Transaction.
Only Payment Reconciliation or Receipt
Reconciliation are possible.
Mandatory.
iBankCurrencyArray      - Array with Currency of the Bank
Transaction. If not filled, the Bank
Currency will be determined based on
the Bank Transaction Type or the Bank.
Optional.
iBankRateArray          - Array with Currency Rate of the Bank
Transaction. Only if the Bank Currency
is different from the Local Currency
of the Financial Company, the given
Bank Rate will be used.
If not filled, the default rate will
be determined based on the Document
Date.
Optional.
iAnticipatedTransactionTypeArray
- Array with Transaction Type of the
Anticipated Payment/Receipt.
Mandatory.
iAnticipatedDocumentArray
- Array with Document of the Anticipated
Payment/Receipt.
Mandatory.
iAnticipatedScheduleLineNumberArray
- Array with Schedule Line Number of the
Anticipated Payment/Receipt.
Optional.
iSerialNumberComposedAnticipatedDocumentArray
- Array with Serial Number of Composed
Anticipated Payment/Receipt.
Optional.
iPaymentDocumentStatusArray
- Array with Payment Document Status to
which the Anticipated Payment/Receipt
must be set.
Only Open, Complete or Rejected are
possible.
Partial Reconciliation is not
supported.
Mandatory.
Output:
oBankTransactionType    - Bank Transaction Type of the given
Bank.
oBankDocument           - Bank Document created in which the
Bank Reconciliation transactions are
posted.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Bank Reconciliation postings are
created successfully.
<> 0                    - Error occurred during Bank
Reconciliation.
```
