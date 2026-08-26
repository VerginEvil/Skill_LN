# ProcessingOptionSet.Read

> Chapter: Chapter 2 Public Interfaces for Extensibility
>
> Group: Public Interfaces for ProcessingOptionSet
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 84-85

```baan
DLL:   tcextextapi
This function is available from     2026.06 (KB3668896  ).
Syntax: long ProcessingOptionSet.Read(
const           long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Assign default values to the options given and overwrite
from the Processing Option Set. The function
uses variable arguments to specify the options that may
be passed via this interface.
Note that no error is given if the Processing Option Set
contains an option that is not present in the argument triplets.
If consistency checking is required, then function
ProcessingOptionSet.CheckOptionNames in DLL tcextextapi can be
used.
Input:  iProcessingOptionSet                  - reference to processing options set
Variable Arguments:
Repetition of sets of three arguments:
OptionName                                    - option name of type string
OptionVariable                                - option variable (declared)
OptionDefault                                 - default option value, in type
of option variable
Output: Values of each OptionVariable is modified according to its
default option value or value from the Processing Option Set.
WARNING: When the domain of the output value has data type
String, it will NOT be aligned according to its
domain. To prevent unexpected results, alignment
can be programmed using tt.align.according.domain().
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0                     - successfully read
<> 0                                  - failure
```

## Chapter 3 Public Interfaces for Common

## Public Interfaces for Address

The following functions are available: Address.Create Address.GetGPSData Address.StartDetail Address.StartPrintByBusinessPartner
