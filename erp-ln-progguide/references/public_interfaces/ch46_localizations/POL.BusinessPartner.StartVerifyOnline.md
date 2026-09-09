# POL.BusinessPartner.StartVerifyOnline

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for POL.BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1938-1939

```baan
DLL:   lpextpolapi
This function is available from 2025.04 (KB3568308).
Syntax: long POL.BusinessPartner.StartVerifyOnline(
long             iStartMode,
domain  tccom.bpid       iBusinessPartner,
domain  tctax.txnb       iTaxNumber,
domain  tccom.iban       iBankAccountNumber,
domain  tcyesno          iSearchMethod,
domain  tcntdt           iOnDate,
domain  tcntdt           iSkipAfter,
domain  tcyesno          iOneTimeBusinessPartner,
domain  tcyesno          iSkipPhysicalPersons,
domain  tcmcs.cbtp       iBusinessPartnerType,
domain  tcyesno          iNewMessagesOnly,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to start the Verify Business Partner Online
session (lppol4250m000) from public interface
Pre:    Business Partner Verification Webservice URL must be filled
in the Polish Localization Parameters (lppol0100m000) with
https://wl-api.mf.gov.pl/api/
Post:   n/a
Input:  iStartMode
Specifies the start mode for the session.
Possible value is:
MODAL   -       The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
(mandatory)
iBusinessPartner        - Business Partner code of the Polish taxpayer
Note: Business Partner must be empty when Tax Number is filled
iTaxNumber              - Polish Tax Number (NIP)
Note: Tax Number must be empty when Business Partner is filled
iBankAccountNumber      - International Bank Account Number
Note: At least one of the fields above must be filled.
iSearchMethod           - Specifies API method (search or check)
Possible value is:
Yes: looks up all bank accounts and taxpayer status
based on the tax number or bank account.
No: checks whether a tax number and bank account
combination is registered in the KAS database
iOnDate                 - The date for which the check
should be performed
Note: Specify 0 for current date
iSkipAfter              - Skip verification if performed after that date
Note: Specify 0 to use default
iOneTimeBusinessPartner - Include one-time business partners
iSkipPhysicalPersons    - Exclude Physical Persons
iBusinessPartnerType    - Business Partner Type assigned to
Physical Persions in the
Invoice-from Business Partner
(tccom4122s000) session
Note: Mandatory when Skip Perions = Yes.
Must be empty when Skip Perions = No
iNewMessagesOnly        - only those messages will be printed
which have been created since the last
usage of the Verify command
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
