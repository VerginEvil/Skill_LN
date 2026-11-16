# ProductionOrder.ResetCompletedToActive

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 767-768

```baan
DLL:   tiextsfcapi
This function is available from 2020.11 (KB2158213).
Syntax: long ProductionOrder.ResetCompletedToActive(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
boolean          iResetOperations,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to reset the status of a
completed Production Order to active, as in
session ticst0203m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite and its status must be
Completed or To be Completed.
iResetOperations        If true: also reset the status of all
Operations of the specified production
order from Completed to Active.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Rejected quantity is scrapped
<> 0                    Rejected quantity could not be scrapped
```
