# CURRENT_TIMESTAMP
The function CURRENT_TIMESTAMP specifies the current timestamp.

## Syntax
```

<current timestamp>
    ::= CURRENT_TIMESTAMP
```

## Semantics
The data type of CURRENT_TIMESTAMP is *timestamp*. The value of CURRENT_TIMESTAMP is the timestamp on which the SQL statement is executed (in UTC time). Multiple executions of the same SQL statement may yield different values for the CURRENT_TIMESTAMP functions contained in the statement. All occurrences of CURRENT_TIMESTAMP within a SQL statement are effectively evaluated simultaneously.

## Examples
```

CURRENT_TIMESTAMP
```

## Related topics
- [CURRENT_DATE](current_date.md)

- [Infor Enterprise Server SQL](baan_sql.md)
