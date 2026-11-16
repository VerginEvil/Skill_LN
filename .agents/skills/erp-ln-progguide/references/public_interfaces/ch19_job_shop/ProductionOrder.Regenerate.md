# ProductionOrder.Regenerate

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 750-751

```baan
DLL:   tiextsfcapi
This function is available from 2024.02 (KB2300944).
Syntax: long ProductionOrder.Regenerate(
domain  tcsite           iSite,
domain  tcorno           iProductionOrder,
domain  tisfc.revi.sel   iRevisionSelection,
domain  tcdate           iEffectiveDate,
domain  tcyesno          iUpdateWhenNetChange,
domain  tcyesno          iUpdateReferenceDate,
domain  tcdate           iNewReferenceDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to regenerate the given Production
Order. The updated order will be based on the active Bill of
Material and Routing at the given Reference Date. Only
Production Order with selected statuses are Regenerated.
In case production order Version Control is active, regenerate
is possible when the production order status is either Created,
Scheduled or Modify. Without version control,
regenerate is possible when the production order status
is Created, Scheduled, or Printed.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site. Mandatory when the Site concept
is active.
iProductionOrder        Production Order. Mandatory, must be
in iSite. ›¼•
iRevisionSelection ›¼•  ›¼•   Specify the method for selection of
Job Shop Bom and Job Shop
Routing revisions.
Keep Revisions - No changes
Automatic --  Select based on
current date
Manual ---    Select based on
Effective Date
Mandatory when Job Shop by Site is
active. ›¼•
iEffectiveDate          Effective Date for selection of Job Shop
Bom and Job Shop Routing.
Mandatory when Job Shop by Site is
active and iRevisionSelection is Manual.
iUpdateWhenNetChange ›¼•  ›¼• Update only when a net change in product
structure of the produced item exists. ›¼•  ›¼•
Only used when Job Shop by Site is not
active.
iUpdateReferenceDate ›¼•  ›¼• Update Reference Date of
Production Order.
Only used when Job Shop by Site is not
active.
iNewReferenceDate       New Reference Date for the
Production Order.
Mandatory when iUpdateReferenceDate
is YES.
Only used when Job Shop by Site
is not active.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Regenerate succeeded.
<> 0                    Regenerate failed.
```
