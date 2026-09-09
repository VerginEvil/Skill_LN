# tiext.cpr0002.standard.cost.skip.calculate.item

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StandardCost
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2275-2277

```baan
Syntax: long tiext.cpr0002.standard.cost.skip.calculate.item(
domain  tcitem           i.item,
ref             boolean          o.skip.calculate,
ref             string           o.message() )
Usage:        Expl:   This function is called in the process of Standard Cost
Calculation, during bottom-up calculation preparation, in order
to decide if the calculation for the specific Item must be
skipped entirely (i.e. for all its enterprise units).
A message may be returned, to present information about the
decision to the user.
For this decision function no database record is made current.
During the bottom-up calculation preparation process, only the
item level dependencies defined by product structure information
(Bills of Materials, Production Models, Subcontracting Models
etc.) are used to define the calculation order.
The first step in this preparation process is to create the
set of items to calculate. This is where the skip decision
is applied.
External variables available for use by this process extension
function:
- proc_ext_std_cost_skip_calc_calculation_code
[type: domain tccpcc]
Calculation code for which the calculation is executed.
- proc_ext_std_cost_skip_calc_calculation_date
[type: domain tcdate]
The date used for calculation. Used for selection of
date-effective base data, like BOM lines/models, routing
operations/models and/or operation rates.
- proc_ext_std_cost_skip_calc_actualize
[type: domain tcyesno]
Indicates if actualization of calculated standard cost
is requested.
- proc_ext_std_cost_skip_calc_effective_date
[type: domain tcdate]
The date used for calculation. Used for selection of
date-effective base data, like BOM lines/models, routing
operations/models and/or operation rates.
Note: tables and external variables must also be declared in
the Process Extension
Implementation Example:
Intention:
For a specific simulation calculation code (SIM),
only a subset of items need to be included in the
calculations.
Hook Declarations:
extern domain tccpcc proc_ext_std_cost_skip_calc_calculation_code
Hook tiext.cpr0002.standard.cost.skip.calculate.item:
function extern long tiext.cpr0002...
...
{
if proc_ext_std_cost_skip_calc_calculation_code = "SIM"
and not item.in.simulation.set(i.item)
then
o.message = trim$(i.item) & " not in simulation set"
o.skip.calculate = true
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.item                  - item
Output: o.skip.calculate        - decision result
o.message               - message, multibyte - max 300 characters
Return: 0                       - success
DALHOOKERROR            - error
```
