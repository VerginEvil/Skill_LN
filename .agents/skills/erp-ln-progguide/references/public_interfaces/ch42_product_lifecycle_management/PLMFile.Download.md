# PLMFile.Download

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMFile
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1861-1861

```baan
DLL:   pdextpdmapi
This function is available from 2024.04 (KB2328014).
Syntax: long PLMFile.Download(
domain  pdfkey           iFileKey,
domain  pdfrev           iVersion,
domain  pdm260           iFilePath mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is for Downloading File to from PLM Vault
to LN Server appdata folder.
All the parameters are mandatory.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iFile                   - File Key
iVersion                - File Version
iFilePath               - Destination File Path
Eg : ${BSE}\..\..\..
Output: oExceptionMessage       - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID    -       An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long            - 0      if success
- <> 0  if fail
```
