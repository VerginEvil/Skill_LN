# ProjectContractDeliverable.AddCPQConfiguration

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContractDeliverable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1706-1707

```baan
DLL:   tpextpdmapi
This function is available from 2022.10 (KB2240749).
Syntax: long ProjectContractDeliverable.AddCPQConfiguration(
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
domain  tcpono           iDeliverable,
domain  tcitem           iConfigurableItem,
domain  tcmcs.str60      iConfigurationID,
domain  tcmcs.str60      iConfigurationDetailID,
ref     domain  tccpva           oProductVariant,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a Product Variant in LN based on the
supplied CPQ Configuration for the given Contract Deliverable.
The created Product Variant will be updated on the Contract
Deliverable.
Checks:
Before allowing the Contract Deliverable to be updated with a
Product Variant some checks are done. These checks are mostly
similar to the checks done when configuring an item manually
in session 'Contract Deliverables' (tppdm7100m100) using the
form command "Configure Product Variant".
The checks include:
- The Infor Configurator (CPQ) must be implemented
- The Contract Deliverable may not be checked-out for OCM /
Workflow
- The supplied item in input argument iConfigurableItem must
be equal to the item on the Contract Deliverable
- The item on the Contract Deliverable must not be configured
yet, meaning that the value of the Product Variant must be
empty (zero)
- The item must:
- have Item Type Generic
- have property "With PCS" set to No
- not be an Assembly item
- have CPQ assigned as Configurator
- Authorization and Security settings for the Contract Deliverable
must allow the USE of:
- Contract
- Project
- Item
- The Contract Deliverable must:
- have status Free
- not have a Schedule
- not be a Backorder
- not be a Return Deliverable
Restrictions:
This function must only be called from a BOD context.
Pre:    Retry point must be set.
The Contract Deliverable to be updated must already exist.
Post:   Commit or abort transaction.
Input:  iContract               - Contract: Mandatory
iContractLine           - Contract Line: Mandatory
iDeliverable            - Deliverable: Mandatory
iConfigurableItem       - Configurable Item: Mandatory
The Item code to be configured.
iConfigurationID        - Configuration ID: Mandatory
The Configuration ID with which the
configuration is stored in CRM/EQ
(Enterprise Quoting).
iConfigurationDetailID  - Configuration Detail ID: Mandatory
The Configuration Detail ID with which
the configuration is stored in CRM/EQ.
Output:
oProductVariant         - Product Variant
The new created Product Variant.
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
