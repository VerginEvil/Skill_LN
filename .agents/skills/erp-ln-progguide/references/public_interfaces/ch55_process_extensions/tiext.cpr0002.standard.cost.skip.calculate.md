# tiext.cpr0002.standard.cost.skip.calculate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StandardCost
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2273-2275

```baan
Syntax: long tiext.cpr0002.standard.cost.skip.calculate(
long             i.level,
domain  tcitem           i.top.item,
domain  tcemm.grid       i.top.eu,
domain  tcitem           i.parent.item,
domain  tcemm.grid       i.parent.eu,
ref             boolean          o.skip.calculate,
ref             string           o.message() )
Usage:        Expl:   This function is called in the process of Standard Cost
Calculation, in order to decide if the calculation must be
skipped for a specific Item/Enterprise Unit combination.
A message may be returned, to present information about
the decision to the user.
When this function is called all fields of table:
- Item Costing (ticpr007) are read and current.
Note that fields ticpr007.item and ticpr007.eunt refer to the
current Item/Enterprise Unit being considered for calculation.
External variables available for use by this process extension
function:
- proc_ext_std_cost_skip_calc_calculation_code
[type: domain tccpcc]
Calculation code for which the calculation is executed.
- proc_ext_std_cost_skip_calc_calculation_method
[type: domain tcccmt]
single.level:
Limited product structure explosion, standard
cost at second level is read, not calculated.
top.down:
Explodes product structure top-down, calculates
all lower levels and cost is rolled up to top
level.
bottom.up:
Product structure determines which higher level
items need to part of the calculated set.
- proc_ext_std_cost_skip_calc_calculation_mode
[type: long]
0: calculating only
1: printing multilevel
2: printing single level
- proc_ext_std_cost_skip_calc_project
[type: domain tccprj]
The project, set in case the calculation is started in
the context of a project, otherwise empty.
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
- proc_ext_std_cost_skip_calc_analyze_before_print
[type: domain tcyesno]
Special calculation mode, calculating before printing
while in simulation.
- proc_ext_std_cost_skip_calc_uef_calculation
[type: boolean]
Indicates if calculation is done for an effectivity unit.
- proc_ext_std_cost_skip_calc_from_pcs
[type: boolean]
Indicates if calculation is called in Project (PCS)
context.
- proc_ext_std_cost_skip_calc_from_sales
[type: boolean]
Indicates if calculation is called from Sales - or
Quotation line context.
Note: tables and external variables must also be declared in
the Process Extension
******  Example Product Structure.
The example assumes that the actual set of Implemented Software
Components (tccom0100s000) has the concepts Standard Cost by
Enterprise Unit and Job Shop by Site set to Active.
Product A (top-item) requires a standard cost for two enterprise
units. Its enterprise units have the following properties:
A/EU1 (costing source Intercompany Transfer, supplied by
EU2)
A/EU2 (costing source Job Shop)
Because of the trade relation, calculation of A/EU1 uses the
standard cost of A/EU2. Standard cost of A/EU2 (costing source
Job Shop) is based on the Job Shop Bill of Material defined for
the site linked to EU2.
The materials required for production of product A are B and C.
Items B and C only have standard cost in enterprise unit EU2.
A representation of the product structure levels with the
dependencies for standard cost calculation:
A (EU1) (level 1) (Costing Source Intercompany Transfer)
^-----A(EU2) (level 2) (Costing Source Job Shop)
^----B(EU2) (level 3)
^----C(EU2) (level 3)
When this function is called in a top-down calculation for
top item A, then at some point, the calculation encounters
item C and EU2.
Besides the available ticpr007 fields:
ticpr007.item is set to C
ticpr007.eunt is set to EU2
The input parameters provide further information about the
context:
i.level is set to 3,
i.top.item is set to A,
i.top.eu is set to EU1,
i.parent.item is set to A,
i.parent.eu is set to EU2.
Implementation Example:
Intention:
For a specific Enterprise Unit (EU2), when actualization
is requested, calculation (and subsequent actualization)
of standard cost is not allowed.
Hook Declarations:
table tticpr007
extern domain tcyesno proc_ext_std_cost_skip_calc_actualize
Hook tiext.cpr0002.standard.cost.skip.calculate:
function extern long tiext.cpr0002...
...
{
if      proc_ext_std_cost_skip_calc_actualize
= tcyesno.yes
and str.compare(ticpr007.eunt, "EU2   ") = 0
then
o.message = "calculation for EU2 is skipped"
o.skip.calculate = true
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.level         - the depth in the calculation process
i.top.item      - top item
i.top.eu        - top enterprise unit
i.parent.item   - parent item
i.parent.eu     - parent enterprise unit
Output: o.skip.calculate- decision result
o.message       - message, multibyte - max 300 characters
Return: 0                       - success
DALHOOKERROR            - error
```
