# Relational operators
The relational operations are:
| | | |
|---|---|---|
| Operator symbol | Operator keyword | Description |
| < | LT | less than |
| = | EQ | equal to |
| > | GT | greater than |
| <= | LE | less than or equal to (at most) |
| >= | GE | greater than or equal to (at least) |
| <> | NE | not equal to (different from) |
Relational operators compare two operands. If the condition (equal, greater than, less than, and so on) is satisfied, the result becomes TRUE. Otherwise, it becomes FALSE.
Relational operators can be performed on values of every available type, but the operands of the relational operator must be of the same type.
If one operand of the relational operator is of type long and the other of type double, then implicit long to double type conversion is performed on the long operand and comparison of two double values is done.
If both operands of the relational operator are long values, then the comparison is done using signed BitCountOfLong-bit arithmetic.
If both operands of the relational operator are strings, then the string values are compared on the basis of the following rules. The intention of these string comparison rules is to mimic the ordering used in the database.
- The comparison is made on the basis of the weights of the string characters, starting at the leftmost character of each string.
- If two characters are not equal, the string with the lower character weight is considered to be smaller and the comparison is terminated.
- If both strings contain the same number of characters and the characters agree in all cases, then the strings are considered to be equal. If one string is shorter than the other, and the corresponding characters are equal, then the shorter string is considered to be smaller than the longer string.
- Character weights are assigned according to the binary encoding of the characters. For [ASCII](../misc/ascii_table.md) characters, the byte encoding of each character is used. For non-ASCII [TSS](../misc/tss.md) characters, the external, native byte encoding of each character is used.   In Unicode mode, the string comparison is not made on the basis of the weights of the string characters. Instead, the Unicode Collation Algorithm is used. This is a multi-level comparison algorithm, which roughly works as follows. At the first level the strings are compared while ignoring accents (e.g. all five characters a, á, à, ä, and â compare equal), case differences (e.g. characters A and a compare equal) and punctuation (characters like . , : ; " ' ! ? are left out from the comparison). When strings compare equal at the first level, the comparison is extended to higher levels, each next level ignoring less of the available information in the strings.
As an example, consider the six strings "yes", "YES", "Yes", "no", "NO", "No" and order them on the basis of the binary value of the string bytes. In the used [ASCII](../misc/ascii_table.md) encoding, lower case letters have higher byte values than upper case letters, so the strings are ordered as follows.
- NO
- No
- YES
- Yes
- no
- yes  When ordering the same six strings according to the Unicode Collation Algorithm, at the first level the strings "no", "NO", "No" compare equal and are sorted before the strings "yes", "YES", "Yes" (which also compare equal). Then, at a higher level, lower case letters are sorted before upper case letters, so the resulting order is as follows.
- no
- No
- NO
- yes
- Yes
- YES  The used Unicode Collation Algorithm may consider two strings to be equal, even when they do not represent the same sequence of characters. This is the case when the actual differences between the strings are ignored at all levels of the comparison algorithm. For example, differences between various white space characters may be ignored and some control characters may be completely ignored.
In order to avoid problems when the relational operators are meant to test full string equality instead of determining the sorting order, the following exception is made. Relational operators = and <> with single-byte string operands do not use the Unicode Collation Algorithm, but instead use a straightforward byte-by-byte comparison.
Bshell function [mb.cast.to.str$()](../functions_multibyte_strings/mb.cast.to.str.md) can be used to convert multibyte string values to single-byte string values before applying the = or <> operator, in order to enforce the straightforward byte-by-byte comparison described above
Bshell function [mb.cast$()](../functions_multibyte_strings/mb.cast.md) can be used to convert at least one of the string operands of the = or <> operator to a multibyte string value in order to enforce the comparison according to the Unicode Collation Algorithm.
Notice that for single-byte string operands which are not binary equal but which are considered equal according to the Unicode Collation Algorithm, all three operators =, < and > evaluate to FALSE and all three operators <>, <= and >= evaluate to TRUE.
When the intention is to determine the relative position (i.e. less than, equal, or greater than) of two string values in a well-defined but further irrelevant ordering, then functions like [str.compare()](../functions_string_operations/str.compare.md) and [str.equals()](../functions_string_operations/str.equals.md) may be used.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Expressions and operators](expressions_and_operators.md)
- Unicode Collation Algorithm
- [mb.cast.to.str$()](../functions_multibyte_strings/mb.cast.to.str.md)
- [mb.cast$()](../functions_multibyte_strings/mb.cast.md)
- [str.compare()](../functions_string_operations/str.compare.md)
- [str.equals()](../functions_string_operations/str.equals.md)
