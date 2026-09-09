# Replace the invalid characters

## Syntax:
`function long xmlReplaceInvalidCharacters( ref string inputstring, string replacementCharacter(1) )`

## Description
This function replaces each character that is not allowed in an XML document with the specified replacement character. The replacement character must be a single-byte ASCII character in the range from #20 (ASCII space) to #7e (ASCII tilde).
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
| `ref string` | `inputstring` |  The characters in the TSS-encoded *inputstring* are checked for their validity in an XML document. Each character not allowed in an XML document is replaced with the specified replacement character. Upon success, the result is copied back into the *inputstring* argument.  |
| `string` | `replacementCharacter(1)` |  The replacement character to be used to replace the invalid characters in the *inputstring*.  |

## Return values
| | |
|---|---|
| > 0 | Success; the number of invalid characters that were replaced. |
| 0 | Success; all characters in the TSS-encoded *inputstring* are allowed in an XML document, so no replacement was done. |
| -1 | Error; the data in the *inputstring* could not be recognized as a correctly TSS-encoded sequence of characters; no replacement was done. |
| -2 | Error; an invalid replacement character is specified; no replacement was done. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1620.
Note  This function is meant to be applied to a correctly encoded TSS string. The function recognizes the characters that are not allowed in an XML document and replaces them with the supplied replacement character.
The function does not fully check the correct encoding. Incorrect TSS encoding (resulting in return value -1) is only detected in the following cases.

- Invalid TSS single-byte value 0x9C, 0x9D, 0x9E or 0x9F.

- Corrupt TSS multibyte sequence: lead-byte value 0x9B followed by less than three non-0 trail bytes.

Availability  On BaanIVc this function is available from TIV 262. On Infor Enterprise Server it is available from TIV 1620.

## Related topics
- [Verify the used characters](contains_valid_characters_only.md)

- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
