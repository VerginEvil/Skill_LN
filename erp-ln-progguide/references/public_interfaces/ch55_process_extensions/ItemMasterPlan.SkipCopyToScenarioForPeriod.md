# ItemMasterPlan.SkipCopyToScenarioForPeriod

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2073-2074

Skips copying Item Master Plan to Scenario for specific Period. This process extension is available from 2023.06 ( KB2274036 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension ItemMasterPlan.SkipCopyToScenarioForPeriod can be used
to skip copying Master Plan to Scenario per plan Period in the from
Scenario.
Sessions where this Process Extension can be implemented:
-               Copy Master Plan to Scenario (cprmp2203m000)
Fields that are available to be used in this Process Extension:
-               cprpd100.plni (Plan Item),
-               cprpd100.plvl (Plan Level)
-               cprmp300.chan (Channel)
-               cprmp300.plnc (Scenario From),
-               cprmp300.pern (Period)
-               cprmp300.sdat (Period Start Date),
-               cprmp300.pdat (Period Finish Date)
External variables that are available to be used in this Process
Extension:
-               proc_ext_skip_item_masterplan_cpy_period_scen_to
[ type: domain cpcom.plnc ]
```

## Process Extensions for ItemOrderPlan

The following process extension(s) is/are available: ItemOrderPlan.CustomActions
