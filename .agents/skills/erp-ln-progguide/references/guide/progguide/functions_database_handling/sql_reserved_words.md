# SQL reserved words
This section lists the reserved words of the Infor Enterprise Server SQL language.

## Reserved words
```

 ALIKE ALL AND ARRAY AS ASC AVG
 BETWEEN BOTH BUFFER BY
 CASE CAST CLEAR CLEARUNREF COUNT CROSS CURRENT_DATE CURRENT_TIMESTAMP
 DATE DATE.NUM DATE.TO.NUM DELETE DESC DISTINCT
 ELSE EMPTY END ENDCASE ENUM_DESCRIPTION ESCAPE EXISTS
 FALSE FETCHING FIRST FIXCTL FOR FROM FULL
 GROUP
 HAVING HINT HINTS
 IN INDEX INNER INRANGE INTEGER IS
 JOIN
 LAST LEADING LEFT LIKE
 MAX MIN
 NO NOT NULL
 ON OR ORDER ORDERED OUTER
 PATH PREPARED
 RAW REAL REFERS REPEAT RETRY RIGHT ROW ROWS
 SELECT SET SETUNREF SKIP SIZE STRING SUBHINT SUM
 TEXT_CONTENT THEN TIMESTAMP TO TRAILING TRIM TRUE
 UNION UNREF UPDATE USE
 WHEN WHERE WITH
```

## Usage notes
Reserved words can be used as names of parameters. The following example contains the keyword SELECT as a parameter name, but is nonetheless legal.
```

select *
from dbtst120
where empno = :select
```
When using embedded SQL in the Baan 3GL language, you can safely use variable names and function names that are also SQL reserved words. There are only a few exceptions such as the SELECT, UPDATE and DELETE keyword. See also the section on [reserved words in Baan 3GL](../3gl_features/vocabulary.md).
The following program compiles and runs without any complaint.
```

function main()
{
    long where

    where = 10

    select * from dbtst120 where empno = :where
    selectdo
    endselect
}
```
Some care must be taken when using macro definitions in the Baan 3GL language. For example, the following program does not compile because every occurence of the word "select" is replaced with "123".
A general guideline is to never redefine a reserved word.
```

#define select 123

function main()
{
    select * from dbtst120
    selectdo
    endselect
}
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
