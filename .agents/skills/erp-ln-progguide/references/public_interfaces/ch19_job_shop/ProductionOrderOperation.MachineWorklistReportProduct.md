# ProductionOrderOperation.MachineWorklistReportProduct

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 793-794

```baan
DLL:   tiextsfcapi
This function is available from 2026.08 (KB3617574).
Syntax: long ProductionOrderOperation.MachineWorklistReportProduct(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcmcnr           iMachineNumber,
domain  tcutcs           iTransactionDate,
domain  tiqep3           iCompletedQty,
domain  tiqep3           iRejectedQty,
domain  tccdis           iRejectReason,
ref     domain  tcibd.sern       iSerialArrayProduced() fixed,
ref     domain  tcibd.sern       iSerialArrayRejected() fixed,
domain  tcclot           iLotCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:
Expl:   This public interface is designed to report quantities for
machine operations ›¼À” including both completed and rejected
quantities ›¼À” and consolidate those quantities up to the
production order operation level.
The function retrieves Work Center and Machine Type information
based on the provided Production Order, Operation, and Machine
Number. It uses the transaction date to determine the applicable
shift. If no transaction date is supplied, the current date is
used by default.
System validates the following:
1. Shift Status must not be completed
2. Input Production Operation status must not be completed
3. Machine Operation reporting must be Manual
4. Machine Operation status must not be completed.
Successful completion of all the required validations creates a
record in Machine Operation Quantities.
Once the machine operation quantities are inserted, this process
aggregates machine operation quantities to production
operation level.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process. Transaction handling
will be done inside PI.
Input:  iSite                   ›¼À“ Site (Mandatory when the site concept
is active)
iProductionOrder        ›¼À“ Production Order (Mandatory, must
belong to the iSite)
iOperation              ›¼À“ Operation (Mandatory, must belong to
the iProductionOrder)
iMachineNumber          ›¼À“ Machine Number (Mandatory, must
belong to the iProductionOrder and
iOperation)
iTransactionDate        - Transaction Date is used for fetching
the right Shift information for
posting the machine operation
quantities
iCompletedQty           ›¼À“ Quantity to Complete (must be >=0)
If the item is serialized, then it
must be matched with the number of
serials given in
iSerialArrayProduced().
Either the Quantity to Complete or
Quantity to Reject must be input.
iRejectedQty            ›¼À“ Quantity to Reject (must be >=0)
If the item is serialized, then the
Quantity to Reject must be equal to
number of serials in
iSerialArrayRejected().
iRejectReason           ›¼À“ Reject Reason
Mandatory if the Quantity to Reject
> 0
Reject Reason must be of type ›¼À“
"Rejection of Production Result".
iSerialArrayProduced()  ›¼À“ if the item is Serial Controlled,
entered serial numbers must match
with the Quantity to Complete. Entered
Serial Numbers must exist in the
Production Order As-Built.
iSerialArrayRejected()  ›¼À“ if the item is Serial Controlled,
entered serial numbers must match
with the Quantity to Reject. Entered
Serial Numbers must exist in the
Production Order As-Built
iLotCode                ›¼À“ Lot Code must be set if the item is
lot controlled
Entered Lot code must exist in the
system
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
