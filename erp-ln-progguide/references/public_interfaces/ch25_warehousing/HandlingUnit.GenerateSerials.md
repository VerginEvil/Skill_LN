# HandlingUnit.GenerateSerials

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1048-1049

```baan
DLL:   whextwmdapi
This function is available from 2022.01 (KB2212523).
Syntax: long HandlingUnit.GenerateSerials(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will generate serials for the handling
unit.
Generating serials for the handling unit is allowed when:
- iHandlingUnit has status Inactive, Open or Receipt Open.
- iHandlingUnit contains serialized item(s).
- iHandlingUnit does not contain serials.
- iHandlingUnit with a status Receipt Open is not in transit.
If item is serialized NOT IN inventory, generated serials always
will be stored in the entity Handling Unit Stock Point Details
(table whwmd536) of the bottom level Handling Units.
Example 1:
Handling Unit HU1 contains 3 pieces of item.
Item is serialized not in inventory.
Serials SER1, SER2 and SER3 are generated.
---------------------------------------------------------------
| HU stock point details   |    Receipt Line
| (whwmd536)               |    Stock Point Details (whinh320)
---------------------------------------------------------------
| HU1   SER1    1 pcs      |    SER1    1 pcs
| HU1   SER2    1 pcs      |    SER2    1 pcs
| HU1   SER3    1 pcs      |    SER3    1 pcs
If item is serialized IN inventory and handling unit quantity is
greater than 1.0 and no package definition is
defined or handling unit template does not allow multiple stock
points (field Allow Multi Stock Points in the table whwmd460
is on NO), extra handling units can be generated to store serial
numbers.
Example 2:
Handling Unit HU1 contains 3 pieces of item, no package
definition.
Item is serialized in inventory.
Serials SER1, SER2 and SER3 are generated.
Child handling units HU11, HU12 and HU13 are generated and
linked to HU1
---------------------------------------------------------------
| HU stock point details   |    Receipt Line
| (whwmd536)               |    Stock Point Details (whinh320)
---------------------------------------------------------------
| HU11  SER1    1 pcs      |    SER1    1 pcs
| HU12  SER2    1 pcs      |    SER2    1 pcs
| HU13  SER3    1 pcs      |    SER3    1 pcs
If item is serialized IN inventory and handling unit quantity is
greater than 1.0, package definition is defined and handling
unit template allows multiple stock points (field Allow Multi
Stock Points in the table whwmd460 is on Yes), generated serials
will be stored in the entity Handling Unit Stock Point Details
(table whwmd536) of the bottom level Handling Units.
Example 3:
Handling Unit HU1 contains 3 pieces of item.
Package definition is known and handling unit template allows
multiple stock points,
Item is serialized in inventory.
Serials SER1, SER2 and SER3 are generated.
---------------------------------------------------------------
| HU stock point details   |    Receipt Line
| (whwmd536)               |    Stock Point Details (whinh320)
---------------------------------------------------------------
| HU1   SER1    1 pcs      |    SER1    1 pcs
| HU1   SER2    1 pcs      |    SER2    1 pcs
| HU1   SER3    1 pcs      |    SER3    1 pcs
When handling unit has status Receipt Open, all generated
serials will be also stored in the table Receipt Line Stock
Point Details (whinh320).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit   - for this handling unit the serial numbers will
be generated (Mandatory)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Serials are generated and linked to iHandlingUnit.
<> 0    - Error
```
