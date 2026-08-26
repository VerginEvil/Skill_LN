# Assembly.CalculatePartRequirements

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for Assembly
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 843-844

```baan
DLL:   tiextascapi
This function is available from     2021.08 (KB2198443  ).
Syntax: long Assembly.CalculatePartRequirements(
domain  tcncmp           iCompany,
domain  cpitem           iPlanItem,
domain  tiutcd           iDateFrom,
domain  tiutcd           iDateTo,
domain  tcyesno          iUpdateSegmentSchedules,
domain  tcyesno          iUpdatePlanItems,
domain  tiasc.ardt.typ   iReferenceDateType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to calculate the Assembly Part
Requirements for a Product Variant whose Assembly Parts are not
yet allocated. Transaction management is handled in this
function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:
iCompany                                      - Company: Mandatory.
iPlanItem                                     - Plan Item: Mandatory.
iDateFrom                                     - Date From.
iDateTo                                       - Date To.
iUpdateSegmentSchedules                       - Update Segment Schedules: Mandatory.
iUpdatePlanItems                              - Update Plan Items: Mandatory.
iReferenceDateType                            - Reference Date Type: Mandatory.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Assembly Part Requirement Calculated.
<> 0                                          - Otherwise.
```
