# InstructionsByOperationStep.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for InstructionsByOperationStep
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 828-830

```baan
DLL:   tiextsfcapi
This function is available from     2026.09 (KB3673207  ).
Syntax: long InstructionsByOperationStep.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iSessionFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcsern           iOperationStep,
domain  tiinst           iInstruction,
ref     domain  tcpdno           oProductionOrder,
ref     domain  tcopno           oOperation,
ref     domain  tcsern           oOperationStep,
ref     domain  tiinst           oInstruction,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:
Expl:
This function starts the session Instructions by Operation/Step
(tisfc0142m000) in overview mode.
Input :
iStartMode              Specifies the start mode for the
session.
Possible values are:
MODAL                          -              The parent session is blocked until
the child session exits.
The session will be started as a
zoom session.
MODELESS                       -              Parent and child are parallel sessions
that can be manipulated simultaneously.
iSessionFilter          Not used.
iSessionIndex           The index that will be used.
Supported values:
1: sort by requirement
iQueryExtend            A specific query to be used when zooming
to this session.
iProductionOrder        Production Order
iOperation              Operation
iOperationStep          Operation Step
iInstruction            Instruction
Output :
Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and
1 record has been selected.
oProductionOrder         Production Order
oOperation               Operation
oOperationStep           Operation Step
oInstruction             Instruction
oExceptionMessage        The last error message found during the
execution of public interface.
If multiple error messages are found,
by using .oExceptionID., messages can
be retrieved.
oExceptionID             An ID that refers to the exception
information. Use .Exception. related
functions to retrieve related
information.
Return:
0       Session started
<> 0    Otherwise
```

## Chapter 20 Public Interfaces for Subcontracting

## Public Interfaces for SubcontractingModel

The following functions are available: SubcontractingModel.ApproveRevision SubcontractingModel.CreateNewRevision SubcontractingModel.Explode SubcontractingModel.SetUseForCosting SubcontractingModel.SetUseForPlanning SubcontractingModel.StartMultiMain SubcontractingModel.ValidateRevision
