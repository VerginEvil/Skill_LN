# Assignment Operator
The assignment operator [=] stores a value (the right hand side operand) in a variable (the left hand side operand).

## Examples (general)
```

  LONG      I, J, K(100), L(100)
  STRING    S(50), A, B(10)
  DOUBLE    AMOUNT
  J         = 4
  AMOUNT    = 123.45 * J
  L(20)     = 1001
  S         = "This is an example"
  I         = J            | The contents of J are stored in variable I
  L(2)      = L(20)        | Now L(2) is equal to L(20)
  A         = S(3;1)       | The character 'i' is placed in A
  B(1;2)    = S(6;2)       | The word 'is' is placed in the first two
                           | positions of B
  K         = L            | The entire content of array L is copied to K
```
The left hand side operand of the assignment operator must be a variable or an indexed array variable. The variable must not be declared as CONST.
In general, both operands of the assignment operator must have the same type.
Apart from the general rule above, assignment of a double value to a variable of type long is allowed. In such a case, implicit double to long type conversion is performed.
Apart from the general rule above, assignment of a long value to a variable of type double is allowed. In such a case, implicit long to double type conversion is performed.

## Examples (longs and doubles)
```

   LONG      A
   DOUBLE    C
   A = 3.14       | A is set to 3
   C = A          | C now contains 3.0
   C = 45 / 30    | C now equals 1.0, because this division
                  | results in a long
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Expressions and operators](expressions_and_operators.md)
