# str.alloc()

## Syntax:
`function void str.alloc( ref string string$, long nchars )`

## Description
Allocates enough memory for the given string to store (at least) the given number of characters. In case of multibyte strings this is different from from [alloc.mem()](../functions_memory_operations/alloc.mem.md) which allocates enough memory to store a given number of screen positions.
For single-byte strings, this function just calls [alloc.mem()](../functions_memory_operations/alloc.mem.md)
For multibyte strings, the following applies:
- In case the multibyte factor is 1, this function just calls [alloc.mem()](../functions_memory_operations/alloc.mem.md). This will reserve enough memory to store all (mb) characters.
- In case the multibyte factor is 2, [alloc.mem()](../functions_memory_operations/alloc.mem.md) assumes all (mb) characters occupy 2 screen positions. When space is asked for e.g. 4 screen positions, [alloc.mem()](../functions_memory_operations/alloc.mem.md) will reserve (4 screen positions / 2 positions per char =) 2 * 4 bytes per mb char = 8 bytes. As enough memory has to be reserved for the given number of *characters*, this number of characters is multiplied with 2 in order to allocate enough memory. This will reserve enough memory to store all (mb) characters.
- In case the multibyte factor is 4, double-width characters can also occur. Therefore, the number of chars is multiplied with the double-width factor of 2 to ensure no data is lost. The bshell needs extra memory to handle double-width characters.

## Arguments
| | | |
|---|---|---|
| `ref string` | `string$` |  the string to resize  |
| `long` | `nchars` |  the number of characters for which memory must be allocated  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2210.

## Preconditions
- Parameter `string$` must be declared as based; it may not be a substring expression, and it may not be based on another variable.

## Example
```

string	sb.string(1) based
string	mb.string(1) mb based
long	byte.size

|* reserve space for 20 single-byte characters
str.alloc(sb.string, 20)

byte.size = str.sizeof(sb.string)
|* byte.size = 20

|* reserve space for 20 multibyte characters
|* assume this is done in a unicode environment with an mb factor of 4
str.alloc(mb.string, 20)

byte.size = str.sizeof(mb.string)
|* byte.size = 80 bytes (= 20 * 4 bytes per char * 2 (double-width correction factor))
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
