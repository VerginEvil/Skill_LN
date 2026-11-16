# ProjectInvoicing.StartTransferTransactionsToInvoicing

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectInvoicing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1751-1752

```baan
DLL:   tpextpinapi
This function is available from 2024.08 (KB2332111).
Syntax: long ProjectInvoicing.StartTransferTransactionsToInvoicing(
domain  tccono           iFromContract,
domain  tccono           iToContract,
domain  tpctm.cnln       iFromContractLine,
domain  tpctm.cnln       iToContractLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to start the session
Transfer Transactions To Invoicing (tppin4200m000).
Pre:    N.A
Post:   N.A
Input:  iFromContract                   - From Contract. Optional
iToContract                     - To Contract. Optional
iFromContractLine               - From Contract Line. Optional
iToContractLine                 - To Contract Line. Optional
iProcessingOptionSet -
Optional, if 0, the default options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form
fields on session Transfer Transactions To Invoicing (tppin4200m000)
are not explained in further detail here.
Please refer to the session help for additional information.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
|* Type of Invoices to be Transferred
AdvancePayments                 domain  tcyesno         tcyesno.yes
UnitRates                       domain  tcyesno         tcyesno.yes
Extensions                      domain  tcyesno         tcyesno.yes
Installments                    domain  tcyesno         tcyesno.yes
ProgressPayments                domain  tcyesno         tcyesno.yes
Holdback                        domain  tcyesno         tcyesno.yes
CostPlus                        domain  tcyesno         tcyesno.yes
FeesAndPenalties                domain  tcyesno         tcyesno.yes
|* Selection Range
FromRegistrationDate            domain  tpdate          <Minimum Value>
ToRegistrationDate              domain  tpdate          <Maximum Value>
FromBillingCycle                domain  tpctm.blcl      <Minimum Value>
ToBillingCycle                  domain  tpctm.blcl      <Maximum Value>
FromContractType                domain  tpctm.ctyp      tpctm.ctyp.fixed.price
ToContractType                  domain  tpctm.ctyp      tpctm.ctyp.time.materials
FromProject                     domain  tccprj          <Minimum Value>
ToProject                       domain  tccprj          <Maximum Value>
FromSoldToBusinessPartner       domain  tccom.bpid      <Minimum Value>
ToSoldToBusinessPartner         domain  tccom.bpid      <Maximum Value>
FromExtension                   domain  tpptc.cstl      <Minimum Value>
ToExtension                     domain  tpptc.cstl      <Maximum Value>
FromTransactionTime             domain  tppdm.date      <Minimum Value>
ToTransactionTime               domain  tppdm.date      <Maximum Value>
|* Print Options
PrintProcessReport              domain  tcyesno         tcyesno.no
PrintErrorReport                domain  tcyesno         tcyesno.yes
|* Transfer Values
InvoiceStatus                   domain  tcsli.stat      tcsli.stat.confirmed
CutOffDate                      domain  tcdate          Current Date and Time
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Successful
<> 0                    - An error occurred
```
