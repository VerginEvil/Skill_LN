# Common.CalculateDueDates

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 93-94

```baan
DLL:   tcextmcsapi
This function is available from     2025.01 (KB3540996  ).
Syntax: long Common.CalculateDueDates(
domain  tcncmp           iFinancialCompany,
domain  tccpay           iPaymentTerms,
domain  tcccp.ccal       iCalendar,
domain  tcccp.ract       iAvailabilityType,
domain  tcgld.date       iInvoiceDate,
ref     domain  tcmcs.long       oNumberOfScheduleLines,
ref     domain  tcgld.date       oDueDateArray(),
ref     domain  tcgld.date       oFirstDiscountDateArray(),
ref     domain  tcgld.date       oSecondDiscountDateArray(),
ref     domain  tcgld.date       oThirdDiscountDateArray(),
ref     domain  tcmcs.s250m      oErrorMessage mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to calculate the due dates and
the discount dates for a certain payment terms.
If a schedule is linked to the payment terms, the calculated
dates are based on the schedule line details of tcmcs221. If no
schedule is linked to the payment terms, the calculated dates
are based on the payment terms details of tcmcs013.
Pre:    The array output arguments should be declared as BASED.
Post:   Free the allocated memory of the arrays.
Input:  iFinancialCompany                     - Financial Company
This is a Mandatory field.
iPaymentTerms                                 - Payment Terms
This is a Mandatory field.
iCalendar                                     - Calendar
iAvailabilityType                             - Availability Type
iInvoiceDate                                  - Invoice Date
Default set to Current Date if passed
empty.
Output: oNumberOfScheduleLines                - Number of Schedule Lines
oDueDateArray                                 - Array of Due Dates
oFirstDiscountDateArray                       - Array of First Discount Date
oSecondDiscountDateArray                      - Array of Second Discount Date
oThirdDiscountDateArray                       - Array of Third Discount Date
oErrorMessage                                 - Error Message
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Success
<> 0                                          - Error calculating the due dates
```
