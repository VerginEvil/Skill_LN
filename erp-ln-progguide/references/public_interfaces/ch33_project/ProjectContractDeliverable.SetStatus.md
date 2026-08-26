# ProjectContractDeliverable.SetStatus

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContractDeliverable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1690-1693

```baan
DLL:   tpextpdmapi
This function is available from     2024.05 (KB2311994  ).
Syntax: long ProjectContractDeliverable.SetStatus(
domain  tccono           iContract,
domain  tcpono           iDeliverable,
domain  tcpono           iSchedule,
domain  tpctm.dlst       iSourceStatus,
domain  tpctm.dlst       iTargetStatus,
domain  tcyesno          iContinueIfNoCFMForDescription,
domain  tcyesno          iContinueIfNoCFMForItem,
domain  tcyesno          iContinueIfNoCFMForComponent,
domain  tcyesno          iContinueIfSerialsQuantityMismatch,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will set Contract Deliverable/Schedule
status to the specified new status
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iContract                     - Contract: Mandatory
iDeliverable                          - Deliverable: Mandatory
iSchedule                             - Schedule: Optional
If iSchedule = 0 and delivery schedule is present then
all the schedule lines along with the deliverable will
be updated to the specified target status
else the given schedule line along with the deliverable
will be updated to the specified target status.
iSourceStatus                         - SourceStatus: Optional
If passed empty, then all the contract
deliverable/schedules irrespective of their current
status will be changed to iTargetStatus.
If not empty, then all the contract
deliverable/schedules with their current status as
iSourceStatus will be changed to iTargetStatus.
Allowed Values for iSourceStatus are:
tpctm.dlst.free                                               - Free
tpctm.dlst.active                                             - Active
tpctm.dlst.released.to.wh                                     - Release to Warehousing
tpctm.dlst.delivered                                          - Delivered
tpctm.dlst.closed                                             - Closed
iTargetStatus                         - TargetStatus: Mandatory
Allowed Values for TargetStatus are:
tpctm.dlst.free                                               - Free
tpctm.dlst.active                                             - Active
tpctm.dlst.released.to.wh                                     - Release to Warehousing
tpctm.dlst.delivered                                          - Delivered
tpctm.dlst.closed                                             - Closed
tpctm.dlst.canceled                                           - Canceled
Note: Below arguments are relevant while changing the status
to 'Active'
iContinueIfNoCFMForDescription                       - Continue If Item
Description cannot be used as Customer Furnished
Material: Mandatory (Yes/No)
iContinueIfNoCFMForItem                        - Continue If Customer
Furnished Material defined for Item but Deliverable
does not have Contains Customer Furnished Material
selected: Mandatory (Yes/No)
iContinueIfNoCFMForComponent                        - Continue If Customer
Furnished Material defined for component of Main Item
but Deliverable does not have Contains Customer
Furnished Material selected: Mandatory (Yes/No)
iContinueIfSerialsQuantityMismatch                       - Continue If Serials Do Not
Match Deliverable Quantity: Mandatory (Yes/No)
Following status changes are allowed:
---------------------------------------------------------------
Active                                  Free
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Active to Free
---------------------------------------------------------------
Free                                    Active
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Free to Active
---------------------------------------------------------------
Release to Warehousing                  Active
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Release to Warehousing to Active
---------------------------------------------------------------
Active                                  Release to Warehousing
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Active to Release to Warehousing
where the item is handled by Warehousing
---------------------------------------------------------------
Active                                  Delivered
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Active to Delivered where the item is
not handled by Warehousing
(Deliverable of type Non                      -hardware, cost/service items)
---------------------------------------------------------------
Closed                                  Delivered
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Closed to Delivered when the current
status of the deliverable/schedule is closed and the contract
line status is not closed
---------------------------------------------------------------
Delivered                               Closed
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Delivered to Closed if the following
conditions are met:
-                       Lines must have been received:
* Deliverable line without schedule lines:
The deliverable line must have status delivered
* Deliverable line with schedule lines:
All the schedule lines must have status delivered
-                       When Acceptance Point on the contract line is
Source Acceptance and/or Destination Acceptance the shipment
line for the Deliverable Line or Schedule line must be
Source and/or destination accepted:
* Deliverable line without schedule lines:
The deliverable line must be Source Accepted and/or
Destination Accepted
* Deliverable line with schedule lines:
All the schedule lines must be Source Accepted and/or
Destination Accepted
-                       When Invoicing Method is Delivery Based then the
Deliverable Line or Schedule line must have been invoiced:
* Deliverable line without schedule lines:
The deliverable line must have been invoiced.
* Deliverable line with schedule lines:
All the schedule lines must have been invoiced.
-                       Contract Status is not on hold
-                       Contract Line Status is not on hold
---------------------------------------------------------------
Free                                    Canceled
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Free to Canceled
---------------------------------------------------------------
Active                                  Canceled
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Active to Canceled
---------------------------------------------------------------
Release to Warehousing                  Canceled
---------------------------------------------------------------
It is allowed to change all the deliverable/schedules that has
current or iSourceStatus Release to Warehousing to Canceled
---------------------------------------------------------------
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     - Contract Deliverable / Schedule Status changed
<> 0                          - Contract Deliverable / Schedule Status could not
be changed
```
