# Row value constructor
The row value constructor constructs a row value from a value or a list of values.

## Syntax
```

<row value constructor>
    ::= <value expression>
      | { <value expression> [ , <value expression> ]... }
```

## Examples
```

3.14
```
```

{ salary * 2.20371 }
```
```

{ 'Hello ' & 'World!' }
```
```

{ 'tt', 'adv', '101' }
```
```

{ firstnme, lastname }
```
```

{ AVG( salary ), AVG( bonus ) }
```
```

dbtst120._index1
```
```

dbtst120.phoneno
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
