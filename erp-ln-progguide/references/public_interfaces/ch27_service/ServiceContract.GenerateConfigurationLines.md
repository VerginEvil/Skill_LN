# ServiceContract.GenerateConfigurationLines

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1389-1391

```baan
DLL:   tsextctmapi
This function is available from     2023.10 (KB2289318  ).
Syntax: long ServiceContract.GenerateConfigurationLines(
domain  tsctm.termappl   iGenerateFor,
domain  tcorno           iServiceContractOrContractQuote,
domain  tsctm.cchn       iServiceContractChange,
domain  tsbsc.clst       iInstallationGroup,
domain  tcitem           iFromItem,
domain  tcitem           iToItem,
domain  tcibd.sern       iFromSerialNumber,
domain  tcibd.sern       iToSerialNumber,
domain  tsctm.cgru       iRunIdentification,
domain  tsctm.ctin       iInstallmentTemplate,
domain  tsctm.ccte       iContractTemplate,
domain  tcyesno          iApplyItemPriceListForContractTemplate,
domain  tcyesno          iPickBestFitTemplateFromItemPriceList,
domain  tcyesno          iGenerateBaseInstallation,
domain  tcyesno          iGenerateOnlyForInstallations,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates Configuration Lines for the passed
Service Contract Change, or Contract Quote.
Use this Public Interface to copy an Installation Group and
Items or Serialized Items to Contract Configuration Lines.
The functionality offered in this Public Interface is the same
as available in session Generate Contract Configuration Lines
(tsctm2210m000). See the session's documentation for more
information.
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be
executed.
Input:  iGenerateFor
Generate Configuration Lines for Service Contract, or
Contract Quote
Mandatory
iServiceContractOrContractQuote
Service Contract, or Contract Quote
Mandatory
iServiceContractChange
Service Contract Change; when 0 is passed, the Change
Number of the original Service Contract is used.
Not mandatory
iInstallationGroup
Installation Group
Mandatory
iFromItem
From Item
Not mandatory
iToItem
To Item; when left empty it is defaulted to
its maximum value.
Not mandatory
iFromSerialNumber
From Serial Number
Not mandatory
iToSerialNumber
To Serial Number; when left empty it is defaulted to
its maximum value.
Not mandatory
iRunIdentification
Run Identification. A user                              -definable identification.
Not mandatory
iInstallmentTemplate
Installment Template: Not mandatory
iContractTemplate
Contract Template: Not mandatory
iApplyItemPriceListForContractTemplate
Apply Item Price List For Contract Template
Mandatory yes/no
iPickBestFitTemplateFromItemPriceList
Pick Best                              -Fit Template from Item-Price List
Mandatory yes/no
iGenerateBaseInstallation
Generate Base                              -Installation
Mandatory yes/no
iGenerateOnlyForInstallations
Generate Only for Installations
Mandatory yes/no
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Generation successful
<> 0                          - Error occurred during Generation.
```
