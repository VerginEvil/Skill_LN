# whext.dll0005.picking.mission.handle.after.generate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PickingMission
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2127-2128

```baan
Syntax: long whext.dll0005.picking.mission.handle.after.generate(
domain  whinh.btno       i.runnumber,
domain  tccwar           i.warehouse,
domain  whinh.picm       i.picking.mission,
domain  tcncmp           i.company,
ref             boolean          o.remove.picking.mission )
Usage:        Expl:   This process extension allows to include customer specific
functionality after the process of generating picking
missions. This process extension will be called from Infor LN
standard when the picking mission is generated via session
"Generate Picking List" (whinh4415m000), or when the generation
of picking lists is an automatic order step. For each picking
mission the process extension is executed after generation.
No table fields are current, based on the input arguments the
records must be fetched.
When the process extension is executed, the picking missions are
committed to the database. Any transactions which are required
to the database (inserts, updates, deletes) must be accompanied
with a new transaction (db.retry.point / abort/commit).
Picking missions are removed when o.remove.picking.mission is
set to True or when this function returns a value <> 0.
Pre:    N.a.
Post:   N.a.
Input:  i.runnumber     - The run number for which the picking mission
is created
i.warehouse     - Warehouse
i.picking.mission - Picking Mission which is generated
i.company       - Logistic Company of the outbound advice
Output: o.remove.picking.mission - Indicator if the standard should
remove the picking mission.
Return: 0: Success / <> 0: Error
```
