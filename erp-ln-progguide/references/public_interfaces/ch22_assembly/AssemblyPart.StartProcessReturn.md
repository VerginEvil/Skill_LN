# AssemblyPart.StartProcessReturn

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyPart
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 860-861

```baan
DLL:   tiextascapi
This function is available from     2023.01 (KB2259064  ).
Syntax: long AssemblyPart.StartProcessReturn(
long             iStartMode,
domain  tccwoc           iLineStationFrom,
domain  tccwoc           iLineStationTo,
domain  tiutcd           iEffectiveDateFrom,
domain  tiutcd           iEffectiveDateTo,
domain  tcitem           iAssemblyPartFrom,
domain  tcitem           iAssemblyPartTo,
domain  tcyesno          iDirectProcessInbound,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Return Assembly Parts
(tiasc7245m000).
Pre:                  -
Post:                 -
Input:  iStartMode (Mandatory)
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS                               -
Parent and child are parallel
sessions that can be manipulated
simultaneously.
iLineStationFrom (Optional)
Lower bound of the Line Station selection range.
iLineStationTo (Optional)
Upper bound of the Line Station selection range. If
empty, the maximum value is used.
iEffectiveDateFrom (Optional)
Lower bound of the Effective Date selection range.
iEffectiveDateTo (Optional)
Lower bound of the Effective Date selection range. If
empty, the current date is used.
iAssemblyPartFrom (Optional)
Lower bound of the Assembly Part selection range.
iAssemblyPartTo (Optional)
Lower bound of the Assembly Part selection range. If
empty, the maximum value is used.
iDirectProcessInbound
If yes, the quantity that is completed is posted to
inventory. The inbound procedure is processed
automatically.
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - If the Return Assembly Parts session was started
succesfully.
<> 0                          - Otherwise.
```

## Public Interfaces for AssemblyProductVariant

The following functions are available: AssemblyProductVariant.CalculateStandardCost AssemblyProductVariant.GenerateStructure
