# StandardCosts.Calculate

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 603-604

```baan
DLL:   tiextcprapi
This function is available from     2020.07 (KB2135360  ).
Syntax: long StandardCosts.Calculate(
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
domain  tcrvdt           iWhichDateForRevaluate,
domain  tcdate           iSpecificDate,
domain  tcyesno          iDeleteHistory,
boolean          iRevaluationReport,
domain  tcmcs.str14      iDevice,
domain  tcmcs.str1       iLanguage,
long             iReportOpenMode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates and actualizes the standard costs
and revaluates the inventory (if needed) for the specified item.
This function is not allowed and will return an error when:
-                       economic inventory exists for the item and the user does not
have permission for session ticpr2225m000
-                       the item does not have economic inventory and the Calculate
and Actualize from Items                         - Costing Session,
as defined in the Standard Costs Parameters (ticpr0100m000),
is not allowed
-                       the item is customized and does have economic inventory.
The function will calculate and actualize and the standard costs
and revaluate the inventory if needed:
-                       for standard and customized items, but not for customized
items having economic inventory
-                       using the standard price calculation code for standard items
and the project's price calculation code for customized
items
-                       standard items are calculated single level, customized items
are calculated top.down (as in StandardCosts.CalculateForNewItem
and as in ticpr0107m000)
-                       optionally a report can be printed to show the revaluation
values.
Retry points and commit / abort transactions are set and
executed within this public interface.
Input:  iItem                         -       Item, having no economic inventory
iEnterpriseUnit                       -       Enterprise Unit (mandatory filled when
the concept Standard Cost per EU
is active, otherwise empty)
iWhichDateForRevaluate  Date used for evaluation:
(Mandatory):
. current date (tcrvdt.current.date), or
. last date of previous period
(tcrvdt.last.prev.peri), or
. a specific date (tcrvdt.specific.date).
The last 2 options are not applicable when
the Standard Cost Calculation Parameter
›¼À˜Backdate Valuation Price Allowed›¼À                                              ™ = No.
In that case the current date will be used.
iSpecificDate           Only applicable if iWhichDateForRevaluate
has the value 'a specific date'.
iDeleteHistory          Delete history, as defined in the
Calculation Parameters (ticpr0100m000).
iRevaluationReport      If true and revaluation of inventory is
done, then a report with the old and
new value of the inventory will be
created; else no report.
Is a device is already opened in the
session, then that device will be used.
If no device is opened yet, then
specify the device using the 3 arguments
below.
iDevice                 The device for the RevaluationReport.
Mandatory when iRevaluationReport = True
and iReportOpenMode = 0 and no device
is opened yet.
iLanguage               Optional. If empty then the user's
language will be used.
iReportOpenMode         Open mode for the Revaluation Report:
0                                               - User is not prompted to select a  device.
1                                               - User is prompted to select a device.
With Close (= cancel) button.
2                                               - User is prompted to select a device.
No cancel button
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                             -       Standard Cost calculated and actualized
<> 0                                  -       Standard Costs could not be calculated or
actualized
```
