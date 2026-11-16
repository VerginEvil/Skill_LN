# ServiceOrder.CheckAllMaterialLinesHaveBeenReceivedAndIssued

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1418-1419

```baan
DLL:   tsextsocapi
This function is available from 2021.12 (KB2216885).
Syntax: long ServiceOrder.CheckAllMaterialLinesHaveBeenReceivedAndIssued(
const   domain  tcorno           iServiceOrder fixed,
const   domain  tsmdm.acln       iActivityLine,
const           boolean          iCheckSubsequentDeliveryQuantity,
const           boolean          iCheckNonConsumed,
ref             boolean          oAllMaterialLinesHaveBeenReceivedAndIssued,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to see if for a certain service order or
service order activity all related material lines (tssoc220)
have been issued (delivery types with an issue) or received (
delivery types with a receipt).
If all material lines related to the service order have to be
checked, then give for the iActivityLine the value 0.
If only for a specific activity line number this check has to
be executed then specify the iActivityLine with an existing
activity line number.
If the subsequent delivery quantity also has to be taken into
account, then set the iCheckSubsequentDeliveryQuantity to
True else to False. The subsequent delivery quantity is
used for all the From-Warehouse kind of flows, so it concerns
issues.
Normally you also would want to check the subsequent delivery
quantity, so fill this input boolean with True.
Not checking the subsequent delivery quantity can be an option,
when during the costing process the user indicates that
the subsequent quantity will be removed automatically.
If that is the normal way of working, then you can indicate
that the subsequent quantity should not be taken into account
when checking if everything has been issued.
If also the non-consumed lines have to be taken into account,
then set the iCheckNonConsumed to True else to False.
If a to-warehouse line is linked (related line number is filled),
with a from-warehouse line, then, if the iCheckNonConsumed
is set to True, this function will also check whether the
receipt for this non-consumed line has been executed.
Pre:    N.A.
Post:   N.A.
Input:  iServiceOrder                           - The service order.
This is mandatory input and the service order should
exist.
iActivityLine                           - The activity line
number. If a value of 0 is specified, then this function
will check all material lines (tssoc220) related to
the iServiceOrder. If a value <> 0 is specified, then
this service order activity has to exist and only the
material lines linked to this specific activity line
are checked.
iCheckSubsequentDeliveryQuantity        - If set to True, then
for material lines with a delivery type which are
dealing with an issue the system will also check if the
subsequent delivery quantity (tssoc220.qtsd) has been
issued.
iCheckNonConsumed                       - If a To Warehouse
material line is linked with the related line
number field to a From Warehouse line, and this
input boolean is set to True, then the system will
also check that these non-consumed material lines have
been received.
Output: oAllMaterialLinesHaveBeenReceivedAndIssued      -
If True is returned, then all material lines linked
to the service order or service order activity have
been received and issued.
If False is returned, then not all material lines
linked to the service order or service order activity
have been received and issued.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
If the return value equals 0, but the
oAllMaterialLinesHaveBeenReceivedAndIssued is False,
then it contains the last message indicating for which
material line (and the reason) not everything has been
issued or received.
If more than one message is given, these are present in
the oExceptionID
oExceptionID
An ID that refers to all error information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation.
If the return value = 0 (so not an error), but the
oAllMaterialLinesHaveBeenReceivedAndIssued is False,
then this contains all the useful information for the
first material line for which not everything has been
received/issued.
Return: 0       -       No Error.
<> 0    -       Error.
```
