# Purchase.GenerateRetrobilledPriceChangeAdvices

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for Purchase
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 394-397

```baan
DLL:   tdextpurapi
This function is available from     2019.12 (KB2079838  ).
Syntax: long Purchase.GenerateRetrobilledPriceChangeAdvices(
domain  tcorno           iAdviceNumber,
boolean          iGenerateForOrders,
boolean          iGenerateForSchedules,
boolean          iGenerateForReceipts,
domain  tcorno           iPurchaseOrderFrom,
domain  tcorno           iPurchaseOrderTo,
domain  tcpono           iOrderLineFrom,
domain  tcpono           iOrderLineTo,
domain  tcorno           iPurchaseScheduleFrom,
domain  tcorno           iPurchaseScheduleTo,
domain  tcorno           iReceiptFrom,
domain  tcorno           iReceiptTo,
domain  tdpur.corg       iOrderOriginFrom,
domain  tdpur.corg       iOrderOriginTo,
domain  tccom.bpid       iBuyFromBusinessPartnerFrom,
domain  tccom.bpid       iBuyFromBusinessPartnerTo,
domain  tccom.bpid       iShipFromBusinessPartnerFrom,
domain  tccom.bpid       iShipFromBusinessPartnerTo,
domain  tccom.bpid       iInvoiceFromBusinessPartnerFrom,
domain  tccom.bpid       iInvoiceFromBusinessPartnerTo,
domain  tccono           iContractFrom,
domain  tccono           iContractTo,
domain  tcpono           iContractLineFrom,
domain  tcpono           iContractLineTo,
domain  tcdate           iDateFrom,
domain  tcdate           iDateTo,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
domain  tdpur.utyp       iUpdateType,
domain  tcprcg           iUpdatePercentage,
domain  tcamnt           iUpdateAmount,
domain  tcccur           iCurrency,
domain  tcyesno          iShowProgressIndicator,
ref     domain  tcorno           oAdviceNumber,
ref             boolean          oAdviceLinesGenerated,
ref             boolean          oProcessStopped,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate Retro-Billed Advices* and Advice Lines
based on the given input parameters. The price change is
calculated from the given Update Type, Update Amount and Update
Percentage.
* If the given Advice Number (iAdviceNumber) is a series, then
a new Advice header will be created based upon that series.
If it is an existing Advice, then the given Advice will be used.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iAdviceNumber                         -  Advice Number.
Can be a series or an existing
Advice ID.
iGenerateForOrders                            -  True/False
Indicates if Retro Billed advices
must be generated for orders.
iGenerateForSchedules                         -  True/False
Indicates if Retro Billed advices
must be generated for schedules
iGenerateForReceipts                          -  True/False
Indicates if Retro Billed advices
must be generated for receipts
iPurchaseOrderFrom                            -  Purchase Order from
iPurchaseOrderTo                              -  Purchase Order to
iOrderLineFrom                                -  Purchase Position from
iOrderLineTo                                  -  Purchase Position to
iPurchaseScheduleFrom                         -  Purchase Schedule from
iPurchaseScheduleTo                           -  Purchase Schedule to
iReceiptFrom                                  -  Receipt from
iReceiptTo                                    -  Receipt to
iOrderOriginFrom                              -  Order Origin from
iOrderOriginTo                                -  Order Origin to
iBuyFromBusinessPartnerFrom
-                                                Buy-from Business Partner from
iBuyFromBusinessPartnerTo
-                                                Buy-from Business Partner to
iShipFromBusinessPartnerFrom
-                                                Ship-from Business Partner from
iShipFromBusinessPartnerTo
-                                                Ship-from Business Partner to
iInvoiceFromBusinessPartnerFrom
-                                                Invoice-from Business Partner from
iInvoiceFromBusinessPartnerTo
-                                                Invoice-from Business Partner to
iContractFrom                                 -  Contract from
iContractTo                                   -  Contract to
iContractLineFrom                             -  Contract Line from
iContractLineTo                               -  Contract Line to
iDateFrom                                     -  Date from
iDateTo                                       -  Date to
iItemFrom                                     -  Item from
iItemTo                                       -  Item to
iUpdateType                                   -  Update Type
The method used to update the existing
price of the purchase document.
Possible values:
-                                                  Value:
The price update is a fixed amount.
-                                                  Percentage:
The price update is a percentage.
iUpdatePercentage                             -  Update Percentage
The percentage by which the existing
price of the specified purchase documents is
updated.
iUpdateAmount                                 -  Update Amount
The value by which the existing price
of the specified purchase documents is updated.
iCurrency                                     -  Currency
iShowProgressIndicator                        -  Yes/No
Indicates if showing the
progress indicator is allowed.
Yes: If applicable, the progress
indicator is shown.
No:  The progress indicator
will not be shown.
Output: oAdviceNumber                         -  Advice Header that is used.
If the given Advice (iAdviceNumber)
did not exist yet, then this
argument contains the created
Advice.
oAdviceLinesGenerated                         - True/False
Indicates if advice lines have been
generated.
oProcessStopped                               - True/False
Indicates if the process was aborted
by the user.
oExceptionMessage                             - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Function was executed successfull.
Price change advices may have been
generated.
<> 0                                          - An error occurred during the execution
of the function.
```
