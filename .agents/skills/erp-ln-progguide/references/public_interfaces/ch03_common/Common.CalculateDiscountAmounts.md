# Common.CalculateDiscountAmounts

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 93-94

```baan
DLL:   tcextmcsapi
This function is available from 2024.01 (KB2305449).
Syntax: long Common.CalculateDiscountAmounts(
domain  tcncmp           iFinancialCompany,
domain  tccpay           iPaymentTerms,
domain  tcccur           iInvoiceCurrency,
domain  tcamnt           iInvoiceAmount,
domain  tcamnt           iTaxAmount,
ref     domain  tcmcs.long       oNumberOfScheduleLines,
ref     domain  tcamnt           oScheduleLineAmountArray(),
ref     domain  tcamnt           oFirstDiscountAmountArray(),
ref     domain  tcamnt           oSecondDiscountAmountArray(),
ref     domain  tcamnt           oThirdDiscountAmountArray(),
ref     domain  tcmcs.s250m      oErrorMessage mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to calculate the schedule amounts
and the discount amounts for a certain payment terms.
If a schedule is linked to the payment terms, the calculated
amounts are based on the schedule line details of tcmcs221. If
no schedule is linked to the payment terms, the calculated
amounts are based on the payment terms details of tcmcs013.
Pre:    The array output arguments should be declared as BASED.
Post:   Free the allocated memory of the arrays.
Input:  iFinancialCompany       - Financial Company
This is a Mandatory field.
iPaymentTerms           - Payment Terms
This is a Mandatory field.
iInvoiceCurrency        - Invoice Currency
This is a Mandatory field.
iInvoiceAmount          - Invoice Amount
iTaxAmount              - Tax Amount
Output: oNumberOfScheduleLines  - Number of Schedule Lines
oScheduleLineAmountArray -
Array of Schedule Line Amount
oFirstDiscountAmountArray -
Array of First Discount Amount
oSecondDiscountAmountArray -
Array of Second Discount Amount
oThirdDiscountAmountArray -
Array of Third Discount Amount
oErrorMessage           - Error Message
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success
<> 0                    - Error calculating the discount amounts
```
