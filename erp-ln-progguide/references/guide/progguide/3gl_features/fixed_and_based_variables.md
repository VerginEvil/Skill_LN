# Fixed and based variables

## Fixed variables and space-padding
A string variable can be declared as fixed. The intention is that the character count of its value always equals the character limit of the variable. When a string value with a lower character count is assigned to such a string variable, it is space-padded to reach the desired character count. For example:
```

STRING my_string(10) FIXED
my_string = "andrew"   | Variable my_string now does not contain the value "andrew",
                       | but it contains the space-padded value "andrew␣␣␣␣",
                       | where each ␣ represents one space character.
```
The keyword FIXED is applicable to one-dimensional strings only. Strings in arrays are always space-padded; string arrays do not need to be declared with the keyword FIXED.

## Based variables
The BASED mechanism is applicable to strings and to arrays of all possible types. It determines that a variable will be based on the memory of another variable. For based variables, no memory is reserved when they are declared. At runtime they use the same memory as the variable on which they are based. So by using this mechanism, the same section of memory can be accessed via different names.
You use the following construction to base a based variable on a basic variable: `BASE based_variable AT basic_variable`
If the basic_variable is declared as CONST, then also the based_variable must be declared as CONST.
See the [at.base(basic_value [, position, ...], based_variable [, length, ...])](../functions_variables_based/at.base1.md) function and the [at.base(process_id, basic_variable_name [, position, ...], based_variable [, length, ...])](../functions_variables_based/at.base2.md) function for other methods to base a based variable on a basic variable.

## Based string variables
In the case of a string, the based variable is always fixed, i.e. assignments to it trigger space-padding. You must ensure that the based variable always fits in the basic variable on which it is based. So it will be safe to declare the basic variable as FIXED.

## Example
```

STRING       a(10) FIXED
STRING       b(5)  BASED
CONST STRING c(1)  BASED
BASE b AT a(3)        | This indicates that the space occupied
                      | by b is the same as the space for a(3;5)
b(2;3) = "yes"        | a(4;3) now also contains "yes"
a(1;8) = "12345678"   | b now contains "34567"
BASE c AT a(3)
c      = "x"          | ERROR: c is declared as CONST, assignment to it is not allowed

FUNCTION VOID f(CONST STRING d)
{
   BASE b AT d    | ERROR: d is declared as CONST, b cannot be based on it
   BASE c AT d
   c = "y"        | ERROR: c is declared as CONST, assignment to it is not allowed
   a = c          | c can be used to access, but not modify, the value of const argument d
}
```

## Variable length strings and fixed length strings
The following points summarize the rules for variable length strings and fixed length strings:
- Any 1-dimensional string variable not declared as BASED or FIXED is a *variable length string*.
- Any other string variable is a *fixed length string* – that is: any string variable declared as FIXED or BASED, any string array, any substring, and any database table field.
- When a value is assigned to a variable length string, then no space padding is performed; however, notice that a substring of a variable length string is itself a fixed length string.
- When a value is assigned to a fixed length string, then space-padding is performed to the end of the variable.
- When a value is assigned to a substring with an explicitly specified length, then the space-padding is restricted to the end of the substring, and does not extend into the part of the surrounding string *after* the substring.
- When a value is assigned to a substring, then any zero-padding in the surrounding string *before* the substring is replaced by space-padding.    In the following example, each ␣ represents one space character.
```

string my_string(10)

my_string(1)   = "abcde"   | my_string now contains the value "abcde␣␣␣␣␣"
my_string      = "abcde"   | my_string now contains the value "abcde"
my_string(2;3) = "2"       | my_string now contains the value "a2␣␣e"
my_string(7;1) = "7"       | my_string now contains the value "a2␣␣e␣7"
my_string(9)   = "9"       | my_string now contains the value "a2␣␣e␣7␣9␣"
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Variables](variables.md)
- Other methods to base a based variable on a basic variable: [at.base(basic_value [, position, ...], based_variable [, length, ...])](../functions_variables_based/at.base1.md), [at.base(process_id, basic_variable_name [, position, ...], based_variable [, length, ...])](../functions_variables_based/at.base2.md)
