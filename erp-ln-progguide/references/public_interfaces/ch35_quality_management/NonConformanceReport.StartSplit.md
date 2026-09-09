# NonConformanceReport.StartSplit

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for NonConformanceReport
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1794-1794

```baan
DLL:   qmextncmapi
This function is available from 2024.02 (KB2313189).
Syntax: long NonConformanceReport.StartSplit(
domain  tcorno           iNonConformanceReport,
domain  tcorno           iNonConformanceReportSeries,
domain  tcqiv1           iSplitQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Split Non-Conformance Material Report
(qmncm1200m100) in MODAL mode.
Input:  iNonConformanceReport   - Non-Conformance Report; Mandatory
iNonConformanceReportSeries     - Split/New NCMR Series; Not Mandatory
iSplitQuantity          - Split Quantity; Not Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
