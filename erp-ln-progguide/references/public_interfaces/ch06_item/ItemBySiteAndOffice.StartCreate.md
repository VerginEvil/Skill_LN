# ItemBySiteAndOffice.StartCreate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemBySiteAndOffice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 193-195

```baan
DLL:   tcextibdapi
This function is available from     2025.12 (KB3638446  ).
Syntax: long ItemBySiteAndOffice.StartCreate(
long             iStartMode,
domain  tckitm           iItemTypeFrom,
domain  tckitm           iItemTypeTo,
domain  tccitg           iItemGroupFrom,
domain  tccitg           iItemGroupTo,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Create Items by Site and Office
(tcibd1253m000)
Input:
iStartMode
Not used.
iItemTypeFrom
Item Type From selection field is filled with this value.
iItemTypeTo
Item Type To selection field is filled with this value.
iItemGroupFrom
Item Group From selection field is filled with this value.
iItemGroupTo
Item Group To selection field is filled with this value.
iItemFrom
Item From selection field is filled with this value.
iItemTo
Item To selection field is filled with this value.
iProcessingOptionSet
Optional, if 0, the default options are applied.
A Processing Option Set can be created via a call to
function ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Create Items by Site and Office (tcibd1253m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
CreateForSite                   domain tcyesno          tcyesno.yes
SiteFrom                        domain tcsite           Minimum Value
SiteTo                          domain tcsite           Maximum Value
CreateForPurchaseOffice         domain tcyesno          tcyesno.no
PurchaseOfficeFrom              domain tccwoc           Minimum Value
PurchaseOfficeTo                domain tccwoc           Maximum Value
CreateForSalesOffice            domain tcyesno          tcyesno.no
SalesOfficeFrom                 domain tccwoc           Minimum Value
SalesOfficeTo                   domain tccwoc           Maximum Value
CreateForServiceOffice          domain tcyesno          tcyesno.no
ServiceOfficeFrom               domain tccwoc           Minimum Value
ServiceOfficeTo                 domain tccwoc           Maximum Value
Simulate                        domain tcyesno          tcyesno.yes
PrintReport                     domain tcyesno          tcyesno.yes
PrintErrorsOnly                 domain tcyesno          tcyesno.no
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started.
<> 0                                          - Otherwise.
```

## Public Interfaces for ItemCodeSystem

The following functions are available: ItemCodeSystem.StartOverview
