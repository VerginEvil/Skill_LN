# ServiceContractInstallment.Cancel

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContractInstallment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1412-1413

```baan
DLL:   tsextctmapi
This function is available from 2025.10 (KB3606613).
Syntax: long ServiceContractInstallment.Cancel(
domain  tcorno           iServiceContract,
domain  tsctm.inst       iInstallmentNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to cancel a service contract
installment line.
The functionality offered in this Public Interface is the same
as available in session Cancel Contract Installments
(tsctm4202m000). See the session's documentation for more
information.
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be
executed.
Input:  iServiceContract
The service contract based on which the status of the
installment must be cancelled.
Mandatory Input.
iInstallmentNumber
The Installment number which must be cancelled.
Mandatory Input.
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0    :  The status of the contract installment line is changed
to 'Cancelled'.
<> 0 :  Error occurred during cancelling the contract
installment line.
```
