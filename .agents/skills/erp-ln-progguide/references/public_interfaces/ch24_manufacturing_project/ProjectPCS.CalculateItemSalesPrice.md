# ProjectPCS.CalculateItemSalesPrice

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 886-888

```baan
DLL:   tiextpcsapi
This function is available from 2026.08 (KB3647208).
Syntax: long ProjectPCS.CalculateItemSalesPrice(
domain  tipcs.ccgr       iCalculationGroup,
domain  tcitem           iItem,
domain  tcyesno          iGlobalPrice,
domain  tcyesno          iPricePerOffice,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will Calculate Sales Prices for Project
Items according to the logic of session in Calculate Item Sales
Prices by Project (tipcs2241m000).
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process. Transaction handling
will be done inside Public Interface.
Input:  iCalculationGroup - (Optional).
- If provided, the value must exist in Calculation
Groups. When specified the calculation is performed
using the given Calculation Group. If not provided,
the calculation is done based on remaining input
arguments.
iItem - (Optional).
- If provided, the value must exist in Items. When
specified the calculation is performed for specific
Item. If not provided, the calculation is done based
on remaining input arguments.
iGlobalPrice - (Optional).
- If input variable field "iGlobalPrice" is given, it
will be used as default value. Otherwise, it will be
defaulted with "tcyesno.yes".›¼• "iGlobalPrice" No can be
applicable only if "iPricePerOffice" is yes. If
"iGlobalPrice" is selected,›¼• the Sales Price›¼• for the
selected calculation group or item is calculated on
company level. Note: This field is applicable only if
the multisite functionality is activated.›¼•
iPricePerOffice - (Optional).
- If input variable field "iPricePerOffice" is given,
it will be used as default value. Otherwise, it will
be defaulted with "tcyesno.no". If "iPricePerOffice"
is selected,›¼• the Sales Price›¼• is calculated for a
specific sales office or range of offices.
Note: This field is applicable only if the multisite
functionality is activated.
iProcessingOptionSet
- Processing Option Set (Optional). If 0, then user
default/session default values are applied.
A Processing Option Set can be created via a call to
ProcessingOptionSet.Create() in DLL tcextextapi. After
the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                            TYPE                    DEFAULT
FromItem                        domain tcitem           ""
ToItem                          domain tcitem           Max.of Domain
IncludeBudgetSurcharges         domain tcyesno          tcyesno.no
IncludeItemSalesSurcharges      domain tcyesno          tcyesno.no
CostCalculationCode             domain tccpcc           ""
FromSalesOffice                 domain tccwoc           ""
ToSalesOffice                   domain tccwoc           Max.of Domain
RoundingMethod                  domain tccrou           ""
PrintReport                     domain tcyesno          tcyesno.no
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
Default Values:
IncludeBudgetSurcharges
›¼À“ If input variable field "IncludeBudgetSurcharges" is
given, it will be used as default value. Otherwise, it
will be defaulted with "tcyesno.no". If
"IncludeBudgetSurcharges" is activated, LN adds the
budget surcharges to the Item Sales Price.
IncludeItemSalesSurcharges
- If input variable field "IncludeItemSalesSurcharges"
is given, it will be used as default value. Otherwise,
it will be defaulted with "tcyesno.no".  If
"IncludeItemSalesSurcharges" is activated, user must
enter the Cost Calculation Code. The Cost Calculation
Code is used to retrieve the Item Surcharges.
CostCalculationCode
- If "IncludeItemSalesSurcharges" is activated this
field is mandatory and it should present in
"Cost Calculation Codes".
FromSalesOffice
- If "PricePerOffice" is activated this field is
applicable. If input variable field "FromSalesOffice"
is given, it will be used as default value. Otherwise,
it will be defaulted with BLANK. Note: This field is
applicable only if the multisite functionality is
activated.
ToSalesOffice
- If "PricePerOffice" is activated this field is
applicable. If input variable field "ToSalesOffice" is
given, it will be used as default value
with maximum value of its Domain.
Note: This field is applicable only if the
multisite functionality is activated.
RoundingMethod
- If input variable field "RoundingMethod" is given, it
will be used as default value and it should be present
in "Rounding Codes". Otherwise, it will be defaulted
with BLANK.
PrintReport
›¼À“ If input variable field "PrintReport" is given, it
will be used as default value. Otherwise, it will be
defaulted with "tcyesno.no". If PrintReport is
activated, input variable fields "PrintingDevice" and
"PrintingFileOutPathName" will be used as default
values otherwise these values will be defaulted with
empty string.
Output:
oExceptionMessage - The last message if any message is found. If
more than one message is given, these are
present in the oExceptionID.
oExceptionID      - An ID that refers to the exception
information. Use the functions in Exception
to get all relevant information.
Return:
0       - Success. Item Sales Prices calculated.
<> 0    - Error occurred during sales price calculation.
```
