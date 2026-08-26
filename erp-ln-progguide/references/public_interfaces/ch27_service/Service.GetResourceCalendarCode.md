# Service.GetResourceCalendarCode

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Service
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1337-1338

```baan
DLL:   tsextsocapi
This function is available from     2020.04 (KB2117506  ).
Syntax: long Service.GetResourceCalendarCode(
domain  tcncmp           iLogisticCompany,
domain  tsclm.crtc       iResponseType,
domain  tsbsc.clst       iInstallationGroup,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcemno           iAssignedServiceEngineer,
domain  tcemno           iPreferredServiceEngineer,
domain  tccwoc           iServiceDepartment,
ref     domain  tcccp.ccal       oCalendarCode,
ref     domain  tczone           oTimeZone,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function determines a calendar code and the time zone
that is related to the calendar.
The calendar code and time zone are retrieved in the
following way.
When the parameter 'Use Engineer Calendar for Planning'
is No, the calendar/timezone is searched in the following
order:
1. Response Type
2. Serialized Item
3. Installation Group
4. Assigned Service Engineer
5. Preferred Service Engineer
6. Service Center
7. Company
This means that the Response Type calendar is retrieved first.
When no Response Type calendar is available the calendar of
the Serialized Item is retrieved. And so on.
When for the first 6 levels no calendar is found, finally
the Company calendar/timezone is retrieved; this
calendar/timezone is mandatory, so is always available.
When the parameter 'Use Engineer Calendar for Planning'
is Yes, the calendar/timezone is searched in the following
order:
1. Assigned Service Engineer
2. Preferred Service Engineer
3. Service Center
4. Response Type
5. Serialized item
6. Installation Group
7. Company
Pre     : None
Post    : None
Input   : iLogisticCompany                            - Logistic Company: Mandatory
iResponseType                                         - Response Type: Not Mandatory
iInstallationGroup                                    - Installation Group:
Not Mandatory
iItem                                                 - Item: Not Mandatory
iSerialNumber                                         - Serial Number: Not Mandatory
iAssignedServiceEngineer                              - Assigned Service Engineer:
Not Mandatory
iPreferredServiceEngineer                             - Preferred Service Engineer:
Not Mandatory
iServiceDepartment                                    - Service Department:
Not Mandatory
Output  : oCalendarCode                               - Calendar Code
oTimeZone                                             - Time Zone
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - Data read
<> 0                                                  - An error occurred
```
