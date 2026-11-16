# ProjectActivityBudget.AddCPQConfiguration

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectActivityBudget
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1715-1716

```baan
DLL:   tpextptcapi
This function is available from 2022.10 (KB2240749).
Syntax: long ProjectActivityBudget.AddCPQConfiguration(
domain  tccprj           iProject,
domain  tppss.cpla       iPlan,
domain  tppdm.cact       iActivity,
domain  tppdm.serd       iSequenceNumber,
domain  tcitem           iConfigurableItem,
domain  tcmcs.str60      iConfigurationID,
domain  tcmcs.str60      iConfigurationDetailID,
ref     domain  tccpva           oProductVariant,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a Product Variant in LN based on the
supplied CPQ Configuration for the given Activity Budget Line
(Material). The created Product Variant will be updated on
the Activity Budget Line.
Checks:
Before allowing the Activity Budget Line to be updated with a
Product Variant some checks are done. These checks are mostly
similar to the checks done when configuring an item manually
in session 'Activity Budget (Material)' (tpptc2110m000) using
the form command "Configure".
The checks include:
- The Infor Configurator (CPQ) must be implemented
- The supplied item in input argument iConfigurableItem must
be equal to the item on the Activity Budget Line
- The item on the Activity Budget Line must not be configured
yet, meaning that the value of the Product Variant must be
empty (zero)
- The item must:
- have Item Type Generic
- have CPQ assigned as Configurator
- Authorization and Security settings for the Activity Budget
Line must allow USE of:
- Project
- Item
Restrictions:
This function must only be called from a BOD context.
Pre:    Retry point must be set.
The Activity Budget Line to be updated must already exist.
Post:   Commit or abort transaction.
Input:  iProject                - Project: Mandatory
iPlan                   - Plan: Optional
If the Plan is not specified, the
default or actual Plan of the Project
will be used.
iActivity               - Activity: Mandatory
iSequenceNumber         - Sequence Number: Mandatory
The Line number of the Budget Line.
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
