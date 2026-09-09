# _compnr predicate
The _compnr predicate specifies the actual company number of a table.

## Syntax
```

<compnr predicate>
    ::= <compnr column reference> = <compnr value>

<compnr column reference>
    ::= !! a <column reference> whose column name is _compnr

<compnr value>
    ::= <integer constant>
      | <parameter>
```

## Syntactical restrictions
The value of the integer constant must lie between 0 and 999, all inclusive.
The parameter must be of type *integer*.

## Semantics
The _compnr predicate always evaluates to True.

## Examples
The following _compnr predicate sets the actual company number of table dbtst120 to 812.
```

dbtst120._compnr = 812
```
The following _compnr predicate sets the actual company number of table dbtst120 to whatever value the parameter *current.compnr* has at the time the containing SQL statemtent is executed.
```

dbtst120._compnr = :current.compnr
```

## Related topics
- [FROM clause](from.md)
