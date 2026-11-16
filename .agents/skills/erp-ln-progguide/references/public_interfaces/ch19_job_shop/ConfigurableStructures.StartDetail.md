# ConfigurableStructures.StartDetail

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 820-821

```baan
DLL:   tiextpcfapi
This function is available from 2026.10 (KB3684755).
Syntax: long ConfigurableStructures.StartDetail(
long             iStartMode,
domain  tcitem           iProduct,
domain  tibmrv           iVersion,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Configurable
Structures (tipcf3150m000) in detail mode. Use this session
to view and maintain the Configurable Structures.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iProduct                Product. Mandatory.
iVersion                Version. Mandatory.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
