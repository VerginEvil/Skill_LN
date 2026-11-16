# ExportControl.Check

> Chapter: Chapter 47 Public Interfaces for ZWF AG Shipment and Customs
>
> Group: Public Interfaces for ExportControl
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1941-1942

```baan
DLL:   tzextzfcapi
This function is available from 2025.10 (KB3629872).
Syntax: domain tcmcs.long ExportControl.Check(
domain  tcorno           iCode,
domain  tzzfc.epc.doc    iBaseType,
domain  tzzfc.sanc.ain   iAdditionalIntegration,
boolean          iShowPopupMessage,
ref     domain  tcdate           oDateOfCheck,
ref     domain  tzzfc.epc.did    oCheckID,
ref     domain  tcyesno          oBlockProzess,
ref     domain  tcmcs.str300m    oMessage mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage: Functions starts the ZWFAG Export Control check. A 3GL Session is called.
The function checks the export control information for the given document
information and returns if the process should be blocked or not.
Within the zwf module the whole checking process is logged.
Function can send E-Mails depending on export control parameter.
This function is only usable with a licensed and working ZWFAG Export Control Check.
Pre:    -
Post:   -
Input:  iCode                   - Document or Adress ID
iBaseType               - Base document type
iAdditionalIntegration  - Additional Customised Integration Type
iShowPoupMessage        - Show poupmessage with result y/n
Output: oDateOfCheck            - Date of the check
oCheckID                - Checking ID generated
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
- -1 error occured in check
```
