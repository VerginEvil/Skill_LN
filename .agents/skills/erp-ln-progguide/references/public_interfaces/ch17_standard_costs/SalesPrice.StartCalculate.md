# SalesPrice.StartCalculate

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for SalesPrice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 619-621

```baan
DLL:   tiextcprapi
This function is available from 2025.06 (KB3539789).
Syntax: long SalesPrice.StartCalculate(
long             iStartMode,
domain  tcitem           iItem,
domain  tccpcc           iStandardCostCalculationCode,
domain  tccpcc           iSalesPriceCalculationCode,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to start the process session
Calculate Sales Prices (ticpr2250m000). Use this session to
calculate sales prices for standard items.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS -
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dialog.
iItem                   Item (Optional)
iStandardCostCalculationCode
Standard Cost Calculation Code (Optional)
iSalesPriceCalculationCode
Sales Price Calculation Code (Optional)
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields on
session Calculate Sales Prices (ticpr2250m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
NAME                            TYPE                    DEFAULT
FromItem                        tcitem                  ""
ToItem                          tcitem                  "ZZZZZZZZZZZZ.."
FromItemGroup                   tccitg                  ""
ToItemGroup                     tccitg                  "ZZZZZZ"
FromSalesPriceGroup             tccprg                  ""
ToSalesPriceGroup               tccprg                  "ZZZZZZ"
CalculateStandardCosts          tcyesno                 empty
CalculationDate                 tiutcs                  utc.num()
SalesPriceType                  tckosp                  empty
RoundingMethod                  tccrou                  ""
GlobalPrice                     tcyesno                 empty
PricePerOffice                  tcyesno                 empty
FromSalesOffice                 tccwoc                  ""
ToSalesOffice                   tccwoc                  "ZZZZZZ"
ActualizeSalesPrices            tcyesno                 empty
PrintChangedSalesPrices         tcyesno                 empty
SalesPriceBasedOnStandardCost   tcyesno                 empty
ZeroSalesPriceAllowed           tcyesno                 empty
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started successfully.
<> 0                    Errors occurred.
```
