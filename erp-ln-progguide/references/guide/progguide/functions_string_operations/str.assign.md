# str.assign()

## Syntax:
`function void str.assign( ref string target$, const string source$ )`

## Description
Assigns the value of string `source$` to (multi- or single-byte) string `target$`.
If string `target$` is a resizable/based string, it is resized so that the value of string `source$` will fit. If string `target$` is not resizable, `source$` is just assigned to `target$`, but then the value may be truncated.
If `target$` is a resizable string, you can determine the new length of string `target$` using [len()](len.md) or [len.in.bytes()](len.in.bytes.md).
Note that if `target$` is a resizable multibyte string, the actual number of bytes allocated can be much higher than the length of the string. This is done to prevent truncation of the value of `target$` when that value is assigned to other string variables, after using this function.

## Arguments
| | | |
|---|---|---|
| `ref string` | `target$` |  the string to which the value of the `source$` argument must be assigned  |
| `const string` | `source$` |  the string or string expression to assign to `target$`  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2210.

## Example
```

string	source(12)
string	non.based.target(5)
string	based.target(1) based
string	based.mb.target(1) mb based
long	char.len
long	byte.len
long	byte.size

|                  1         2
| pos     12345678901234567890
source = "hello world!"	| 12 characters

| assign source to a non-resizable string; the value will be truncated
str.assign(non.based.target, source)
| non.based.target now contains "hello"

| assign source to a resizable (based) string; the target will be resized to fit the value
str.assign(based.target, source)
| based.target is allocated and now contains "hello world!"

char.len = len(based.target)
| char.len = 12 chars

byte.len = len.in.bytes(based.target)
| byte.len = 12 bytes

byte.size = str.sizeof(based.target)
| byte.size = 12 bytes

| assume the following is done in a Unicode environment with a multibyte factor of 4
|                  1         2
| pos     12345678901234567890
source = "€ 123.45"	| 8 characters, 11 bytes (4 for the Euro sign + 7 for the other characters)

| assign source to a resizable (based) multibyte string;
| the target will be resized to fit the value
str.assign(based.mb.target, source)
| based.mb.target is allocated and now contains "€ 123.45" (without any trailing spaces)

char.len = len(based.target)
| char.len = 8 chars

byte.len = len.in.bytes(based.target)
| byte.len = 11 bytes

byte.size = str.sizeof(based.target)
| byte.len = 72 bytes !
```
Why do 72 bytes have to be reserved for just 8 characters?
A multibyte character uses 4 bytes. As all characters in the source string can be multibyte characters, at least 8 characters * 4 bytes = 32 bytes are required to store all these characters.
Further, it is possible that each multibyte character is a so-called double-width character. Such characters use 2 positions on e.g. a report.
Now, when function [alloc.mem()](../functions_memory_operations/alloc.mem.md) is used for multibyte strings, it reserves enough memory for a number of *positions*, but in this case enough memory needs to be reserved to store a number of *characters*. Therefore a so-called double-width factor of 2 is applied. This leads to 32 * 2 = 64 bytes.
(If this correction would not be done, and the target string is used elsewhere in assignments to other strings, its value will be truncated).
Next, based strings are fixed by definition. This means that after an assignment takes place, the rest of the string is filled with spaces. This behavior however does not result in an exact copy of the value of the source string. In order to overcome this, a terminating \0 byte is stored in the target string right after the last character that was copied. As the target string is a multibyte string, this \0 byte takes 4 bytes as well.
So memory needs to be reserved for a total of 9 characters (8 characters + a \0 byte). Each character can be a multibyte character consuming 4 bytes. Each chatacter can be a double-width character, requiring a correction factor of 2. In total 9 * 4 * 2 = 72 bytes is required.

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
