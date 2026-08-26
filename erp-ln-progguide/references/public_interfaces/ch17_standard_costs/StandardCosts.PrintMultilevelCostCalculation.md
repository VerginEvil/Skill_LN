# StandardCosts.PrintMultilevelCostCalculation

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 612-613

```baan
DLL:   tiextcprapi
This function is available from     2024.09 (KB2329136  ).
Syntax: long StandardCosts.PrintMultilevelCostCalculation(
domain  tcitem           iItem,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to print Multilevel Cost
Calculation report (ticpr2420m000). This function makes use of a
Processing Option Set, which can be created via a call to
ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete().
Pre:    N.A.
Post:   N.A.
Input:  iItem               -         Item for which the standard cost should be
calculated (Optional).
iProcessingOptionSet                       -
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
If 0, then user default/session default values
are applied (Optional).
Processing Options have a direct relationship with the form fields
on session Print Multilevel Cost Calculation (ticpr2420m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
Print Multilevel Cost Calculation options which are not available as
Processing Options will get defaulted in accordance with the session
logic.
NAME                            TYPE                    DEFAULT
CostCalculationCode             domain  tccpcc          standard cost
calculation code
EffectivityUnit                 domain  tcuef.effn      0
CalculationDate                 domain  tiutcs          current date
EnterpriseUnitFrom              domain  tcemm.grid      ""
EnterpriseUnitTo                domain  tcemm.grid      "ZZZZZZZZZ"
Currency                        domain  tcccur          ""
PredefinedOrderQuantityMainItem domain  tcyesno         tcyesno.yes
UseOrderQuantity                domain  tiqep1          0.0
PredefinedOrderQuantitySubItems domain  tcyesno         tcyesno.yes
IncludeFixedCosts               domain  tcyesno         tcyesno.yes
RecalculateStandardParts        domain  tcyesno         tcyesno.no
CalculationCodeStandardParts    domain  tccpcc          ""
PrintDetailsByComponent         domain  tcyesno         tcyesno.no
PrintHighPrecision              domain  tcyesno         tcyesno.yes
PrintingDevice                  domain  tcmcs.str14     ""
PrintingFileoutPathAndName      domain  tcmcs.str100    ""
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Print Multilevel Cost Calculation
is successfully.
<> 0                                          - Otherwise.
```
