# NonConformanceReport.StartWorkbench

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for NonConformanceReport
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1775-1777

```baan
DLL:   qmextncmapi
This function is available from     2025.08 (KB3606310  ).
Syntax: long NonConformanceReport.StartWorkbench(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcyesno          iAllOrderOrigin,
domain  qmncm.orgn       iOrderOrigin,
domain  tccwar           iWarehouse,
domain  tccwoc           iDepartment,
domain  tccprj           iProject,
domain  tccom.bpid       iBusinessPartner,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Non-Conformance Reports Workbench session
(qmncm1600m000) with Filters.
Input:  iStartMode                    - Specifies the start mode for the session
Possible values are:
MODAL   :       The parent session is  blocked
until the child session exits, in case
of a multi                                              -occurrence the session will
be started as a zoom session.
MODELESS:       Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
Not Used.
The Following Input Arguments are Filters,
And this Arguments are Optional.
----------------------------------------------------------------
iAllOrderOrigin                         - All Order Origin. Possible Input values are,
Yes: All Order Origins are included in filter.
No : Not All Order Origins are included, and
Filter will be applied based on iOrderOrigin.
iOrderOrigin                            - Order Origin, This filter is only
considered when iAllOrderOrigin is NO.
iWarehouse                              - Warehouse.
iDepartment                             - Department.
iProject                                - Project.
iBusinessPartner                        - Business Partner.
iItem                                   - Item.
Output: oExceptionMessage               - The last message if any message is found.
If more than one message is given, these are
present in the oExceptionID.
oExceptionID                            - An ID that refers to the exception
information. Use the functions in Exception
to get all relevant information.
Return: 0                               - Session started
<> 0                                    - An error occurred
```

## Public Interfaces for QualityResourceAssignment

The following functions are available: QualityResourceAssignment.Cancel QualityResourceAssignment.Complete QualityResourceAssignment.Start QualityResourceAssignment.Stop
