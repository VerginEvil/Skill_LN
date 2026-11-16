# MaintenanceNotification.FollowUpUnderCurrentOrder

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceNotification
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1373-1373

```baan
DLL:   tsextcfgapi
This function is available from 2025.11 (KB3603078).
Syntax: long MaintenanceNotification.FollowUpUnderCurrentOrder(
domain  tcorno           iMaintenanceNotification,
ref     domain  tsmdm.acln       oActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a follow-up activity under the originating
order of the given Maintenance Notification, based on the
Follow-up Reference Activity defined on that Maintenance
Notification.
It offers the same functionality as form command "Follow-up
under current Order" from the Maintenance Notification(s)
session.
Pre:    A db.retry.point() must have been specified.
Post:   An abort.transaction() or commit.transaction() must be executed.
Input:  iMaintenanceNotification
The Maintenance Notification for which a Follow-up
Activity must be generated; Mandatory
Output: oActivityLine
The Activity Line number of the created followup
activity under the current order, if the process
succeeded.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0:      No error
<> 0:   An error occurred
```
