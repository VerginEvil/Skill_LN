# Project.StartCopy

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1676-1677

```baan
DLL:   tpextpdmapi
This function is available from     2022.02 (KB2214144  ).
Syntax: long Project.StartCopy(
long             iStartMode,
domain  tccprj           iSourceProject,
ref     domain  tccprj           oTargetProject,
ref     domain  tcdsca           oTargetProjectDescription mb,
ref             boolean          oProjectCopied,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl    This function starts the Copy Project session (tppdm7840m000).
The source Project and the most relevant fields for a new
Project can be passed to the session.
Other fields can be set in the session or one can
use the Saved Defaults or use the Defaults Saved to
Personalization.
Input:  iStartMode
Specifies the start mode for the session (Mandatory).
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSourceProject
The Project to be copied
...
Additional input, specifies the option in a string, followed by
the required value in the proper format.
Possible options are:
TargetProject   A string containing the Project code of the new
Project or a Project Series to generate a new code
TargetProjectDescription
A string for the description of the new Project
SubProject      A boolean to indicate a Sub Project:
True    when the new Project must be linked to a
Main Project
False   when the new Project is a Single Project
MainProject     A string containing the Project code of the Main
Project in case of a Sub Project
ProjectAddress  A string for the Project Address code
ShipfromAddress A string for the standard Ship                      -from Address code
for project deliveries
ProjectManager  A string containing the code of the Manager of
the Project
ProjectManagementOffice
A string containing the code of the Office
responsible for the Project
EnterpriseUnit  A string containing the code of the Enterprise
Unit to which the Project belongs
PrioritySupplyWarehouse
A string containing the code of the general
Warehouse for receiving and for deliveries to
the Project
StartDate       A long UTC value for Project Start Date
FinishDate      A long UTC value for Project Finish Date
Example: The Copy Project session will be started and has the
source Project filled, with a target project series for a new
'Single Project', with a description and a start date:
Project.StartCopy(
|* Fixed arguments:
start.mode,                                                           - input
source.project,                                                       - input
target.project,                                                       - output
target.project.description,                                           - output
project.copied,                                                       - output
exception.message,                                                    - output
exception.id,                                                         - output
|* Variable arguments:
"TargetProject",                                                      - input
project.series,                                                       - input
"TargetProjectDescription",                                           - input
project.description,                                                  - input
"SubProject",                                                         - input
true,                                                            -      input
"StartDate",                                                          - input
date.time.utc)                                                        - input
Output:
Note: the session must be started modal to have the copy
results returned in the output.
oTargetProject                                - The created Project
oTargetProjectDescription
-                                               The Description of the created Project
oProjectCopied                                - True, if the Project has been copied
-                                               False, otherwise
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```
