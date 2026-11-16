# Tool.Return

> Chapter: Chapter 23 Public Interfaces for Manufacturing Tools
>
> Group: Public Interfaces for Tool
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 877-878

```baan
DLL:   tiexttrpapi
This function is available from 2022.01 (KB2186743).
Syntax: long Tool.Return(
domain  titrp.otyp       iOrderType,
domain  tcsite           iOrderSite,
domain  tcpdno           iOrderNumber,
domain  tcopno           iOperation,
domain  tcsern           iOperationStep,
domain  tcponl           iLineNumber,
domain  tcitem           iTool,
domain  tcibd.sern       iToolNumber,
domain  tccwoc           iWorkCenter,
domain  tcyesno          iReturnToWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface returns a Tool like session titrp0215m000.
If iWorkCenter is not empty, the Tool will be returned to the
Work Center. If iWarehouse is 'Yes', the Tool will be returned
to the warehouse. If iWorkcenter is empty and iWarehouse is on
'No', the Tool is planned for the next request line.
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
iWorkCenter             - Work Center to return the Tool to
(Optional, should be emtpy if
iWarehouse is 'Yes')
iReturnToWarehouse      - If the Tool should be returned to the
Warehouse (Should be 'No' if
iWorkCenter is not empty)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Tool returned.
<> 0                    - Otherwise.
```
