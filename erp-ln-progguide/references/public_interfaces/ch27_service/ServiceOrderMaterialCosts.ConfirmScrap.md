# ServiceOrderMaterialCosts.ConfirmScrap

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderMaterialCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1453-1454

```baan
DLL:   tsextsocapi
This function is available from     2026.09 (KB3691643  ).
Syntax: long ServiceOrderMaterialCosts.ConfirmScrap(
domain  tcorno           iServiceOrder,
domain  tcpono           iMaterialLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to confirm scrap for a service order
material line.
Pre:    Set db.retry.point
Post:   Abort/Commit Transaction
Input:  iServiceOrder
Service Order
Mandatory.
iMaterialLine
Service Order Material Line
Not Mandatory.
If not specified, Confirm Scrap is done for Material
Lines of the Service Order with delivery type "To Scrap".
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Not Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
ContinueWhenSerialNumberNotFilledForSerializedControlledItem
domain  tcyesno         tcyesno.no
If this option is no, then confirming scrap is not allowed
when the item is serialized controlled, but no serial number is
filled.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No Error
<> 0                          - Error
```
