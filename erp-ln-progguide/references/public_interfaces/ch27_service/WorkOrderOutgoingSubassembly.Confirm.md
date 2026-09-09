# WorkOrderOutgoingSubassembly.Confirm

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrderOutgoingSubassembly
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1519-1520

```baan
DLL:   tsextwcsapi
This function is available from 2026.06 (KB3671833).
Syntax: long WorkOrderOutgoingSubassembly.Confirm(
domain  tcorno           iWorkOrder,
domain  tcpono           iSubassemblyLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to confirm the given Outgoing Subassembly.
Pre:    Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Input:  iWorkOrder
Work Order number: Mandatory
iSubassemblyLine
Subassembly Line number: Mandatory
iProcessingOptionSet
Processing Option Set:
A processing option set number referring to a processing
option set: Optional.
NAME                    TYPE                    DEFAULT
================================================================
ContinueIfIncomingSubassemblyLinkedToHeader
domain  tsyesno         tsyesno.no
If the Incoming Subassembly linked to this Outgoing
Subassembly is directly linked to the Work Order header
and the Incoming Subassembly Action is not "No Action"
and this option is set to 'No', this Outgoing
Subassembly will not be confirmed.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - Subassembly was confirmed successfully
<> 0    - Error during confirming the Outgoing Subassembly
```
