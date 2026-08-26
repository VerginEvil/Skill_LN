# Maps Workbench examples

## Maps Example
Below part of a UI script is shown where a map object is created and shown. This example uses a set of functions to retrieve the required information from a datasource. The implementation of these functions is not shown in this example.
```

#include <bic_maps>		| Needed for map functions

long mid

choice.interrupt:
on.choice:
	distance = map.getroutedistance(mid)
	display("distance")
	map.delete(mid)

functions:

| An external function which can be invoked as a 4GL Form command.
function extern void show.map()
{
	long fromCity
	long toCity
	long viaCity1
	long viaCity2

	|Get reference to a number of cities.
	|Each city object contains city specific data.
	fromCity = getCity(strip$(from.city))
	viaCity1= getCity(strip$(via.city1))
	viaCity2= getCity(strip$(via.city2))
	toCity = getCity(strip$(to.city))

	mid = map.create()
	add.city.point(mid, fromCity)
	if viaCity1 <> 0 then
		add.city.point(mid, viaCity1)
	endif

	if viaCity2 <> 0 then
		add.city.point(mid, viaCity2)
	endif
	add.city.point(mid, toCity)

	if legend = teyeno.yes then
		add.legend.info(mid)
	endif

	map.show(mid, "Route Map")

	set.alarm(1000) | Optional, in case the distance of the route will be displayed.
}

function void add.city.point(long mid, long cityNode)
{
	long rpid
	long infoid

	|Add a route point
	rpid = map.add.point(mid, val(getCityLat(cityNode)),
		 val(getCityLon(cityNode)), getCityIconType(cityNode))

	|Add tooltip data for this route point
	infoid = map.add.info(rpid, getCityName(cityNode))
	map.add.infoline(infoid, "Inhabitants:", getCityInhabitants(cityNode))
	map.add.infoline(infoid, "Longitude:", getCityLon(cityNode))
	map.add.infoline(infoid, "Latitude:", getCityLat(cityNode))
}

function void add.legend.info(long mid)
{
	map.add.legendline(mid, "Customer", CIRCLE)
	map.add.legendline(mid, "Warehouse", TRIANGLE)
	map.add.legendline(mid, "Supplier", PENTAGON)
	map.add.legendline(mid, "Other", SQUARE)
}
```

## Related topics
- [Maps Workbench overview](overview.md)
- [Maps Workbench synopsis](synopsis.md)
