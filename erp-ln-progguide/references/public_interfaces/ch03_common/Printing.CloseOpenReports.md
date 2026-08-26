# Printing.CloseOpenReports

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Printing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 147-148

```baan
DLL:   tcextcomapi
This function is available from     2026.05 (KB3669196  ).
Syntax: long Printing.CloseOpenReports(
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the closing of reports.
This function should be called when indicated in other
public interfaces. Typically after the printing has been done.
Pre:                  -
Post:                 -
Input:                -
Output:               -
Return: void
```

## Chapter 4 Public Interfaces for Calendar

## Public Interfaces for Calendar

The following functions are available: Calendar.CalculateDaysFromHours Calendar.GetPeriodCapacity Calendar.GetWorkingDays Calendar.PlanLeadTimeBackward Calendar.PlanLeadTimeForward Calendar.StartUpdateWorkingHours Calendar.UpdateWorkingHours
