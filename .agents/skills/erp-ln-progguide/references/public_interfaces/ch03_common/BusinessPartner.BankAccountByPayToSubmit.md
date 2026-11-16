# BusinessPartner.BankAccountByPayToSubmit

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 117-118

```baan
DLL:   tcextcomapi
This function is available from 2022.11 (KB2267391).
Syntax: long BusinessPartner.BankAccountByPayToSubmit(
domain  tccom.bpid       iPayToBusinessPartner,
domain  tccban           iBankAccountCode,
domain  tcmcs.str30      iAction,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will submit a draft version of the Bank Account by
pay to BusinessPartner which is being controlled by
Object Configuration Management.
Pre:    db.retry.point() must have been set.
This function will read the Bank Account Code By Pay-to BP, so
that is not required from the calling process.
Post:   Commit or abort the transaction
Input:  iPayToBusinessPartner   - Pay-to Business Partner; Mandatory
iBankAccountCode        - Bank Account Code; Mandatory
iAction                 - The action to be performed; Mandatory
This action can be one of the default
actions:
Create, Change, Delete.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Success
<> 0    - Error
```
