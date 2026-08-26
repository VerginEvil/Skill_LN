# PLMFile.View

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMFile
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1842-1842

```baan
DLL:   pdextpdmapi
This function is available from     2024.08 (KB3515163  ).
Syntax: long PLMFile.View(
domain  pdfkey           iFileKey,
domain  pdfrev           iVersion,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is for Viewing File from PLM Vault
appdata folder.
All the parameters are mandatory.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iFile                                 - File Key
iVersion                                      - File Version
Output: oExceptionMessage                     - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                          -       An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long                          - 0      if success
-                                       <> 0  if fail
```

## Public Interfaces for PLMProductItem

The following functions are available: PLMProductItem.SendToReceivedJSBOM
