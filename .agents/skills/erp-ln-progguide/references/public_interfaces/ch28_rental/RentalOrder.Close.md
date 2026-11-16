# RentalOrder.Close

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1557-1558

```baan
DLL:   tsextsocapi
This function is available from 2024.05 (KB2331668).
Syntax: long RentalOrder.Close(
domain  tcorno           iRentalOrder fixed,
domain  tcyesno          iDeleteRentalOrder,
domain  tcyesno          iCopyRentalOrderToHistory,
domain  tcyesno          iClosePhysicalBreakdownChanges,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Close a Rental Order.
The same functionality is offered as available in session
Close Rental Orders (tssoc2201m100).
Pre:    db.retry.point() set
Post:   commit/abort transaction
Input:  iRentalOrder
Rental Order
Mandatory
iDeleteRentalOrder
Delete Rental Order
Mandatory
iCopyRentalOrderToHistory
Copy Rental Order to History. This argument is
mandatory when Rental Order Parameter Rental Order
History is checked. When iDeleteRentalOrder is Yes,
iCopyRentalOrderToHistory is defaulted to Yes.
iClosePhysicalBreakdownChanges
Close Physical Breakdown Changes. This argument is
mandatory when Physical Breakdown Changes is checked
in Configuration Management Parameters.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No Error
<> 0    - Error
```
