# whext.dll0015.overrule.location

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for LocationSearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2081-2084

```baan
Syntax: long whext.dll0015.overrule.location(
domain  tccwar           i.warehouse,
domain  whloca           i.location,
domain  tcncmp           i.rental.owner.company,
domain  tccwoc           i.rental.owner,
domain  tcitem           i.item,
domain  tcatse           i.attribute.set,
domain  tcqst1           i.required.quantity,
domain  tccuni           i.required.unit,
ref     domain  tcitem           i.multi.item.array() fixed,
ref     domain  tcqst1           i.multi.item.required.quantity.array(),
ref     domain  tccuni           i.multi.item.required.unit.array() fixed,
domain  tcmcs.long       i.number.of.units,
domain  tcclot           i.lot,
domain  tccom.bpid       i.owner,
domain  tcwght           i.required.weight,
domain  tcleng           i.required.volume,
domain  tcleng           i.required.floor,
domain  tcleng           i.required.depth,
domain  tcleng           i.required.width,
domain  tcleng           i.required.height,
domain  whwmd.pkdf       i.package.definition,
domain  tcqiv1           i.quantity.package.definition.received,
domain  tcqiv1           i.quantity.package.definition.advised,
domain  whinh.ittp       i.transaction.type,
boolean          i.assign.location.to.business.partner,
boolean          i.all.on.one.location,
boolean          i.must.be.multi.item,
boolean          i.must.be.multi.lot,
domain  whwmd.loct       i.location.type,
boolean          i.minimal.put.away,
ref     domain  whloca           o.new.location )
Usage:        Expl:   This function allows a user to specify a new location to be used
instead of the location suggested by Standard LN Search Engine.
This is particularly useful in situations where it is necessary
to change the storage location for goods or materials.
The function provides flexibility and adaptability, enabling the
user to easily manage changes in planning and logistics.
After executing the function, warehouse location constraints
will be checked according to LN standards. If the replaced
location does not match the conditions for storing the goods,
the function will proceed to search for the next location.
If at each iteration, as a result of executing the extension,
the same location (or a location that does not fit the placement
conditions) is obtained, then a situation may arise that the LN
won't be able to successfuly complete the location search.
In case of generating Inbound Advice with a selected option
'Detailed Inbound Advice Log', a message about the location
replacement will be added to this Log.
IMPORTANT: it is not possible to use the Public Interface
'InboundAdvice.GetAvailableLocation' inside this process
extension, as this would cause a recursion error.
As an example of the extnesion implementation, can be considered
creation of a manual Inbound Advice where the user can specify
a location of their own choice. However, after verification by
the LN standard, the specified location may not meet the storage
conditions and the advice cannot be completed.
Pre:    NA
Post:   Location found by LN Standard may be replaced by a user              -defined
location if it meets the storage conditions
Input:  i.warehouse                           - Warehouse
i.location                                    - Found Location
i.rental.owner.company                        - Rental Owner Company
i.rental.owner                                - Rental Owner
i.item                                        - Item
i.attribute.set                               - Attribute Set. Applicable in case of
Product Dimensions
i.required.quantity                           - Quantity that must be advised
i.required.unit                               - Unit of i.required.qty
i.multi.item.array()                          - The items in the handling unit
structure
i.multi.item.required.quantity.array()
-                                               The quantities in the handling unit
structure
i.multi.item.required.unit.array()
-                                               The units in the handling unit
structure
i.number.of.units                             - The number of handling units in the
handling unit structure (excluding
dummy handling units)
i.lot                                         - Lot code
i.owner                                       - The business partner allocated to
the location
i.required.weight                             - Required weight
i.required.volume                             - Required volume
i.required.floor                              - Required floor in location units.
Where floor = length unit*length unit
i.required.depth                              - Required depth
i.required.width                              - Required width
i.required.height                             - Required height
i.package.definition                          - Package definition
i.quantity.package.definition.received
-                                               Only applicable in case of package
definitions.
i.quantity.package.definition.advised
-                                               Only applicable in case of package
definitions.
i.transaction.type                            - Transaction type (receipt, issue, etc)
i.assign.location.to.business.partner
-                                               true: if no location can be found for
the given owner then an empty,
unassigned location is searched for.
If found, then this location is
assigned to the owner and advise is
done to this location.
false: no location will be assigned to
an owner.
i.all.on.one.location                         - true: advise must be done to one
location. If not possible, then no
advice will be generated.
false: advise can be done to several
locations.
i.must.be.multi.item                          - true: location must be multi item
false:location may also be single item
Note: a multi item HU can not be
placed on a single item location.
i.must.be.multi.lot                           - true: location must be a multi lot
location
false: location may be single lot as
well
i.location.type                               - Location type to search for
i.minimal.put.away                            - Minimal put away
Output: o.new.location                        - Location that might replace
Found Location. Initially initialized
by i.location
Return: 0/DALHOOKERROR
```
