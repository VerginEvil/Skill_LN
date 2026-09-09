# Column reference
The column reference references a column.

## Syntax
```

<column reference>
    ::= <table name>.<column name>
      | <correlation name>.<column name>
      | <column name>

<table name>
    ::= !! a valid table name

<column name>
    ::= !! a valid column name
      | "<array column name>(<unsigned integer>)"

<array column name>
    ::= !! a valid array column name

<unsigned integer>
    ::= <integer constant>

<correlation name>
    ::= <identifier>
```

## Syntactical restrictions
The *<**unsigned integer**>* shall not start with a minus sign ('–') and the value shall be at least 1 and at most the depth of the referenced array column.

## Semantics
The data type of the column reference is the data type of the column that it references. The following table shows the correspondence between database types and SQL types.
| | |
|---|---|
| Database type | SQL type |
| char int long enum bitset mail text | integer |
| float double | real |
| date | date |
| time (UTC) | timestamp |
| string multibyte string | string |
| raw | raw |

## Examples
```

dbtst120.bonus
```
```

employees.lastname
```
```

salary
```
```

employees."phoneno(1)"
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
