# BOD.ExecuteRequest

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1666-1667

```baan
DLL:   tcextbodapi
This function is available from 2022.06 (KB2246414).
Syntax: long BOD.ExecuteRequest(
long             iXMLRequest,
ref             long             oXMLAcknowledge,
ref             long             oXMLConfirm,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes an incoming request for a public BOD. The
incoming request should be a BOD XML file in the same format as
a BOD XML file that is received from ION. This function can be
used in a custom LN program that builds a BOD XML file (e.g a
ProcessSalesOrder or a SyncPerson) and calls this function to
process this BOD request in LN (e.g. create or update the sales
order, or create an employee). The processing is similar to the
Test Business Object Method (tlbct3232m000) session in which
the Is BOD check box is selected.
A request that is part of a batch is not supported.
Tools TIV must be greater than or equal to 2430.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iXMLRequest             - BOD XML structure with request. Mandatory.
Output: oXMLAcknowledge         - XML structure with Acknowledge BOD. This
XML structure is returned if the incoming
request has the Process verb. If the incoming
request has another verb, 0 is returned.
oXMLConfirm             - XML structure with Confirm BOD. This XML
structure is returned if the incoming BOD
XML request was not processed successfully.
It contains the errors that occurred during
processing the incoming BOD XML request. If
no errors occurred, 0 is returned.
oExceptionMessage       - A message if the return value is not equal
to 0. This message contains the root cause of
the request failure.
oExceptionID            - An ID that refers to all error information
if the return value is <> 0. It includes
errors that originate from the Confirm BOD.
Use the functions in Exception to get
all relevant information.
Return:
0                       - The BOD request was processed successfully.
<> 0                    - The BOD request was not processed
successfully.
```
