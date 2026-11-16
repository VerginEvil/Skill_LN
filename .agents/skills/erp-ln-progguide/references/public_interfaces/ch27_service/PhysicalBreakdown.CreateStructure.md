# PhysicalBreakdown.CreateStructure

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PhysicalBreakdown
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1368-1371

```baan
DLL:   tsextcfgapi
This function is available from 2025.05 (KB3567711).
Syntax: long PhysicalBreakdown.CreateStructure(
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function creates a Physical Breakdown Structure.
It offers the same functionality as session Create Physical
Breakdown Structure (tscfg2210m000).
The Help of this session can be used as reference.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions
should either have been aborted or committed).
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
Source
domain  tscfg2210.src   item.breakdown
Selects the source of the new physical breakdown.
Allowed values are:
tscfg2210.src.item.breakdown
tscfg2210.src.as.built
tscfg2210.src.bom
UseDeliveries
domain  tcyesno         no
Use this option to create a physical breakdown from
Sales (after sales). The end item (of the sales order)
P-BOM is copied to a physical breakdown.
If UseDeliveries is Yes, the following options are
applicable:
FromInstallationGroup
ToInstallationGroup
FromCreationTime
ToCreationTime
FromItem
ToItem
FromSerialNumber
ToSerialNumber
SkipParents
domain  tcyesno         yes
The creation of the new physical breakdown
relations between the existing parent serialized
items and the child items that are part of an
As-built Structure, is skipped.
Target
domain  tscfg2210.link  new.breakdown
Determines the target of the created Physical Breakdown
Structure.
Allowed values are:
tscfg2210.link.install.group
tscfg2210.link.breakdown
tscfg2210.link.new.breakdown
LinkToInstallationGroup
domain  tsbsc.clst      ""
The target Installation Group; applicable when Target
is Installation Group.
LinkToItem
domain  tcitem          ""
The target Item; applicable when Target is Breakdown.
LinkToSerialNumber
domain  tcibd.sern      ""
The target Serial Number; applicable when Target is
Breakdown.
FromInstallationGroup
domain  tsbsc.clst      ""
From Installation Group; applicable when UseDeliveries
is Yes.
ToInstallationGroup
domain  tsbsc.clst      ""
To Installation Group; applicable when UseDeliveries
is Yes.
FromCreationTime
domain  tsmdm.utct      0
From Creation Time; applicable when UseDeliveries
is Yes.
ToCreationTime
domain  tsmdm.utct      utc.num()
To Creation Time; applicable when UseDeliveries
is Yes.
FromItem
domain  tcitem          ""
From Item; applicable when UseDeliveries is Yes.
ToItem
domain  tcitem          ""
To Item; applicable when UseDeliveries is Yes.
FromSerialNumber
domain  tcibd.sern      ""
From Serial Number; applicable when UseDeliveries
is Yes.
ToSerialNumber
domain  tcibd.sern      ""
To Serial Number; applicable when UseDeliveries is Yes.
DefaultSerializedItemGroup
domain  tscfg.sigr      ""
The Serialized Item Group to which the serialized items
in the newly-created physical breakdown will belong.
DefaultServiceOffice
domain  tccwoc          ""
The service department that will carry out service
and maintenance activities, on the serialized items in
the newly-generated physical breakdown.
DefaultOwner
domain  tcccom.bpid     ""
The Owner to which the serialized items
in the newly-created physical breakdown will belong.
SerialStatus
domain  tscfg.cfst      actv
The default Serialized Item Status. This field is only
applicable when Configuration Status Usage is checked in
the Configuration Management Parameters.
Allowed values are:
tscfg.cfst.stup
tscfg.cfst.actv
DeliveryTime
domain  tsmdm.utct      0
The date and time that the item is delivered by the
service organization.
InstallationTime
domain  tsmdm.utct      0
The date and time when the new serialized item is
installed.
CheckEffectivity
domain  tcyesno         yes
Check Effectivity
EffectiveTime
domain  tsmdm.utct      utc.num()
The date on which the service item's breakdown terms
are checked for validity.
GenerateDummySerials
domain  tcyesno         no
When GenerateDummySerials is Yes, and the physical
breakdown is created from an Item Breakdown, or a
Bill of Material, the serial numbers generated for the
new serialized items will be marked as dummy serial
numbers. These can be replaced later by their real
serial numbers.
GenerateServiceItemData
domain  tcyesno         yes
When GenerateServiceItemData is Yes, and the physical
breakdown is created from an Item Breakdown, or a
Bill of Material, Service Item Data is generated for
the new serialized items when they are not present yet.
FallBackOnBillOfMaterial
domain  tcyesno         yes
When the physical breakdown is created from an Item
Breakdown, the Bill of Material is used when there is
no Item Breakdown.
CompletedProductionOrdersOnly
domain  tcyesno         no
If CompletedProductionOrdersOnly is Yes, only completed
production orders are processed to create the physical
breakdown structure.
CreateOtherBreakdownWhenBreakdownPresent
domain  tcyesno         no
When there is already a Physical Breakdown present where
the Parent Item/Serial is equal to the LinkToItem /
LinkToSerialNumber, another Breakdown is created
when CreateOtherBreakdownWhenBreakdownPresent is Yes.
Otherwise, nothing is done.
Output  :
ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0                     - No error; however, error messages can
have been set.
<> 0                  - An error occurred
```
