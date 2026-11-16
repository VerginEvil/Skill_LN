# ItemMasterPlan.SkipCopyToScenario

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2094-2094

```baan
Skips copying Item Master Plan to Scenario.
This process extension is available from 2022.06 (KB2239394).
To implement this process extension, you can use the information below:
Usage:        Process Extension ItemMasterPlan.SkipCopyToScenario can be used
to skip certain plan items when copying Plan Item Master Plan data
from one scenario to another.
Sessions where this Process Extension can be implemented:
- Copy Master Plan to Scenario (cprmp2203m000)
Fields that are available to be used in this Process Extension:
- cprpd100.plni (Plan Item),
- cprpd100.plvl (Plan Level)
External variables that are available to be used in this Process
Extension:
- proc_ext_skip_item_masterplan_cpy_scen_from [ type: domain cpcom.plnc ]
- proc_ext_skip_item_masterplan_cpy_scen_to   [ type: domain cpcom.plnc ]
```
