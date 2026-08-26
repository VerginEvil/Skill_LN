# StandardCosts.CalculateSingleItem

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 610-612

```baan
DLL:   tiextcprapi
This function is available from     2025.06 (KB3537464  ).
Syntax: long StandardCosts.CalculateSingleItem(
domain  tccpcc           iCalculationCode,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
domain  tcccmt           iCalculationMethod,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface allows for calculation of standard cost
starting off of a single item. The calculation may be executed
top                      -down or single-level. When executed top-down, all items and
enterprise units in the product structure starting at the top
level Item/Enterprise Unit(s) will get addressed. Transaction
management is executed within this function, so no pending
transactions should be present before calling this function.
Pre:    N.A.
Post:   N.A.
Input:  iCalculationCode        Cost Calculation Code (Mandatory)
iItem                   Item (Mandatory)
Top                                              -level item to calculate.
Only supports single item calculations.
It is not allowed to calculate the cost
for a project item.
iEnterpriseUnit         Enterprise Unit
May only be given when the concept
Standard Cost by Enterprise Unit is
active.
Mandatory for the case, when the Item
uses Standard Cost by Enterprise Unit
and the Calculation Method is single                                              -level.
If left empty, then, by default,
standard cost is calculated for all
related Enterprise Units.
The Enterprise Unit that serves as the
starting point for the calculation.
Note that in case of top                                              -down
calculation, cost for other Enterprise
Units will get calculated because of
dependencies.
iCalculationMethod      Calculation Method (Mandatoty)
Either top                                              -down or single-level
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields on
session Calculate Standard Cost (ticpr2210m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
NAME                            TYPE                    DEFAULT
EnterpriseUnitFrom              tcemm.grid (string)     ""
EnterpriseUnitTo                tcemm.grid (string)     "ZZZZZZZZZ"
CalculationDate                 tcdate                  Current date
IncludeStandardSubassemblies    tcyesno                 tcyesno.no
PrintErrorReport                tcyesno                 tcyesno.no
PrintingDeviceErrorReport       tcmcs.str14             ""
PrintingFileoutPathAndNameErrorReport
tcmcs.str100            ""
If PrintErrorReport is tcyesno.yes then the error report will be printed.
If it is tcyesno.no then errors will be logged in exception structure.
Output:
oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Successfully calculated the standard costs.
<> 0                    Errors occurred.
```
