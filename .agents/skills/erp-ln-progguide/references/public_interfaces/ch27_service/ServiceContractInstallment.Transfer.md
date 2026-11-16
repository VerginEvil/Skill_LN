# ServiceContractInstallment.Transfer

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContractInstallment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1414-1415

```baan
DLL:   tsextctmapi
This function is available from 2025.06 (KB3597592).
Syntax: long ServiceContractInstallment.Transfer(
domain  tcorno           iServiceContract,
domain  tsctm.inst       iInstallmentNumber,
domain  tcsli.stat       iInvoiceStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to transfer installments of a Contract
with the status "Accepted" to the central invoicing module.
The transferred installment can have the status "On Hold" or
"Confirmed" in the central invoicing module.
The functionality offered in this Public Interface is the same
as available in session Transfer Installments to Invoicing
(tsctm4203m000). See the session's documentation for more
information.
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be
executed.
Input:  iServiceContract
The service contract for which the installment will
be transfered.
Mandatory Input.
iInstallmentNumber
The installment number which will be transfered to
central invoicing.
Mandatory Input.
iInvoiceStatus
This is the status of the invoice after the transfer.
The invoice can have the status "On Hold" or "Confirmed".
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
