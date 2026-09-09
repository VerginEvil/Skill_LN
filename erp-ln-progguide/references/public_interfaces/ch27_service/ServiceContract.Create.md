# ServiceContract.Create

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1399-1401

```baan
DLL:   tsextctmapi
This function is available from 2025.06 (KB3566270).
Syntax: long ServiceContract.Create(
long             iProcessingOptionSet,
ref     domain  tcorno           oServiceContract fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function creates a Service Contract.
It offers the same functionality as session Service Contract
(tsctm3100m000).
Normal defaulting will be applied  for attributes if not
specified as input arguments.
The Help of this session can be used as reference.
Pre:    A db.retry.point() must have been specified.
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   An abort.transaction() or commit.transaction() must be
executed.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE
================================================================
Series
domain  tcorno
Description
domain  tsmdm.dsca      mandatory
ContractType
domain  tsctm.ctpc
ContractEffectiveDate
domain  tsmdm.date
ServiceOffice
domain  tccwoc
InternalSalesRepresentative
domain  tcemno
SalesPriceList
domain  tccplt
SoldToBusinessPartner
domain  tccom.bpid      mandatory
SoldToAddress
domain  tccom.cadr
SoldToContact
domain  tccom.ccnt
FirstInvoiceReference
domain  tcrefa
SecondInvoiceReference
domain  tcrefb
LineOfBusiness
domain  tccbrn
ContractDuration
domain  tsmdm.numb
ContractDurationPeriodUnit
domain  tsmdm.peru
PricingMethod
domain  tsctm.prmt
PercentageOfSalesValue
domain  tsmdm.perc
OvertimeAllowed
domain  tcyesno
ContractRenewal
domain  tcyesno
RenewalPeriod
domain  tsmdm.numb
RenewalPeriodPeriodUnit
domain  tsmdm.peru
BpPricesAndDiscounts
domain  tccom.bpid
SalesArea
domain  tccreg
Indexation
domain  tcyesno
IndexationStartDate
domain  tsmdm.date
IndexationInterval
domain  tsmdm.numb
IndexationIntervalPeriodUnit
domain  tsmdm.peru
IndexationTemplate
domain  tsctm.cind
IncidentalChanges
domain  tcyesno
PenaltyAmount
domain  tcamnt
InstallmentTemplatePerConfiguration
domain  tcyesno
InstallmentTemplate
domain  tsctm.ctin
LatePaymentSurcharge
domain  tcccrs
PaymentTerms
domain  tccpay
Currency
domain  tcccur
TaxCountry
domain  tcccty
TaxClassification
domain  tctax.bpcl
TaxCode
domain  tccvat
BusinessPartnerTaxCountry
domain  tcccty
TaxExempt
domain  tcyesno
TaxExemptionCertificate
domain  tcfovn
TaxExemptionReason
domain  tccdis
InvoiceToBusinessPartner
domain  tccom.bpid
InvoiceToAddress
domain  tccom.cadr
InvoiceToContact
domain  tccom.ccnt
PayByBusinessPartner
domain  tccom.bpid
PayByAddress
domain  tccom.cadr
PayByContact
domain  tccom.ccnt
SalesType
domain  tcpsty
RevenueRecognitionBasedOn
domain  tsctm.rvmd
RecognizeRevenuePerContractRenewal
domain  tcyesno
RecognizeRevenuePerConfiguration
domain  tcyesno
Provision
domain  tsmdm.perc
Project
domain  tccprj
Eelement
domain  tccspa
Activity
domain  tccact
ServiceContractText
domain  tsmdm.text
HeaderText
domain  tsmdm.text
FooterText
domain  tsmdm.text
InstallmentText
domain  tsmdm.text
Output: oServiceContract
The ID of the created service contract.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - No error; however, error messages can have
been set.
<> 0            - An error occurred
```
