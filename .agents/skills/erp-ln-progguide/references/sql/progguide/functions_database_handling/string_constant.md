# String constant
The string constant specifies a (TSS) string value.

## Syntax
```

<string constant>
    ::= '[<non single quoted character>...]'

<non single quoted character>
    ::= !! any (TSS) character except ' and new line
      | ''
```

## Semantics
The type of a string constant is *string*. The value is identical to the character string enclosed in the quotes, with escape quotes removed.

## Examples
*Example 1*:
```

'CHRISTINE'
```
*Example 2*: The following string shows how to use a single quote within a single quoted string.
```

'Not the 9 O''Clock News'
```
*Example 3*: The next string contains a TSS multibyte character. A TSS multibyte character is a four-byte character that starts with a *9b* character (or the decimal equivalent 155). Note that this *9b* is a *single* character. The three characters that follow the *9b* character are taken *literally*. This includes all characters, except the NULL character ('\0') and the new-line character ('\n').
```

'My name is 9b'an'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
