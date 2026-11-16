# Identifier
An identifier is a name that consists of a sequence of letters and digits.

## Syntax
```

<identifier>
    ::= <unquoted identifier>
      | <quoted identifier>

<unquoted identifier>
    ::= <letter>[{<letter>|<digit>}...]

<quoted identifier>
    ::= "<non-double-quote character>..."

<non-double-quote character>
    ::= !! Any printable ASCII character, except "
      | ""

<letter>
    ::= a | b | c | d | e | f | g | h | i | j | k | l | m
      | n | o | p | q | r | s | t | u | v | w | x | y | z
      | A | B | C | D | E | F | G | H | I | J | K | L | M
      | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
      | _ | .

<digit>
    ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

## Examples
```

empno

dbtst120.empno

"Description"
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
