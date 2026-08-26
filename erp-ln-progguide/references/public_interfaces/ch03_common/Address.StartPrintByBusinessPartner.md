# Address.StartPrintByBusinessPartner

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Address
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 88-90

```baan
DLL:   tcextcomapi
This function is available from     2025.05 (KB3566667  ).
Syntax: long Address.StartPrintByBusinessPartner(
domain  tccom.bpid       iBusinessPartnerFrom,
domain  tccom.bpid       iBusinessPartnerTo,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session
'Print Addresses by Business Partner' (ttccom4430m100).
Input:  iBusinessPartnerFrom                  - Business Partner From
iBusinessPartnerTo                            - Business Partner To: Mandatory
iProcessingOptionSet                          - Optional, if 0, the session is started
with regular defaulting logic (user
defaults or session defaults), except
selection range for Business Partner,
which is defaulted with
iBusinessPartnerFrom and
iBusinessPartnerTo.
A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields on
session Print Addresses by Business Partner (tccom4430m100) and are not
explained in further detail here. Please refer to the session help for
additional information.
Options which are not available as Processing Options will get
defaulted with the value in column DEFAULT below.
Processing Options that are set while a required Implemented
Software Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
BusinessPartnerFrom     domain  tccom.bpid      iBusinessPartnerFrom
BusinessPartnerTo       domain  tccom.bpid      iBusinessPartnerTo
SearchKeyFrom           domain  tcseak          minimum value
SearchKeyTo             domain  tcseak          maximum value
ParentFrom              domain  tccom.bpid      minimum value
ParentTo                domain  tccom.bpid      maximum value
CountryFrom             domain  tcccty          minimum value
CountryTo               domain  tcccty          maximum value
ZIPCodeFrom             domain  tcpstc          minimum value
ZIPCodeTo               domain  tcpstc          maximum value
CityFrom                domain  tccity          minimum value
CityTo                  domain  tccity          maximum value
SortBy                  domain  tccom.sortbpad  tccom.sortbpad.bpartner
BusinessPartners        domain  tcyesno         tcyesno.no
SoldTo                  domain  tcyesno         tcyesno.no
ShipTo                  domain  tcyesno         tcyesno.no
InvoiceTo               domain  tcyesno         tcyesno.no
PayBy                   domain  tcyesno         tcyesno.no
BuyFrom                 domain  tcyesno         tcyesno.no
ShipFrom                domain  tcyesno         tcyesno.no
InvoiceFrom             domain  tcyesno         tcyesno.no
PayTo                   domain  tcyesno         tcyesno.no
AllAddressesPerRole     domain  tcyesno         tcyesno.no
Text                    domain  tcyesno         tcyesno.no
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for Warehouse

The following functions are available: Warehouse.StartOverview
