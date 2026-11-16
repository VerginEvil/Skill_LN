# Address.Create

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Address
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 86-88

```baan
DLL:   tcextcomapi
This function is available from 2024.01 (KB2314506).
Syntax: long Address.Create(
domain  tccadr.nama      iAddressName mb,
domain  tcccty           iCountry,
domain  tcdsca           iCityName mb,
boolean          iSetStateProvince,
domain  tcmcs.cste       iStateProvince,
boolean          iSetName2,
domain  tccadr.namb      iName2 mb,
boolean          iSetCity2,
domain  tccadr.namf      iCity2 mb,
boolean          iSetPostalCode,
domain  tcpstc           iPostalCode mb,
boolean          iSetStreet,
domain  tccadr.namc      iStreet mb,
boolean          iSetStreet2,
domain  tccadr.namd      iStreet2 mb,
boolean          iSetHouseNumber,
domain  tccom.nmbr       iHouseNumber mb,
boolean          iSetPOBoxNumber,
domain  tccom.nmbr       iPOBoxNumber mb,
boolean          iSetBuilding,
domain  tccom.bldg       iBuilding mb,
boolean          iSetBuildingFloor,
domain  tccom.blfl       iBuildingFloor mb,
boolean          iSetBuildingUnit,
domain  tccom.blun       iBuildingUnit mb,
boolean          iSetAddressLine1,
domain  tcmcs.str100m    iAddressLine1 mb,
boolean          iSetAddressLine2,
domain  tcmcs.str100m    iAddressLine2 mb,
boolean          iSetAddressLine3,
domain  tcmcs.str100m    iAddressLine3 mb,
boolean          iSetAddressLine4,
domain  tcmcs.str100m    iAddressLine4 mb,
boolean          iSetAddressLine5,
domain  tcmcs.str100m    iAddressLine5 mb,
boolean          iSetAddressLine6,
domain  tcmcs.str100m    iAddressLine6 mb,
ref     domain  tccom.cadr       oAddressCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a new address. If an existing address code
is found based on the given input information then the existing
address code is returned. Otherwise a new address code is
created and returned.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iAddressName            - Name of the Address
(This is a Mandatory field.)
iCountry                - Country
(This is a Mandatory field.)
iCityName               - City Name
(This is a Mandatory field.)
iSetStateProvince        - Set State/Province
iStateProvince          - State/Province
iSetName2               - Set Name 2 (True/False)
iName2                  - Name 2
iSetCity2               - Set City 2 (True/False)
iCity2                  - City 2
iSetPostalCode          - Set ZIP Code/Postal Code (True/False)
iPostalCode             - ZIP Code/Postal Code
iSetStreet              - Set Street (True/False)
iStreet                 - Street
iSetStreet2             - Set Street 2 (True/False)
iStreet2                - Street 2
iSetHouseNumber         - Set House Number (True/False)
iHouseNumber            - House Number
iSetPOBoxNumber         - Set P.O. Box Number (True/False)
iPOBoxNumber            - P.O. Box Number
iSetBuilding            - Set Building (True/False)
iBuilding               - Building
iSetBuildingFloor       - Set Building Floor (True/False)
iBuildingFloor          - Building Floor
iSetBuildingUnit        - Set Building Unit (True/False)
iBuildingUnit           - Building Unit
iSetAddressLine1        - Set Address Line 1 (True/False)
iAddressLine1           - Address Line 1
iSetAddressLine2        - Set Address Line 2 (True/False)
iAddressLine2           - Address Line 2
iSetAddressLine3        - Set Address Line 3 (True/False)
iAddressLine3           - Address Line 3
iSetAddressLine4        - Set Address Line 4 (True/False)
iAddressLine4           - Address Line 4
iSetAddressLine5        - Set Address Line 5 (True/False)
iAddressLine5           - Address Line 5
iSetAddressLine6        - Set Address Line 6 (True/False)
iAddressLine6           - Address Line 6
Output: oAddressCode            - Address Code
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Address Found/Create
<> 0                    - Error
```
