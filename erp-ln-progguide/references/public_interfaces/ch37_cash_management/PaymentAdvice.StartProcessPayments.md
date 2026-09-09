# PaymentAdvice.StartProcessPayments

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for PaymentAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1808-1809

```baan
DLL:   tfextcmgapi
This function is available from 2021.06 (KB2178744).
Syntax: long PaymentAdvice.StartProcessPayments(
long             iStartMode,
domain  tfgld.user       iUserFrom,
domain  tfgld.user       iUserTo,
domain  tfgld.btno       iPaymentBatchFrom,
domain  tfgld.btno       iPaymentBatchTo,
domain  tfcmg.stpp       iPaymentBatchStatusFrom,
domain  tfcmg.stpp       iPaymentBatchStatusTo,
domain  tfgld.date       iBatchCreationDateFrom,
domain  tfgld.date       iBatchCreationDateTo,
domain  tfcmg.paym       iPaymentProcessDefaultID,
domain  tfcmg.bank       iDefaultBankRelation,
domain  tfgld.desc       iTextForRemittance mb,
domain  tcyesno          iIncludeRemittanceIDInReference,
domain  tcmcs.str3       iSuffix,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Process Payments (tfcmg1240m000)
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
iUserFrom               - User From             Not Mandatory
iUserTo                 - User To               Not Mandatory
iPaymentBatchFrom       - Payment Batch From    Not Mandatory
iPaymentBatchTo         - Payment Batch To      Not Mandatory
iPaymentBatchStatusFrom - Payment Batch Status From     Not Mandatory
iPaymentBatchStatusTo   - Payment Batch Status To       Not Mandatory
iBatchCreationDateFrom  - Batch Creation Date From      Not Mandatory
iBatchCreationDateTo    - Batch Creation Date To        Not Mandatory
iPaymentProcessDefaultID        -Payment Process Default ID     Not
Mandatory
iDefaultBankRelation    - Default Bank Relation Not Mandatory
iTextForRemittance      - Text For Remittance   Not Mandatory
iIncludeRemittanceIDInReference - Include Remittance ID in Reference
Not Mandatory
iSuffix                 -Suffix                 Not Mandatory
Output: for iStartMode MODAL:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
