# SerializedItem.GetActiveContracts

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1356-1358

```baan
DLL:   tsextctmapi
This function is available from 2023.04 (KB2286306).
Syntax: long SerializedItem.GetActiveContracts(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref             long             oNumberOfCoverageContracts,
ref     domain  tcorno           oCoverageContracts() fixed,
ref     domain  tsmdm.desc       oCoverageContractDescriptions() fixed mb,
ref     domain  tccom.bpid       oCoverageBusinessPartners() fixed,
ref             long             oNumberOfPricingContracts,
ref     domain  tcorno           oPricingContracts() fixed,
ref     domain  tsmdm.desc       oPricingContractDescriptions() fixed mb,
ref     domain  tccom.bpid       oPricingBusinessPartners() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function will check if the specified Configuration is
covered by any Coverage or Pricing Contract. Details of the
most specific contract are returned.
Searching for a contract is done in the following order:
1. Search for a Contract for the Serialized Item
2. Search for a Contract for the Parent Serialized Items
in the Physical Breakdown Tree if any.
3. Search for a Contract for the Installation
Group of the Serialized Item.
4. Search for a Contract for just the Item code.
5. Search for a Contract for just the Item codes of the
Parent Serialized Items in the Physical Breakdown
Tree if any.
A Serialized Item can be covered by a contract
for the Owner of the Serialized Item, but also by a contract
for the In-use by Business Partner. When this is the case,
both contracts are returned. As a result, the output arrays
are filled with 0, 1, or 2 contracts, indicated by the output
arguments o.nr.of.coverage.contracts and
o.nr.of.pricing.contracts respectively.
When one contract is found, it is for the Owner/Sold-to
Business Partner of the Serialized Item.
When two contracts are found, the first is for the
Owner/Sold-to Business Partner of the Serialized Item,
the second is for the In-use by Business Partner of the
Serialized Item.
Two contracts are possible when the Contract Parameter
Allow Multple Contracts for Serialized Items is Yes.
The Contract Descriptions, and the related Business Partners,
are also returned.
Pre     : Serialized Item should be passed as input.
Arrays must be declared as based.
Post    : Free memory
Input   : iItem
Item; Mandatory
iSerialNumber
Serial Number; Mandatory
Output  : oNumberOfCoverageContracts
Number of Coverage Contracts
oCoverageContracts
Coverage Contracts
oCoverageContractDescriptions
Coverage Contract Descriptions
oCoverageBusinessPartners
Sold to/In Use by Business Partner for Coverage
Contracts
oNumberOfPricingContracts
Number of Pricing Contracts
oPricingContracts
Pricing Contracts
oPricingContractDescriptions
Pricing Contract Descriptions
oPricingBusinessPartners
Sold to/In Use by Business Partner for Pricing Contracts
oExceptionMessage
The last message if the return value is not equal to 0.
If more than one  message is given, these are present
in the oExceptionID.
oExceptionID
An ID that refers to all error information. Use the
functions in Exception to get all relevant information.
Return  : 0             - Search routine successful
<> 0          - An error occurred
```
