# SalesQuote.Process

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 292-293

```baan
DLL:   tdextslsapi
This function is available from     2023.10 (KB2300933  ).
Syntax: long SalesQuote.Process(
domain  tcqono           iFromQuote,
domain  tccom.bpid       iFromSoldToBusinessPartner,
domain  tccwoc           iFromSalesOffice,
domain  tcqono           iToQuote,
domain  tccom.bpid       iToSoldToBusinessPartner,
domain  tccwoc           iToSalesOffice,
domain  tcseri           iSalesOrderSeries,
domain  tcpsts           iInitialProjectStatus,
domain  tcyesno          iConsolidateBySoldToBusinessPartner,
domain  tcyesno          iCopyAfterSalesServiceLines,
domain  tcyesno          iEquateProjectWithSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes a range of sales quotes to
sales orders. It is using the same logic and transaction
handling as the LN session 'Process Sales Quotations'.
(tdsls1200m000).
Pre:    LN Application sets retry              -point, so not by caller
Post:   LN Application sets commit/abort transaction, so not by caller
Input:  iFromQuote                                - From Quote selection field
is filled with this value.
iFromSoldToBusinessPartner                        - From Sold-to Business Partner
selection field is filled with
this value.
iFromSalesOffice                                  - From Sales Office selection
field is filled with this value.
iToQuote                                          - To Quote selection field is
filled with this value.
iToSoldToBusinessPartner                          - To Sold-to Business Partner
selection field is filled with
this value.
iToSalesOffice                                    - To Sales Office selection
field is filled with this value.
iSalesOrderSeries                                         - Sales Order Series,
optional.
iInitialProjectStatus                                     - Mandatory in case Project
Control(PCS) is
implemented.
iConsolidateBySoldToBusinessPartner                       - Consolidate by Sold-to
BusinessPartner, must be
Yes or No.
iCopyAfterSalesServiceLines                               - Copy After Sales Service
Lines, must be Yes or No.
iEquateProjectWithSalesOrder                              - Equate Project with Sales
Order, must be Yes or No.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```
