# ComposeShippingStructure.CommandHandling

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ComposeShippingStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1990-1991

Allows to disable commands and to define additional actions before and after execution within the sh. This process extension is available from 2022.10 ( KB2262990 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension it is possible to disable a command and
to execute additional actions before and/or after one of the following
commands is executed in the compose shipping structure tree:
-               Freeze
-               Reopen
-               Confirm
-               Select Carrier/LSP
-               New Load
For disabling commands the process extension is called when selecting an
object in the compose shipping structure tree and for which the standard
has decided the command should be enabled.
Upon execution of a command, the process extension is called twice, once
before the action will be performed and once when the command has been
executed for each of the selected entities in the compose shipping
structure tree.
```

To implement this process extension, you need to implement the following method(s):
