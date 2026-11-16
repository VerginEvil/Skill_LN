# ProductionOrder.PrintCustomReports

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2155-2156

```baan
Production Order Custom Reports.
This process extension is available from 2022.10 (KB2262990).
Technical information for this process extension:
Usage:        With this Process Extension it is possible to integrate Custom Linked
Reports to the session Print Production Order Documents (tisfc0408m000)
as additions to the Production Order's standard document set. The
extension provides hooks for:
- Registration of the Custom Linked Reports
(method tiext.sfc0001.register.custom.reports).
- Decision logic to decide whether or not for a specific order the
document should be printed
(method tiext.sfc0001.check.print.condition).
- The retrieval of required data and sending it to the report driver
(method tiext.sfc0001.print.custom.report).
- The update of the print status for the report
(method tiext.sfc0001.update.print.status).
Note that for this Process Extension to work, in session extension Print
Production Order Documents (tisfc0408m000), each Custom Linked Report
must be added as the single report in a new report group.
To implement this process extension, you need to implement the following method(s):
```
