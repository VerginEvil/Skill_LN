# Workflow.RecallByTypedObjectID

> Chapter: Chapter 44 Public Interfaces for Object Configuration Management
>
> Group: Public Interfaces for Workflow
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1914-1914

```baan
DLL:   tcextocmapi
This function is available from 2023.11 (KB2310367).
Syntax: long Workflow.RecallByTypedObjectID(
domain  ttocm.toid       iTypedObjectID,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function recalls the record belonging to the specified
Typed Object ID that had been submitted for approval through ION
Workflow. It publishes a Process.WorkflowBOD with actionCode
"Replace" to interrupt the related Workflow in ION.
Example: an external application wants to update a sales order.
The update fails because the workflow status of the sales order
is 'Pending'. This function can be called to recall the sales
order so that the sales order can be updated after the related
Workflow was successfully interrupted in ION.
Pre:    An Object Type must be configured in the OCM Model for the
table belonging to the specified Typed Object ID and this Object
Type must be deployed. The related Workflow must be activated in
ION. Retry point must be set.
Post:   Transaction must be committed or aborted.
Input:  iTypedObjectID          - Workflow Typed Object ID belonging to
the record that must be recalled.
Mandatory.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success
<> 0                    - An error occurred
```
