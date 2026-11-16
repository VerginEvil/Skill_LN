# JobShopRouting.Copy

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 660-661

```baan
DLL:   tiextrouapi
This function is available from 2021.05 (KB2156270).
Syntax: long JobShopRouting.Copy(
domain  tcsite           iSourceSite,
domain  tcitem           iSourceProduct,
domain  tirou.rouc       iSourceRouting,
domain  tirou.revi       iSourceRevision,
domain  tcitem           iTargetProduct,
domain  tirou.rouc       iTargetRouting,
domain  tirou.revi       iTargetRoutingRevision,
domain  tcdsca           iTargetRoutingRevisionDescription mb,
boolean          iCopyRelations,
boolean          iCopyOperationSteps,
boolean          iCopyTools,
boolean          iCopySkills,
boolean          iCopyProcessVariables,
boolean          iCopySetup,
boolean          iCopyInstructions,
boolean          iCopyExceptions,
boolean          iCopySetupClassStates,
boolean          iCopyText,
ref     domain  tirou.revi       oNewRoutingRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to copy a Job Shop Routing to the
target Job Shop Routing where related data is copied based on
input options.
If the target revision number is empty, a new revision is
created based on the existing revisions.
This Public Interface cannot be used to copy to or from
Standard Job Shop Routings.
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point has been set.
Post:   Abort or commit the transaction.
Input:  iSourceSite             Original Site (Mandatory).
iSourceProduct          Original Product (Mandatory).
iSourceRouting          Original Job Shop Routing (Mandatory).
iSourceRevision         Original Revision (Mandatory).
iTargetProduct          Target Product.
iTargetRouting          Target Job Shop Routing.
iTargetRoutingRevision  Target Revision.
iTargetRoutingRevisionDescription
Target Job Shop Routing Description.
iCopyRelations          Copy Relations
iCopyOperationSteps     Copy Operation Steps
iCopyTools              Copy Tools
iCopySkills             Copy Skills
iCopyProcessVariables   Copy Process Variables
iCopySetup              Copy Setup
iCopyInstructions       Copy Instructions
iCopyExceptions         Copy Exceptions
iCopySetupClassStates   Copy Setup Class States
iCopyText               Copy Text
Output: oNewRoutingRevision     New Job Shop Routing Revision.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       Function is executed successfully.
<> 0    An error occurred. The Job Shop Routing could not be
copied.
```
