# PurchaseOrder.StartPrintReminders

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 449-451

```baan
DLL:   tdextpurapi
This function is available from     2026.01 (KB3643777  ).
Syntax: long PurchaseOrder.StartPrintReminders(
long             iStartMode,
boolean          iIgnoreSelectionFields,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function starts the session Print Purchase Order
Reminders (tdpur4403m000). Depending on the main table of the
calling session, Non                      -Consecutive Record Selection (NCRS) is
applied. Specifically, when the main table is either:
* Purchase Orders (tdpur400), or
* Purchase Order Lines (tdpur401),
the session processes the selected records accordingly.
If the parameter iIgnoreSelectionFields is set to false, any
ranges provided in the option set are applied as additional
filters to further refine the selected records.
Pre:    N/A
Post:   N/A
Input:  iStartMode                            - Not used
iIgnoreSelectionFields                        - If true, the session is started with
the session                                                -defaults, instead of
filling the fields through this Public
Interface.
iProcessingOptionSet                          - Processing Option Set (optional).
If 0, the default options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session Print Purchase Order Reminders (tdpur4403m000)) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
Supported Processing Options and their defaults:
NAME                              TYPE                  DEFAULT
------------------------------------------------------------------------
BuyFromBPFrom                     domain tccom.bpid     Minimum Value
BuyFromBPTo                       domain tccom.bpid     Maximum Value
ShipFromBPFrom                    domain tccom.bpid     Minimum Value
ShipFromBPTo                      domain tccom.bpid     Maximum Value
PurchaseOfficeFrom                domain tccwoc         Minimum Value
PurchaseOfficeTo                  domain tccwoc         Maximum Value
BuyerFrom                         domain tcemno         Minimum Value
BuyerTo                           domain tcemno         Maximum Value
PlannerFrom                       domain tcemno         Minimum Value
PlannerTo                         domain tcemno         Maximum Value
PurchaseOrderFrom                 domain tcorno         Minimum Value
PurchaseOrderTo                   domain tcorno         Maximum Value
PurchaseOrderLineFrom             domain tcpono         Minimum Value
PurchaseOrderLineTo               domain tcpono         Maximum Value
ItemFrom                          domain tcitem         Minimum Value
ItemTo                            domain tcitem         Maximum Value
ReferenceDate                     domain tcdate         Current Date/Time
DateOnReminder                    domain tcdate         Current Date/Time
AddressTo                         domain tccom.bprp     tccom.bprp.buy.from
SortedBy                          domain tdpur.orso     tdpur.orso.otbp
PrintRemindersByBuyFromBP         domain tcyesno        tcyesno.yes
IgnoreOrderLinesNotYetPrinted     domain tcyesno        tcyesno.no
PrintLinesWithUnconfirmedReceipt  domain tcyesno        tcyesno.yes
PrintToPredefinedDevice           domain tcyesno        tcyesno.yes
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information
Return: 0                                     - Session started
<> 0                                          - An error occurred
```
