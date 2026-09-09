# Comparison predicate
The comparison predicate compares two row value constructors.

## Syntax
```

<comparison predicate>
    ::= <row value constructor> <comparison operator> <row value constructor>

<comparison operator>
    ::= =
      | <>
      | !=
      | <
      | <=
      | >
      | >=
      | #<
      | #<=
      | #>
      | #>=
```

## Syntactical restrictions
If one of the *<**row value constructor**>**s* contains a reference to an array column then the comparison operator shall be one of =, <> or !=.

## Semantics
In general, evaluation of a comparison predicate can be quite complicated. This section explains the semantics of the more complicated predicates in terms of the [simplest comparison predicate](simplest_comparison_predicate.md).
The following equivalence rules allow a (general) predicate to be rewritten into simpler predicates.

## Equivalence rules
(1) The following rules apply to comparison predicates of which the two row value constructors have a different number of value expressions. It states that the longer row value constructor can be truncated to the length of the shorter row value constructor.
```

(1a)  { A } [#]<op> { B, ... }   ⟺   { A } [#]<op> { B }
(1b)  { A, ... } [#]<op> { B }   ⟺   { A } [#]<op> { B }
```
(2) The following rule states that comparing row value constructors that each contain exactly one value expression, is equivalent to comparing the contained value expressions.
```

(2)   { A } [#]<op> { B }   ⟺   A <op> B
```
(3) The following rule defines the semantics of the = operator for row value constructors containing more than one value expression.
In words: two row value constructors compare equal if and only if all pairs of corresponding value expressions compare equal.
```

(3)   { A1, A2, ... } = { B1, B2, ... }   ⟺   { A1 } = { B1 }  AND  { A2, ... } = { B2, ... }
```
(4) The following rule defines the semantics of the <> and != operator for row value constructors containing more than one value expression.
In words: two row value constructors compare different if and only if any pair of corresponding value expressions compares different.
```

(4)   { A1, A2, ... } <> { B1, B2, ... }   ⟺   { A1 } <> { B1 }  OR  ( { A2, ... } <> { B2, ... } )
```
(5) The following rule defines the semantics of the <, <=, > and >= operator for row value constructors that contain more than one value expression.
In words: row values are compared lexicographically in the left to right order of their elements.
```

(5)   { A1, A2, ... } <op>[=] { B1, B2, ... }   ⟺   { A1 } <op> { B1 }  OR  ( { A1 } = { B1 }  AND  { A2, ... } <op>[=] { B2, ... } )
```
Specialized forms of this rule (one for each of the operators <, <=, > and >=) are as follows.
```

(5a)  { A1, A2, ... } <  { B1, B2, ... }   ⟺   { A1 } < { B1 }  OR  ( { A1 } = { B1 }  AND  { A2, ... } <  { B2, ... } )
(5b)  { A1, A2, ... } <= { B1, B2, ... }   ⟺   { A1 } < { B1 }  OR  ( { A1 } = { B1 }  AND  { A2, ... } <= { B2, ... } )
(5c)  { A1, A2, ... } >  { B1, B2, ... }   ⟺   { A1 } > { B1 }  OR  ( { A1 } = { B1 }  AND  { A2, ... } >  { B2, ... } )
(5d)  { A1, A2, ... } >= { B1, B2, ... }   ⟺   { A1 } > { B1 }  OR  ( { A1 } = { B1 }  AND  { A2, ... } >= { B2, ... } )
```
(6) The following rule defines the semantics of the #<, #<=, #> and #>= operator for row value constructors that contain more than one value expression.
In words: comparison of row values according to a certain #-operator yields true if and only if for all pairs of corresponding value expressions comparison according to that operator yields true.
```

(6)   { A1, A2, ... } #<op> { B1, B2, ... }   ⟺   { A1 } #<op> { B1 }  AND  { A2, ... } #<op> { B2, ... }
```
Specialized forms of this rule (one for each of the operators #<, #<=, #> and #>=) are as follows.
```

(6a)  { A1, A2, ... } #<  { B1, B2, ... }   ⟺   { A1 } #<  { B1 }  AND  { A2, ... } #<  { B2, ... }
(6b)  { A1, A2, ... } #<= { B1, B2, ... }   ⟺   { A1 } #<= { B1 }  AND  { A2, ... } #<= { B2, ... }
(6c)  { A1, A2, ... } #>  { B1, B2, ... }   ⟺   { A1 } #>  { B1 }  AND  { A2, ... } #>  { B2, ... }
(6d)  { A1, A2, ... } #>= { B1, B2, ... }   ⟺   { A1 } #>= { B1 }  AND  { A2, ... } #>= { B2, ... }
```
*Example 1*:
```

{ salary, bonus } > { 20000 }
    => (rule 1b)
{ salary } > { 20000 }
    => (rule 2)
salary > 20000
```
*Example 2*:
```

{ salary, bonus, sex } #> { 20000, 1000 )
    => (rule 6c)
{ salary } #> { 20000 } AND { bonus, sex } #> { 1000 }
    => (rule 1b)
{ salary } #> { 20000 } AND { bonus } #> { 1000 }
    => (rule 2, twice)
salary > 20000 AND bonus > 1000
```

## Derived equivalences
The following equivalences can be derived from the equivalence rules.
(7) The <> operator is the inverse of the = operator.
```

(7)   { A, ... } <> { B, ... }   ⟺   NOT ( { A, ... } = { B, ... } )
```
(8) The <= and >= operators are combinations of the < and > operators with the = operator.
```

(8a)  { A, ... } <= { B, ... }   ⟺   { A, ... } < { B, ... }  OR  { A, ... } = { B, ... }
(8b)  { A, ... } >= { B, ... }   ⟺   { A, ... } > { B, ... }  OR  { A, ... } = { B, ... }
```
(9) The > and >= operators can easily be expressed in terms of the < and <= operators.
```

(9a)  { A, ... } >  { B, ... }   ⟺   { B, ... } <  { A, ... }
(9b)  { A, ... } >= { B, ... }   ⟺   { B, ... } <= { A, ... }
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
