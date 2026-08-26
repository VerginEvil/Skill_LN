# SupplierClaim.SetRMAReceived

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SupplierClaim
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1534-1535

```baan
DLL:   tsextcmmapi
This function is available from     2023.06 (KB2294949  ).
Syntax: long SupplierClaim.SetRMAReceived(
domain  tcorno           iSupplierClaim,
domain  tcpono           iClaimLine,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcyesno          iReturnMaterialRequired,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to set the field "Receive RMA" of the Supplier
Claim Delivery Line related to the given Supplier Claim Line to
Received.
If Return Material is required and a Warehouse order does not
yet exist, this function creates a Warehouse order for the
Supplier Claim Delivery Line.
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be
executed.
Input:  iSupplierClaim
Supplier Claim: Mandatory
iClaimLine
Supplier Claim Line: Mandatory
iItem
Item: Mandatory if return material is required
iSerialNumber
Serial Number: Mandatory if Item is serialized
iReturnMaterialRequired
Whether or not return material is required: Mandatory
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No error
<> 0                          - An error occurred
```

## Public Interfaces for SupplierClaimLine

The following functions are available: SupplierClaimLine.Approve SupplierClaimLine.Reject SupplierClaimLine.Settle
