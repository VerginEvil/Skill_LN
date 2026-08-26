# SpecialDemandByItem.StartPrint

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for SpecialDemandByItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 589-590

```baan
DLL:   cpextdspapi
This function is available from     2024.07 (KB2329989  ).
Syntax: long SpecialDemandByItem.StartPrint(
long             iStartMode,
domain  cpcom.plnc       iScenarioFrom,
domain  cpcom.plnc       iScenarioTo,
domain  cpcom.date       iDemandDateFrom,
domain  cpcom.date       iDemandDateTo,
domain  cpitem           iPlanItemFrom,
domain  cpitem           iPlanItemTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to start session Print Special Demand by
Item (cpdsp2400m000). This session is used to print the special
demand by plan item as defined in the Special Demand by Item
(cpdsp2100m000) session.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode                            - Specifies the start mode for the
session (Mandatory). Possible values:
MODAL                                                 - The parent session is blocked
until the child session exits. The
session will be started as a zoom
session.
MODELESS_ALWAYS                                                 - Parent and child are
parallel sessions that can be
manipulated simultaneously, even if
the session is a Dialog.
iScenarioFrom                                 - Planning Scenario range from
iScenarioTo                                   - Planning Scenario range to
iDemandDateFrom                               - Demand date range from
iDemandDateTo                                 - Demand date range to
iPlanItemFrom                                 - Plan Item range from
iPlanItemTo                                   - Plan Item range to
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Print Special Demand by Item is
started successfully.
<> 0                                          - Print Special Demand by Item is not
started successfully.
```

## Public Interfaces for ExceptionMessages

The following functions are available: ExceptionMessages.StartOverview
