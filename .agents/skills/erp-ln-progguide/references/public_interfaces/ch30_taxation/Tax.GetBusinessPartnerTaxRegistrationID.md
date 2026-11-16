# Tax.GetBusinessPartnerTaxRegistrationID

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1640-1641

```baan
DLL:   tcexttaxapi
This function is available from 2024.01 (KB2311239).
Syntax: long Tax.GetBusinessPartnerTaxRegistrationID(
domain  tcncmp           iFinancialCompany,
const   domain  tccom.bpid       iBusinessPartner,
const   domain  tcccty           iCountry,
const   domain  tcmcs.cste       iState,
const   domain  tcezty           iEconomicZoneType,
domain  tcdate           iReferenceDate,
ref     domain  tctax.txnb       oBusinessPartnerTaxRegistrationID,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the business partner's tax registration
ID.
Pre:    NA
Post:   NA
Input:  iFinancialCompany       - Financial Company     (Mandatory)
iBusinessPartner        - Business Partner      (Mandatory)
iCountry                - Country               (Mandatory)
iState                  - State
iEconomicZoneType       - Economic Zone Type
iReferenceDate          - Reference Date
(This is a UTC Date/Time.)
Output: oBusinessPartnerTaxRegistrationID -
Business Partner Tax Registration ID
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success
<> 0                    - Error
```
