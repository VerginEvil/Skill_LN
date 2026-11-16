# MachineOperation.StartDetail

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for MachineOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 828-829

```baan
DLL:   tiextsfcapi
This function is available from 2026.09 (KB3666965).
Syntax: long MachineOperation.StartDetail(
long             iStartMode,
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcsern           iMachineSequence,
domain  tcopno           iOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Machine Operations(tisfc4100m000)
in detail mode. Use this session to display, define and modify
the planning for a specific Machine Operation. Note that the
session can only be started if the parameter 'Job Shop by Site'
is 'In Preparation' or 'Active'.
Pre:    None
Post:   None
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL   - The parent session is blocked until the child
session exits. The session will be started as a
zoom session.
MODELESS - Parent and child are parallel sessions that
can be manipulated simultaneously.
iSite           - Site(Mandatory)
- If this value is entered then the Site
must exist in Sites.
iProductionOrder›¼À“ Production Order (Mandatory)
›¼À“ If this value is entered then the Production
Order must exist in Production Orders.
iMachineSequence - Machine Sequence (Mandatory).
iOperation      - Operation (Mandatory)
- If this value entered then the Production
Order and Operation must exist in Operations.
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oExceptionMessage - The last error message found during the
execution of public interface.
If multiple error messages are found,
by using ›¼ÀœoExceptionID›¼À•, messages can be
retrieved.
oExceptionID    - An ID that refers to the exception information.
Use the functions in Exception to get all
relevant information
Return: 0                       Session started.
<> 0                    Otherwise.
```
