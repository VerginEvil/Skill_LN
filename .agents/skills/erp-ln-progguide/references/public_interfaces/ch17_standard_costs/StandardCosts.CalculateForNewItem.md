# StandardCosts.CalculateForNewItem

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 611-612

```baan
DLL:   tiextcprapi
This function is available from 2020.06 (KB2130365).
Syntax: long StandardCosts.CalculateForNewItem(
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates and actualizes the standard costs
for a new item.
This function is not allowed and will return an error when:
- Calculate and Actualize from Items - Costing Session,
as defined in the Standard Costs Parameters (ticpr0100m000),
is not allowed
- the item does have economic inventory.
The function will calculate and actualize the standard
costs using the same calculation logic als the Calculate
and Actualize Standard Costs option in session ticpr0107m000:
- using the standard price calculation code for standard items
and the project's price calculation code for customized
items
- using the current date as calculation and revaluation date
- standard items are calculated single level, customized items
are calculated top.down.
Retry points and commit / abort transactions are set and
executed within this API.
Input:  iItem           -       Item, having no economic inventory
iEnterpriseUnit -       Enterprise Unit (mandatory filled when
the concept Standard Cost per EU
is active, otherwise empty)
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               -       Standard Cost calculated and actualized
<> 0            -       Standard Costs could not be calculated or
actualized
```
