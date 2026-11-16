# PlannedInventoryTransaction.Rebuild

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PlannedInventoryTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 933-935

```baan
DLL:   whextinpapi
This function is available from 2025.04 (KB3568895).
Syntax: long PlannedInventoryTransaction.Rebuild(
domain  tcitem           iItem,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will rebuild the Planned Inventory Transactions
for an Item(s) using the defaults or options as
provided in the iProcessingOptionSet.
Be aware that transaction management is handled within this
function.
Opening/Closing of the reports is also handled within this
function.
Restrictions:
This function cannot be executed from a BDE/BOD context.
Pre:    N.a.
Post:   N.a.
Input:  iItem                   Optional
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iItem is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- ItemArray
Rebuilding will then be performed for the given iItem.
In case option ItemArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
Rebuilding will be performed for the items in the array.
Processing Options have a direct relationship with the form fields
on session Rebuild Planned Inventory Transactions (whinp1200m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Additional Processing Options:
ShowPI - Show Progress Indicator (Yes/No)
Sort - Sort Item Array before processing (Yes/No)
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
ItemGroupFrom                   domain tccitg           Minimum Value
ItemGroupTo                     domain tccitg           Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
ShowPI                          domain tcyesno          tcyesno.no
UpdateMode                      domain tcyesno          tcyesno.no
DetailedReport                  domain tcyesno          tcyesno.yes
IgnoreItemsWithDeliveries       domain tcyesno          tcyesno.no
Sort                            domain tcyesno          tcyesno.no
ItemArray                       domain ttjson           0
JSON Object ItemArray has the following structure:
"ItemArray": [
{
"Item": "         ITEM0001"
},
{
"Item": "         ITEM0003"
}
]
This structure can be created with the following code:
ItemArray = Json.newArray()
Item = Json.newObject()
Json.setString(Item, "Item", "         ITEM0001")
Json.add(ItemArray, Item)
Item = Json.newObject()
Json.setString(Item, "Item", "         ITEM0003")
Json.add(ItemArray, Item)
Output: oDataProcessed          - true:  Data Processed and Printed.
false: Nothing Processed and Printed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
