# WorkOrder.GenerateSerializedItem

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1492-1493

```baan
DLL:   tsextwcsapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long WorkOrder.GenerateSerializedItem(
domain  tcorno           iWorkOrder,
domain  tcpono           iLine,
domain  tsmdm.mtyp       iMaterialType,
domain  tcibd.sern       iSerialNumber,
domain  tcyesno          iUpdateSerialOnWorkOrder,
ref     domain  tcibd.sern       oGeneratedSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates a serialized item based on the data of
the given:
Work Order
Work Order Batch Repair Serial
Work Order Outgoing Subassembly
Work Order Material Resource Line
When the work order is linked to a maintenance sales order part
maintenance line, the sold                      -to business partner of the
maintenance sales order will be set as owner of the serialized
item.
Optionally the generated serial number can be updated on the
given work order objects.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Input:  iWorkOrder
The order number based on which a new serialized item
must be generated.
(mandatory)
iLine
The line number of the batch repair serial, outgoing
subassembly or material resource line based on which a
new serialized item must be generated.
(optional)
iMaterialType
Indicates the work order object for which a serialized
item must be generated.
Allowed values:
-                               Material Resource
-                               Batch Repair
-                               Outgoing Subassembly
-                               Not Applicable
(mandatory)
iSerialNumber
The Serial Number to be used for generating a
serialized item.
When not set, a new serial number will be generated
based on a predefined mask.
(optional)
iUpdateSerialOnWorkOrder
Controls if the serial number must be set on the
work order objects based on which the serialized item is
generated.
-                               yes: The serial number on the order/line is updated
with the generated serial number.
-                               no: Only a serialized item is generated.
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
Return: 0                     - Serialized Item generated succesfull and (optionally)
updated on the work order objects.
<> 0                          - Error during generating serialized item occurred
When oGeneratedSerialNumber is filled, the serialized
item is generated successfully but the update of the
serial number on the work order objects failed.
```
