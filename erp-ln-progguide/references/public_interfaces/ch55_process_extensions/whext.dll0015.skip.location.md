# whext.dll0015.skip.location

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for LocationSearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2084-2085

```baan
Syntax: long whext.dll0015.skip.location(
domain  tccwar           i.warehouse,
domain  whloca           i.location,
domain  tcncmp           i.rental.owner.company,
domain  tccwoc           i.rental.owner,
domain  tcitem           i.item,
domain  tcatse           i.attribute.set,
domain  tcqst1           i.required.quantity,
domain  tccuni           i.required.unit,
ref             boolean          o.skip.location )
Usage:        Expl:   This function allows skipping the warehouse location suggested
by the Standard LN Search Engine based on user                      -defined criteria.
The user can set specific conditions or parameters that will be
used to filter the suggested locations. If the proposed location
does not match these criteria, the function will automatically
skip it and move to the next possible location.
This ensures a more accurate and personalized location selection
process that meets the user's specific requirements.
In case of generating Inbound Advice with a selected option
'Detailed Inbound Advice Log', a message about the skipped
location will be added to this Log.
IMPORTANT: it is not possible to use the Public Interface
'InboundAdvice.GetAvailableLocation' inside this process
extension, as this would cause a recursion error.
Following tables are current when this extension is triggered:
whwmd300                       - Locations
Pre:    NA
Post:   NA
Input:  i.warehouse                           - Warehouse
i.location                                    - Found Location
i.rental.owner.company                        - Rental Owner Company
i.rental.owner                                - Rental Owner
i.item                                        - Item
i.attribute.set                               - Attribute Set. Applicable in case of
Product Dimensions
i.required.quantity                           - Required Quantity
i.required.unit                               - Required Unit
Output: o.skip.location                       - location must be skipped (true/false)
Return: 0/DALHOOKERROR
```

## Process Extensions for MaterialSupplyLines

The following process extension(s) is/are available: MaterialSupplyLines.HandleCombining
