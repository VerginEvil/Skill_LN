# Project.UpdateWorkAuthorizationStatus

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1679-1681

```baan
DLL:   tpextpssapi
This function is available from     2026.09 (KB3668094  ).
Syntax: long Project.UpdateWorkAuthorizationStatus(
domain  tccprj           iProject,
domain  tppdm.cact       iFromActivity,
domain  tppdm.cact       iToActivity,
domain  tppdm.cspa       iFromElement,
domain  tppdm.cspa       iToElement,
domain  tcyesno          iFromAnyStatus,
domain  tppdm.wast       iFromStatus,
domain  tppdm.wast       iToStatus,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to Update / Set Work Authorization
Status of Activities, Elements of a given Project.
This function offers similar functionality as session
Update Work Authorization Status (tppss2205m000).
Be aware that transaction management is handled within this function.
Note : This function should be called for one project at a time.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iProject                              - Project. Mandatory
iFromActivity                                 - From Activity. Optional
iToActivity                                   - To Activity. Optional
If iToActivity not filled and iFromActivity is
filled,
iToActivity defaults to iFromActivity.
iFromElement                                  - From Element. Optional
iToElement                                    - To Element. Optional
If iToElement not filled and iFromElement is
filled,
iToElement defaults to iFromElement.
iFromAnyStatus                                - From Any Status (Yes/No). Mandatory
If Yes, All applicable statuses are considered
and iFromStatus is ignored.
If No, Only activities with status equal to
iFromStatus are selected (iFromStatus becomes
Mandatory).
iFromStatus                                   - From Status. Optional
iToStatus                                     - To Status. Mandatory
Allowed values for iFromStatus, iToStatus are:
tppdm.wast.free                                       - Free
tppdm.wast.onhold                                     - On Hold
tppdm.wast.released                                   - Released
tppdm.wast.finished                                   - Finished
tppdm.wast.closed                                     - Closed
iProcessingOptionSet                          - Optional
if 0, the default options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Update Work Authorization Status (tppss2205m000) are
not explained in further detail here. Please refer to the session help
for additional  information. Update Work Authorization Status
options which are not available as Processing Options will get defaulted in
accordance with the session logic.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                               TYPE          DEFAULT
ExtensionFrom                       domain  tpptc.cstl  Minimum Value
ExtensionTo                         domain  tpptc.cstl  Maximum Value
SubtreeOfActivityStructure          domain  tppdm.yeno  tppdm.yeno.no
TopActivity                         domain  tppdm.cact  <Top Activity>
OnlyWithReason                      domain  tcyesno     tcyesno.no
SelectOnHoldStatusReason            domain  tccdis      <Empty>
OnHoldReasonCode                    domain  tccdis      <Empty>
ConsiderOpenPLMBusinessProcessActivities
domain  tppdm.yeno  tppdm.yeno.no
SetPLMBusinessProcessToCompleted    domain  tppdm.yeno  tppdm.yeno.no
ReasonToSetPLMBusinessProcessToCompleted
domain  tcmcs.str215m <Empty>
UpdateBasedOnScheduledDateProgress  domain  tppdm.yeno  tppdm.yeno.no
ScheduledStartDate                  domain  tcdate      <Current Date and Time>
UpdateBasedOnActualDateProgress     domain  tppdm.yeno  tppdm.yeno.no
ActualFinishDate                    domain  tcdate      <Current Date and Time>
UpdateBasedOnPercentageProgress     domain  tppdm.yeno  tppdm.yeno.no
PercentageCompleted                 domain  tppdm.pera  100
UpdateBasedOnMilestones             domain  tppdm.yeno  tppdm.yeno.no
Output:
oExceptionMessage                             - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0. If more than one message is
given, these are present in the oExceptionID.
oExceptionID                                  - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Process successful
<> 0                          - An error occurred
```

## Public Interfaces for ProjectContract

The following functions are available: ProjectContract.GetTotalAmountContractLines ProjectContract.StartMultiMain
