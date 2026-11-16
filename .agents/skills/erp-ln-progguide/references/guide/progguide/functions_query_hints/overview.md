# Query hints overview

## Introduction
When a query is submitted to the query processor, it determines an evaluation plan. It creates this plan based on a fixed set of rules. An application developer may have knowledge about the data that the query processor does not have, and therefore he or she may be capable of determining a more efficient execution plan. For this the application developer can add hints to the query.
Hints can be added to each select query, including subqueries. A hint is supplied to a query by adding a hint clause to the query statement. The hint clause is the last clause of the query.
Hints can consist of multiple sets that are enabled or disabled by a condition. When a hint set is enabled, it overwrites all previously specified hints. When a hint set is disabled, it is ignored.
The <hint fixctl set> is available as off bshell TIV 2300.

## Syntax
```

<hint clause>
    ::= hint <hint first set> [ { <hint fixctl set> }... ]

<hint first set>
    ::= <hint list>
      | <hint fixctl set>

<hint fixctl set>
    ::= when fixctl <identifier> is on <hint list>

<hint list>
    ::= <hint>
      | <hint> and <hint list>

<hint>
    ::= use index <nr list> on <table name> [asc|desc]
      | array fetching
      | no array fetching
      | array size <n>
      | all rows
      | first rows
      | buffer <n> rows
      | <string literal>
      | ordered
      | no hints

<nr list>
    ::= <n>
      | <n> ',' <nr_list>

<n> ::= a positive integer

<table name>
    ::= the name of a table or a table name alias.

<string literal>
    ::= string enclosed in double quotes
```

## Examples
Before we go into the semantics of the hints let us first give you some examples to illustrate the syntax.
```

select   tfacr200.*
from     tfacr200
where    _index2 = {"  1001"}
and      {ttyp, ninv, line, tdoc, docn, lino} >= {"",0,0,"",0,0}
order by _index2
as prepared set
hint     use index 2 on tfacr200
         and array fetching
    when fixctl msql_4231 is on no hints and array fetching

select   a.cuno
from     tccom010 a
where    a.cuno in ( select b.cuno
                     from   tfgld106 a, tccom010 b
                     where  a.cuno = b.cuno
                     hint   ordered )
order by cuno
hint     buffer 100 rows
```

## Related topics
- [Hint types](hint_types.md)
