# ProductionOrder.CreateAsBuilt

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 711-712

```baan
DLL:   tiextsfcapi
This function is available from 2021.04 (KB2181351).
Syntax: long ProductionOrder.CreateAsBuilt(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to add a created Serial Number to the
As-Built Header of the Production Order. The Serial Number can
be created using ProductionOrder.CreateSerialNumber.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory if active).
iProductionOrder        Production Order (mandatory).
iItem                   Item (mandatory).
iSerialNumber           Serial Number (mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Serial Number has been added
<> 0                    - Serial Number has not been added
```
