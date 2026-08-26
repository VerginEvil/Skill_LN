# PLMItem.SendToProductionBOM

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1839-1840

```baan
DLL:   pdextpdmapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long PLMItem.SendToProductionBOM(
domain  pdcmpy           iERPCompany,
domain  pdikey           iKey,
domain  pdirev           iRevision,
domain  pdintr           iLevels,
domain  pddate           iEffectiveDate,
domain  pdyesno          iSendPurchasedBOM,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface function is for transferring
item structure from PLM to Production BOM.
All the parameters are mandatory.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iERPCompany                           - ERP Company
iKey                                          - Item Key
iRevision                                     - Item Revision
iLevels                                       - Number of Levels
iEffectiveDate                                - Effective Date
iSendPurchasedBOM                             - Whether to send Purchase BOM or Not
Allowed values
pdyesno.yes                                                       - Yes
pdyesno.no                                                            - No
Output: oExceptionMessage                     - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                          - An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long                          - 0      if success
-                                       <> 0  if fail
```
