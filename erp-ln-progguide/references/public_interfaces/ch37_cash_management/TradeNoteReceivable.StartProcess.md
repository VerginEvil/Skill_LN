# TradeNoteReceivable.StartProcess

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for TradeNoteReceivable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1815-1816

```baan
DLL:   tfextcmgapi
This function is available from 2026.10 (KB3688452).
Syntax: long TradeNoteReceivable.StartProcess(
long             iStartMode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session
Process Trade Notes Receivable (tfcmg4226m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise
```
