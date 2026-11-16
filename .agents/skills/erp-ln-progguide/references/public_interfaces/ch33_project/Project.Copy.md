# Project.Copy

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1690-1692

```baan
DLL:   tpextpdmapi
This function is available from 2024.03 (KB2307181).
Syntax: long Project.Copy(
domain  tccprj           iSourceProject,
domain  tcseri           iTargetProjectSeries,
domain  tccprj           iTargetProject,
long             iProcessingOptionSet,
ref     domain  tccprj           oTargetProject,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to copy the iSourceProject to a
new project (in case iTargetProject is empty) or to iTargetProject.
The iSourceProject, along with the relevant fields and options
required for the new project, can be passed. This function can
also be used to create a Project from a Template Project.
Pre:    - db.retry.point()
Post:   - abort.transaction() or commit.transaction()
Input:  iSourceProject   - The Project to be copied, Mandatory
iTargetProjectSeries -
A string used to generate a new Project code
that contains the Project Series, Optional.
Note : The project series being passed should
belong to the project number group defined in
the Project User Profiles of the user
(if a profile exists), or it should belong to
the number group defined in the project parameters.
iTargetProject  -
The code for new Project, Optional.
Note:
1) Either iTargetProjectSeries or iTargetProject should
be passed.
2) If iTargetProjectSeries and iTargetProject
are empty, the project series will be derived from
Project User Profiles (if they exist); otherwise,
it will be derived from Project Parameters.
iProcessingOptionSet -
Optional, if 0, the default copy options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Copy Project / Create Project from Template (tppdm7840m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Copy Project options which are not available as Processing Options
will get defaulted in accordance with the session logic.
NAME                               TYPE          DEFAULT
targetProjectDescription                domain tcitm.dscr   ""
subProject                              domain tppdm.yeno  tppdm.yeno.no
mainProject                             domain tccprj
projectAddress                          domain tccom.cadr  <from source Project>
shipFromAddress                         domain tccom.cadr  <from source Project>
projectManager                          domain tcemno      <from source Project>
projectManagementOffice                 domain tccwoc      <from source Project>
enterpriseUnit                          domain tcemm.grid  <from source Project>
prioritySupplyWarehouse                 domain tccwar      <from source Project>
startDate                               domain tcdate
finishDate                              domain tcdate
copyEstimateToProject                   domain tppdm.yeno  tppdm.yeno.no
createAsTemplate                        domain tppdm.yeno  tppdm.yeno.no
generalProjectData                      domain tppdm.yeno  tppdm.yeno.yes
projectRelatedCostObjectsData           domain tppdm.yeno  tppdm.yeno.yes
costingBreaks                           domain tppdm.yeno  tppdm.yeno.yes
scope                                   domain tppdm.yeno  tppdm.yeno.yes
baseLines                               domain tppdm.yeno  tppdm.yeno.yes
estimating                              domain tppdm.yeno  tppdm.yeno.no
useSourceLineNumbers                    domain tppdm.yeno  tppdm.yeno.no
bottomUpBudget                          domain tppdm.yeno  tppdm.yeno.yes
topDownBudget                           domain tppdm.yeno  tppdm.yeno.yes
budgetCostAnalysisVersions              domain tppdm.yeno  tppdm.yeno.yes
timePhasedBudgetAnalysisCodes           domain tppdm.yeno  tppdm.yeno.yes
budgetSurcharges                        domain tppdm.yeno  tppdm.yeno.yes
costSurcharges                          domain tppdm.yeno  tppdm.yeno.yes
revenueSurcharges                       domain tppdm.yeno  tppdm.yeno.yes
conversionFactors                       domain tcynna      tcynna.not.app
Notes                                   domain tcyesno     tcyesno.no
projectText                             domain tcyesno     tcyesno.yes
Output:
oTargetProject          - The created Project.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The Project was copied.
<> 0                    - Otherwise.
```
