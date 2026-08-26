# GeneralLedger.CheckBatchLineIsBalanced

> Chapter: Chapter 40 Public Interfaces for General Ledger
>
> Group: Public Interfaces for GeneralLedger
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1810-1811

```baan
DLL:   tfextgldapi
This function is available from     2023.12 (KB2301011  ).
Syntax: long GeneralLedger.CheckBatchLineIsBalanced(
domain  tcncmp           iFinancialCompany,
domain  tfgld.year       iFiscalYear,
domain  tfgld.btno       iBatch,
domain  tfgld.ttyp       iTransactionType,
ref             boolean          oNonFinalizedTransactionPresent,
ref             boolean          oBatchLineIsBalanced,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks whether all documents of the given
batch and transaction type are balanced. A batch line
becomes balanced when all documents within the batch line
are balanced.
If one of the documents within the batch line is not balanced
then oBatchLineIsBalanced will be false.
In case of Batch is not found or has been already finalized,
then an error message is given. So, only Non                      -Finalized
batches should be used.
Pre:    NA
Post:   NA
Input:  iFinancialCompany                     - Financial Company     - Mandatory
iFiscalYear                                   - Fiscal Year           - Mandatory
iBatch                                        - Batch                 - Mandatory
iTransactionType                              - Transaction type      - Mandatory
Output: oNonFinalizedTransactionPresent               -
Non                                              -finalized transaction present
(True or False)
oBatchLineIsBalanced                          - Batch Line is balanced indicator
(True or False)
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - OK
<> 0                                          - on errors
```
