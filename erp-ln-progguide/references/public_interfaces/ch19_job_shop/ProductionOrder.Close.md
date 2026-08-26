# ProductionOrder.Close

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 710-711

```baan
DLL:   tiextsfcapi
This function is available from     2025.12 (KB3573796  ).
Syntax: long ProductionOrder.Close(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is designed to programmatically close
production orders. Its functionality closely mirrors that of the
standard LN session Close Production Orders (ticst0201m000).
Transaction handling is handled in the public interface.
Options for simulation and printing are left out deliberately.
This function makes use of a Processing Option Set, which can be
created via a call to ProcessingOptionSet.Create(), and cleaned
up after use, via a call to ProcessingOptionSet.Delete().
Pre:    N.A.
Post:   N.A.
Input:  iSite                   Site. (Mandatory when the Site concept
is active and an input Production Order
is provided).
iProductionOrder        Production Order.
iProcessingOptionSet    A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create(). If 0, then
defaults are applied.
NAME                            TYPE                    DEFAULT
SiteFrom                        domain tcsite           ""
SiteTo                          domain tcsite           "ZZZZZZZZZ"
ProductionOrderFrom             domain tcpdno           ""
ProductionOrderTo               domain tcpdno           "ZZZZZZZZZ"
CompletionDateFrom              domain tisfc.utcm       0
CompletionDateTo                domain tisfc.utcm       Current Date
PCSProjectFrom                  domain tccprj           ""
PCSProjectTo                    domain tccprj           "ZZZZZZZZZ"
ItemFrom                        domain tcitem           ""
ItemTo                          domain tcitem           "ZZZZZZZZZ"
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Production Orders closed successfully.
<> 0                    Otherwise.
```
