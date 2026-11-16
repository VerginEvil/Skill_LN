# SQL reserved words
This section lists the reserved words of the Infor Enterprise Server SQL language.

## Reserved words
```

 ALIKE ALL AND ARRAY AS ASC AVG
 BETWEEN BOTH BUFFER BY
 CASE CAST CHAR CHARACTER CLEAR CLEARUNREF COALESCE CONVERT_TZ COUNT CROSS CURRENT_DATE CURRENT_TIMESTAMP
 DATE DATE.NUM DATE.TO.NUM DAY DELETE DESC DISTINCT
 ELSE EMPTY END ENUM_DESCRIPTION ESCAPE EXISTS EXTRACT
 FALSE FETCHING FIRST FIXCTL FOR FROM FULL
 GROUP
 HAVING HINT HINTS HOUR
 IN INDEX INNER INRANGE INT INTEGER INTERVAL IS
 JOIN
 LAST LEADING LEFT LIKE LOWER
 MAX MIN MINUTE MONTH
 NO NOT NULL
 ON OR ORDER ORDERED OUTER
 PATH PREPARED
 RAW REAL REFERS REPEAT RETRY RIGHT ROW ROWS
 SECOND SELECT SET SETUNREF SKIP SIZE STRING SUBHINT SUBSTRING SUM
 TEXT_CONTENT THEN TIMESTAMP TO TRAILING TRIM TRUE
 UNION UNREF UPDATE UPPER USE
 VARCHAR
 WHEN WHERE WITH
 YEAR
```

## Usage notes
Reserved words can be used as names of parameters. The following example contains the keyword SELECT as a parameter name, but is nonetheless legal.
```

select *
from dbtst120
where empno = :select
```
Reserved words can be used if they are double-quoted. The following example contains the keyword WHERE as an alias name.
```

select location as "WHERE"
from dbtst100
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
