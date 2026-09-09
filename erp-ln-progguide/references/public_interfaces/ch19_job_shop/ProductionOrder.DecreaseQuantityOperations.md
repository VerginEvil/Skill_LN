# ProductionOrder.DecreaseQuantityOperations

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 712-712

```baan
DLL:   tiextsfcapi
This function is available from 2026.06 (KB3626769).
Syntax: long ProductionOrder.DecreaseQuantityOperations(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcyesno          iDoBackflush,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:
Expl:   This public interface decreases the last operation quantities
when negative quantity is reported at production order level.
This will execute the functionality behind Decrease Operation
Quantities form command in Report Orders Completed
(tisfc0120s000).
Execution of this Public Interface is conditional upon:
configuration authorization, valid production order status,
valid status of the order's final operation, and absence of any
open Quantity to Deliver, which would prevent the decrease.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process. Transaction handling
will be done inside PI.
Input:  iSite                   - Site (mandatory when the Site concept
is active).
iProductionOrder        - Production Order (Mandatory).
iDoBackFlush            - Execute Backflushing when backflushing
is not done automatically if the value
is tcyesno.yes. Otherwise,
backflushing will not be executed.
Output:
oExceptionMessage
- The last error message found during the execution of
public interface. If multiple error messages are found,
by using "oExceptionID", messages can be retrieved.
oExceptionID
- An ID that refers to the exception information. Use
"Exception" related functions to retrieve related
information.
Return: 0       - Success
<>0     - Error occurred during the process
```
