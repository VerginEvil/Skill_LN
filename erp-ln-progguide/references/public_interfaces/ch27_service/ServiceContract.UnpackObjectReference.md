# ServiceContract.UnpackObjectReference

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1392-1394

```baan
DLL:   tsextctmapi
This function is available from     2026.01 (KB3644790  ).
Syntax: long ServiceContract.UnpackObjectReference(
domain  tcborf           iObjectReference,
ref     domain  tsctm.cchn       oContractChange,
ref     domain  tsmdm.seqn       oConfigurationLine,
ref     domain  tsctm.inst       oInstallmentLine,
ref     domain  tcpono           oRevenueLine,
ref     domain  tcemm.seqn       oCostLine,
ref     domain  tcccp.yrno       oYear,
ref     domain  tcccp.peri       oPeriod,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function unpacks the object reference string to Contract
Installment Line number, Contract Revenue Line number or
Contract Cost Line number.
Pre:                  -
Post:                 -
Input:  iObjectReference                      - Object Reference; Mandatory
Output: oContractChange                       - Contract Change number
oConfigurationLine                            - Line number of the Contract
Configuration Line
oInstallmentLine                              - Line number or Contract Installment
Line
oRevenueLine                                  - Line number or Revenue Line
oCostLine                                     - Line number or Contract Cost Line
oYear                                         - Year number
oPeriod                                       - Period number
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation.
Return: 0                     - No Error, and the object reference could be
unpacked correctly.
<> 0                          - Error, and the object reference could not be
unpacked correctly.
```

## Public Interfaces for ServiceContractChange

The following functions are available: ServiceContractChange.Create
