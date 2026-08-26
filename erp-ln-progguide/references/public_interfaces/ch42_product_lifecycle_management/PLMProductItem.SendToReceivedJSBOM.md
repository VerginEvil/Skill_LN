# PLMProductItem.SendToReceivedJSBOM

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMProductItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1842-1846

```baan
DLL:   pdextpdmapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long PLMProductItem.SendToReceivedJSBOM(
domain  pdcmpy           iERPCompany,
domain  pderp.site       iSite,
domain  pdpdm.eprj       iPCSProject,
domain  tcmcs.str60      iBillofMaterialsID,
domain  pdikey           iKey,
domain  pdirev           iRevision,
domain  pdintr           iLevels,
domain  pddate           iEffectiveDate,
domain  pdyesno          iSendPurchasedBOM,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface for transferring product item structure
from PLM to Received JS BOM.
All the parameters are mandatory.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iERPCompany                           - ERP Company
iSite                                         - Site
iPCSProject                                   - PCS project
iBillofMaterialsID                            - Bill of Materials ID in Production BOM
iKey                                          - Item Key
iRevision                                     - Revision
iLevels                                       - Number of Levels
iEffectiveDate                                - Effective Date
iSendPurchasedBOM                             - Whether to send Purchase BOM or Not
Allowed values
pdyesno.yes                                                       - Yes
pdyesno.no                                                            - No
Output: oExceptionMessage                     - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                          - An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long                          - 0      if success
-                                       <> 0  if fail
```

## Chapter 43 Public Interfaces for Extended Time

## Management

## Public Interfaces for Attendance

The following functions are available: Attendance.DeleteActualAttendance Attendance.DeleteActualAttendanceGenerated Attendance.DeleteActualAttendanceManuallyAdded Attendance.GetActualAttendance Attendance.GetActualAttendanceForDate Attendance.GetActualHours Attendance.GetActualHoursForDate Attendance.GetAttendanceTypeAbsence Attendance.GetAttendanceTypeAttendanceTime Attendance.GetAttendanceTypeAutoBreak Attendance.GetAttendanceTypeBasicShiftDifference Attendance.GetAttendanceTypeClosingDifference Attendance.GetAttendanceTypeNormalTime Attendance.GetAttendanceTypeOffsite Attendance.GetAttendanceTypePostingDifferenceClockIn Attendance.GetAttendanceTypePostingDifferenceClockOut Attendance.GetAttendanceTypePunchedBreak Attendance.GetAttendanceTypeStandbyTime Attendance.GetAttendanceTypeTravel Attendance.GetBalanceBeginningHours Attendance.GetBalanceBeginningOvertime Attendance.GetBalanceBeginningVacation Attendance.GetBalanceEndHours Attendance.GetBalanceEndOvertime Attendance.GetBalanceEndVacation Attendance.GetBalanceHours Attendance.GetBalanceHoursForDate Attendance.GetDate Attendance.GetDayOfMonth Attendance.GetDays Attendance.GetDaysForDate Attendance.GetDayType Attendance.GetDepartment Attendance.GetEmployee Attendance.GetEmployeeGroup Attendance.GetFirstDayOfPeriod Attendance.GetHours Attendance.GetHoursForDate Attendance.GetLastDayOfPeriod Attendance.GetMonth Attendance.GetNumberOfStartTransactions Attendance.GetNumberOfStartTransactionsForKindOfTime Attendance.GetNumberOfStopTransactions Attendance.GetNumberOfStopTransactionsForKindOfTime Attendance.GetNumberOfTransactions Attendance.GetNumberOfTransactionsForKindOfTime Attendance.GetOvertimeHours Attendance.GetOvertimeHoursForDate Attendance.GetPaidHours Attendance.GetPaidHoursForDate Attendance.GetPeriodNumber Attendance.GetPeriodTableCode Attendance.GetPeriodYear Attendance.GetPlannedHours Attendance.GetPlannedHoursForDate Attendance.GetVacationDays Attendance.GetVacationDaysForDate Attendance.GetWeek Attendance.GetWeekDay Attendance.GetYear Attendance.GetYearDay Attendance.IsFirstDayOfPeriod Attendance.IsLastDayOfPeriod Attendance.NewRemark Attendance.SetActualAttendance Attendance.SetDayType Attendance.UpdateActaulAttendance Attendance.UseAttendanceTypeAbsence Attendance.UseAttendanceTypeAttendanceTime Attendance.UseAttendanceTypeAutoBreak Attendance.UseAttendanceTypeBasicShiftDifference Attendance.UseAttendanceTypeOffSite Attendance.UseAttendanceTypePostingDifferenceTypeClockIn Attendance.UseAttendanceTypePostingDifferenceTypeClockOut Attendance.UseAttendanceTypePunchedBreak Attendance.UseAttendanceTypeStandbyTime Attendance.UseAttendanceTypeTravel
