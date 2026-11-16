# StandardCosts.Actualize

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 604-605

```baan
DLL:   tiextcprapi
This function is available from 2025.04 (KB3536706).
Syntax: long StandardCosts.Actualize(
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Actualize and revalue the current calculated standard cost for
the given Item. The process behind this function is similar to
the execution of the session Actualize Standard Cost and Revalue
Inventory (ticpr2220m000). Transaction management is executed
within this function, so no pending transactions should be
present before calling this function.
Pre:    N.A.
Post:   N.A.
Input:  iItem                   Item should be standard item and project
should be empty.
iEnterpriseUnit         Enterprise Unit
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields on
session Actualize Standard Cost and Revalue Inventory (ticpr2220m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
NAME                            TYPE                    DEFAULT
EnterpriseUnitFrom              tcemm.grid (string)     ""
EnterpriseUnitTo                tcemm.grid (string)     "ZZZZZZZZZ"
OnlyItemsWithoutStandardCost    tcyesno                 tcyesno.no
DeleteStandardCostHistoryData   tcyesno                 tcyesno.no
EffectiveDate                   tcdate                  current date
LastDateOfPreviousPeriod        tcyesno                 tcyesno.no
ReverseToOriginal               tcyesno                 tcyesno.no
PrintHoursValues                tcyesno                 tcyesno.yes
PrintReport                     tcyesno                 tcyesno.no
PrintingDevice                  tcmcs.str14             ""
PrintingFileoutPathAndName      tcmcs.str100            ""
PrintErrorReport                tcyesno                 tcyesno.no
PrintingDeviceErrorReport       tcmcs.str14             ""
PrintingFileoutPathAndNameErrorReport
tcmcs.str100            ""
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Successfully standardized costs.
<> 0                    Errors occurred.
```
