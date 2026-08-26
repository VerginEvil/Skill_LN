# BusinessPartner.GetCreditLimitAndBalances

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 119-120

```baan
DLL:   tcextcomapi
This function is available from     2020.08 (KB2122836  ).
Syntax: long BusinessPartner.GetCreditLimitAndBalances(
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccwoc           iDepartment,
domain  tcyesno          iIncludeOpenOrdersInFinancialRisk,
ref     domain  tcamnt           oCreditLimit,
ref     domain  tcamnt           oOrderBalance,
ref     domain  tcamnt           oInvoiceBalance,
ref     domain  tcamnt           oBillingRequestBalance,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function calculates the credit limit and the balances
of an invoice                        -to business partner.
Pre     : NA
Post    : NA
Input   : iInvoiceToBusinessPartner
-                                               invoice-to business partner - mandatory
iDepartment                                   - department for checking credit limit (optional)
iIncludeOpenOrdersInFinancialRisk
-                                               Include open orders in financial risk y/n
(tcmcs064.ioso)                                                 - mandatory
Output  : oCreditLimit                        - total credit limit
oOrderBalance                                 - open order balance
oInvoiceBalance                               - open invoice balance
oBillingReqBalance                            - open billing request balance
Return: 0                                     - Credit Limit and Balances determined
successfully.
<> 0                                          - Error occurred.
```
