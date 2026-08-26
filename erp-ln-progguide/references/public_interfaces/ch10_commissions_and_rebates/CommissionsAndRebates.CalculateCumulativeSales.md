# CommissionsAndRebates.CalculateCumulativeSales

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionsAndRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 372-374

```baan
DLL:   tdextcmsapi
This function is available from     2020.10 (KB2134632  ).
Syntax: long CommissionsAndRebates.CalculateCumulativeSales(
domain  tdcms.type       iCommissionRebateType,
domain  tdcms.prty       iAgreementSearchPriority,
domain  tccom.bpid       iAgreementSoldToBusinessPartner,
domain  tccom.bpid       iAgreementRelation,
domain  tdcms.agrp       iAgreementGroup,
domain  tccprj           iAgreementProject,
domain  tcitem           iAgreementItem,
domain  tdcms.cmgp       iAgreementCommissionRebateGroup,
domain  tcdate           iAgreementEffectiveDate,
domain  tcccp.cpdt       iAgreementPeriodTable,
domain  tcyrno           iAgreementYear,
domain  tcpern           iAgreementPeriod,
domain  tcorno           iSalesOrderFrom,
domain  tcorno           iSalesOrderTo,
domain  tcpono           iSalesOrderLineFrom,
domain  tcpono           iSalesOrderLineTo,
domain  tccwoc           iSalesOfficeFrom,
domain  tccwoc           iSalesOfficeTo,
domain  tcyesno          iFullUpdate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function calculates commissions and rebates based on
cumulative sales for all those agreements which have cumulative
set to 'Yes'. When the commission and rebate has been calculated
for a cumulative sales order line, the field 'Cumulative
Processed (Y/N)' is set to 'Yes'.
Pre:    Retry point must be set
Post:   Transaction must be committed or aborted.
Input:  iCommissionRebateType                 - Type Commission or Rebate
iAgreementSearchPriority
-                                               Agreement search priority
as defined in Commissions and Rebates
parameters
iAgreementSoldToBusinessPartner
-                                               Agreement Sold-to Business Partner
iAgreementRelation                            - Agreement Relation
iAgreementGroup                               - Agreement Group
iAgreementProject                             - Agreement Project
iAgreementItem                                - Agreement Item
iAgreementCommissionRebateGroup
-                                               Agreement Commission/Rebate Group
iAgreementEffectiveDate
-                                               Agreement Effective Date
iAgreementPeriodTable
-                                               Commission Period Table
iAgreementYear                                - Agreement Year
iAgreementPeriod                              - Agreement Period
iSalesOrderFrom                               - Sales Order range From
iSalesOrderTo                                 - Sales Order range To
iSalesOrderLineFrom                           - Sales Order Line range From
iSalesOrderLineTo                             - Sales Order Line range To
iSalesOfficeFrom                              - Sales Office range From
iSalesOfficeTo                                - Sales Office range To
iFullUpdate                                   - Yes/No. Indicate if previous
calculated Cumulative Commissions and
Rebates need to be removed and
calculated again
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Calculation of commission/rebate amount
was successfull
<> 0                    An error occurred
```
