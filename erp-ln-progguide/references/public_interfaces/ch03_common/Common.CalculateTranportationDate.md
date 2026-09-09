# Common.CalculateTranportationDate

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 95-97

```baan
DLL:   tcextcomapi
This function is available from 2026.05 (KB3666857).
Syntax: long Common.CalculateTranportationDate(
domain  tccom.cadr       iAddressFrom,
domain  tccom.cadr       iAddressTo,
domain  tcdate           iDate,
domain  tcmcs.str1       iOperator,
domain  tccfrw           iCarrier,
domain  tccom.trmd       iTransportCategory,
domain  tccom.dstt       iPriorityOfDistance,
domain  tcitem           iItem,
domain  tccrte           iRoute,
domain  tcmcs.serv       iServiceLevel,
domain  fmfmd.cmtg       iTransportMeansGroup,
domain  tctmcb           iTransportMeansCombination,
domain  fmmotr           iMeansOfTransport,
domain  tccdec           iTermsOfDelivery,
domain  tcptpa           iPointOfTitlePassage,
ref     domain  tcdate           oCalculatedDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:
If Freight Management is implemented this function will calculate
the transportation time required
to transport the goods from one address to the other address.
While calculating the transportation time it will consider the
Route, Loading time and unloading time,Speed of the TMG,and
route plan if it is multi stop.According to the transportation
time required it will give the loading date when unloading date
is known and unloading date when loading date is knwon.
If service level is given as input, then unload / load date is
calculated and compared with the service level time and if the
service level time is less than the transportation time message
will be returned.
If Freight Management is not implemented this function calculates
a new date from a particular given date, taking into account the
distance (expressed in time, or
the "lead time") between two addresses and taking into account
the calendar of the carrier. Together with the calendar usage
also an availability type should be used accordingly as defined
in the Common Parameters (tccom999.ract).
"Forward" calculation will allow you to determine the (expected)
customer's (required) receipt date based on a delivery date.
This is done as follows:
- take delivery data as time goods are available at origin;
- determine calendar linked to carrier (that is buy-from BP);
- determine distance (expressed in time, not distance) between
origin and destination by taking into account the transport
mode;
- take delivery data as starting point in calendar, add time by
fitting this in the calendar when available (forward), and
determine the receipt date.
"Backward" calculation will allow you to determine the
"shipment date" (the date on which delivery should commence)
based on a customer's (required) receipt date.
This is done as follows:
- take receipt data as time goods are requested at destination;
- determine calendar linked to carrier (that is buy-from BP);
- determine distance (expressed in time, not distance) between
origin and destination by taking into account the transport
mode;
- take receipt data as starting point in calendar, deducted time
by fitting this in the calendar when available (backward),
and determine the delivery date.
If either the priority search sequence (PriorityOfDistance) is not
applicable; or the addresses (iAddressFrom and iAddressTo)
are unknown; or the conversion factors are not found; or an
error will occur within the calendar module then the calculated
date (oCalculatedDate) will be zero.
Pre:    The base unit as defined in the Common Parameters
(tccom999.dsbt) should be seconds, with the appropriate
conversion factor to the standard base unit for time as defined
in the Base Units in MCS Parameters (tcmcs000.ctim), since the
distance must be expressed in seconds, in order to increase the
given date (of domain type UTC) with the distance in seconds.
Post:   not applicable
Input:  iAddressFrom                    - Address from which the goods
have to be transported.(Mandatory)
iAddressTo                      - Address to which the goods
have to be transported.(Mandatory)
iDate                           - date from where lead time needs
to be calculated (if empty,
system date will be defaulted)
iOperator                       - "+" forward planning (default)
"-" backward planning.
iCarrier                        - carrier to determine both the
calendar code and transport
mode (if empty, the company
calendar code and transport
mode <none> will be defaulted)
iTransportCategory              - Transport Category
***  parameter below can be used ***
***  if Freight Management (FM) is not implemented. ***
iPriorityOfDistance             - forced search sequence (if
empty, parameter tccom999.dstt
will be used)
*** parameters below can be used ***
*** if Freight Management (FM) is implemented.  ***
iItem                           - Item to be transported
iRoute                          - Route to be followed
iServiceLevel                   - Service Level
iTransportMeansGroup            - Transport Means Group
iTransportMeansCombination      - Transport Means Combination
iMeansOfTransport               - Means of Transport
iTermsOfDelivery                - Terms of delivery
iPointOfTitlePassage            - Point of title passage
Output: oCalculatedDate                 - Start Date for BACKWARD planning
- End Date for FORWARD planning
Return: 0               Succesfully transportation date determined
<> 0            Otherwise
```
