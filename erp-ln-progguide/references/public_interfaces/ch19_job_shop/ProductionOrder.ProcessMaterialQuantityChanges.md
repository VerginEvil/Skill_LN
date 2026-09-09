# ProductionOrder.ProcessMaterialQuantityChanges

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 747-748

```baan
DLL:   tiextsfcapi
This function is available from 2025.03 (KB3536492).
Syntax: long ProductionOrder.ProcessMaterialQuantityChanges(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcpono           iMaterialPosition,
boolean          iUseQuantityToIssue,
domain  tcqst1           iQuantityToIssue,
boolean          iUseQuantitySubsequentDelivery,
domain  tcqst1           iQuantitySubsequentDelivery,
boolean          iUseQuantityToCancel,
domain  tcqst1           iQuantityToCancel,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to update the quantities of material
lines in Production Warehouse Orders. This Public Interface
behaves similarly to the process form command for session
timfc0101m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                           Site. (Mandatory if sites
concept is active)
iProductionOrder                Production Order. (Mandatory)
iMaterialPosition               Material Position. (Mandatory)
iUseQuantityToIssue             Use Quantity To Issue.
iQuantityToIssue                Quantity To Issue. Only used
when iUseQuantityToIssue is set
to true.
iUseQuantitySubsequentDelivery  Use Quantity Subsequent
Delivery.
iQuantitySubsequentDelivery     Quantity Subsequent Delivery.
Only used when
iUseQuantitySubsequentDelivery
is set to true.
iUseQuantityToCancel            Use Quantity To Cancel.
iQuantityToCancel               Quantity To Cancel. Only used
when iUseQUantityToCancel is set
to true.
Output: oExceptionMessage               The last message if any message
is found. If more than one
message is given, these are
present in the oExceptionID.
oExceptionID                    An ID that refers to the
exception information. Use the
functions in Exception to get
all relevant information.
Return: 0                               Successfully Processed
Production Warehouse Order.
<> 0                            Otherwise.
```
