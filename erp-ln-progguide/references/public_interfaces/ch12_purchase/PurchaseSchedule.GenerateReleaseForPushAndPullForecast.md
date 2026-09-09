# PurchaseSchedule.GenerateReleaseForPushAndPullForecast

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseSchedule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 439-440

```baan
DLL:   tdextpurapi
This function is available from 2022.06 (KB2241446).
Syntax: long PurchaseSchedule.GenerateReleaseForPushAndPullForecast(
domain  tcorno           iPurchaseSchedule,
domain  tdstyp           iPurchaseScheduleType,
domain  tcyesno          iGenerateMaterialRelease,
domain  tcyesno          iGenerateShippingSchedule,
boolean          iRebuildRelease,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate the purchase releases for
Push and Pull-Forecast schedules.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseSchedule               Purchase Schedule (Mandatory)
iPurchaseScheduleType           Schedule Type (Mandatory)
Allowed values:
Push
Pull Forecast
iGenerateMaterialRelease        No: Release of type 'Material
Release' is not generated.
Yes: Release of type 'Material
Release' will be generated
if applicable.
iGenerateShippingSchedule       No: Release of type 'Shipping
Schedule' is not generated.
Yes: Release of type 'Shipping
Schedule' will be generated
if applicable.
iRebuildRelease                 Rebuild the release
false: If the latest release
line for the given
schedule has status
'Scheduled', the
release line is not
rebuilt. The function
will return an error in
that case.
true:  If the latest release
line for the given
schedule has status
'Scheduled', the
release line will be
rebuilt and put to status
'Created'.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The purchase release(s) is/are generated.
<> 0                    An error occurred
```
