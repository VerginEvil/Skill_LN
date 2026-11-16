# Unicode
Unicode is a unification of all (or at least: almost all) currently available character sets. See the [Unicode Home Page](https://home.unicode.org). In this Programmers Guide, Version 4.0.1 of the Unicode Standard is used, officially referenced as:
The Unicode Consortium. The Unicode Standard, Version 4.0.1, defined by: The Unicode Standard, Version 4.0 (Reading, MA, Addison-Wesley, 2003. ISBN 0-321-18578-1), as amended by Unicode 4.0.1 ( [http://www.unicode.org/versions/Unicode4.0.1/](http://www.unicode.org/versions/Unicode4.0.1/)).
The Unicode Standard is quite elaborate, and not everything of it is relevant in the context of this Programmers Guide. Some topics which certainly are relevant:

- Encoding forms UTF-16 and UTF-8. See also [UTF-16 Encoding](utf16.md) and [UTF-8 Encoding](utf8.md) in this Programmers Guide.

- Encoding schemes UTF-16BE and UTF-16LE See also [UTF-16 Encoding](utf16.md) in this Programmers Guide.

- Canonical Equivalence and Normalization.

- Case Conversion and Caseless Matching.

- Sorting and the Unicode Collation Algorithm (UCA, see [UTS #10](http://www.unicode.org/reports/tr10/tr10-11.html)).

- East Asian Width (see [UAX #11](http://www.unicode.org/reports/tr11/tr11-13.html)).

## Unicode support in Infor Enterprise Server
In Infor Enterprise Server, several aspects of the Unicode Standard are supported.

- Conversion from TSS to UTF-16 or UTF-8. See [uni.export()](../functions_multibyte_strings/uni.export.md) and [utf8.export()](../functions_multibyte_strings/utf8.export.md).

- Conversion from UTF-16 or UTF-8 to TSS. See [uni.import()](../functions_multibyte_strings/uni.import.md) and [utf8.import()](../functions_multibyte_strings/utf8.import.md).

- Embedding of the complete Unicode repertoire in TSS. See [UTF-T Encoding](utft.md).

## Related topics
- [ASCII table (C0 Controls and Basic Latin)](ascii_table.md)

- [UTF-16 Encoding](utf16.md)

- [UTF-8 Encoding](utf8.md)

- [UTF-T Encoding](utft.md)
