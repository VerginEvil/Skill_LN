# ProductionOrder.CancelV2

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 707-708

```baan
DLL:   tiextsfcapi
This function is available from 2026.08 (KB3658170).
Syntax: long ProductionOrder.CancelV2(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
boolean          iAutoComplete,
boolean          iReturnMaterials,
boolean          iSimulate,
boolean          iResetSerialsBeforeCancel,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will cancel a Production Order in
status "Released" or "Active".
Transaction management is handled by this public interface.
Pre:    None.
Post:   None.
Input:  iSite                   - Site (mandatory if active).
iProductionOrder        - Production Order (mandatory).
iAutoComplete           - Option if Active Production Orders have
to be completed automatically.
iReturnMaterials        - Option if already issued Materials have
to be returned.
iSimulate               - Simulate.
iResetSerialsBeforeCancel
- iResetSerialsBeforeCancel functions only
In simulation mode. Set the serial status
To created before Canceling the production
Order.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Production Order has been cancelled.
<> 0                    - Production Order has not been
cancelled.
```
