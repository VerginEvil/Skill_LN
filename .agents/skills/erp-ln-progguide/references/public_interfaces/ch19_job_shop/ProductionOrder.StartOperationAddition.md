# ProductionOrder.StartOperationAddition

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 775-777

```baan
DLL:   tiextsfcapi
This function is available from 2024.10 (KB3511148).
Syntax: long ProductionOrder.StartOperationAddition(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iPrecedingOperation,
domain  tcopno           iNextOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, a production order is prepared for
having operation(s) added to the production order's operation
network at a given location, as identified by its preceding
and its next operation.
To ensure Data integrity it is required that operations
are only inserted with this preparation.
After finishing the insert of a new operation, the function
ProductionOrder.FinishOperationAddition() must be called to
reset the system to normal.
Start Example Usage:
domain  tcsite  site
domain  tcpdno  production.order
domain  tcopno  operation.to.add
domain  tcopno  preceding.operation
domain  tcopno  subsequent.operation
operation.to.add = 15
preceding.operation = 10
subsequent.operation = 20
ret = ProductionOrder.StartOperationAddition(
site,
production.order,
preceding.operation,
subsequent.operation,
exception.message,
exception.id)
db.retry.point()
|* insert new operation via DAL operations.
dal.new.object( "tisfc010" )
dal.set.field( "tisfc010.pdno", production.order )
dal.set.field( "tisfc010.opno", operation.to.add )
dal.set.field( "tisfc010.nopr", subsequent.operation )
|* set other required fields
dal.set.field ( "tisfc010....
...
...
dal.save.object( "tisfc010" ) <> 0
then
|* something went wrong
endif
commit.transaction()
|* Finish operation addition
ret = ProductionOrder.FinishOperationAddition(
site,
production.order,
exception.message,
exception.id)
End Example Usage.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iPrecedingOperation     The operation of the current operation
network that must precede the
operation to be added. If 0 is given,
the operation to be added will have no
predecessor operation.
iNextOperation          The operation of the current operation
network that must succeed the operation
to be added. If 0 is given, the added
operation must be the last in order.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Able to add operation(s) to the
production order.
<> 0                    Errors occurred.
```
