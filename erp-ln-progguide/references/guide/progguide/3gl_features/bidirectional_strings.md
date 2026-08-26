# Bidirectional strings
Bidirectional functionality is necessary to support languages that read and write from right to left- for example, Arabic and Hebrew. Bidirectional input is supported only on fields of type [Multibyte strings](multibyte_strings.md). A string is bidirectional when it contains at least one bidirectional character. You can check whether a string includes bidirectional characters by calling [mb.hasbidi()](../functions_multibyte_strings/mb.hasbidi.md). All strings, including bidirectional, are stored in logic order - that is, the first typed character is the leftmost one in the string. This means that all regular string handling functions like [pos()](../functions_string_operations/pos.md), and constructors like the semicolon [;], work correctly.
Special attention must be paid when concatenating or splitting strings. When bidirectional and non-bidirectional strings are concatenated, one part must be reversed.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Variables](variables.md)
