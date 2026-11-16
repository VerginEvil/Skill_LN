# JobShopRouting.CopyOperations

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 661-662

```baan
DLL:   tiextrouapi
This function is available from 2021.11 (KB2202744).
Syntax: long JobShopRouting.CopyOperations(
domain  tcsite           iSourceSite,
domain  tcitem           iSourceProduct,
domain  tirou.rouc       iSourceRouting,
domain  tirou.revi       iSourceRevision,
domain  tcopno           iFromOperation,
domain  tcopno           iToOperation,
domain  tcitem           iTargetProduct,
domain  tirou.rouc       iTargetRouting,
domain  tirou.revi       iTargetRevision,
boolean          iCopyOperationSteps,
boolean          iCopyTools,
boolean          iCopySkills,
boolean          iCopyProcessVariables,
boolean          iCopySetup,
boolean          iCopyInstructions,
boolean          iCopyExceptions,
boolean          iCopySetupClassStates,
boolean          iAppend,
boolean          iCopyText,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to copy Job Shop Routing Operations of
one Routing to another one based on input options.
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point has been set.
Post:   Abort or commit the transaction.
Input:  iSourceSite             Original Site (Mandatory).
iSourceProduct          Original Product (Mandatory).
iSourceRouting          Original Job Shop Routing (Mandatory).
iSourceRevision         Original Revision (Mandatory).
iFromOperation          Start Operation range to be copied (Mandatory).
iToOperation            End Operations to be copied (Mandatory).
iTargetProduct          Target Product (Mandatory).
iTargetRouting          Target Job Shop Routing (Mandatory).
iTargetRevision         Target Revision (Mandatory).
iAppend                 True (append) or False (overwrite).
iCopyOperationSteps     Copy Operation Steps.
iCopyTools              Copy Tools.
iCopySkills             Copy Skills.
iCopyProcessVariables   Copy Process Variables.
iCopySetup              Copy Setup.
iCopyInstructions       Copy Instructions.
iCopyExceptions         Copy Exceptions.
iCopySetupClassStates   Copy Setup Class States.
iCopyText               Copy Text.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       The Job Shop Routing Operations are succesfully copied.
<> 0    An error occurred. The Job Shop Routing Operations
could not be copied.
```
