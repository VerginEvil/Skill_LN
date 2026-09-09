# ConfigurableStructure.StartValidateRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 818-819

```baan
DLL:   tiextpcfapi
This function is available from 2026.10 (KB3684750).
Syntax: long ConfigurableStructure.StartValidateRevision(
long             iStartMode,
domain  tcitem           iProductFrom,
domain  tcitem           iProductTo,
domain  tibmrv           iRevisionFrom,
domain  tibmrv           iRevisionTo,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Validate
Configurable Structure (tipcf3260m200).
This session validates the configurable structures
for the specified product range (revision controlled).
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -
The parent session is blocked until the
child session exits.
MODELESS_ALWAYS -
Parent and child are parallel sessions that
can be manipulated simultaneously.
iProductFrom            - Product From (optional).
Project segment is disabled.
iProductTo              - Product To (optional).
Project segment is disabled.
iRevisionFrom           - Revision From (optional).
iRevisionTo             - Revision To (optional).
iProcessingOptionSet    - Processing Option Set.
If 0, then user default/session default
values are applied. A Processing Option
Set can be created via a call to
ProcessingOptionSet.Create() in DLL
tcextextapi. After the call the option
set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                            TYPE                    DEFAULT
PrintValidStructures            domain tcyesno          tcyesno.no
PrintingDevice                  domain tcmcs.str14      ""
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
