# Inventory.CheckAndRepair

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 934-936

```baan
DLL:   whextwmdapi
This function is available from     2026.03 (KB3647801  ).
Syntax: long Inventory.CheckAndRepair(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  whloca           iCorrectionLocation,
domain  tcclot           iCorrectionLot,
domain  tccprj           iCorrectionProject,
domain  tcpdm.cspa       iCorrectionElement,
domain  tcpdm.cact       iCorrectionActivity,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function performs the logic to evaluate the inventory
levels for the given ranges. When discrepancies are found,
it reports these discrepancies and will correct these if the
UpdateMode in the iProcessingOptionSet is set to Update.
Pre:    N.A.
Post:   N.A.
Input:  iItem                   The item for which inventory to be
rebuild. Optional.
iWarehouse              The warehouse whose inventory is to be
rebuild. Optional.
iCorrectionLocation     A location where the difference
in quantity to be stored.
Mandatory.
iCorrectionLot          A lot where the difference in quantity
to be stored.
Mandatory if lot control is in use.
iCorrectionProject      An existing project where the difference
in quantity to be stored.
Mandatory if Project functionality is
implemented.
iCorrectionElement      An existing element which is linked to
the existing correction project.
Mandatory if Project elements are
implemented.
iCorrectionActivity     An existing activity which is linked to
the existing correction project.
Mandatory if Projects activities are
implemented.
iDevice                 Optional, if empty, the reports will not
be printed.
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iItem is filled then the following options
of the iProcessingOptionSet will be ignored:
-                       selection range fields (Item From/To)
-                       ItemArray
Rebuilding will then be performed for the given iItem.
In case option ItemArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
Rebuilding will be performed for the items in the array.
In case iWarehouse is filled then the following options
of the iProcessingOptionSet will be ignored:
-                       selection range fields (Warehouse From/To)
Processing Options have a direct relationship with the form fields
on session Rebuild Check and Repair Inventory (whwmd6290m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
CorrectBasedOnReceipts          domain tcyesno          tcyesno.yes
AllowAdjustmentOrders           domain tcyesno          tcyesno.no
Employee                        domain tcemno           Minimum Value
AdjustmentReason                domain tccdis           Minimum Value
PrintOnlyDifferences            domain tcyesno          tcyesno.yes
PrintInventoryStructure         domain tcyesno          tcyesno.yes
PrintBasicReport                domain tcyesno          tcyesno.no
SuppressZeroInventory           domain tcyesno          tcyesno.yes
UpdateMode                      domain whsmup           whsmup.simulate
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
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
