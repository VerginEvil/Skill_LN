# Verify the used characters

## Syntax:
`function long xmlContainsValidCharactersOnly( string inputstring )`

## Description
This function verifies whether the supplied string contains valid XML characters only, i.e. only characters that are allowed in an XML document.
According to [XMLSTD], the following Unicode characters are allowed in an XML document:
```

  Char ::=  #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]
```
All other characters are forbidden. There is no possibility to escape them. The forbidden characters are:

- ASCII control characters in the range [#x0-#x1F], except the allowed characters #x9 (Horizontal Tab), #xA (Line Feed), and #xD (Carriage Return);

- Unicode surrogate characters in the range [#xD800-#xDFFF];

- The <not a character> Unicode values #xFFFE and #xFFFF.

## Arguments
| | | |
|---|---|---|
| `string` | `inputstring` |  The characters in the TSS-encoded *inputstring* are checked for their validity in an XML document.  |

## Return values
| | |
|---|---|
| 1 | Success; all characters in the TSS-encoded *inputstring* are allowed in an XML document. |
| 0 | Error; at least one character in the TSS-encoded *inputstring* is not allowed in an XML document or the data in the *inputstring* could not be recognized as a correctly TSS-encoded sequence of characters. |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  This function is meant to be applied to a correctly encoded TSS string. The function simply recognizes the characters that are not allowed in an XML document and returns false upon the first encounter of such a character.
The function does not fully check the correct encoding. Incorrect TSS encoding is only detected in the following cases.

- Invalid TSS single-byte value 0x9C, 0x9D, 0x9E or 0x9F.

- Corrupt TSS multibyte sequence: lead-byte value 0x9B followed by less than three non-0 trail bytes.

## Related topics
- [Replace the invalid characters](replace_invalid_characters.md)

- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
