# BOD.GetAddressFromLocationNode

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1668-1669

```baan
DLL:   tcextbodapi
This function is available from 2026.09 (KB3686801).
Syntax: long BOD.GetAddressFromLocationNode(
long             iXmlNode,
domain  tcbod.name       iNoun,
domain  tcmcs.str132     iAddressPath,
domain  tccom.cadr       iCurrentAddress,
ref     domain  tccom.cadr       oAddress,
ref             boolean          oAddressIsSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function gets the address code, or creates an address
code, based on the address details in an incoming BOD
message.
The address is read from the Location node that is found at
iAddressPath. When more than one Location node is present at
that path, the preferred Location is used: this is the Location
for which the element Address/Preference/Indicator is "true".
When none of the Locations is marked as preferred, the first
Location is used.
Based on the address fields of the selected Location, the
interface either gets an existing LN address code or creates a
new one:
- GET: when an LN address already exists with the same address
fields, the code of that existing address is returned.
- CREATE: when no matching LN address exists, a new LN address
is created and the code of the newly created address is
returned.
iCurrentAddress is the address that is currently linked to the
business object (for example when an existing address is being
changed). When it is supplied, it is used as the starting point
of the search so that the existing address can be reused or
updated instead of creating a duplicate. The update only fills
fields that are empty in the current address with the
corresponding data from the address in the incoming BOD
message; it never overwrites a field that already has a value
in the current address with different data.
When a mandatory address field (the country or the city) for
creating an address code is empty in the BOD message,
the address is considered empty: no address code is returned
and oAddressCodeIsSet is false.
Pre:    NA
Post:   NA
Input : iXmlNode                - The xml node to search in. Mandatory
iNoun                   - Noun. e.g. "ServiceOrderInBOD".
Mandatory.
iAddressPath            - The path to the Location node in the xml node.
e.g.
"<ServiceOrderHeader><CustomerParty><Location>".
Mandatory.
iCurrentAddress         - The current address code. Only relevant
in case of a change; otherwise it can
be left empty. e.g. "ADD000232".
Output: oAddress                - The address code that was found or
created. e.g. "ADD000232".
oAddressIsSet           - Indicator whether the address code was
set (true or false).
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK.
<> 0                    - Error occurred.
```
