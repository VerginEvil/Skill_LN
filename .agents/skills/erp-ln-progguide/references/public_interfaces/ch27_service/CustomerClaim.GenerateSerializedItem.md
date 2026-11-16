# CustomerClaim.GenerateSerializedItem

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaim
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1537-1538

```baan
DLL:   tsextcmmapi
This function is available from 2023.04 (KB2286306).
Syntax: long CustomerClaim.GenerateSerializedItem(
domain  tcorno           iCustomerClaim,
domain  tcpono           iClaimLine,
domain  tcpono           iDeliveryLine,
domain  tcibd.sern       iSerialNumber,
domain  tcyesno          iUpdateSerialOnCustomerClaim,
ref     domain  tcibd.sern       oGeneratedSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates a serialized item based on the data of
the given Customer Claim (Delivery) Line.
A new serial will be generated for the item defined on the
Customer Claim Line or, when iDeliveryLine is filled, on the
Customer Claim Delivery Line.
The sold-to business partner defined on the Customer Claim will
be set as owner of the serialized item.
Optionally the Customer Claim (Delivery) Line can be updated
with the generated serial number.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Input:  iCustomerClaim
The customer claim based on which a new serialized item
must be generated.
(mandatory)
iClaimLine
The customer claim line based on which a new serialized
item must be generated.
(mandatory)
iDeliveryLine
The customer claim delivery line based on which a new
serialized item must be generated.
(optional)
iSerialNumber
The Serial Number to be used for generating a
serialized item.
When not set, a new serial number will be generated
based on a predefined mask.
(optional)
iUpdateSerialOnCustomerClaim
Controls if the serial number must be set on the
Customer Claim (Delivery) Line based on which the
serialized item is generated.
- yes: The serial number on the Customer Claim
(Delivery) Line is updated with the generated
serial number.
- no: Only a serialized item is generated.
(mandatory)
Output: oGeneratedSerialNumber
The serial number of the generated serialized item.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - Serialized Item generated succesfull and (optionally)
updated on the Customer Claim (Delivery) Line.
<> 0    - Error during generating serialized item occurred
When oGeneratedSerialNumber is filled, the serialized
item is generated successfully but the update of the
serial number on the Customer Claim (Delivery) Line
failed.
```
