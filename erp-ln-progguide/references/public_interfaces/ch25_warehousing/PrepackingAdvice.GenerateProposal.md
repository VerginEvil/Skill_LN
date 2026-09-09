# PrepackingAdvice.GenerateProposal

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PrepackingAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1320-1321

```baan
DLL:   whextwmdapi
This function is available from 2026.08 (KB3680199).
Syntax: long PrepackingAdvice.GenerateProposal(
domain  whinh.gnps       iAction,
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLineFrom,
domain  tcpono           iShipmentLineTo,
domain  tcpono           iReferenceSequenceFrom,
domain  tcpono           iReferenceSequenceTo,
domain  whinh.oalg       iAdviceLog,
domain  tcmcs.str15      iDevice,
domain  tcyesno          iPrintReport,
domain  tcmcs.str16      iReportName,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will generate, delete or regenerate
proposed stock points for the given selection range.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iAction                 - Action (Mandatory)
Possible values:
- whinh.gnps.delete (Delete)
- whinh.gnps.generate (Generate)
- whinh.gnps.regenerate (Regenerate)
iShipment               - Shipment (Mandatory)
iShipmentLineFrom       - From Shipment Line (Optional)
iShipmentLineTo         - To Shipment Line (Optional)
iReferenceSequenceFrom  - From Reference Sequence (Optional)
iReferenceSequenceTo    - To Reference Sequence (Optional)
iPrintReport            - Print Report (Mandatory)
Possible values:
- tcyesno.yes (print the report)
- tcyesno.no (don't print the report)
iAdviceLog              - Advice Log (Optional)
iDevice                 - Device (Mandatory if iPrintReport is yes)
iReportName             - Customized Report Name (Optional).
iReportName only needs to filled for
customized reports, otherwise the standard
report is automatically used.
iReportName must start with an "r",
e.g. "rwhwmd425711000".
Output: oExceptionMessage       - The last message if any message is found.
If more than one message is given,
these are present in the oExceptionID.
oExceptionID            - An ID that refers to all error information.
Use the functions in Exception to get
all relevant information.
Return: 0       - Proposed Stock Points processed successfully
<> 0    - Error
```
