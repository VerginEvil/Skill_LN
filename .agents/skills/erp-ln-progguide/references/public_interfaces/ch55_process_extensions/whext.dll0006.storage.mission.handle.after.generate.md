# whext.dll0006.storage.mission.handle.after.generate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StorageMission
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2285-2286

```baan
Syntax: long whext.dll0006.storage.mission.handle.after.generate(
domain  whinh.btno       i.runnumber,
domain  tccwar           i.warehouse,
domain  whinh.picm       i.storage.mission,
domain  tcncmp           i.company,
ref             boolean          o.remove.storage.mission )
Usage:        Expl:   This process extension allows to include customer specific
functionality after the process of generating storage missions.
This process extension will be called from Infor LN
standard when the storage mission is generated via session
"Generate storage List" (whinh3415m000), or when the generation
of storage lists is an automatic order step. For each storage
mission the process extension is executed after generation.
No table fields are current, based on the input arguments the
records must be fetched.
When the process extension is executed, the storage missions are
committed to the database. Any transactions which are required
to the database (inserts, updates, deletes) must be accompanied
with a new transaction (db.retry.point / abort/commit).
Storage missions are removed when o.remove.storage.mission is
set to True or when this function returns a value <> 0.
Pre:    N.a.
Post:   N.a.
Input:  i.runnumber             - The run number for which the storage
mission is created
i.warehouse             - Warehouse
i.storage.mission       - Storage Mission which is generated
i.company               - Logistic Company of the inbound advice
Output: o.remove.storage.mission - Indicator if the standard should
remove the storage mission.
Return: 0: Success / <> 0: Error
```
