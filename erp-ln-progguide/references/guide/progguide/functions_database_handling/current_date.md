# CURRENT_DATE
The function CURRENT_DATE specifies the current date.

## Syntax
```

<current date>
    ::= CURRENT_DATE
```

## Semantics
The data type of CURRENT_DATE is *date*. The value of CURRENT_DATE is the date on which the SQL statement is executed. Multiple executions of the same SQL statement may yield different values for the CURRENT_DATE functions contained in the statement. All occurrences of CURRENT_DATE within a SQL statement are effectively evaluated simultaneously.

## Examples
```

CURRENT_DATE
```

## Related topics
- [CURRENT_TIMESTAMP](current_timestamp.md)

- [Infor Enterprise Server SQL](baan_sql.md)
