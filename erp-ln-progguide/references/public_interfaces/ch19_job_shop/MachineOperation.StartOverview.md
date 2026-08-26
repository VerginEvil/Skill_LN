# MachineOperation.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for MachineOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 827-828

```baan
DLL:   tiextsfcapi
This function is available from     2026.09 (KB3666965  ).
Syntax: long MachineOperation.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcsern           iMachineSequence,
domain  tccwoc           iWorkCenter,
domain  tcmtyp           iMachineType,
domain  tcmcnr           iMachineNumber,
ref     domain  tcpdno           oProductionOrder,
ref     domain  tcopno           oOperation,
ref     domain  tcsern           oMachineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Machine Operations(tisfc4100m000)
in overview mode. Use this session to display, define and modify
the planning for a specific Machine Operation.
Pre:    None
Post:   None
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                                 - The parent session is blocked until the child
session exits. The session will be started as a
zoom session.
MODELESS                               - Parent and child are parallel sessions that
can be manipulated simultaneously.
iStartFilter                                  - Not used.
iSessionIndex                                 - The index that will be used.
Standard supported values:
1: Sort by Site, Production Order,
Operation, Machine Sequence (default)
2: Sort by Site, Work Center, Machine
Type, Machine Number, Planned Setup Start
Date, Production Order, Operation,
Machine Sequence
iQueryExtend                                  - A specific query to be used when zooming
to this session.
iSite                                         - Site(Optional)
-                                               If this value is entered then the Site
must exist in Sites.
iProductionOrder        . Production Order (Optional)
. If this value is entered then the
Production
Order must exist in Production Orders.
iOperation                                    - Operation (Optional)
-                                               If this value entered then the
Production Order and Operation must
exist in Operations.
iMachineSequence                              - Machine Sequence (Optional).
iWorkCenter                                   - Work Center (Optional)
iMachineType                                  - Machine Type (Optional)
iMachineNumber                                - Machine Number (Optional)
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProductionOrder        . Production Order
oOperation                                    - Operation
oMachineSequence                              - Machine Sequence
oExceptionMessage                             - The last error message found during the
execution of public interface.
If multiple error messages are found,
by using .oExceptionID., messages can
be retrieved.
oExceptionID                                  - An ID that refers to the exception
information.Use the functions in
Exception to get all relevant information
Return: 0                                     - Session started.
<> 0                                          - Otherwise.
```

## Public Interfaces for InstructionsByOperationStep

The following functions are available: InstructionsByOperationStep.StartOverview
