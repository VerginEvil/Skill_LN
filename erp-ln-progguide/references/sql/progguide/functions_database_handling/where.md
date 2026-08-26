# WHERE clause
The WHERE clause specifies a search condition that acts as a filter by evaluating the search condition for each row of the table specified by the FROM clause. It rejects each row for which the search condition evaluates to False or Unknown.

## Syntax
```

<where clause>
    ::= WHERE Search condition
```

## Semantics
The columns of the result table have the same names and descriptors as the table the WHERE clause operates on.
A row is in the result table if and only if the *<search condition>* evaluates to True for that row.

## Related topics
- [FROM clause](from.md)
- [Search condition](search_condition.md)
- [Infor Enterprise Server SQL](baan_sql.md)
