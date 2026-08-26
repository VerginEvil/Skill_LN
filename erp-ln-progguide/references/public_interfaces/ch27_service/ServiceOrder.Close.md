# ServiceOrder.Close

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1407-1408

```baan
DLL:   tsextsocapi
This function is available from     2023.11 (KB2297823  ).
Syntax: long ServiceOrder.Close(
domain  tcorno           iServiceOrder,
domain  tcyesno          iDeleteServiceOrder,
domain  tcyesno          iCopyServiceOrderToHistory,
domain  tcyesno          iClosePhysicalBreakdownChanges,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Close a Service Order.
The same functionality is offered as available in session
Close Service Orders (tssoc2201m000).
Pre:    db.retry.point() set
Post:   commit/abort transaction
Input:  iServiceOrder
Service Order
Mandatory
iDeleteServiceOrder
Delete Service Order
Mandatory
iCopyServiceOrderToHistory
Copy Service Order to History. This argument is
mandatory when Service Order Parameter Service Order
History is checked. When iDeleteServiceOrder is Yes,
iCopyServiceOrderToHistory is defaulted to Yes.
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
Return: 0                     - No Error
<> 0                          - Error
```
