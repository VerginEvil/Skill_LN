# ProductionOrder.PrintSubcontractingNote

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 746-747

```baan
DLL:   tiextsfcapi
This function is available from     2024.05 (KB2308452  ).
Syntax: long ProductionOrder.PrintSubcontractingNote(
domain  tcsite           iSite,
domain  tcorno           iProductionOrder,
domain  tcopno           iOperationFrom,
domain  tcopno           iOperationTo,
domain  tcemm.grid       iEnterpriseUnit,
boolean          iPrintSpecification,
boolean          iPrintOriginal,
boolean          iPrintDuplicate,
boolean          iPrintModified,
domain  tcmcs.str15      iPrintDevice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Function is used to print Production Order Subcontracting Note
Report.
Enterprise Unit limits the printing of reports to only those
work centers that belong to the given Enterprise Unit.
Control for printing Original/Duplicate/Modified is provided.
In case, more than one option is true then system will determine
which Report Type can be printed based on the document status.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory).
iOperationFrom          Range of Operation From (Mandatory).
iOperationTo            Range of Operation To (Mandatory).
iEnterpriseUnit         Enterprise Unit for which production
order documents must be printed.
iPrintSpecification     Control for printing Specifications.
iPrintOriginal          Control for printing Original Document.
iPrintDuplicate         Control for printing Duplicate Document.
iPrintModified          Control for printing Modified Document.
iPrintDevice            Device for Printing the Report.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Subcontracting Note Printed.
<> 0                    Errors occurred.
```
