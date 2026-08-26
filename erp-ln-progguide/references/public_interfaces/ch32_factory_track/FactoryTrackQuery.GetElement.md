# FactoryTrackQuery.GetElement

> Chapter: Chapter 32 Public Interfaces for Factory Track
>
> Group: Public Interfaces for FactoryTrackQuery
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1668-1670

```baan
DLL:   brextqryapi
This function is available from     2020.09 (KB2143379  ).
Syntax: long FactoryTrackQuery.GetElement(
const           string           iElementID(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Use this public interface to get the specified element node from
the current query output row.
This public interface can only be used in the context of process
extension 'FactoryTrackQuery.QueryExtend'.
Example:
If the current query output row contains this element node,
<itemcode
Type="String"
Domain="tcitem">         MAIN ITEM</itemcode>
then this can be read by this public interface as follows.
long            ReturnValue
domain  tcitem          Item
ReturnValue = FactoryTrackQuery.GetElement(
"itemcode",
ExceptionMessage,
ExceptionID
Item)
Now Item = "         MAIN ITEM".
Example:
If the current query output row contains this element node,
<outdate
Type="String"
Domain="tcmcs.str20"
Date="04/25/2018"
Time="13:51:40">2018/04/25</outdate>
then this can be read by this public interface as follows.
long            ReturnValue
domain  tcmcs.str20     OutDate
domain  tcmcs.str10     DateAttribute
domain  tcmcs.str8      TimeAttribute
ReturnValue = FactoryTrackQuery.GetElement(
"outdate",
ExceptionMessage,
ExceptionID
OutDate,
DateAttribute,
TimeAttribute)
Now OutDate = "2018/04/25", DateAttribute = "04/25/2018", and
TimeAttribute = "13:51:40".
Pre:    N.A.
Post:   N.A.
Input:
iElementID                                    - Mandatory. The name of the element
node to be read.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
... (1 to 3 arguments)                        - The data of the element node and
optionally the date and time in string
format. Date and time can only be read
if the date and time attributes are
present in the element node.
Return:
0                                             - Success
<> 0                                          - Failure
```

## Chapter 33 Public Interfaces for Project

## Public Interfaces for Project

The following functions are available: Project.Activate Project.Copy Project.GetCostRateTask Project.Start360 Project.StartCopy Project.StartMultiMain Project.UpdateStatus Project.UpdateWorkAuthorizationStatus
