# InspectionOrderLine.Complete

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for InspectionOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1784-1784

```baan
DLL:   qmextptcapi
This function is available from 2023.09 (KB2288392).
Syntax: long InspectionOrderLine.Complete(
domain  tcorno           iInspection,
domain  tcpono           iInspectionLine,
boolean          iEvaluateAlgorithm,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the completion of Inspection Order Lines.
When the iInspectionLine is zero all Inspection Lines related to
the Inspection Order which are not completed will be completed.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iInspection - QM Inspection Order that needs to be completed
(mandatory)
iInspectionLine - QM Inspection Order Line that needs to be
completed (not mandatory)
iEvaluateAlgorithm - Evaluate Algorithm to evaluate test data lines
related to the testing algorithm for which test results
are not inspected.(mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Inspection Order Line(s) has been completed successfully
<>0     - Error.
```
