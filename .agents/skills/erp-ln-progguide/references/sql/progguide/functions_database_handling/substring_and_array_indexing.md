# Substring and array indexing
The substring function returns a portion of a string argument.
The array indexing function returns an element of an array column.

## Syntax
```

<substring and array indexing>
    ::= <array column reference> <array indexing>
      | <column reference> <substring>
      | <array column reference> <array indexing with substring>
      | <string constant> <substring>
      | <raw constant> <substring>
      | <parameter> <substring>

<array column reference>
    ::= <column reference>

<substring>
    ::= ( <start> [; <length> ] )

<array indexing>
    ::= ( <index> )

<array indexing with substring>
    ::= ( <index>, <start> [; <length> ] )

<start>
    ::= <value expression>

<length>
    ::= <value expression>

<index>
    ::= <value expression>
```
*Note:* This grammar is ambiguous. The expression phoneno(1) can be either the array indexing function or the substring function. The type of the column reference is used to disambiguate the expression. If the column is an array column then the expression must be the array indexing function. Otherwise, it must be the substring function.

## Syntactical restrictions
The type of *<**start**>*, *<**length**>* and *<**index**>* shall be *integer*. The type of *<**parameter**>* shall be *string* or *raw*. The type of *<**column reference**>* shall be *string* or *raw* and may reference an array column. An *<**array column reference**>* shall reference an array column.

## Semantics
The type of the array indexing function is the type of the column reference to which it is applied. For example, if array indexing is applied to an array column of type *string* then the type is *string*. The value of the array indexing function is the value of the array column reference indexed by *<**index**>*.
The type of the substring function is the same as the value expression to which it is applied. The value of the substring function is the string that starts at position *<**start**>* and is *<**length**>* (raw) characters long. If *<**start**>* is greater than the length of the string then the result is the empty string. If the sum of *<**start**>* and *<**length**>* is greater then the length of the string then *<**length**>* is effectively decreased until the sum of *<**start**>* and *<**length**>* equals the length of the string.

## Usage notes
*Note:* It is advised to keep *<**index**>* in the safe range from 1 to the length of the string. If *<**index**>* is outside this range, the behavior is [implementation defined](sql_glossary.md#ImplementationDefined).
*Note:* Each character of a *raw* string takes two characters in the literal representation. The substring operates on the raw string and not on the literal representation. For example, the following is True.
```

x'abcdef'(2;1) = x'cd'  AND  x'abcdef'(3;1) = x'ef'
```

## Examples
The following expression takes the substring starting at position 7 and of length 4 of the string. The result is 'dull'.
```

'Not a dull moment'(7;4)
```
The following expression takes the substring starting at position 7. The result is 'a dull moment'.
```

'Never a dull moment'(7)
```
The following expression takes the substring starting at position 3 and of length 2 of a raw string. The result is the raw string x'beef'.
```

x'deadbeef'(3;2)
```

## Related topics
- [SUBSTRING function](substring_function.md)

- [Infor Enterprise Server SQL](baan_sql.md)
