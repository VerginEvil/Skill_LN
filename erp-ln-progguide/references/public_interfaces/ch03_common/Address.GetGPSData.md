# Address.GetGPSData

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Address
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 87-88

```baan
DLL:   tcextcomapi
This function is available from     2024.12 (KB3541249  ).
Syntax: long Address.GetGPSData(
domain  tcccty           iCountry,
domain  tcdsca           iCityDescription mb,
domain  tccadr.namc      iStreet mb,
domain  tccom.nmbr       iHouseNumber mb,
domain  tccom.nmbr       iPOBoxNumber mb,
domain  tcpstc           iZIPCode mb,
domain  tcmcs.cste       iStateProvince,
ref     domain  tcglat           oLatitude,
ref     domain  tcglon           oLongitude,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Based on addressdata the GPS Latitude and GPS Longitude is
determined by means of a webservice ( AVATAX or Bing)
Pre:    A licence key for AVATAX or Bing must be avialable in the
relevant parameter sessions.
Input:  iCountry                              - Country (m)
iCityDescription                              - City description (m)
iStreet                                       - Street (m)
iHouseNumber                                  - House Number
iPOBoxNumber                                  - PO Box
iZIPCode                                      - ZIP Cde
iStateProvince                                - State or Province
Output: oLatitude                             - Latitude
oLongitude                                    - Longitude
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Success
<> 0                                          - Otherwise
```
