# FinancialIntegration.RetrieveContributionToPcsWip

> Chapter: Chapter 36 Public Interfaces for FinancialIntegration
>
> Group: Public Interfaces for FinancialIntegration
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1787-1788

```baan
DLL:   tcextfinapi
This function is available from     2024.07 (KB3507629  ).
Syntax: long FinancialIntegration.RetrieveContributionToPcsWip(
domain  tcidty           iIntegrationDocumentType,
domain  tcdecr           iDebitCredit,
ref     domain  tcfin.pcsw       oContributionPcsWip,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the contribution to PCS WIP for
Reconciliation purposes
Pre:    N.A.
Post:   N.A.
Input:  iIntegrationDocumentType               - Integration Document Type (mandatory)
iDebitCredit                                   - Debit/Credit (mandatory)
Output: oContributionPcsWip                    - Contribution to Project (PCS) WIP
oExceptionMessage                              - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                   - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Contribution retrieved
<> 0                    otherwise
```

## Chapter 37 Public Interfaces for Cash Management

## Public Interfaces for PaymentAdvice

The following functions are available: PaymentAdvice.StartPrintExceptionErrors PaymentAdvice.StartProcessPayments
