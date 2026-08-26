# Workflow.EnableSubmit

> Chapter: Chapter 44 Public Interfaces for Object Configuration Management
>
> Group: Public Interfaces for Workflow
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1893-1893

```baan
DLL:   tcextocmapi
This function is available from     2023.02 (KB2220087  ).
Syntax: long Workflow.EnableSubmit(
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function enables the Workflow action Submit for all Object
Types that were disabled through function Workflow.DisableSubmit().
See Description of function Workflow.DisableSubmit() for further
explanation.
Pre:    Function Workflow.DisableSubmit() was called one or more times
(for one or multiple object types) in the current process.
Post:   Submitting the checked out Objects is required if this is not
automatically done.
Input:                -
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Success
<> 0                                          - An error occurred
```
