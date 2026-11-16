# ConfigurableStructure.StartDetectLoops

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 817-818

```baan
DLL:   tiextpcfapi
This function is available from 2026.10 (KB3684752).
Syntax: long ConfigurableStructure.StartDetectLoops(
long             iStartMode,
domain  tcitem           iProduct,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Detect Loops in
Configurable Structures (tipcf3250m100).
This session detects loops in the configurable structures
for the specified product range.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session (Mandatory).
Possible values are:
MODAL -
The parent session is blocked until the
child session exits. The session will be started
as a zoom session.
MODELESS_ALWAYS -
Parent and child are parallel sessions that
can be manipulated simultaneously, even if the
session is a Dialog.
iProduct                - Product.
iProcessingOptionSet    - Processing Option Set.
If 0, then user default/session default
values are applied. A Processing Option
Set can be created via a call to
ProcessingOptionSet.Create() in DLL
tcextextapi. After the call the option
set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                            TYPE                    DEFAULT
ProductFrom                     domain tcitem           iProduct.
ProductTo                       domain tcitem           if ProductFrom
is not "" then
ProductFrom,
else
"ZZZZZZZ...." .
CheckForLoopsAgainstDate        domain tcyesno          empty.
AgainstDate                     domain tcutcs           Current Date.
StopAtFirstLoop                 domain tcyesno          empty.
PrintVerifiedStructures         domain tcyesno          empty.
AgainstDate is only applicable when CheckForLoopsAgainstDate is
tcyesno.yes
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started.
<> 0                    - Otherwise.
```
