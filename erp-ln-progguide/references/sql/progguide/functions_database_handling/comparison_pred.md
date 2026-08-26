# Comparison predicate
The comparison predicate compares two row value constructors.

## Syntax
```

<comparison predicate>
    ::= Row value constructor <comparison operator> Row value constructor

<comparison operator>
    ::= < | <= | = | >= | > | <> | != | #< | #<= | #>= | #>
```

## Syntactical restrictions
If one of the *<row value constructor>s* contains a reference to an array column then the comparison operator shall be one of =, <> or !=.

## Semantics
In general, evaluation of a comparison predicate can be quite complicated. This section explains the semantics of the more complicated predicates in terms of the [Simplest comparison predicate](simplest_comparison_predicate.md).
The following equivalence rules allow a (general) predicate to be rewritten into simpler predicates.

## Equivalence rules
The following rules apply to comparison predicates of which the two row value constructors have a different number of value expressions. It states that the longer row value constructor can be truncated to the length of the shorter row value constructor.
```

(1)   { A } <op> { B, ... }  <=>  { A } <op> { B }
      { A, ... } <op> { B }  <=>  { A } <op> { B }
```
The following rule states that comparing two row value constructors that contain exactly one value expression, is equivalent to comparing the two value expressions.
```

(2)   { A } <op> { B }  <=>  A <op> B
```
The following rule defines the semantics of the = operator.
```

(3)   { A, A2, ... } = { B, B2, ... }
        <=>  A = B AND { A2, ... } = { B2, ... }
```
The following rule defines the semantics of the <> and != operator.
```

(4)   { A, A2, ... } <> { B, B2, ... }
        <=>  A <> B  OR  ( { A2, ... } <> { B2, ... } )
```
The following rules define the semantics of the <, <=, > and >= operator.
```

(5)   { A, A2, ... } <[=] { B, B2, ... }
        <=>  A < B  OR  ( A = B AND { A2, ... } <[=] { B2, ... } )
    { A, A2, ... } >[=] { B, B2, ... }
        <=>  A > B  OR  ( A = B AND { A2, ... } >[=] { B2, ... } )
```
The following rule defines the semantics of the #<, #<=, #> and #>= operator.
```

(6a)  { A } #<op> { B }  <=>  A <op> B
(6b)  { A, A2, ... } #<op> { B, B2, ... }
            <=>  A <op> B AND { A2, ... } #<op> { B2, ... }
```
*Example 1*:
```

{ salary, bonus } > { 20000 }
    => (rule 1)
{ salary } > { 20000 }
    => (rule 2)
salary > 20000
```
*Example 2*:
```

{ salary, bonus, sex } #> { 20000, 1000 )
    => (rule 6b)
salary > 20000 AND { bonus, sex } #> { 1000 }
    => (rule 1)
salary > 20000 AND { bonus } #> { 1000 }
    => (rule 6a)
salary > 20000 AND bonus > 1000
```

## Examples
The following comparison predicate evaluates to True if *firstnme* equals 'CHRISTINE', possibly padded with spaces. If *firstnme* is NULL, then it evaluates to Unknown. Otherwise it evaluates to False.
```

firstnme = 'CHRISTINE'
```
The following comparison predicate evaluates to True if both *salary* is larger than 20000 and *bonus* is larger than 1000. If *salary* is NULL or *bonus* is NULL then it evaluates to Unknown or False.
```

{ salary, bonus } #> { 20000, 1000 }
```
This predicate is equivalent with:
```

salary > 20000  AND  bonus > 1000
```
The following comparison predicate evaluates to True if *salary* is larger than 20000. If *salary* is less than 20000 it evaluates to False. If *salary* is NULL then it evaluates to Unknown. If *salary* equals 20000 then the expression " *bonus* > 1000" determines the outcome.
```

{ salary, bonus } > { 20000, 1000 }
```
This predicate is equivalent with:
```

salary > 20000  OR  ( salary = 20000 AND bonus > 1000 )
```
The following comparison predicate evaluates to True if *salary* is larger than 20000. If *salary* is NULL then it evaluates to Unknown. Otherwise it evaluates to False. Note that *bonus* is not used in the evaluation.
```

{ salary, bonus } > 20000
```
This predicate is equivalent with:
```

salary > 20000
```
The following comparison predicate evaluates to True if *salary* is larger than or equal to the maximum salary of any employee.
```

{ salary } >= ( select max( salary ) from dbtst120 )
```
The following comparison demonstrates the use of a scalar subquery in a comparison.
```

{ lastname, firstnme } = { (select lastname from dbtst120 where empno = 10), 'CHRISTINE' }
```

## Related topics
- [Simplest comparison predicate](simplest_comparison_predicate.md)
- [Infor Enterprise Server SQL](baan_sql.md)
