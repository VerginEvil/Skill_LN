# Item.ConvertItemToPlanItem

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 165-165

```baan
DLL:   cpextrpdapi
This function is available from     2020.06 (KB2127795  ).
Syntax: long Item.ConvertItemToPlanItem(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tcemm.clus       iPlanningCluster,
ref     domain  cpitem           oPlanItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the plan item code for the given
general item and cluster.
Pre:    None
Post:   None
Input:  iLogisticCompany        Logistic Company (Mandatory)
iItem                   General Item (Mandatory)
iPlanningCluster        Planning Cluster (Mandatory)
Output: oPlanItem               Plan Item code
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function is executed successfully
<> 0                    An error occurred
```
