# ConfigurableItem.ReadCPQSettings

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 816-817

```baan
DLL:   tiextpcfapi
This function is available from     2024.09 (KB3516936  ).
Syntax: long ConfigurableItem.ReadCPQSettings(
domain  tcitem           iConfigurableItem,
ref     domain  tcmcs.str256m    oApplicationURL mb,
ref     domain  tcmcs.str50m     oInstance mb,
ref     domain  tcmcs.str50m     oApplicationID mb,
ref     domain  tcmcs.str50m     oCPQCompany mb,
ref     domain  tcmcs.str10m     oNameSpace mb,
ref     domain  tcccur           oBaseCurrency,
ref     domain  tipcf.depl       oDeployment,
ref     domain  tcmcs.str256m    oAPIKey mb,
ref     domain  tcmcs.str256m    oExternalApplicationURL mb,
ref     domain  tcmcs.str50m     oExternalInstance mb,
ref     domain  tcmcs.str50m     oExternalApplication mb,
ref     domain  tcyesno          oAllowPartialSave,
ref     domain  tcmcs.str50m     oProfile mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to retrieve the CPQ
Configurator Settings for a specific Configurable Item being
processed.
Pre:    N.A.
Post:   N.A.
Input:  iConfigurableItem                     - Configurable Item. Mandatory.
Output: oApplicationURL                       - Application URL to CPQ System.
oInstance                                     - Instance of CPQ System.
oApplicationID                                - Application ID of CPQ System.
oCPQCompany                                   - CPQ Company.
oNameSpace                                    - Name Space.
oBaseCurrency                                 - Base Currency.
oDeployment                                   - Deployment could be LN, On Premise or
Cloud.
oAPIKey                                       - API Key.
oExternalApplicationURL                       - External Application URL, which
identifies origin of configuration.
oExternalInstance                             - External Instance, which identifies
origin of configuration.
oExternalApplication                          - External Application, which identifies
origin of configuration.
oAllowPartialSave                             - Allow Partial Save.
oProfile                                      - User Profile.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Read CPQ Settings successfully.
<> 0                                          - An error occurred.
```

## Public Interfaces for ConfigurableStructures

The following functions are available: ConfigurableStructures.StartDetail ConfigurableStructures.StartOverview
