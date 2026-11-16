# String constants
A *string constant* (or *string literal*) consists of zero or more displayable single-byte or multibyte characters enclosed by a pair of quotation mark characters ["]. The quotation mark character is also known as the *double quote* character, in order to distinguish it clearly from the apostrophe character ['], which is also known as the *single quote* character.
According to this definition, two adjacent quotation marks represent an empty string. Within a non-empty string literal, a quotation mark is denoted by an escape sequence consisting of two quotation marks.
```

""                          | An empty string.
"Hello"                     | A string literal containing 5 characters.
"He said ""Hello"" to me."  | The escape sequence "" denotes the quotation mark ".
```
A string literal can span more than one line of text. Each new line must start with the circumflex accent character [^], also known as the caret character. This character is used as a continuation symbol. The compiler completely ignores any new line that is immediately followed by a continuation symbol. For string literals this means that the new line and the continuation symbol do not become part of the resulting string value.
```

"Begin
^Middle
^End"     | Multi-line string literal with the same value as "BeginMiddleEnd".
```
[Non-ASCII](../misc/ascii_table.md) characters in the string literal must be encoded in [TSS](../misc/tss.md).
```

"French in French is Français." | String literal with a non-ASCII character 'ç'.
```
Independent of its contents, the type of a string literal is always 'single-byte string'.
```

| Use mb.type() to demonstrate that the type of a string literal is 'single-byte'.
mb.type("♔")         | Result: 0.

| Use mb.cast$() to cast a string literal to type 'multibyte'.
| Use asc() to demonstrate the internal representation of the code points.
asc(mb.cast$("♔"))   | Result: 0x9bbcccd4 (Unicode character U+2654 WHITE CHESS KING).
asc("♔")             | Result: 0x2f7, i.e. 0x9b + 0xbc + 0xcc + 0xd4.
```
There is no escape mechanism to specify characters in string literals by means of the underlying TSS code point values. Use the function [chr$()](../functions_ascii_conversion/chr.md) to construct characters from underlying TSS code point values.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Constants](constants.md)
