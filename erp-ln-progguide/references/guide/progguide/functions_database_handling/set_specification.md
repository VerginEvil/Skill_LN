# SET specification
Infor Enterprise Server SQL supports the following options in relation to sets:
- Maximum set size. With this option you can indicate the maximum number of rows the SELECT statement can produce.
- Prepared set. With this option, the entire set is retrieved before the first row is returned to the application. The set is temporarily stored. This option is useful when a process simultaneously selects and maintains (or deletes or adds) rows of a table. In this case, changes must not be visible in the selected records. The prepared set option forces a consistent read.

## Syntax
```

<set specification>
    ::= AS PREPARED SET
      | AS [PREPARED] SET WITH Integer constant ROWS
```

## Semantics
If the keyword *PREPARED* is specified, then the entire row set is read from the database before the first row is returned to the application.
If the phrase *WITH <integer constant> ROWS* is specified then the containing SELECT statement returns at most *<integer constant>* rows.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
