# PhysicalBreakdown.Change

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PhysicalBreakdown
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1352-1354

```baan
DLL:   tsextcfgapi
This function is available from     2022.10 (KB2262990  ).
Syntax: long PhysicalBreakdown.Change(
domain  tscfg.actn       iAction,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcitem           iReplaceWithItem,
domain  tcibd.sern       iReplaceWithSerialNumber,
domain  tcclot           iReplaceWithLot,
domain  tsmdm.qmat       iReplaceWithQuantity,
domain  tcpono           iReplaceAtPosition,
domain  tcclot           iInstallWithLot,
domain  tcitem           iParentReplaceItem,
domain  tcibd.sern       iParentReplaceSerialNumber,
domain  tscfg.cfst       iTopItemStatus,
domain  tsbsc.clst       iInstallationGroup,
domain  tsbsc.lino       iInstallationGroupLineNumber,
domain  tsmdm.qmat       iQuantity,
domain  tsmdm.utct       iChangeDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function executes changes within the Physical Breakdown.
The following changes are supported:
(1) REPLACE:
The replacement of Serialized Items or the replacement of
Anonymous Items in a Physical Breakdown.
When replacing an Item in a Physical Breakdown, the Top
Item Status is changed from Active to Revision.
After That the changes to the Physical Breakdown are done.
Finally the Top Item Status is set back to Active again.
Quantity, and Position play a key role in case of Anonymous
Items replacement. The replacement can be either full
or partial.
(2) INSTALL:
For the Serialized Item that is installed a check is done if
it is present in any Installation Group.
If this is the case then the Installation Group line will be
set to expired. Next the Serialized Item can be installed
(again) as Installation Group line. This will be done if
installation group is filled.
If the installation Group is empty it can be installed under
any other Serialized Item within its Physical Breakdown.
If the Serialized Item, the Physical Breakdown in which it
is present in, or the Installation Group in which it is
present is covered by an active Service Contract the
Serialized Item will not be directly installed, but
preparation for the installation will be done.
This is done by:
-                         Setting Status of Installation Group line to
'To be Installed'
-                         Or setting the Status of the Physical Breakdown relation
under which the Serialized Item is present to
'To be Installed'.
In both cases the status time will be set to the current time.
When installing an Anonymous Item in a Physical Breakdown,
the Top Item Status is changed from Active to Revision.
After that the changes to the Physical Breakdown are done.
Finally the Top Item Status is set back to Active again.
Lot, Quantity, and Position play a key role in case of
Anonymous Items Installation.
(3) REMOVE:
For the Serialized Item that is removed a check is done if
it is present in any Installation Group.
If this is the case then the Installation Group line will be
set to expired.
If not present in an Installation Group the Serialized Item
will be removed from the Physical Breakdown it is part of.
If the Serialized Item, the Physical Breakdown in which it
is present in, or the Installation Group in which it is
present is covered by an active Service Contract the
Serialized Item will not be directly removed, but preparation
for the removal will be done.
This is done by:
-                         Setting status of Installation Group line to
'To be Removed',
-                         Or setting the status of the Physical Breakdown relation
under which the Serialized Item is present to
'To be Removed'.
In both cases the status time will be set to the current time.
When removing an Anonymous Item from a Physical Breakdown, the
Top Item status is changed from Active to Revision.
After that changes to the Physical Breakdown are done.
Finally the top most Parent Item status is set back to Active
again.
Lot, Quantity, and Position play a key role in case of
Anonymous Item removal. The removal can be either full
or partial.
When changing a Physical Breakdown, the status of the Top
Item will be set to 'Revision' and then back to 'Active' only
in case the status of the Item is 'Active' or 'Working
Condition' prior to this operation.
NOTE: this function can be used if Configuration Management
Parameter 'Physical Breakdown Changes' is selected, but only
if no Physical Breakdown Change is present for the provided
item and serial.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input   :               - iAction             - Action to be done.
Possible values are:
-                                                       tscfg.actn.add     - Install
-                                                       tscfg.actn.replace - Replace
-                                                       tscfg.actn.remove  - Remove
-                         iItem               - The Item the action is performed at.
In case of Installation:
-                                                      The Item to be installed
In case of Replacement:
-                                                      The Item that is to be replaced
In case of Removal:
-                                                      The Item that is removed
-                         iSerialNumber       - The Serial Number of the item
action is performed at.
-                         iReplaceWithItem    - The Item which replaces the existing
Anonymous Item.
-                         iReplaceWithSerialNumber
-                                               Serial Number of the Replacing Item.
-                         iReplaceWithLot     - Lot of the Replacing Item.
-                         iReplaceWithQuantity
-                                               Anonymous Item Quantity.
-                         iReplaceAtPosition
-                                               Position in the Breakdown under the
Parent Serialized Item where exactly
the replacement has to be made.
-                         iInstallWithLot     - Lot of Item which needs to be
installed or removed or replaced.
-                         iParentReplaceItem
-                                               The Replacement Item or the Parent
Item the new component is to be
installed at (depending on the action).
-                         iParentReplaceSerialNumber
-                                               The Serial Number of the Replacement
Item or the Parent Item the new
component is to be installed at
(depending on the action).
-                         iTopItemStatus   - The Top Item Status
-                         iInstallationGroup- The Installation Group to which
the Serialized Item will be linked
as Top Item.
-                         iInstallationGroupLineNumber
-                                               The Installation Group line number.
-                         iQuantity           - The Quantity of the Anonymous
item being installed or removed.
Output  :               - ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
-                         oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0                                   - No error
<> 0                                          - An error occurred
```
