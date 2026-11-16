# EngineeringBillOfMaterial.GenerateMBCCopyData

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 261-261

```baan
DLL:   tiextedmapi
This function is available from 2026.09 (KB3633088).
Syntax: long EngineeringBillOfMaterial.GenerateMBCCopyData(
domain  tcorno           iMBCNumber,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface processes the MBC numbers and copy data.
It works similarly to the session Process MBC (tiedm3250m000)
with Copy data options.
Transaction handling is done in this public Interface.
Pre:    N.A.
Post:   N.A.
Input:  iMBCNumber              Mass BOM Change Number.
iProcessingOptionSet    Processing Option Set.
If 0, then user default/session default
values are applied. A Processing Option
Set can be created via a call to
ProcessingOptionSet.Create() in DLL
tcextextapi. After the call the option
set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                            TYPE                    DEFAULT
MBCNumberFrom                   domain tcorno           ""
MBCNumberTo                     domain tcorno           ZZZZZZZZZ
OverwriteExistingEBOMCopyData   domain tcyesno          tcyesno.yes
PrintErrorReport                domain tcyesno          tcyesno.no
PrintingDeviceErrorReport       domain tcmcs.str14      ""
PrintingFileoutPathAndNameErrorReport
domain tcmcs.str100     ""
Default values:
MBCNumberFrom    -      If the input variable field iMBCNumber is
given, it will be used as the default value,
otherwise it will be defaulted with blank.
MBCNumberTo      -      If MBCNumberFrom field is set, then
MBCNumberTo field will be the defaulted
with MBCNumberFrom field or If input variable
"MBCNumberFrom" is given, it will be used as
default value, otherwise the MBCNumberTo field
will be defaulted to the maximum domain value
(i.e. "ZZZZZZZZZ").
If PrintErrorReport is tcyesno.yes, then the error(s) will be printed
in the report.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Generated EBOM copy data successfully.
<> 0                    Error Occurred.
```
