# company_nr predicate
The company_nr predicate is used to restrict the set of possible values for the company_nr column. In that respect a company_nr predicate is just the same as any other search condition involving an arbitrary column reference.
One aspect in which the company_nr predicate deviates is that when no company_nr predicate is specified, then the set of possible values for the company_nr column is restricted to just one company number: the current company number of the user.

## Syntax
```

<company_nr predicate>
    ::= <company_nr column reference> = <company value>
      | <company_nr column reference> IN <company number set>

<company_nr column reference>
    ::= !! a <column reference> whose column name is company_nr

<company value>
    ::= <company number>
      | <company_nr column reference>
      | <parameter>

<company number set>
    ::= ( <company number> [ { , <company number> }... ] )

<company number>
    ::= <integer constant>
```

## Syntactical restrictions
*I.* The value of the *<**company number**>* must lie between 0 and 999, all inclusive.
*II.* The *<**parameter**>* must be of type *integer*.
*III.* A *<**company_nr predicate**>* shall neither be contained in an [OR condition](or_sc.md) nor be contained in a [NOT condition](not_sc.md).
The following example demonstrates the incorrect use of a *<**company_nr predicate**>* in an [OR condition](or_sc.md).
```

SELECT * FROM dbtst120
WHERE dbtst120.company_nr IN (100,200) OR empno = 10
```
*IV.* A [query specification](query_specification.md) shall contain at most one *<**company number set**>*.
The following example demonstrates the incorrect use of more than one *<**company number set**>* in one [query specification](query_specification.md).
```

SELECT * FROM dbtst120, dbtst100
WHERE dbtst120.company_nr IN (100,200) AND dbtst100.company_nr IN (200,300)
```
*V.* At most one *<**company_nr predicate**>* shall reference any one [table reference](from.md).
The following example demonstrates the incorrect use of more than one *<**company_nr predicate**>* referencing the same [table reference](from.md).
```

SELECT * FROM dbtst120
WHERE company_nr = 100 AND company_nr = 200
```
*VI.* If a company number set of any [table reference](from.md) is restricted with a *<**company_nr predicate**>*, then the company number set of *every*[table reference](from.md) shall be restricted with a *<**company_nr predicate**>*.
The following example demonstrates the incorrect use of more than one *<**company_nr predicate**>* referencing the same [table reference](from.md).
```

SELECT * FROM dbtst120 AS "emps" LEFT JOIN dbtst100 ON workdept = deptno
WHERE "emps".company_nr = 100
```

## Semantics
The company_nr predicate always evaluates to True.

## Examples
The following company_nr predicate restricts the set of possible company numbers of table dbtst120 to the single-element set containing the value 812.
```

dbtst120.company_nr = 812
```
The following company_nr predicate restricts the set of possible company numbers of table dbtst120 to the single-element set containing the value of the parameter *current.compnr* at the time the containing SQL statemtent is executed.
```

dbtst120.company_nr = :current.compnr
```
The following example restricts table dbtst120 ("emps") to company numbers 100 and 200, and because of the join condition on the company_nr column, also restricts table dbtst100 ("depts") to company number 100 and 200. Note that the data of the tables is joined only within a single company number, as requested by the ON condition of the join.
```

SELECT "emps".firstnme, "depts".deptname
FROM dbtst120 AS "emps" LEFT JOIN dbtst100 AS "depts"
        ON workdept = deptno AND "emps".company_nr = "depts".company_nr
WHERE "emps".company_nr IN (100,200)
```

## Related topics
- [FROM clause](from.md)

- [Infor Enterprise Server SQL](baan_sql.md)
