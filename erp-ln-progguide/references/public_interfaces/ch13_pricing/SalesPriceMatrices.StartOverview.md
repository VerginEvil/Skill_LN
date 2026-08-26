# SalesPriceMatrices.StartOverview

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for SalesPriceMatrices
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 529-531

```baan
DLL:   tdextpcgapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long SalesPriceMatrices.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tdpcg.maty       iMatrixType,
domain  tdpcg.malv       iMatrixLevel,
domain  tdpcg.made       iMatrixDefinition,
domain  tdpcg.prse       iSequence,
ref     domain  tdpcg.maty       oMatrixType,
ref     domain  tdpcg.malv       oMatrixLevel,
ref     domain  tdpcg.made       oMatrixDefinition,
ref     domain  tdpcg.prse       oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Sales Price Matrices Overview
(tdpcg0130m010).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used
iSessionIndex
Specifies the table                              -index that is to be used.
Allowed values: 0 or 1. Both will start the session with
the primary index.
iQueryExtend
A specific query to be used when zooming to this session.
iMatrixType
Matrix Type
Mandatory. Should always be tdpcg.maty.sobook
iMatrixLevel
Matrix Level; Optional
iMatrixDefinition
Matrix Definition; Optional
iSequence
Sequence; Optional
Output: for iStartMode MODAL:
oMatrixType     The selected Matrix Type
oMatrixLevel    The selected Matrix Level
oMatrixDefinition
The selected Matrix Definition
oSequence       The selected Sequence
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - An error occurred
```

## Chapter 14 Public Interfaces for Landed Costs

## Public Interfaces for LandedCosts

The following functions are available: LandedCosts.GetSettings
