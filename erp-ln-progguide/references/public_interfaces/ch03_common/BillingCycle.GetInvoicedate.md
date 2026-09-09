# BillingCycle.GetInvoicedate

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BillingCycle
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 140-140

```baan
DLL:   tcextmcsapi
This function is available from 2024.09 (KB3519213).
Syntax: long BillingCycle.GetInvoicedate(
domain  tcncmp           iCompany,
domain  tcbicy           iBillingCycle,
domain  tcdate           iCutOffDate,
domain  tcdate           iDeliveryDate,
domain  tcamnt           iBillableLineAmount,
domain  tcccur           iBillableLineCurrency,
domain  tcdate           iRateDate,
domain  tcrtyp           iRateType,
ref     domain  tcdate           oInvoiceDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to determine the next invoice
date for a billing cycle (including time). The next invoice
date is determines using the recurrence from the billing cycle
of the billable line.
Note:
1) If the input Billing Cycle is empty then the input Cut off
Date is returned as the Invoice Date. In this case if Cut
off Date is passed as 0 then Invoice Date 0 is returned.
2) If Billing Cycle is filled and if input Cut-off Date is 0
then current date is used.
3) If Delivery date is 0 then current date is used.
Pre:    preconditions
Post:   postconditions
Input:  iCompany                - Company Number
iBillingCycle           - Billing Cycle
iCutOffDate             - Current Cut off Date / Invoice Date
iDeliveryDate           - Delivery Date
iBillableLineAmount     - Line Amount of the Billable line
iBillableLineCurrency   - Currency of Billable Line
iRateDate               - Rate Date of the Billable Line
iRateType               - Rate Type of the Billable Line
Output: oInvoiceDate            - New Invoice Date based on Billing
Cycle
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - New Invoice Date determined
successfully
<> 0                    - Error
```
