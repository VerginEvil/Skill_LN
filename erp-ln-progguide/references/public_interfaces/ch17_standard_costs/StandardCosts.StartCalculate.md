# StandardCosts.StartCalculate

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 616-617

```baan
DLL:   tiextcprapi
This function is available from 2024.06 (KB2329983).
Syntax: long StandardCosts.StartCalculate(
long             iStartMode,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the process session Calculate
Standard Cost (ticpr2210m000). This function makes use of a
Processing Option Set, which can be created via a call to
ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete().
Pre:    N.A.
Post:   N.A.
Input:  i.start.mode -  Specifies the start mode for the session
(Mandatory). Possible values are:
MODAL - The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS - Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dialog.
i.item -        Item for which the standard cost should be
calculated (Optional).
i.enterprise.unit -
Enterprise Unit for which the standard cost
should be calculated (Optional).
iProcessingOptionSet -
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
If 0, then user default/session default values
are applied (Optional).
Processing Options have a direct relationship with the form fields
on session Calculate Standard Cost (ticpr2210m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
Calculate Standard Cost options which are not available as Processing
Options will get defaulted in accordance with the session logic.
NAME                            TYPE                    DEFAULT
CostCalculationCode             domain  tccpcc          ""
CalculationMethod               domain  tcccmt          empty
CalculationDate                 domain  tiutcs          0
EnterpriseUnitFrom              domain  tcemm.grid      iEnterpriseUnit
EnterpriseUnitTo                domain  tcemm.grid      ""
ItemGroupFrom                   domain  tccitg          ""
ItemGroupTo                     domain  tccitg          ""
ItemFrom                        domain  tcitem          iItem
ItemTo                          domain  tcitem          ""
OnlyItemsWithoutStandardCost    domain  tcyesno         empty
IncludeStandardSubassemblies    domain  tcyesno         empty
ExcludeConfiguredStandardItems  domain  tcyesno         empty
BatchSize                       domain  tcpono          0
ActualizeStandardCostAndRevaluateInventory
domain  tcyesno         empty
UseEffectiveDate                domain  tcrvdt          empty
SpecificDate                    domain  tcdate          0
DeleteStandardCostHistoryData   domain  tcyesno         empty
PrintHoursValues                domain  tcyesno         empty
InventoryValueBasedOnLCMV       domain  tcyesno         empty
ReverseToOriginalInventoryValue domain  tcyesno         empty
ValuePurchaseReceiptAfterLMVDate
domain  tcprus          empty
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started successfully.
<> 0                    - Otherwise.
```
