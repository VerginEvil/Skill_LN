# Tool.Request

> Chapter: Chapter 23 Public Interfaces for Manufacturing Tools
>
> Group: Public Interfaces for Tool
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 876-877

```baan
DLL:   tiexttrpapi
This function is available from 2022.01 (KB2186743).
Syntax: long Tool.Request(
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
Usage:        Expl:   This Public Interface requests a Tool like session titrp0215m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:
iOrderType              - Order Type
iOrderSite              - Order Site (Mandatory when Active)
iOrderNumber            - Order Number (Mandatory)
iOperation              - Operation (Mandatory if iOrderType is
Production Order or Service Order)
iOperationStep          - Operation Step (Optional. Only used
if iOrderType is Production Order)
iLineNumber             - Line Number (Mandatory if iOrderType
is Service Order, Maintenance Work
Order or Production Schedule)
iTool                   - Tool (Mandatory)
iToolNumber             - Tool Number (Mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Tool requested.
<> 0                    - Otherwise.
```
