# ProcessingOptionSet.CheckOptionNames

> Chapter: Chapter 2 Public Interfaces for Extensibility
>
> Group: Public Interfaces for ProcessingOptionSet
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 82-82

```baan
DLL:   tcextextapi
This function is available from     2026.06 (KB3668896  ).
Syntax: long ProcessingOptionSet.CheckOptionNames(
const           long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function checks the validity of the given option-set, by
checking whether the option                      -set contains options that are *not*
provided in the variable arguments. The function can be used to
verify whether the option                      -set contains options that are not
supported.
Input:  iProcessingOptionSet                  - reference to processing options set
Variable Arguments:
Repetition of argument:
OptionName                                    - option name of type string
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0                     - Success
<> 0                                  - An error occurred
```
