# Multi Table Overview
In order to support editing multiple tables, so called 'secondary tables' are introduced. Secondary tables have a 1:1 relation with the main table. It is not required that there is a database reference from the maintable to the secondary table. However it must be possible to fetch a secondary table record through a 4GL-Engine query extend. Such a fetch must result in zero or one secondary table record. Comparable to the functionality for the main table, the 4GL-Engine will handle transactions / reads etc. for secondary tables. A secondary table requires that a DAL2 implementation is available for that table. It will not be possible to use unmodified 'old' sessions in a MT way. At least some parts of the UI script for the session must change.

## Specific Requirements
The query.extend functionality must be handled very carefully. For secondary tables to work properly, it is necessary to add the complete secondary table record to the session query. Selecting only a part of the fields will result in data loss. (Fields that are not present in the query will be emptied on save). Furthermore, the query.extend REPLACE construction must be kept in mind. In the current design no measures are taken to protect the coupling with secondary tables. A query.extend REPLACE will destroy the coupling to a secondary table (if the developer doesn’t add the secondary tables as previous). Also care must be taken to use the “UNREF CLEAR” construction in the query.extend.where clause. The 4GL-Engine requires that when no reference to a secondary table record is found, the related record buffer is cleared.
When in a DAL script of a secondary table, the corresponding record from the maintable is needed, special care must be taken to prevent that the DAL of the secondary table overwrites the maintable record which is already read (and perhaps modified) by the 4GL-Engine. When a new secondary table record is added within the same transaction with the addition of a new maintable record, the DAL script of the secondary table record cannot yet fetch this maintable record from the database. Both above mentioned issues will be handled using the existing function: dal.get.object(). In the DAL script of the secondary table, the function dal.get.object() must be called to get the required maintable record. The implementation of this function will make sure that when the keyfields match with the keyfields of the current maintable record in the 4GL-Engine, no read from the database is done. Instead the 4GL-Engine maintained record is made actual.
The following standard program features are handled differently for secondary tables.
- The 4GL-Engine will not generate the queries for retrieving and updating the secondary table records. The UI script of the application is responsible for passing the correct queries to the 4GL-Engine through the query.extend functions.
- Maintain references and related reference buffers. The UI script of the application is responsible for filling reference fields referred to by secondary table fields (for instance descriptions).
- Secondary tables without DAL2 scripts are not supported.
- Auto complete in BW mode will not be available for secondary table fields.
- Secondary table fields cannot be shown above the grid as view fields.
- The sort order is always based upon the available main table indices and not on secondary table indices.
- Running MT sessions through application functionserver (AFS) is not supported.
- When a main table record is deleted related secondary table records are not automatically deleted by the 4GL-Engine. The DAL of the main table is responsible for cleanup of related secondary table records.
- Query extend can be used to read additional fields from other tables, but then the filtering on those fields is not possible. Function [sec.add.table()](sec.add.table.md) can be used to enable filtering on the fields from the added tables.    Note  Multi Table functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Example
```

before.program:
        query.extend.select( "bpmdm001.* ", EXTEND_APPEND)
        query.extend.from(   "bpmdm001 ", EXTEND_APPEND)
        query.extend.where(  ":tccom001.emno REFERS TO bpmdm001 " &
                                               "UNREF CLEAR " ,
                             EXTEND_APPEND)
        g.bpmdm001.table.id = sec.add.table("bpmdm001")
```

## Related topics
- [Multi Table synopsis](synopsis.md)
