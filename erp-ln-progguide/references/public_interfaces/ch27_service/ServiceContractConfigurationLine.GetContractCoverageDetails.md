# ServiceContractConfigurationLine.GetContractCoverageDetails

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContractConfigurationLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1410-1412

```baan
DLL:   tsextctmapi
This function is available from 2025.10 (KB3627884).
Syntax: long ServiceContractConfigurationLine.GetContractCoverageDetails(
domain  tsbsc.clst       iInstallationGroup,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tcdate           iCoverageTime,
long             iProcessingOptionSet,
ref             boolean          oConfigurationCoveredByContract,
ref     domain  tcorno           oContract,
ref     domain  tsctm.term       oTermId,
ref     domain  tsmdm.seqn       oConfigurationLine,
ref     domain  tsmdm.date       oEffectiveDate,
ref     domain  tsmdm.date       oExpiryDate,
ref     domain  tsctm.ccte       oContractTemplate,
ref     domain  tsmdm.dsca       oContractDescription mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function will check if the specified Configuration is
covered by any Service Contract. The details of the most
specific contract that is found are then returned.
Searching for a contract will be done in the following order:
- If a Serial Number is provided:
1. Search for a Contract for the Serialized Item.
2. Search for a Contract for the Parent Serialized Items
in the Physical Breakdown Tree, if any.
3. Search for a Contract for the given Installation Group
or, if not given, the Installation Group of the
Serialized Item and the Item code, if any.
4. Search for a Contract for just the given Installation
Group or if not given, the Installation Group of the
Serialized Item, if any.
5. Search for a Contract for just the Item code.
6. Search for a Contract for just the Item codes of the
Parent Serialized Items in the Physical Breakdown Tree,
if any.
- If no Serial Number is provided, but an Installation Group is:
1. Search for a Contract for the given Installation Group
and the Item code, if any.
2. Search for a Contract for the given Installation Group.
3. Search for a Contract for just the Item code.
- If no Serial Number or Installation Group are provided:
1. Search for a Contract for just the Item code.
Note: In this case, a Business Partner is necessary.
- If not enough information is provided:
1. No search will be done.
Pre:    Installation Group, Item or Serial must be provided.
If only Item is provided, a Business Partner must be provided as
well.
If Serial number is provided then contract coverage must be
enabled for that Serialized Item.
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iInstallationGroup      - Installation group to check coverage
for.
iItem                   - Item to check coverage for.
iSerialNumber           - Configuration to check coverage for.
iSoldToBusinessPartner  - Search for contracts for this business
partner only when the given
configuration only consists of an Item
code, or when the Constracts parameter
"Allow Multiple Contracts" is enabled
for Serialized Items or Installation
Groups in Service Parameters.
Note:   iInstallationGroup, iItem, or iSerialNumber is Mandatory.
If only an item is provided, then iSoldToBusinessPartner
is Mandatory as well.
iCoverageTime           - The date at which the Contract (change)
must be (or have been) active.
Mandatory.
iProcessingOptionSet
- Processing Option Set: a processing
option set number referring to a
processing option set containing at
least one valid option. Mandatory.
NAME                    TYPE
================================================================
CheckPricing            Boolean; default is false.
If true, then the Pricing Terms field
on the contract configuration line
(tsctm110.ptrm) must be YES.
If false, then the Coverage Terms
field on the contract configuration
line (tsctm110.ctrm) must be YES.
Output: oConfigurationCoveredbyContract
True if a contract has been found for this configuration.
False if not. Then all other output variables will be
empty.
oContract
Contract Number
oTermId
Term ID of the found Contract Change
oConfigurationLine
The found contract configuration line number
oEffectiveDate
Effective Date of the Configuration Line
oExpiryDate
Expiry Date of the Configuration Line
oContractTemplate
Contract Template of the Configuration Line
oContractDescription
Description of the found Contract
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
