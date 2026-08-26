# ProjectPCS.PrintEstimatedCost

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 888-889

```baan
DLL:   tiextpcsapi
This function is available from     2024.12 (KB3519655  ).
Syntax: long ProjectPCS.PrintEstimatedCost(
domain  tipcs.ccgr       iCalculationGroup,
domain  tccprj           iProject,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to print Estimated Cost
Calculation by PCS Project. This Public Interface is similar to
session tipcs3471m000.
Pre:                  -
Post:                 -
Input:  iCalculationGroup                     - Calculation Group. Optional.
iProject                                      - Project for which the report must be
printed. Optional.
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default printing options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Print Estimated Cost Calculation by Project" (tipcs3471m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Print options which are not available as Processing Options
will get defaulted in accordance with the session logic.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
For the Processing Option "CurrencyForDetails" following values are
allowed :
tiusec.home.ref                       - Reference
tiusec.calc.office                    - Calculation Office
tiusec.any                            - Currency Total
NAME                                    TYPE                    DEFAULT
CalculationGroupFrom            domain  tipcs.ccgr      iCalculationGroup
CalculationGroupTo              domain  tipcs.ccgr      CalculationGroupFrom
when set. Otherwise
max domain value.
ProjectFrom                     domain  tccprj          iProjectFrom
ProjectTo                       domain  tccprj          ProjectFrom when
set. Otherwise max
domain value.
CurrencyForDetails              domain  tiusec          tiusec.home.ref.
CurrencyForTotals               domain  tcccur          Reference currency
of the company.
IncludeFixedCosts               domain  tcyesno         According to PCS
parameter: "Include
Fixed Costs in
Project Valuation".
Details                         domain  tcyesno         tcyesno.no.
PrintingDevice                  domain  tcmcs.str14     ""
PrintingFileoutPathAndName      domain  tcmcs.str100    ""
Output: oDataProcessed                        - true:  Data Printed.
false: Nothing Printed.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - OK.
<> 0                                          - Otherwise.
```
