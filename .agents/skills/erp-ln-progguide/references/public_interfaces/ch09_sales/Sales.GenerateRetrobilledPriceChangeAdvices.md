# Sales.GenerateRetrobilledPriceChangeAdvices

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 276-278

```baan
DLL:   tdextslsapi
This function is available from 2019.12 (KB2079838).
Syntax: long Sales.GenerateRetrobilledPriceChangeAdvices(
domain  tdsls.updn       iAdviceNumber,
domain  tcyesno          iSeparateAdviceLinesForReturnOrders,
boolean          iGenerateForOrders,
boolean          iGenerateForSchedules,
boolean          iGenerateForShipments,
domain  tcorno           iSalesOrderFrom,
domain  tcorno           iSalesOrderTo,
domain  tcorno           iSalesScheduleFrom,
domain  tcorno           iSalesScheduleTo,
domain  tdshpm           iShipmentFrom,
domain  tdshpm           iShipmentTo,
domain  tccono           iContractFrom,
domain  tccono           iContractTo,
domain  tcpono           iContractLineFrom,
domain  tcpono           iContractLineTo,
domain  tccom.bpid       iSoldToBusinessPartnerFrom,
domain  tccom.bpid       iSoldToBusinessPartnerTo,
domain  tccom.bpid       iShipToBusinessPartnerFrom,
domain  tccom.bpid       iShipToBusinessPartnerTo,
domain  tccom.bpid       iInvoiceToBusinessPartnerFrom,
domain  tccom.bpid       iInvoiceToBusinessPartnerTo,
domain  tcdate           iDateFrom,
domain  tcdate           iDateTo,
domain  tdsls.corg       iOrderOriginFrom,
domain  tdsls.corg       iOrderOriginTo,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
domain  tcccur           iCurrency,
domain  tdsls.utyp       iUpdateType,
domain  tcamnt           iUpdateAmount,
domain  tcprcg           iUpdatePercentage,
domain  tcyesno          iOnlyRetrobillingItems,
ref     domain  tdsls.updn       oAdviceNumber,
ref             long             oNumberOfAdviceLines,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate Retro-Billed Advices* and Advice Lines
based on the given input parameters. The price change is
calculated from the given Update Type, Update Amount and Update
Percentage.
* If the given Advice Number (iAdviceNumber) is a series, then
a new Advice header will be created based upon that series.
If it is an existing Advice, then the given Advice will be used.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  - iAdviceNumber                 - The ID of the Advice Header
Can be a series or an existing
Advice ID.
- iSeparateAdviceLinesForReturnOrders
-> Yes/No
Create separate advice lines for
linked sales return sales order
(invoice) lines.
- iGenerateForOrders            - True/False
Indicates if Retro Billed advices
must be generated for orders
- iGenerateForSchedules         - True/False
Indicates if Retro Billed advices
must be generated for schedules
- iGenerateForShipments         - True/False
Indicates if Retro Billed advices
must be generated for receipts
- iSalesOrderFrom               - Sales Order from
- iSalesOrderTo                 - Sales Order to
- iSalesScheduleFrom            - Sales Schedule from
- iSalesScheduleTo              - Sales Schedule to
- iShipmentFrom                 - Shipment from
- iShipmentTo                   - Shipment to
- iContractFrom                 - Contract from
- iContractTo                   - Contract to
- iContractLineFrom             - Contract Line from
- iContractLineTo               - Contract Line to
- iSoldToBusinessPartnerFrom    - Sold-to Business Partner from
- iSoldToBusinessPartnerTo      - Sold-to Business Partner to
- iShipToBusinessPartnerFrom    - Ship-to Business Partner from
- iShipToBusinessPartnerTo      - Ship-to Business Partner to
- iInvoiceToBusinessPartnerFrom - Invoice-to Business Partner from
- iInvoiceToBusinessPartnerTo   - Invoice-to Business Partner to
- iDateFrom                     - Date from
- iDateTo                       - Date to
- iOrderOriginFrom              - Order Origin from
- iOrderOriginTo                - Order Origin to
- iItemFrom                     - Item from
- iItemTo                       - Item to
- iCurrency                     - Currency
- iUpdateType                   - Update Type
The method used to update the existing
price of the sales document.
Possible values:
- Value:
The price update is a fixed amount.
- Percentage:
The price update is a percentage.
- iUpdateAmount                 - Update Amount
The value by which the existing price
of the specified sales documents is
updated.
- iUpdatePercentage             - Update Percentage
The percentage by which the existing
price of the specified sales
documents is updated.
- iOnlyRetrobillingItems        -> Yes/No
Only process Retrobilling items
Output: - oAdviceNumber         - The ID of the Advice Header that is used.
If the given Advice (iAdviceNumber)
did not exist yet, then this
argument contains the created
Advice.
- oNumberOfAdviceLines  - Number of Advice Lines generated
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function was executed successful.
Price change advices may have been
generated.
<> 0                    - An error occurred during the execution
of the function.
```
