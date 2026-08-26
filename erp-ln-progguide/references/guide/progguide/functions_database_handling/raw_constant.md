# Raw constant
The raw constant specifies a raw string (string of bytes) using hexadecimal digits.

## Syntax
```

<raw constant>
    ::= x'<hex digit>[<hex digit>...]'
      | x"<hex digit>[<hex digit>...]"

<hex digit>
    ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
      | A | B | C | D | E | F
      | a | b | c | d | e | f
```

## Semantics
The type of a raw constant is *raw*.
If the number of hexadecimal digits in the raw constant is odd, then it is effectively right-padded with a 0-digit.
The value of the raw constant is a raw string of which the length is half of the number of hexadecimal digits in the raw constant. The first two hexadecimal digits in the raw constant define the value of the first byte of the raw string. The two hexadecimal digits are interpreted as a hexadecimal number. The next two hexadecimal digits define the value of the second byte. And so on.

## Examples
The following raw constant represents a string of three bytes: the first byte has value 1 (hex 01), the second byte has value 0 (hex 00) and the third byte has value 171 (hex ab).
```

x'0100ab'
```
The following raw constant represents a string of 4 bytes.
```

x'CafeBabe'
```
The following raw constant represents a string of 2 bytes. The first byte has value 171 (hex ab). The second byte has value 192 (hex c0).
```

x'abc'
```
The following comparison is true, because x'abc' is equivalent to x'abc0'.
```

x'abc' & x'def' = x'abc0def0'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
