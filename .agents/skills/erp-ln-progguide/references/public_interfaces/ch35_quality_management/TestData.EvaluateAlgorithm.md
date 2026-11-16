# TestData.EvaluateAlgorithm

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for TestData
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1800-1801

```baan
DLL:   qmextptcapi
This function is available from 2025.04 (KB3568308).
Syntax: long TestData.EvaluateAlgorithm(
domain  qmptc.iorn       iInspectionOrder,
domain  tcpono           iInspectionLine,
domain  qmptc.saml       iSample,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function will Evaluate the Algorithm of given Inspection
Order line and sample, if the line method is 'Algorithm'.
And before calling this function, Inspection order lines with
'character for Algorithm' as 'Yes' must have test result,
Otherwise the Algorithm line will not have a result.
Pre     : db.retry.point has to be set before calling this function.
Post    : commit.transaction() or abort.transaction should be done.
Input   : iInspectionOrder : Inspection order, mandatory.
iInspectionLine  : Inspection Line, mandatory.
iSample
: Sample for which the numeric value will be calculated.
In case the sample is zero, all samples will be
taken into account.
Output  : oExceptionMessage     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No Error.
<> 0                    - Error found.
```
