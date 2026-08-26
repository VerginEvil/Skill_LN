# ServiceOrder.ReadShippingAddressForCostLine

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1426-1427

```baan
DLL:   tsextsocapi
This function is available from     2022.10 (KB2262990  ).
Syntax: long ServiceOrder.ReadShippingAddressForCostLine(
domain  tcorno           iServiceOrder,
domain  tcpono           iCostLine,
domain  tsmdm.cotp       iCostType,
ref     domain  tccom.cadr       oShippingAddress,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function reads the shipping address of the given service
order cost line.
For cost type material the ship                      -to address of the material cost
line is returned.
For other cost types or if the material cost line ship                      -to
address is empty, first the related Ship Material To
attribute is read.
Based on the Ship Material To the shipping address is
retrieved from one of the following addresses:
-                       Ship-to BP Address
Address taken from order header or activity.
-                       Location Address
Address taken from order header or activity.
-                       In-use by BP Address
Address taken from the installation of order header
or activity.
-                       Dealer Address
Address taken from the installation of order header
or activity.
-                       Subcontractor Address
Address taken from the Buy                              -from BP (Subcontractor).
Whether a line is linked to an activity or directly to the
service order header determines whether attributes from the
header or activity are used. This applies for the Ship Material
To and other attributes used to determine the shipping address.
The installation is the serialized item or (if empty) the
installation group.
Pre:    N.A.
Post:   N.A.
Input:  iServiceOrder           The service order: Mandatory
iCostLine               The cost line: Mandatory
iCostType               The Cost Type: Mandatory
The cost line should exist.
Output: oShippingAddress        The shipping address.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
