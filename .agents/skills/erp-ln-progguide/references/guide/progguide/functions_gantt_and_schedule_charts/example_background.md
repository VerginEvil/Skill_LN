# Example structure availability
```

function init.planboard.legend.colors()
{
	|**********************************************************************
	|* Define LEGEND at gantt, defaults like in the ERP LN activities
	|**********************************************************************
	...
		| legends application
	...

	| Add the used legend for the unavailability, for example:
	g.ret.long = plcm.create.legend.entry( LEGEND_ID_BACKGROUND,
			PLCM_BACKGROUND,
			"Unavailable")

	g.ret.long = plcm.create.legend.entry( LEGEND_ID_BLOCKED,
			PLCM_YELLOW,
			"Blocked")
{

function extern void plcm.get.activity.unavailability( const string activity.id(),
							 long i.start.date,
							 long i.end.date)
{
	|**********************************************************************
	|* Callback-function when the scope of the view of unavailabilities of the activity have been changed in the UI.
	|*
	|* Function is called:
	|*  1. at the start of the session
	|*  2. at change of the scope of the view
	|*
	|* Function can be used to fill the background with unavailabilities.
	|* To do this, use the plcm.set.activity.unavailability()
	|* add the array of unavailability's for activity in the scope of given interval
	|**********************************************************************

	domain	tcccp.ract	availability.type
	domain	tcmcs.long	no.elements
	domain	tcdate		start.dates(1) based
	domain	tcdate		end.dates(1) based
	domain 	tcdesc		description(1) based
	string			legend(1,1) based
	long	lret

	if i.start.date = 0 or i.end.date = 0 then
		| nothing to do
		return
	endif

	| Retrieve the no.elements from for example calendar dates
	...
		|			application logic
	...

	if no.elements <= 0 then
		return
	endif

	| Allocate and fill start.dates, end.dates, description and legend
	...
		|			application logic
	...

	lret = plcm.set.activity.unavailability(
					activity.id,
					no.elements,
					start.dates,
					end.dates,
					description,
					legend)

	| Free allocated start.dates, end.dates, description and legend
	...
		|			application logic
	...

}

function extern void plcm.get.resource.unavailability( const string resource.id(),
							long i.start.date,
							long i.end.date)
{
	| Same structure as plcm.get.activity.unavailability() for the resource
	...
	...
}
```
