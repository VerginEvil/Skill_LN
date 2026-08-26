# QuarantineInventoryDispositionLine.GenerateInboundAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryDispositionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1212-1213

```baan
DLL:   whextwmdapi
This function is available from     2025.07 (KB3590515  ).
Syntax: long QuarantineInventoryDispositionLine.GenerateInboundAdvice(
domain  tcorno           iQuarantineIdentifier,
domain  tcmcs.long       iDispositionLine,
domain  whloca           iPreferenceLocation,
boolean          iPutAway,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface generates an inbound advice for the
quarantine inventory disposition classified as 'Use As Is' or
'No Fault Found'.
Optionally, it can be put away directly.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier                 - Quarantine ID (Mandatory)
iDispositionLine                              - Disposition Line (Mandatory)
iPreferenceLocation                           - Advise will preferably be generated
to this location. (Optional)
iPutAway                                      - Directly Put Away (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Disposition line has been advised
succesfully.
<> 0                                          - Error.
```
