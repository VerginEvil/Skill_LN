# AdditionalFile.Download

> Chapter: Chapter 53 Public Interfaces for Application Development
>
> Group: Public Interfaces for AdditionalFile
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1941-1942

```baan
DLL:   ttextadvapi
This function is available from     2026.06 (KB3672721  ).
Syntax: long AdditionalFile.Download(
domain  ttscm.sofc       iAdditionalFile mb,
domain  ttaud.path       iDestinationFolder mb,
ref     domain  ttadv.lfil       oFileName mb,
ref             string           oExceptionMessage() mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface downloads an additional file to the given folder.
The following rules apply for the download action.
-                       The download action can only handle additional files in package tx and
BFlow files from all packages
-                       The additional file argument (iAdditionalFile) consists of package,
module and additional file name. If the component does not exists
an error will be returned
-                       The additional file will be searched in the package VRC of package tx
of the current package combination of the user
-                       When the lowercase filename already exists in iDestinationFolder,
it is overwritten.
Pre:                  -
Post:                 -
Input:  iAdditionalFile               - The additional file to be downloaded. Including package,
module, additional file and extension. Mandatory
iDestinationFolder                            - Complete path of the destination
folder. Mandatory
Output: oFileName                             - The lowercase name of the Additional File
oExceptionMessage                             - A message if the return value is not equal
to 0. This message contains the root cause of
the method failure.
oExceptionID                                  - An ID that refers to all error information. Use
the functions in Exception to get the error
messages.
Return values:
0                                     - Function is executed successfully
<> 0                                  - Error(s) occurred
```
