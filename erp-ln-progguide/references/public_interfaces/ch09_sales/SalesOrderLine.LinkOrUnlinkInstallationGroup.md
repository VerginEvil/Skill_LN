# SalesOrderLine.LinkOrUnlinkInstallationGroup

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 354-355

```baan
DLL:   tdextslsapi
This function is available from 2025.12 (KB3622010).
Syntax: long SalesOrderLine.LinkOrUnlinkInstallationGroup(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcyesno          iLinkInstallationGroup,
domain  tcclst           iInstallationGroupToBeLinked,
ref     domain  tcclst           oUnlinkedInstallationGroup,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function links or unlinks an installation group to a sales order
line and does the same as linking or unlinking an installation group
to a sales order line in the session "Sales Order Lines" (tdsls4101m000).
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                     - Sales order (mandatory)
iSalesOrderLine                 - Sales order line (mandatory)
iSalesOrderLineSequence         - Sales order line sequence
(should always be '0')
iLinkInstallationGroup          -
Yes: If installation group should be linked to sales order line.
No: If installation group should be unlinked from sales order
line.
iInstallationGroupToBeLinked    -
Installation group to be linked
* if input argument "iLinkInstallationGroup" is 'Yes' then
- if installation group to be linked is filled this one
is used;
- if installation group to be linked is empty an
installation
group from Service is determined if possible.
* if input argument "iLinkInstallationGroup" is 'No' then
installation group to be linked should be empty
(not applicable).
Output: oUnlinkedInstallationGroup      - The unlinked installation group (if
input argument "iLinkInstallationGroup"
is 'No' and successfully unlinked)
oExceptionMessage               - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID                    - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information
Return: 0                               - No error
<> 0                            - Error occurred
```
