# Comparable data types in Infor Enterprise Server SQL
Certain constructions within the Infor Enterprise Server SQL language require that the data types of two entities are *comparable*. Such constructions include:
- Comparison predicates
- UNION  The following list shows which data types are comparable. Two data types are comparable if they are on the same line.
- integer, real
- string, multibyte string
- date
- interval days
- datetime (UTC)
- interval seconds
- raw  Note: the types *interval days* and *interval seconds* are not types that can be defined in the Data Dictionary, but that can only occur during evalution of an expression. A value that is the result of the subtraction of two values of type *date* is of type *interval days*. A value that is the result of the subtraction of two values of type *datetime* is of type *interval seconds*.

## Examples
The following constructions are allowed:
The data types *integer* and *real* are comparable.
```

3 < 3.25
```
The data type *integer* is comparable with itself. The type of *dbtst120.sex* is *integer* (in the data dictionary it is DB.ENUM, see section Correspondence of SQL data types with database data types in [SQL data types](sql_data_types.md)).
```

dbtst120.sex > 0
```
In the following example, the data type *integer* ( *dbtst120.sex*), *integer* ( *dbtst120.edlevel*) and *real* ( *dbtst120.salary*) are all comparable.
```

SELECT sex FROM dbtst120
UNION ALL
SELECT edlevel FROM dbtst120
UNION ALL
SELECT salary FROM dbtst120
```
The following constructions are *not* allowed:
The data types *integer* and *string* are not comparable.
```

3 < "Hello world"
```
The data types *date* ( *hiredate*) and *interval days* ( *hiredate - birthdte*) are not comparable.
```

hiredate = hiredate - birthdte
```
The data types *string* ( *dbtst120.firstnme*) and *real* ( *dbtst120.salary*) are not comparable.
```

SELECT firstnme FROM dbtst120
UNION ALL
SELECT salary FROM dbtst120
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
