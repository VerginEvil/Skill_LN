# Item.ChangeOutboundMethod

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 164-165

```baan
DLL:   whextwmdapi
This function is available from 2025.04 (KB3568308).
Syntax: long Item.ChangeOutboundMethod(
domain  tcitem           iItem,
domain  tcobpr           iOldOutboundMethod,
domain  tcobpr           iNewOutboundMethod,
domain  tcinvt.date      iInventoryDate,
domain  tcyesno          iPrintErrors,
domain  tcmcs.str15      iDevice,
domain  tcmcs.str16      iReportName,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will change outbound priority of
items using the defaults or options as provided in the
iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Pre:    N.a.
Post:   N.a.
Input:  iItem                   Optional
iOldOutboundMethod      Optional, ignored if iItem is empty.
1 - LIFO
2 - FIFO
3 - By Location
iNewOutboundMethod      Optional, ignored if iItem is empty.
1 - LIFO
2 - FIFO
3 - By Location
iInventoryDate  Optional, required if iNewOutboundPriority
is FIFO or LIFO.
iDevice         Optional, ignored if iPrintRrrors is No.
iReportName
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iItem is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
Processing Options have a direct relationship with the form fields
on session Change Outbound Method (whwmd3202m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
ItemGroupFrom                   domain tccitg           Minimum Value
ItemGroupTo                     domain tccitg           Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
OldOutboundMethod               domain tcobpr           tcobpr.fifo
NewOutboundMethod               domain tcobpr           tcobpr.loca
InventoryDate                   domain tcinvt.date      0
PrintErrorReport                domain tcyesno          tcyesno.no
ReportName                      domain tcmcs.str16      Empty String
JSON Object ItemArray has the following structure:
"ItemArray": [
{
"Item": "Item1",
"OldOutbounMethod": 1
"NewOutbounMethod": 3
},
{
"Item": "Item2",
"OldOutbounMethod": 3
"NewOutbounMethod": 2
}
]
This structure can be created with the following code:
ItemArray = Json.newArray()
Item = Json.newObject()
Json.setString(Item, "Item", "Item1")
Json.setNumber(Item, "oldOutboundMethod", 1)
Json.setNumber(Item, "NewOutboundMethod", 3)
Json.add(ItemArray, Item)
Item = Json.newObject()
Json.setString(Item, "Item", "Item2")
Json.setNumber(Item, "OldOutboundMethod", 3)
Json.setNumber(Item, "NewOutboundMethod", 2)
Json.add(ItemArray, Item)
ReportName only needs to filled for customized reports,
otherwise the standard report is used based on the ReportNumber.
ReportName must start with an "r", e.g. "rwhwmd320201001"
Output: o.data.processed        - true:  Method Changed.
false: Method not changed.
Return: 0: OK, <> 0: Error
```
