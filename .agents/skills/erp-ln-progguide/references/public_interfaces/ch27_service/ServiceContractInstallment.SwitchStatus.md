# ServiceContractInstallment.SwitchStatus

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContractInstallment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1413-1414

```baan
DLL:   tsextctmapi
This function is available from 2025.06 (KB3597586).
Syntax: long ServiceContractInstallment.SwitchStatus(
domain  tcorno           iServiceContract,
domain  tsctm.inst       iInstallmentNumber,
domain  tsctm.stin       iInstallmentStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to switch the status of a service
contract installment line from 'Free' to 'Accepted' or change
the status from 'Accepted' to 'Free'.
The functionality offered in this Public Interface is the same
as available in session Switch Status of Contract Installments
(tsctm4201m000). See the session's documentation for more
information.
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be
executed.
Input:  iServiceContract
The service contract based on which the status of the
installment must be switched.
Mandatory Input.
iInstallmentNumber
The Installment number which status must be switched
from free to accepted or form accepted to free.
Mandatory Input.
iInstallmentStatus
This is the status the service contract installment will
be switched to. Only the status 'Free' or 'Accepted' are
applicable for this public interface. If the installment
already has the status of this argument,
the status will not be changed.
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
to 'Accepted'.
<> 0 :  Error occurred during the change of the status of the
contract installment line.
```
