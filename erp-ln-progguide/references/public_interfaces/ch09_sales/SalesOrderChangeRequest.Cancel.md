# SalesOrderChangeRequest.Cancel

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderChangeRequest
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 368-369

```baan
DLL:   tdextslsapi
This function is available from     2026.04 (KB3666352  ).
Syntax: long SalesOrderChangeRequest.Cancel(
domain  tcorno           iChangeRequest,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function cancels the given sales order change request.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iChangeRequest                        - Sales Order Change Request (Mandatory)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default cancel options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Cancel Sales Order Change Request" (tdsls4201s300) and are
not explained in further detail here.
Please refer to the session help for additional information.
Supported Processing Options and their defaults:
NAME                            TYPE                    DEFAULT
------------------------------------------------------------------------
OrderHeaderAcknowledgementCode  domain tcmcs.str2       ""
OrderHeaderChangeOrderSequence  domain tcmcs.str8       ""
OrderHeaderChangeReason         domain tccdis           ""
OrderHeaderChangeType           domain tccdis           ""
OrderLineAcknowledgementCode    domain tcmcs.str2       ""
OrderLineChangeOrderSequence    domain tcmcs.str8       ""
OrderLineChangeReason           domain tccdis           ""
OrderLineChangeType             domain tccdis           ""
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     -> The change request has been cancelled
<> 0                          -> An error occurred
```
