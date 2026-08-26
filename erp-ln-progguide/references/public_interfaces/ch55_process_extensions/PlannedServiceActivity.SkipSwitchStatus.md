# PlannedServiceActivity.SkipSwitchStatus

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PlannedServiceActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2109-2111

Skips Planned Service Activity when Switching its Status. This process extension is available from 2020.05 ( KB2120655 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PlannedServiceActivity.SkipSwitchStatus can be used
to skip Planned Service Activities when switching the status.
Sessions where this Process Extension can be implemented:
-               Switch Status Maintenance Plan (tsspc2201m000).
Fields that are available to be used in this Process Extension:
-               All fields of table Planned Activities (tsspc200).
-               If in the selection range of session 'Switch Status Maintenance Plan'
(tsspc2201m000) the field which controls the selection of
serialized items is either set to 'Selection of Serialized Items',
or set to 'Selection of Top Items', then also all fields of table
'Serialized Items' (tscfg200) can be used.
-               If in the selection range of session 'Switch Status Maintenance Plan'
(tsspc2201m000) the field which controls the selection of maintenance
scenarios is set to 'Selection of Scenarios', then also all fields of
table 'Preventive Maintenance Scenario Lines' (tsspc131) can be used.
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table ttsspc200
|**************************************************************
|* Fields of tscfg200 can be used if Selection of Serialized
|* Items is set to 'Selection of Serialized Items' or set to
|* 'Selection of Top Items'.
|**************************************************************
table ttscfg200
|**************************************************************
|* Fields of tsspc131 can be used if Selection of Maintenance
|* Scenarios is set to 'Selection of Scenarios'.
|**************************************************************
table ttsspc131
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tsspc200 = true> then
return(true)
endif
if Selection of Serialized Items is set to
'Selection of Serialized Items' or set to
'Selection of Top Items' then
if <condition on tscfg200 = true> then
return(true)
endif
endif
if Selection of Maintenance Scenarios is set to
'Selection of Scenarios' then
if <condition on tsspc131 = true> then
return(true)
endif
endif
return (false)
}
```

## Process Extensions for PriceBookLine

The following process extension(s) is/are available: PriceBookLine.SkipGlobalUpdatePricesViaPriceBooks
