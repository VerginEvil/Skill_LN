# dir.entry()

## Syntax:
`function string dir.entry( long dfd, long read_type, [ ref long return_type, ref long filesize, ref long mode ] )`

## Description
This retrieves entries from a previously opened directory. It retrieves the entries sequentially.

## Arguments
| | | |
|---|---|---|
| `long` | `dfd` |  The pointer to the required directory, as returned when the directory was opened by [dir.open()](dir.open.md) or [dir.open.tree()](dir.open.tree.md).  |
| `long` | `read_type` |  Specifies the type of entry to be retrieved. Allowed values are listed below. These values can be combined with [bit.or()](../functions_bit/bit_and_exor_in_inv_or.md).  |
| `[ ref long` | `return_type ]` |  Returns the type of entry retrieved. Optional argument as of TIV 2150. Possible values are:  |
| `[ ref long` | `filesize ]` |  Returns the size of the entry retrieved. Optional argument as of TIV 2150.  |
| `[ ref long` | `mode ]` |  If the user can access the entry, this argument returns the type of access the user has. Optional argument as of TIV 2150. Possible options (returned as a bitset) are:  |

## Return values
The directory entry. Or an empty string if the end of the entry list has been reached.

## Context
This function is implemented in the porting set and can be used in all script types.
Symbolic links  The TLINK macro is allowed to be used on all platforms, but its functionality (support for symbolic links) is limited to UNIX/Linux only. This macro has no effect on Windows. This macro is available as of [TIV](../tiv/tiv_overview.md) [level 2150](../tiv/tiv_2150.md).

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
