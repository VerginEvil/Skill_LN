# WITH RETRY clause
The WITH RETRY clause offers a facility to retry only a part of the table that is specified by a SELECT statement after a jump to a [db.retry.point()](../functions_db_operations/db.retry.point.md). It can only be used in combination with the [ORDER BY clause](order_by.md).

## Syntax
```

<with retry clause>
    ::= WITH RETRY [ REPEAT LAST ROW ]
```

## Examples
The following example is a Baan 3GL program that demonstrates the use of the WITH RETRY clause.
```

    table tdbtst120

    function main()
    {
        long edlev
        string name(20)

1)      db.retry.point()

2)      SELECT edlevel:edlev, firstnme:name
        FROM dbtst120 FOR UPDATE
        ORDER BY edlevel, firstnme DESC
        WITH RETRY
        SELECTDO
            message("Fetched edlevel = %d, firstnme = '%s'", edlev, name )
3)          IF ( name = "THEODORE" OR name = "SYBIL" )
            THEN
4)              commit.transaction()
5)              db.insert( tdbtst120, db.retry )  | Will fail, EDUPL
            ENDIF
        SELECTEOS
6)          commit.transaction()
        ENDSELECT
    }
```
The following table shows the result of the SELECT statement at line 2.
```

    edlevel    firstnme
    ---------- --------------------
1)  12         MAUDE
2)  12         JOHN
3)  14         WING
4)  14         THEODORE
5)  14         SEAN
6)  14         PHILIP
7)  14         JAMES
8)  15         MARIA
9)  15         DANIEL
10) 16         SYBIL
11) 16         RAMLAL
    ...        ...
```
The execution of the program is as follows:
Rows 1, 2, 3 and 4 are fetched. Then a commit.transaction() (line 4) is performed and the current values of the columns in the ORDER BY clause ( 14, "THEODORE" ) are saved. An insert that will fail is buffered (line 5).
Next, rows 5, 6, 7, 8, 9 and 10 are fetched. The commit.transaction() (line 4) fails, because flushing the buffered insert fails. This results in a jump to the db.retry.point() (line 1).
The SELECT statement is executed from the saved retry values ( 14, "THEODORE" ). The rows 5, 6, 7, 8, 9 and 10 are fetched again. The commit.transaction() now succeeds and the current values ( 16, "SYBIL" ) are saved. An insert that will fail is buffered (line 5).
All remaining rows are fetched. The commit.transaction() in the SELECTEOS section (line 6) fails because flushing the buffered insert fails. This results in a jump to the db.retry.point() (line 1).
The SELECT statement is executed from the saved retry values ( 16, "SYBIL" ). The row 11, 12, ... are fetched again. The commit.transaction() at line 6 now succeeds.

## Semantics
If a SELECT statement contains a WITH RETRY clause, then a commit.transaction() call will save the retry values. The retry values are the values of the columns in the ORDER BY clause at the time of the commit.transaction(). If a jump to the db.retry.point() occurs then the statement is retried from the saved retry values. To achieve this a "retry clause" is added to the WHERE clause of the SELECT statement and the saved retry values are bound to the parameters of the retry clause.
If the ORDER BY clause is as follows
```

ORDER BY c1, c2, c3 WITH RETRY
```
Then the following retry clause is generated
```

{ c1, c2, c3 } > { :v1, :v2, :v3 }
```
If the ORDER BY clause is as follows.
```

ORDER BY c1, c2, c3 WITH RETRY REPEAT LAST ROWS
```
Then the following retry clause is generated
```

{ c1, c2, c3 } >= { :v1, :v2, :v3 }
```
If the ORDER BY clause is as follows.
```

ORDER BY c1, c2 DESC WITH RETRY
```
Then the following retry clause is generated
```

c1 > :v1 OR ( c1 = :v1 AND c2 < :v2 )
```

## Related topics
- [WHERE clause](where.md)
- [ORDER BY clause](order_by.md)
- [Retry points](retry_points.md)
- [Hints for using db.retry.point](hints_for_using_db.retry.point.md)
- [Infor Enterprise Server SQL](baan_sql.md)
