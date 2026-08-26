# Tool.ReturnToOrder

> Chapter: Chapter 23 Public Interfaces for Manufacturing Tools
>
> Group: Public Interfaces for Tool
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 868-869

```baan
DLL:   tiexttrpapi
This function is available from     2022.01 (KB2186743  ).
Syntax: long Tool.ReturnToOrder(
domain  titrp.otyp       iOrderType,
domain  tcsite           iOrderSite,
domain  tcpdno           iOrderNumber,
domain  tcopno           iOperation,
domain  tcsern           iOperationStep,
domain  tcponl           iLineNumber,
domain  tcitem           iTool,
domain  tcibd.sern       iToolNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface returns a Tool to Order like session
titrp0215m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:
iOrderType                                    - Order Type
iOrderSite                                    - Order Site (Mandatory when Active)
iOrderNumber                                  - Order Number (Mandatory)
iOperation                                    - Operation (Mandatory)
iOperationStep                                - Operation Step (Mandatory)
iLineNumber                                   - Line Number (Mandatory)
iTool                                         - Tool (Mandatory)
iToolNumber                                   - Tool Number (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Tool returned to Order.
<> 0                                          - Otherwise.
```
