# RequestForQuote.StartCancel

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for RequestForQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 410-411

```baan
DLL:   tdextpurapi
This function is available from     2026.04 (KB3654355  ).
Syntax: long RequestForQuote.StartCancel(
long             iStartMode,
domain  tcqono           iRequestForQuote,
domain  tcpono           iRequestForQuoteLine,
domain  tcpono           iRequestForQuoteSequence,
domain  tcpono           iRequestForQuoteAlternative,
domain  tccom.bpid       iRequestForQuoteBidder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function starts the session Cancel Request for Quotation
(tdpur1200m000). Depending on the input different instances of
the Cancel Request for Quotation session can be started:
| Field:                          \   Combination: |1|2|3|4|5|6
|                      ----------------------------|---|---|---|---|---|---
| iRequestForQuote           | F | F | F | F | F | F
| iRequestForQuoteLine       | E | F | F | E | F | F
| iRequestForQuoteSequence   | E | E | E | E | F | E
| iRequestForQuoteAlternative| E | E | F | E | E | F
| iRequestForQuoteBidder     | E | E | E | F | F | F
F = Filled, E = Empty
Depending on the input, the following instance is started::
1. Cancel Request for Quotation
2. Cancel Request for Quotation Line
3. Cancel Request for Quotation Alternative
4. Cancel Request for Quotation Bidder
5. Cancel Request for Quotation Response
6. Cancel Request for Quotation Response Preparations
Pre:    N/A
Post:   N/A
Input:  iStartMode                            - Not used
iRequestForQuote                              - Request for Quote (mandatory).
iRequestForQuoteLine                          - Request for Quote Line (optional)
iRequestForQuoteSequence
-                                               Request For Quote Sequence (optional)
iRequestForQuoteAlternative
-                                               Request For Quote Alternative (optional)
iRequestForQuoteBidder                        - Request for Quote Bidder (optional)
iProcessingOptionSet                          - Processing Option Set (optional).
If 0, the default options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Supported Processing Options and their defaults:
NAME                              TYPE                  DEFAULT
------------------------------------------------------------------------
CancelReasonForRFQ                domain tccdis         Empty
CancelTypeForRFQ                  domain tccdis         Empty
CancelReasonForRFQBidders         domain tccdis         Empty
CancelTypeForRFQBidders           domain tccdis         Empty
CancelReasonForRFQLines           domain tccdis         Empty
CancelTypeForRFQLines             domain tccdis         Empty
CancelReasonForRFQResponses       domain tccdis         Empty
CancelTypeForRFQResponses         domain tccdis         Empty
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information
Return: 0                                     - Session started
<> 0                                          - An error occurred
```
