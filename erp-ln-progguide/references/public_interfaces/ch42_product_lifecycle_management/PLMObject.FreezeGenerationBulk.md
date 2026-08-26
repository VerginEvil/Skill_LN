# PLMObject.FreezeGenerationBulk

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMObject
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1829-1829

```baan
DLL:   pdextpdmapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long PLMObject.FreezeGenerationBulk(
domain  tcguid.extend    iBatchGuid,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is to perform freeze generation for bulk
objects.
The transaction management has to be taken care by the calling
program.
All the parameters are mandatory.
Pre:    A list of objects for which generation needs to be freezed, by
inserting them into table "Input Set Of Objects" (pdsnp030) with
a unqiue "Batch Guid".
While creating entries in the table Input Set Of Objects (pdsnp030),
specify the change mode of that object.
Post:   Delete the records from Input Set Of Objects (pdsnp030) based
on the Batch Guid generated in the Pre step.
Input:  iBatchGuid                      - Batch Guid
Output: oExceptionMessage               - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                            - An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long                           - 0     if success
-                                        <> 0  if fail
```
