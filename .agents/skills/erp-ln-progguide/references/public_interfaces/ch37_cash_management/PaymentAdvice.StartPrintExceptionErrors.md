# PaymentAdvice.StartPrintExceptionErrors

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for PaymentAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1807-1808

```baan
DLL:   tfextcmgapi
This function is available from 2023.11 (KB2307655).
Syntax: long PaymentAdvice.StartPrintExceptionErrors(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tfgld.btno       iPaymentBatchFrom,
domain  tfgld.btno       iPaymentBatchTo,
domain  tccom.bpid       iPayToBusinessPartnerFrom,
domain  tccom.bpid       iPayToBusinessPartnerTo,
domain  tcccur           iCurrencyFrom,
domain  tcccur           iCurrencyTo,
domain  tfcmg.bank       iBankFrom,
domain  tfcmg.bank       iBankTo,
domain  tfcmg.paym       iPaymentMethodFrom,
domain  tfcmg.paym       iPaymentMethodTo,
domain  tccban           iBusinessPartnerBankFrom,
domain  tccban           iBusinessPartnerBankTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session 'Print Exception Errors'
(tfcmg1492m000).
Input:  iStartMode
Specifies the start mode for the session.
Not used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
(Below arguments are only valid if iIgnoreSelectionFields
is false)
iPaymentBatchFrom
From Payment Batch selection field
is filled with this value.
iPaymentBatchTo
To Payment Batch selection field
is filled with this value.
iPayToBusinessPartnerFrom
From Pay-to Business Partner selection field
is filled with this value.
iPayToBusinessPartnerTo
To Pay-to Business Partner selection field
is filled with this value.
iCurrencyFrom
From Currency selection field
is filled with this value.
iCurrencyTo
To Currency selection field
is filled with this value.
iBankFrom
From Bank selection field
is filled with this value.
iBankTo
To Bank selection field
is filled with this value.
iPaymentMethodFrom
From Payment Method selection field
is filled with this value.
iPaymentMethodTo
To Payment Method selection field
is filled with this value.
iBusinessPartnerBankFrom
From Business Partner Bank selection field
is filled with this value.
iBusinessPartnerBankTo
To Business Partner Bank selection field
is filled with this value.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0
Session started.
<> 0
Error.
```
