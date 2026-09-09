# Assignment
The syntax to be used for an assignment is as follows.
```

<left hand side> = <right hand side>
```
The <left hand side> specifies a storage location. The <right hand side> is an expression.
The <left hand side> must be a variable or an indexed array variable. The variable must not be declared as CONST.
The <right hand side> is evaluated and the result is stored in the storage location specified by the <left hand side>.
An assignment does not yield a result. An assignment cannot be used as an operand in an expression.

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
As a general rule, both sides of an assignment must have the same type.
Apart from the general rule above, assignment of a double value to a variable of type long is allowed. In such a case, [implicit](type_conversions.md#implicit_type_conversion) [double to long type conversion](type_conversions.md#double_to_long_type_conversion) is performed.
Apart from the general rule above, assignment of a long value to a variable of type double is allowed. In such a case, [implicit](type_conversions.md#implicit_type_conversion) [long to double type conversion](type_conversions.md#long_to_double_type_conversion) is performed.

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
