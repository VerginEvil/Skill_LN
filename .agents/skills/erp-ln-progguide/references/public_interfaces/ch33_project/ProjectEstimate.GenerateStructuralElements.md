# ProjectEstimate.GenerateStructuralElements

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectEstimate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1704-1706

```baan
DLL:   tpextestapi
This function is available from 2021.12 (KB2220662).
Syntax: long ProjectEstimate.GenerateStructuralElements(
domain  tccprj           iProject,
domain  tpest.vers       iEstimateVersionFrom,
domain  tpest.vers       iEstimateVersionTo,
domain  tpest.esid       iEstimateStructureFrom,
domain  tpest.esid       iEstimateStructureTo,
domain  tccpcp           iCostComponentFrom,
domain  tccpcp           iCostComponentTo,
domain  tpptc.cstl       iExtensionFrom,
domain  tpptc.cstl       iExtensionTo,
domain  tppdm.cspa       iBudgetTopElement,
boolean          iUpdateFreeVersions,
boolean          iUpdateActualVersions,
boolean          iUpdateOnlyUsedStructures,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function updates the Estimate Structures for a given
Project and its Estimate Versions as in session "Generate
Structural Elements" (tpest1220m000).
The Structural Elements of the Estimate Structures are generated
from the applicable sources like Activities, Elements, Cost
Components, Extensions and User Defined Structures.
Pre:    This function has its own transaction management. There should
be no pending logical transaction before calling this function.
Post:   There is no need to execute an abort or commit after calling
this function, that is handled within the function.
Input:  iProject                - Project: Mandatory
iEstimateVersionFrom    - Estimate Version From
iEstimateVersionTo      - Estimate Version To
iEstimateStructureFrom  - Estimate Structure From
iEstimateStructureTo    - Estimate Structure To
iCostComponentFrom      - Cost Component From
Only relevant when Estimate Structures
of type 'Cost Component' are selected.
iCostComponentTo        - Cost Component To
Only relevant when Estimate Structures
of type 'Cost Component' are selected.
iExtensionFrom          - Extension From
Only relevant when Estimate Structures
of type 'Extension' are selected.
iExtensionTo            - Extension To
Only relevant when Estimate Structures
of type 'Extension' are selected.
iBudgetTopElement       - Budget Top Element: Optional
The Top Element for structures of
type Element.
Only relevant when only one Estimate
Version is selected, and Estimate
Structures of type 'Element' are
selected.
iUpdateFreeVersions     - Update Free Versions: Mandatory
Update Estimate Structures of
Estimate Versions with Status 'Free'.
Possible values:
True : Update Free Versions
False: Do not update Free versions
iUpdateActualVersions   - Update Actual Versions: Mandatory
Update Estimate Structures of
Estimate Versions with Status 'Actual'.
Possible values:
True : Update Actual Versions
False: Do not update Actual Versions
iUpdateOnlyUsedStructures
- Update Only Used Structures: Mandatory
Only update Estimate Structures which
are used in an Estimate Version.
Possible values:
True : Update only Estimate Structures
which are used in an Estimate
Version
False: Update all Estimate Structures
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Successful
<> 0                    - An error occurred
```
