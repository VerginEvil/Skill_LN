# bc$()

## Syntax:
`function string bc$( long type, long rows, string barcode, long options )`

## Description
Use this to create a barcode of the specified type.

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  barcode type. The mapping to a type depends on the used client. For BWPrint the type is a number in the range 1-1000 for a 1D-barcode and 1001-2000 for a 2D-barcode.  |
| `long` | `rows` |  The height of the barcode, as a number of lines.  |
| `string` | `barcode` |  The string (or binary data) that must be converted to a barcode.  |
| `long` | `options` |  Options for the barcode, see below  |

## Return values
The returned data is an encoded string. In case of error, the return value is an empty string. The returned string should not be modified. Truncation or modification of this return value will result in undefined behavior if the value is interpreted (e.g. by BwPrint).

## Context
This function is implemented in the porting set and can be used in all script types.

## Options for barcodes specific to BWprint
| | |
|---|---|
| 1D-Barcode option | Description |
| BC_AUTOPARITY | calculate parity |
| BC_TRANSPARENTBACKGRND | transparent background |
| BC_SHOWLIGHTMARGINS | show light margins |
| BC_SHOWBEARERS | show bearer bars |
| BC_EXTENDBEARERS | extend bearer bar into light margin |
| BC_SHOWTEXT | show barcode caption text |
| BC_CALCCHECKSUM | calculate checksum |
| BC_SHOWCHKDIGIT | show checksum digit |
| BC_FIXEDXUNIT | use fixed xunits for barcode width |
| BC_EXTRA_FLAG1 | barcode specific extra1 flag |
| BC_EXTRA_FLAG2 | barcode specific extra2 flag |
| | |
|---|---|
| 2D-Barcode option | Description |
| BC2D_TRANSPARENTBACKGRND | transparent background |
| BC2D_AZTECFLAG | Aztec flag |
| BC2D_AZTECMENU | Aztec menu option |
| BC2D_AZTECRVIDEO | Aztec reverse video |
| BC2D_DATAMATRIXGS1 | Datamatrix GS1 encoding |
| BC2D_PDF417TRUNCATE | PDF417 truncate |
| BC2D_SET_MODE(m) | mode, valid range: 0x0 - 0xF |
| BC2D_SET_LEVEL(l) | security level, valid range: 0x00 - 0x3F |
| BC2D_SET_XUNIT(x) | set x-unit, valid range: 0x00 - 0xFF |
| BC2D_SET_MULYUNIT(m) | set y-unit multiplier, valid range: 0x0 - 0xF |
| BC2D_SET_COLUMNS(c) | set columns, valid range: 0x0 - 0xF |
Multiple options can be combined with bit.or function or with + operator (e.g. if more than 2 options need to be combined). Note that not all options are applicable to all barcodes.

## Deprecated variants
`string bc$( long type, long rows, string barcode )`
`string bc$( long type, long rows, string barcode, long calc_checksum, long show_checkdigits )`

## Mapping implicit options for deprecated variants
The 4-argument variant of the bc$() function requires all options to be specified explicitly. The deprecated 3- and 5-argument variants of the bc$() function add some implicit options. Use the table below to rewrite a call to a 3- or 5-argument variant of the bc$() function to a 4-argument one.
The 3-argument variant of bc$() controls the calculation of checksum and showing check digit by setting a bit-value of the type argument. See the following table:
| | |
|---|---|
| Argument | Value(s) for the 'options' argument of the 4-argument variant of bc$() |
| BC_CALCCHECKSUM | BC_CALCCHECKSUM, BC_AUTOPARITY |
| BC_SHOWCHKDIGIT | BC_SHOWCHKDIGIT |
The calc_checksum and show_checkdigits arguments for the 5-argument variant of bc$() need to be mapped to explicit options for the 4-argument variant when used. See the following table:
| | |
|---|---|
| Argument | Value(s) for the options argument of the 4-argument variant of bc$() |
| calc_checksum argument set to true | BC_CALCCHECKSUM, BC_AUTOPARITY |
| show_checkdigits argument set to true | BC_SHOWCHKDIGIT |
Some options are always set for the deprecated 3- and 5-argument variants of the bc$() function, but need to be set explicitly for the 4-argument of bc$() function:
- If the provided barcode type is 5, then the BC_SHOWLIGHTMARGINS option is implicitly set. Pass BC_SHOWLIGHTMARGINS value in the options argument of the 4-argument variant of bc$() to get the same behavior.
- The BC_SHOWTEXT and BC_TRANSPARENTBACKGRND options are always implicitly set for the 3- and 5-argument variant of the bc$() function. Pass these values in the options argument of the 4-argument variant of bc$() to get the same behavior.

## Example mapping to 4-argument bc$ variant
```

barcode.string = bc$(2, 3, "87291803", false, true)
```
to
```

barcode.string = bc$(2, 3, "87291803", BC_SHOWCHKDIGIT + BC_SHOWTEXT + BC_TRANSPARENTBACKGRND)
```

## Remarks
- The calc_checksum, show_checkdigits and options arguments are not used on non-Windows platforms.
- The 3-argument variant of bc$() has a limitation to the barcode type, which need to be in range of 1-63.
- The 3- and 5-argument variants of bc$() have a limitation to the barcode string length of 224 bytes.
- 2D-barcodes are supported on Windows platform only, by BWPrint, starting with portingset 6.1c.09 (BW=B40c.95), 8.5a.02 and 8.5b.
- Starting with these BWprint versions: a barcode.pdf file is supplied in the directory where BWprint is installed. This pdf contains information about the capabilities and allowed options for barcodes.
- Do not use 1D-barcode options for 2D-barcodes. Do not use 2D-barcode options for 1D-barcodes.    Windows platform/BwPrint  The barcode type points to a barcode type. Check the barcode-1D and/or barcode-2D test in the Help menu of BwPrint for available barcode types. The number of available barcode types depend on the thirdparty software from dlSoft. This software is used to generate the barcode images.
Non-Windows platforms  The barcode type points to a shell script that is used to generate the barcode. This script is printer and customer specific. The script is stored in the $BSE/lib/barcode directory. The script name has the form 'type *xx* ', where *xx* gets a leading zero for a barcode type with a value lower than 10. For example 'type02' or 'type100'. The script is called by the printer daemon/filter in the form (quotes are added, to surround the barcode caption): $BSE/lib/barcode/type *type* '*barcode* '*rows*.

## Example
```

string barcode.string(500)
barcode.string = bc$(2, 3, "87291803", bit.or(BC_TRANSPARENTBACKGRND,BC_SHOWTEXT))
```
