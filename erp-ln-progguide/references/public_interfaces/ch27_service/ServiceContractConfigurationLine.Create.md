# ServiceContractConfigurationLine.Create

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContractConfigurationLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1408-1410

```baan
DLL:   tsextctmapi
This function is available from 2025.06 (KB3566270).
Syntax: long ServiceContractConfigurationLine.Create(
domain  tcorno           iServiceContract fixed,
domain  tsctm.cchn       iContractChange,
long             iProcessingOptionSet,
ref     domain  tsctm.cchn       oContractChange,
ref     domain  tsmdm.seqn       oConfigurationLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function creates a Service Contract Configuration Line.
It offers the same functionality as session Contract
Configuration Lines (tsctm1110m300).
Normal defaulting will be applied  for attributes if not
specified as input arguments.
The Help of this session can be used as reference.
Pre:    A db.retry.point() must have been specified.
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   An abort.transaction() or commit.transaction() must be
executed.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iServiceContract
The service contract for which a new configuration line
is to be created.
Mandatory.
iContractChange
The contract change number for which a new configuration
line is to be created. When not set the configuration
line will be added to the first Free contract change of
the given service contract.
Optional.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE
================================================================
RunIdentification
domain  tsctm.cgru
InstallationGroup
domain  tsbsc.clst
Item
domain  tcitem
SerialNumber
domain  tcibd.sern
NumberOfItems
domain  tsctm.nitm
TypeOfConfigurationLine
domain  tsctm.cltp
ReferenceActivity
domain  tsacm.cact
NumberOfActivities
domain  tsctm.nrac
CoverageType
domain  tsmdm.cctp
Duration
domain  tsmdm.tmdu
ContractTemplate
domain  tsctm.ccte
PricingMethod
domain  tsctm.prmt
PercentageOfSalesValue
domain  tsmdm.perc
InstallmentTemplate
domain  tsctm.ctin
EffectiveDate
domain  tsmdm.date
ContractDiscountDate
domain  tsmdm.date
ExpiryDate
domain  tsmdm.date
SalesPrice
domain  tcpric
NumberOfPeriods
domain  tsmdm.numb
PeriodUnit
domain  tsmdm.peru
SalesAmount
domain  tcamnt
SurchargePercentage
domain  tcdisc
SurchargeAmount
domain  tcamnt
ContractDiscountScheme
domain  tsctm.ccds
CostAmount
domain  tcamnt
MarkedForExpiry         |* Exclude from Renewal
domain  tcyesno
Project
domain  tccprj
Element
domain  tccspa
Activity
domain  tccact
ServiceArea
domain  tsmdm.csar
CoverageTerms
domain  tcyesno
TimeAndMaterialSalesPrices
domain  tcyesno
FixedSalesPrices
domain  tcyesno
ConformanceReporting
domain  tcmcs.cncd
ProblemSolvingMethod
domain  tcmcs.pbsm
Text
domain  tsmdm.text
Output: oContractChange
The contract change number the created contract
configuration line is added.
oConfigurationLine
The created contract configuration line number.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No error; however, error messages can have been set.
<> 0    - An error occurred
```
