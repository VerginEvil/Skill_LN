# SanctionList.Check

> Chapter: Chapter 47 Public Interfaces for ZWF AG Shipment and Customs
>
> Group: Public Interfaces for SanctionList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1940-1941

```baan
DLL:   tzextzfcapi
This function is available from 2025.10 (KB3629872).
Syntax: domain tcmcs.long SanctionList.Check(
domain  tzzfc.sanc.doc   iBaseType,
domain  tcncmp           iFinancialComp,
domain  tzzfc.sanc.ain   iAdditionalIntegration,
domain  tctran           iTransactionID,
domain  tcorno           iCode,
boolean          iShowPopupMessage,
boolean          iIsAdressCheck,
boolean          iIsUpdate,
ref     domain  tcdate           oDateOfCheck,
ref     domain  tcmcs.long       oCheckSequence,
ref     domain  tcyesno          oBlockProzess,
ref     domain  tcmcs.str300m    oMessage mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage: Functions starts the ZWFAG Sanction List check. A 3GL Session is called.
The function checks the sanction list information for the given address or
document information and returns if the process should be blocked or not.
Within the zwf module the whole checking process is logged.
Function can send E-Mails depending on Sanction list parameter.
This function is only usable with a licensed and working ZWFAG Sanction List Check.
Pre:    -
Post:   -
Input:  iBaseType               - Base document type
iFinancialComp          - Financial company (for invoices)
iAdditionalIntegration  - additional integration string
iTransactionID          - Transaction type (for invoices)
iCode                   - Document or Adress ID
iShowPopupMessage       - Show poupmessage with result y/n
iIsAdressCheck          - Is check for LN adress code
iIsUpdate               - True for DAL_UPDATE
- False for DAL_NEW
Output: oDateOfCheck            - Date of the check
oCheckSequence          - Checking sequence generated
oBlockProzess           - Blocking indicator
oMessage                - Message when function was successful
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: domain tcmcs.long       - 0 success
- DALHOOKERROR Error occured in check
```
