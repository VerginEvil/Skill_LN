# ReminderLetter.SkipPrintReminderLetter

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ReminderLetter
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2201-2202

Skips printing of a reminding letter. This process extension is available from 2023.09 ( KB2300210 ). To implement this process extension, you can use the information below:

```baan
Usage:        ReminderLetter.SkipPrintReminderLetter can be used to skip
printing of a reminder letter.
Session where this Process Extension can be implemented:
-               Print Reminder Letter (tfacr3405m100)
Fields that are available to be used in this Process Extension:
-               All fields of "Reminder selection"  (tfacr303)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacr303       |* Reminder Selection
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tfacr303 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for RequestForQuoteConvert

The following process extension(s) is/are available: RequestForQuoteConvert.CustomSorting
