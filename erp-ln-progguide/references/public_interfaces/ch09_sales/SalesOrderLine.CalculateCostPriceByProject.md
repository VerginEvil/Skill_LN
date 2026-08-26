# SalesOrderLine.CalculateCostPriceByProject

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 336-337

```baan
DLL:   tdextslsapi
This function is available from     2026.02 (KB3649820  ).
Syntax: long SalesOrderLine.CalculateCostPriceByProject(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will calculate the PCS Project Cost for
the given sales order line. After that, the status of the
activity is set to 'Executed' and the cost price is updated on
the sales order line.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSalesOrder                           - Sales Order (Mandatory)
iSalesOrderLine                               - Sales Order Line (Mandatory)
iSalesOrderSequence                           - Sales Sequence number ( must be >= 0)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Calculate Standard Costs by Project" (tipcs3250m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Calculate              -options which are not available as Processing Options
will get defaulted in accordance with the defaults shown below.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
NAME                            TYPE                    DEFAULT
CalculateEstimatedCost          boolean                 true
CalculateActualCost             boolean                 false
EffectiveDate                   domain  tcdate          Current Date/Time
NetChangeOnly                   boolean                 false
SimulatedCalculation            boolean                 false
SimulationCalculationCode       domain tccpcc           ""
UpdateCOSDistribution           boolean                 false
RecalculateStandardParts        boolean                 false
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Calculation was successful
<> 0                                          - An error occurred
```
