# ServiceOrder.GenerateSerializedItem

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1426-1428

```baan
DLL:   tsextsocapi
This function is available from 2023.04 (KB2286306).
Syntax: long ServiceOrder.GenerateSerializedItem(
domain  tcorno           iServiceOrder,
domain  tsmdm.acln       iActivityLine,
domain  tcpono           iMaterialLine,
domain  tcibd.sern       iSerialNumber,
domain  tcyesno          iLinkToInstallationGroup,
domain  tcyesno          iUpdateSerialOnServiceOrder,
ref     domain  tcibd.sern       oGeneratedSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates a serialized item based on the data of
the given Service Order, Service Order Activity Line or
Service Order Material Line.
When iActivityLine and iMaterialLine are not filled, a new
serial will be generated for the item defined on the Service
Order header.
When iActivityLine is filled the serial will be generated for
the item on the Service Order Activity Line.
When iMaterialLine is filled the serial will be generated for
the item on the Service Order Material Line.
iActivityLine and iMaterialLine cannot be set both.
The sold-to business partner defined on the Service Order will
be set as owner of the serialized item.
Optionally the generated serialized item can be linked to the
installation group defined on the Service Order and Service
Order Activity Line.
Optionally the Service Order/Activity/Material line can be
updated with the generated serial number.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Input:  iServiceOrder
The order number based on which a new serialized item
must be generated.
(mandatory)
iActivityLine
The Service Order Activity Line number based on which a
new serialized item must be generated.
(optional)
iMaterialLine
The Service Order Material Line number based on which a
new serialized item must be generated.
(optional)
iSerialNumber
The Serial Number to be used for generating a
serialized item.
When not set, a new serial number will be generated
based on a predefined mask.
(optional)
iLinkToInstallationGroup
When an Installation Group is defined on the Service
Order or Service Order Activity Line, the generated
serialized item can be added as installation in this
group.
Note that this is controlled by Configuration Management
(CFG) parameter Link Generated Serialized Item to
Installation Group.
When this parameter is not set or no installation group
is defined, the generated serialized item will not be
linked to the installation group and the value of
iLinkToInstallationGroup will be ignored.
(mandatory)
iUpdateSerialOnServiceOrder
Controls if the serial number must be set on the
Service Order/Activity Line based on which the
serialized item is generated.
- yes: The serial number on the order/line is updated
with the generated serial number.
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
Return: 0       - Serialized Item generated succesfully and (optionally)
updated on the Service Order/Activity/Material Line.
<> 0    - Error during generating serialized item occurred
When oGeneratedSerialNumber is filled, the serialized
item is generated successfully but the update of the
serial number on the Service Order/Activity/Material
Line failed.
```
