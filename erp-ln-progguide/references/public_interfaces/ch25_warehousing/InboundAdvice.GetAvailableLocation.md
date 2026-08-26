# InboundAdvice.GetAvailableLocation

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1068-1071

```baan
DLL:   whextinhapi
This function is available from     2021.08 (KB2196658  ).
Syntax: long InboundAdvice.GetAvailableLocation(
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcqst1           iRequiredQuantity,
domain  tccuni           iRequiredUnit,
ref     domain  tcitem           iMultiItemArray() fixed,
ref     domain  tcqst1           iMultiItemRequiredQuantityArray(),
ref     domain  tccuni           iMultiItemRequiredUnitArray() fixed,
domain  tcmcs.long       iMultiItemNumberOfUnits,
domain  tcclot           iLot,
domain  tccom.bpid       iOwner,
domain  tcwght           iRequiredWeight,
domain  tcleng           iRequiredVolume,
domain  tcleng           iRequiredFloor,
domain  tcleng           iDepth,
domain  tcleng           iWidth,
domain  tcleng           iHeight,
domain  whwmd.pkdf       iPackageDefinition,
domain  whinh.ittp       iTransactionType,
domain  whwmd.loct       iLocationType,
boolean          iIgnoreExpectedOccupationDecrease,
boolean          iAssignLocationToBusinessPartner,
boolean          iAllOnOneLocation,
boolean          iMustBeMultiItem,
boolean          iMustBeMultiLot,
boolean          iIncludeFixedLocations,
boolean          iMinimalPutAway,
ref             boolean          oLocationsAvailable,
ref             long             oNumberOfLocations,
ref     domain  whloca           oLocationsArray() fixed,
ref     domain  tcqst1           oQuantityToAdviseArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will search for a location that is
available.
A location is available if it meets the requirements as
specified by the input of this function, and if it passes the
following possible constraints:
-                       Location occupation
-                       Multi/single item location
-                       Multi/single lot location
-                       Transaction (blocking)
-                       Location ownership
-                       Storage conditions
-                       Location capacity
When the goods to be stored do not fit into the one location,
it will continue to search for other locations until all goods
are stored. For this reason multiple locations can be returned
by this function.
Pre:    oLocationsArray and oQuantityToAdviseArray must be declared as
based variables, this function will allocate the memory.
Post:   After the oLocationsArray and oQuantityToAdviseArray are used,
free the memory.
Input:  iWarehouse                            - Warehouse
-                                               Mandatory
iItem                                         - Item
-                                               Mandatory when iMultiItemNumberOfUnits
is zero.
iRequiredQuantity                             - Quantity that must be advised.
-                                               Mandatory when iMultiItemNumberOfUnits
is zero.
iRequiredUnit                                 - Unit of iRequiredQuantity.
-                                               Mandatory when iMultiItemNumberOfUnits
is zero.
iMultiItemArray                               - Array of Items.
-                                               Mandatory when iItem is not filled.
iMultiItemRequiredQuantityArray
-                                               Array of quantities that must be
advised.
-                                               Mandatory when iItem is not filled.
iMultiItemRequiredUnitArray
-                                               Array of Unit of iRequiredQuantity.
-                                               Mandatory when iItem is not filled.
iMultiItemNumberOfUnits                       - The number of Items in the Multi Item
array.
-                                               Mandatory when iItem is not filled.
iLot                                          - Lot for which the location is
searched for.
-                                               Optional.
iOwner                                        - Owner for which the location is
searched for.
-                                               Optional.
iRequiredWeight                               - Total weight of multi item array.
-                                               Optional.
-                                               Value cannot be negative.
iRequiredVolume                               - Total volume of multi item array.
-                                               Optional.
-                                               Value cannot be negative.
iRequiredFloor                                - Total floor space of multi item array.
-                                               Optional.
-                                               Value cannot be negative.
iDepth                                        - Required depth.
-                                               Optional.
-                                               Value cannot be negative.
iWidth                                        - Required width.
-                                               Optional.
-                                               Value cannot be negative.
iHeight                                       - Required height.
-                                               Optional.
-                                               Value cannot be negative.
iPackageDefinition                            - Package definition of iItem.
-                                               Optional.
iTransactionType                              - Transaction type.
-                                               Mandatory
iLocationType                                 - Location type to search for.
-                                               Mandatory
iIgnoreExpectedOccupationDecrease
-                                               True: Expected occupation decrease is
ignored in the location capacity
calculation.
-                                               False: Expected occupation decrease is
taken into account in the
location capacity calculation.
-                                               Mandatory
iAssignLocationToBusinessPartner
-                                               True: Only unoccupied locations are
included in the search.
When for the warehouse and item
the ownership registration is
done by location and iOwner is
filled then only locations of
that owner or without an owner
are taken into account.
-                                               False: No checks on unoccupied
locations or ownership.
-                                               Mandatory
iAllOnOneLocation                             - True: The required quantity must fit
on one location.
-                                               False: The required quantity does not
need to fit on one location.
completely
-                                               Mandatory
iMustBeMultiItem                              - True: The location must be a multi
item location.
-                                               False: The location does not need to
be a multi item location.
-                                               Mandatory
iMustBeMultiLot                               - True: The location must be a multi lot
location.
-                                               False: The location does not need to
be a multi lot location.
-                                               Mandatory
iIncludeFixedLocations                        - True: Fixed locations are included in
the search.
-                                               False: Fixed location are excluded
from the search.
-                                               Mandatory
iMinimalPutAway                               - True: Locations are sorted on
available capacity to reduce the
number locations as much as
possible.
-                                               False: Locations are not sorted
available capacity.
-                                               Mandatory
Output: oLocationsAvailable                   - true: One or more Locations are found.
false: No locations are found.
oNumberOfLocations                            - Number of available locations.
oLocationsArray                               - Array of available locations.
oQuantityToAdviseArray                        - Array of quantities that can be
advised to this location in
iRequiredUnit.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
