# ProjectInvoicing.TransferTransactionsToInvoicing

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectInvoicing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1753-1754

```baan
DLL:   tpextpinapi
This function is available from 2024.10 (KB3532922).
Syntax: long ProjectInvoicing.TransferTransactionsToInvoicing(
domain  tcyesno          iAdvancePayments,
domain  tcyesno          iUnitRates,
domain  tcyesno          iExtensions,
domain  tcyesno          iInstallments,
domain  tcyesno          iProgressPayments,
domain  tcyesno          iHoldback,
domain  tcyesno          iCostplus,
domain  tcyesno          iFeesAndPenalties,
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
domain  tccprj           iProject,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to Transfer Transactions To
Invoicing. This function offers similar functionality as session
Transfer Transactions To Invoicing (tppin4200m000).
Be aware that transaction management is handled within this function.
Note : This function should be called for one contract and contract line
or one project at a time.
Pre:    N.A
Post:   N.A
Input:  iAdvancePayments        - Advance Payments (Yes/No). Mandatory
iUnitRates              - Unit Rates (Yes/No). Mandatory
iExtensions             - Extensions (Yes/No). Mandatory
iInstallments           - Installments (Yes/No). Mandatory
iProgressPayments       - Progress Payments (Yes/No). Mandatory
iHoldback               - Holdback (Yes/No). Mandatory
iCostplus               - Cost-plus (Yes/No). Mandatory
iFeesAndPenalties       - Fees and Penalties (Yes/No). Mandatory
iContract               - Contract. Optional
iContractLine           - Contract Line. Optional
iProject                - Project. Optional
Note : 1) iContract and iContractLine are mandatory for
Advance Payments , Holdback, Progress Payments and
Fees And Penalties.
2) (iContract and iContractLine) or iProject is mandatory
for Cost-Plus and Installments.
3) iProject is mandatory for Extensions and Unit Rates.
iProcessingOptionSet    -
Optional, if 0, the default options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form
fields on session Transfer Transactions To Invoicing (tppin4200m000)
are not explained in further detail here.
Please refer to the session help for additional information.
Transfer Transactions To Invoicing options which are not
available as Processing Options will get defaulted
in accordance with the session logic
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
|* Selection Range
FromRegistrationDate            domain  tpdate          <Minimum Value>
ToRegistrationDate              domain  tpdate          <Maximum Value>
FromBillingCycle                domain  tpctm.blcl      <Minimum Value>
ToBillingCycle                  domain  tpctm.blcl      <Maximum Value>
FromContractType                domain  tpctm.ctyp      tpctm.ctyp.fixed.price
ToContractType                  domain  tpctm.ctyp      tpctm.ctyp.time.materials
FromSoldToBusinessPartner       domain  tccom.bpid      <Minimum Value>
ToSoldToBusinessPartner         domain  tccom.bpid      <Maximum Value>
FromExtension                   domain  tpptc.cstl      <Minimum Value>
ToExtension                     domain  tpptc.cstl      <Maximum Value>
FromTransactionTime             domain  tppdm.date      <Minimum Value>
ToTransactionTime               domain  tppdm.date      <Maximum Value>
|* Transfer Values
InvoiceStatus                   domain  tcsli.stat      tcsli.stat.confirmed
CutOffDate                      domain  tcdate          Current Date and Time
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
In case of successful transfers,
this message provides information
about the processed transactions.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Successful
<> 0                    - An error occurred
```
