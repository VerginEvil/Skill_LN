# RequestForQuoteResponse.Accept

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for RequestForQuoteResponse
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 414-415

```baan
DLL:   tdextpurapi
This function is available from     2025.12 (KB3634332  ).
Syntax: long RequestForQuoteResponse.Accept(
domain  tcqono           iRequestForQuote,
domain  tcpono           iRequestForQuoteLine,
domain  tcpono           iRequestForQuoteResponseSequence,
domain  tccom.bpid       iRequestForQuoteBidder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function accepts a request for quotation response.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iRequestForQuote                      - Request for Quote (mandatory)
iRequestForQuoteLine                          - Request for Quote Line (mandatory)
iRequestForQuoteResponseSequence
-                                               Request for Quote Response Sequence (optional).
The database field "tdpur106.srnb" is used here
iRequestForQuoteBidder                        - Request for Quote Bidder (mandatory)
iProcessingOptionSet                          - Processing Option Set (optional).
If 0, the default options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Any options which are not available as Processing Option will get defaulted.
Processing Options which are set while a required Implemented Software Component
is not available are ignored.
Supported Processing Option and the default:
NAME                                            TYPE            DEFAULT
AcknowledgeUnacknowledgedNegotiationLine        domain tcyesno  tcyesno.yes
Yes: An unacknowledged negotiation line is automatically acknowledged
No:  An unacknowledged negotiation line is not automatically acknowledged
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information
Return: 0                                     - The Request for Quote is accepted
<> 0                                          - An error occurred
```
