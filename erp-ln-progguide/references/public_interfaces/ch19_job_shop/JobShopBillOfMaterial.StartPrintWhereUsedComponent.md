# JobShopBillOfMaterial.StartPrintWhereUsedComponent

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 651-652

```baan
DLL:   tiextbomapi
This function is available from     2025.09 (KB3564855  ).
Syntax: long JobShopBillOfMaterial.StartPrintWhereUsedComponent(
long             iStartMode,
domain  tcitem           iItem,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts the session Print Where-Used BOM
Components(tibom1412m000). This session print reports that
show, for one or more items, the manufactured item in which
they are used as a component or in which end items certain
component items occur.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                                 -       The parent session is blocked until
the child session exits, the session
will be started as a zoom session.
MODELESS_ALWAYS                               -
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dailog.
iItem                   Item
iProcessingOptionSet    Processing Option Set.
If 0, then user default/session default
values are applied.A Processing Option
Set can be created via a call to
ProcessingOptionSet.Create()in DLL
tcextextapi. After the call the option
set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields on
session Calculate Sales Prices (ticpr2250m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
NAME                            TYPE            DEFAULT
ItemFrom                        tcitem          ""
ItemTo                          tcitem          "ZZZZZZZZZZZZ.."
PrintOptionsReportLevel         tirep.bomlvl    empty
ReportType                      tirep.pbomopt   empty
ValidateComponentsAgainstDates  tcyesno         empty
Date                            tiutcs          0
PrintProductionBOMTexts         tcyesno         empty
TextLanguage                    tcclan          ""
SortBy                          tirep.bycomp    tirep.bycomp.component
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started successfully.
<> 0                    Errors occurred.
```
