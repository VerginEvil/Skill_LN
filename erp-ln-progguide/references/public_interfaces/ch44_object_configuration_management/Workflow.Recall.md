# Workflow.Recall

> Chapter: Chapter 44 Public Interfaces for Object Configuration Management
>
> Group: Public Interfaces for Workflow
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1893-1894

```baan
DLL:   tcextocmapi
This function is available from     2023.10 (KB2289885  ).
Syntax: long Workflow.Recall(
domain  tcmcs.tabl       iRootTable,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function recalls the current record in an LN session
that had been submitted for approval through ION Workflow. It
publishes a Process.WorkflowBOD with actionCode "Replace" to
interrupt the related Workflow in ION. This function should be
called in the on.recall hook of the DAL of the table specified
by iRootTable.
Pre:    An Object Type must be configured in the OCM Model for the
specified iRootTable and this Object Type must be deployed.
The related Workflow must be activated in ION.
Post:   NA
Input:  iRootTable                            - Root Table. Only tables in package "tx"
are allowed. Mandatory.
Output: oExceptionMessage                     - The last message if any message is
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
