# HandlingUnit.GlobalBlock

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1039-1041

```baan
DLL:   whextwmdapi
This function is available from     2025.09 (KB3613947  ).
Syntax: long HandlingUnit.GlobalBlock(
domain  whinh.blre       iBlockingAction,
domain  whinh.tran       iTransaction,
domain  tccdis           iReason,
domain  whhuid           iFromHandlingUnit,
domain  whhuid           iToHandlingUnit,
domain  tccwar           iFromWarehouse,
domain  tccwar           iToWarehouse,
domain  tccom.bpid       iFromOwner,
domain  tccom.bpid       iToOwner,
domain  tcitem           iFromItem,
domain  tcitem           iToItem,
domain  tcatse           iFromAttributeSet,
domain  tcatse           iToAttributeSet,
domain  tcyesno          iPrintChanges,
domain  tcmcs.str15      iDevice,
domain  tcmcs.str16      iReportName,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will (un)block all handling units within
the specified range.
Pre:    db.retry.point() is set.
Post:   commit/abort.transaction.
Input:  iBlockingAction                       - Specifies whether to block or unblock
the handling units. (Mandatory)
possible values are:
-                                                 whinh.blre.block
blocks the handling units
-                                                 whinh.blre.release
unblocks the handling units
iTransaction                                  - Specifies for which transaction to
(un)block the handling units.
(Mandatory)
possible values are:
-                                                 whinh.tran.all
(un)blocks for all transactions
-                                                 whinh.tran.outbound
(un)blocks for outbound
transactions
-                                                 whinh.tran.trans.out
(un)blocks for transfer issue
transactions
-                                                 whinh.tran.assembly
(un)blocks for assembly
transactions
iReason                                         - Reason for (un)blocking (Mandatory)
iFromHandlingUnit                               - From range for handling unit
(Optional)
iToHandlingUnit                                 - To range for handling unit, has to
be alphabetically larger or equal to
iFromHandlingUnit
(Mandatory)
iFromWarehouse                                  - From range for warehouse (Optional)
iToWarehouse                                    - To range for warehouse, has to
be alphabetically larger or equal to
iFromWarehouse (Mandatory)
iFromOwner                                      - From range for owner (Optional)
iToOwner                                        - To range for owner, has to
be alphabetically larger or equal to
iFromOwner (Optional)
iFromItem                                       - From range for item (Optional)
iToItem                                         - To range for item, has to
be alphabetically larger or equal to
iFromItem (Optional)
iFromAttributeSet                               - From range for Attribute Set
(Optional)
iToAttributeSet                                 - To range for Attribute Set, has to
be alphabetically larger or equal to
iFromAttributeSet
(Optional)
iPrintChanges                                   - Specifies whether to print the
changes. (Mandatory)
possible values are:
-                                                   tcyesno.yes
print the changes
-                                                   tcyesno.no
don't print the changes
iDevice                                         - Device (Mandatory if iPrintChanges
is yes)
iReportName                                     - Report Name (Optional)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
