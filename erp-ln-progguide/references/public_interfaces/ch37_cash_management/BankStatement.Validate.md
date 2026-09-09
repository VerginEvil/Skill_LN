# BankStatement.Validate

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for BankStatement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1814-1815

```baan
DLL:   tfextcmgapi
This function is available from 2025.04 (KB3561771).
Syntax: long BankStatement.Validate(
domain  tcncmp           iFinancialCompany,
domain  tfcmg.ebs        iBankStatement,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function validates a bank statement. It checks the
following things (and logs validation warnings/errors in
tfcmg516 if needed):
1a) Opening Balance - Closing Balance = SUM(tfcmg511.amnt)
1b) Opening Balance = previous Closing Balance
1c) Opening Balance Date < Closing Balance Date
1d) Opening Balance Date >= previous Closing Balance Date
2a) Total Number of Transactions = COUNT(tfcmg511)
2b) Total Number of Transactions =
Total Number of Credit Transactions +
Total Number of Debit Transactions
2c) Total Debit Amount = SUM(tfcmg511 debits)
2d) Total Credit Amount = SUM(tfcmg511 credits)
3) Bank Statement ID should not exist in year already.
4) Bank Statement ID Sequence (tfcmg510.bssq) is in sequence.
5) If Detail Lines Present (tfcmg511.dtls=yes) then check if
the SUM(tfcmg512) = tfcmg511.amnt.
6) Last Page Number > 0 and no gaps in Line Page Numbers.
7) At least one line should be present.
Note: Transaction management is handled within this function.
Pre:    Bank Statement Status should be one of the following:
* Converted
* Imported
* Validation Errors
Post:   -
Input:
iFinancialCompany       - Financial company of the
bank statement to be validated.
Mandatory.
iBankStatement          - Bank statement to be validated.
Mandatory.
Output:
oExceptionMessage       - The last message if any message is found.
If more than one message is given,
these are present in the oExceptionID.
oExceptionID            - An ID that refers to the exception information.
Use the functions in Exception to get
all relevant information.
Return:
0                       - Bank statement successfully validated.
<> 0                    - Error.
```
