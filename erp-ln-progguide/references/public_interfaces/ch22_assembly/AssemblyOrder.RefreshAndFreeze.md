# AssemblyOrder.RefreshAndFreeze

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 854-855

```baan
DLL:   tiextascapi
This function is available from     2026.05 (KB3650669  ).
Syntax: long AssemblyOrder.RefreshAndFreeze(
domain  tccpva           iProductVariant,
domain  tiasln           iRollOffLine,
domain  tcyesno          iFreeze,
domain  tiasc.ardt.typ   iAssemblyReferenceDateType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to refresh and freeze Assembly Orders
for the given Product Variant and Roll Off Line.
This function must not be called within a logical transaction
as this function will have its own transaction handling.
Pre:              -   There should be no pending logical transaction before
calling this function.
Post:              -  No need to commit or abort, that is handled within the function.
Input:  iProductVariant
Product Variant(Mandatory)
Product Variant for which Assembly
Orders will be Refreshed/Frozen
iRollOffLine
Roll Off Line (Mandatory)
The Product Variant's roll                              -off line,
or one of the Product Variant's
sub                              -generic Items' Roll-Off Line.
iFreeze
Freeze (Optional)
Default value No.
This flag is used to indicate whether to
attempt to freeze Orders or not
iAssemblyReferenceDateType
Assembly Reference Date Type (Optional)
Default value Configuration Date of Variant.
1. Prod. Configuration Date of Variant
2. Planned Offline Date of Assy Order
3. Planned Start Date of Assy Order
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Assembly Order              - Line Station Orders Status
will be moved to frozen.
<> 0    Error occurred during process.
```
