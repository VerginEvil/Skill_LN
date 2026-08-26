# SalesOrderLine.LinkContract

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 350-352

```baan
DLL:   tdextslsapi
This function is available from     2025.06 (KB3566686  ).
Syntax: long SalesOrderLine.LinkContract(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcyesno          iSimulate,
long             iProcessingOptionSet,
ref     domain  tccono           oContract,
ref     domain  tcpono           oContractLine,
ref     domain  tccwoc           oContractSalesOffice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function tries to find an active contract that matches
the order line data of the given sales order line.
If so, the contract is linked to the sales order line.
If there are multiple valid (special) contracts, the first contract
found is always taken.
When the "Change Request" concept is applied, a change request can be
initiated for the supplied SalesOrder or an already open change request
is used for contract linking. Contract linking can also be done by
providing the change request as input argument for the "SalesOrder" field.
If a change request is initiated by the Public Interface and no contract
is found or the found contract is the same as on the sales order line,
the initiated change request is canceled, because nothing is changed.
Linking of contract to sales order line depends on the setup.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales order (mandatory)
iSalesOrderLine                               - Sales order line (mandatory)
iSalesOrderLineSequence                       - Sales order line sequence
iSimulate                                     - Indicates if contract linking should be
simulated or really done if possible.
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Any options which are not available as Processing Option will get defaulted.
Processing Options which are set while a required Implemented Software Component
is not available are ignored.
Supported Processing Options and their defaults:
NAME                                            TYPE            DEFAULT
StillUseContractIfMaximumQuantityExceeds        domain tcyesno  tcyesno.yes
Yes: If the quantity exceeds the maximum
for a contract, the given input
value, depending on the parameters
of the sales contract, will cause
the found contract to be accepted.
No:  If the quantity exceeds the maximum
for a contract, the given input
value, depending on the parameters
of the sales contract, will cause
the found contract to be skipped.
StillUseContractIfExpiryDateExceeds             domain tcyesno  tcyesno.yes
Yes: If the expiry date exceeds for a
contract, the given input value,
depending on the parameters of the
sales contract, will cause the found
contract to be accepted.
No:  If the expiry date exceeds for a
contract, the given input value,
depending on the parameters of the
sales contract, will cause the found
contract to be skipped.
ApproveAndProcessChangeRequestAutomatically     domain tcyesno  tcyesno.yes
Yes: If Change Requests are applicable
the created change request will be
approved and processed automatically.
No:  Approval and processing of the
change request (if any) is not done
automatically.
Output: oContract                             - Linked contract, if applicable
oContractLine                                 - Linked contract line, if applicable
oContractSalesOffice                          - Linked contract office, if applicable
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No error
<> 0                                          - Error occurred
```
