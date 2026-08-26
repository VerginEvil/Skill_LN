# ServiceContractChange.Create

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContractChange
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1394-1396

```baan
DLL:   tsextctmapi
This function is available from     2025.11 (KB3565748  ).
Syntax: long ServiceContractChange.Create(
domain  tcorno           iServiceContract,
long             iProcessingOptionSet,
ref     domain  tsctm.cchn       oContractChange,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function creates a Service Contract Change.
It offers the same functionality as session Service Contract
(tsctm3120m000).
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
Service Contract.
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
ContractChangeType
domain  tsctm.chng      tsctm.chng.renewed
The type of change to be created for the service
contract.
Description
domain  tsmdm.dsca      ""
The description of the contract change.
When not specified then contract header description is
set on the new contract change.
OriginContractChange
domain  tsctm.cchn      0
The contract change number on which the change of type
Incidental Change is applied.
ChangeDate
domain  tsmdm.date      0
The change date on which the change of type
Incidental Change or Indexation is effective.
When not specified for a change of type Incidental
Change the current date will be defaulted and for a
change of type Indexation, the indexation start date
defined on the service contract header will be applied
to the new contract change.
Penalty
domain  tcamnt          0.0
The to be applied penalty for a contract change of type
Incidental Change.
When not specified the penalty defined on the service
contract header will be applied to the new contract
change.
IndexationTemplate
domain  tsctm.cind      ""
The to be applied indexation template for a contract
change of type Indexation or Renewal with Indexation.
When not specified the indexation template defined on
the service contract header will be applied to the new
contract change.
Output: oContractChange
The contract change number of the created contract
change.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No error; however, error messages can have been set.
<> 0                          - An error occurred
```

## Public Interfaces for

## ServiceContractConfigurationLine

The following functions are available: ServiceContractConfigurationLine.Create ServiceContractConfigurationLine.GetContractCoverageDetails
