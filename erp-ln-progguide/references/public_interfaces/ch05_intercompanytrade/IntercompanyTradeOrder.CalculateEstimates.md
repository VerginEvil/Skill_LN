# IntercompanyTradeOrder.CalculateEstimates

> Chapter: Chapter 5 Public Interfaces for IntercompanyTrade
>
> Group: Public Interfaces for IntercompanyTradeOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 159-161

```baan
DLL:   tcextitrapi
This function is available from 2026.08 (KB3683529).
Syntax: long IntercompanyTradeOrder.CalculateEstimates(
domain  tcncmp           iTradeOrderCompany,
domain  tcorno           iTradeOrder,
domain  tcpono           iTradeOrderLine,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oRecordUpdated,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface calculates the estimates for
Intercompany Trade Order lines.
Ranges can be specified via iProcessingOptionSet to process
multiple trade orders at once.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction().
Input:  iTradeOrderCompany      - Trade Order Company (Optional)
iTradeOrder             - Trade Order (Optional)
iTradeOrderLine         - Trade Order Line (Optional)
iDevice                 - Device for printing reports (Mandatory)
iProcessingOptionSet    - Optional, if 0, the default options
are applied.
Processing Options have a direct relationship with the
processing session Calculate Estimates
(tcitr3200m600) and are not explained in further detail here.
Please refer to the session help for additional information.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
TradeOrderCompanyFrom           domain tcncmp           Minimum Value
TradeOrderCompanyTo             domain tcncmp           Maximum Value
TradeOrderFrom                  domain tcorno           Minimum Value
TradeOrderTo                    domain tcorno           Maximum Value
TradeOrderLineFrom              domain tcpono           Minimum Value
TradeOrderLineTo                domain tcpono           Maximum Value
IncludeOpenOrders               domain tcyesno          tcyesno.yes
IncludeReadyForProcessOrders    domain tcyesno          tcyesno.no
PrintErrors                     domain tcyesno          tcyesno.yes
PrintUpdatedOrders              domain tcyesno          tcyesno.yes
ReportName                      domain tcmcs.str16      Empty String
ReportName only needs to filled for customized reports,
otherwise the standard report is automatically used.
ReportName must start with an "r", e.g. "rtcitr320011600"
When corresponding input parameters are filled, the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
When iTradeOrderCompany is empty and no TradeOrderCompanyFrom/To
is specified in the ProcessingOptionSet, the full range of
trade order companies is used.
When iTradeOrder is empty and no TradeOrderFrom/To is
specified in the ProcessingOptionSet, the full range of
trade orders is used.
When iTradeOrderLine is 0 and no TradeOrderLineFrom/To
is specified in the ProcessingOptionSet, the full range
of trade order lines is used.
Output: oRecordUpdated          - Indicates if at least one record
has been updated.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
