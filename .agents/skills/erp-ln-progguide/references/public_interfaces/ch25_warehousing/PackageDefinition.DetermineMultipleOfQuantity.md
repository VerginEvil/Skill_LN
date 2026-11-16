# PackageDefinition.DetermineMultipleOfQuantity

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PackageDefinition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1038-1039

```baan
DLL:   whextwmdapi
This function is available from 2020.08 (KB2139414).
Syntax: long PackageDefinition.DetermineMultipleOfQuantity(
domain  whwmd.pkdf       iPackageDefinition,
domain  tcitem           iItem,
ref             boolean          oMultipleOfQuantityFound,
ref     domain  tcqiv1           oMultipleOfQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface determines the multiple of quantity which
is required for shipping the item. Within the handling unit
template the user can define flags called "Full Packages Only"
and "Full Layers Only". When one of these flag is set,
then the package definition requires full packages/layers only,
which impacts the order quantity. The following examples will
reflect what is determined in this function.
EXAMPLE 1:
--------------------------------------------------------------
Node    Pack    Qty     Qty     Stack   Full    Full    Fill
Item    Pack     St     Height  Pack    Layers  Up
Item    Unit            Only    Only    With
--------------------------------------------------------------
1       Pallet  1       100 pcs 0       Yes     No      N.A.
2       Box     10      100 pcs 5       Yes     No      N.A.
oMultipleOfQuantity = 100.0     (Pallet must be full)
--------------------------------------------------------------
EXAMPLE 2:
--------------------------------------------------------------
Node    Pack    Qty     Qty     Stack   Full    Full    Fill
Item    Pack    St      Height  Pack    Layers  Up
Item    Unit            Only    Only    With
--------------------------------------------------------------
1       Pallet  1       100 pcs         No      No      N.A.
2       Box     10      100 pcs         Yes     No      N.A.
oMultipleOfQuantity = 10.0      (Box must be full)
--------------------------------------------------------------
EXAMPLE 3:
--------------------------------------------------------------
Node    Pack    Qty     Qty     Stack   Full    Full    Fill
Item    Pack    St      Height  Pack    Layers  Up
Item    Unit            Only    Only    With
--------------------------------------------------------------
1       Pallet  1       100 pcs 0       No      No      N.A.
2       Box     10      100 pcs 5       No      Yes     FullHUs
oMultipleOfQuantity = 20.0      (Box Layer contains 2 Boxes
of 10 pcs)
--------------------------------------------------------------
EXAMPLE 4:
--------------------------------------------------------------
Node    Pack    Qty     Qty     Stack   Full    Full    Fill
Item    Pack     St     Height  Pack    Layers  Up
Item    Unit            Only    Only    With
--------------------------------------------------------------
1       Pallet  1       100 pcs 0       No      No      N.A.
2       Box     10      100 pcs 5       Yes     Yes     FullHUs
oMultipleOfQuantity = 20.0      (Box Layer contains 2 Boxes
of 10 pcs)
--------------------------------------------------------------
EXAMPLE 5:
--------------------------------------------------------------
Node    Pack    Qty     Qty     Stack   Full    Full    Fill
Item    Pack    St      Height  Pack    Layers  Up
Item    Unit            Only    Only    With
--------------------------------------------------------------
1       Pallet  1       100 pcs 0       No      No      N.A.
2       Box     10      100 pcs 5       No      Yes     EmptyHU.
oMultipleOfQuantity is 0.0, since Empty Handling
Units are used and zero quantities are allowed.
--------------------------------------------------------------
EXAMPLE 6:
--------------------------------------------------------------
Node    Pack    Qty     Qty     Stack   Full    Full    Fill
Item    Pack    St      Height  Pack    Layers  Up
Item    Unit            Only    Only    With
--------------------------------------------------------------
1       Pallet  1       100 pcs 0       No      No      N.A.
2       Box     10      100 pcs 5       Yes     Yes     EmptyHU.
oMultipleOfQuantity = 10.0      (Box must be full)
The oMultipleOfQuantity is always in inventory unit!
The iPackageDefinition and iItem combination must exist in the
entity Package Definitions by Item (whwmd4130m000) and the
Package Definition must be Validated.
When no multiple of quantity is to be used, as there is no full
packages only or full layers only setup for the package
definition, the oMultipleOfQuantity remains zero.
Pre:    N.a.
Post:   N.a.
Input:  iPackageDefinition      - Package Definition (Mandatory)
Package Definition Type should be
Variable, otherwise an error is given
iItem                   - Item (Mandatory)
Output: oMultipleOfQuantityFound - Multiple of quantity is found, for
the given iPackageDefinition and iItem
oMultipleOfQuantity     - Multiple of quantity in inventory
unit. Will only be filled when a
multiple of quantity can be
determined, otherwise zero.
Return: 0: OK, <> 0: Error
```
