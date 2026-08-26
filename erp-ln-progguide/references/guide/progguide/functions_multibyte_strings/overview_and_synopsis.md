# Multibyte strings overview and synopsis

## Overview
Use these functions for handling multibyte strings.
The character sets used in languages all over the world require often more characters than the 128 characters available in the [ASCII](../misc/ascii_table.md) character set. BAAN software provides foreign character set support via the BAAN Super Set ( [TSS](../misc/tss.md)). In TSS, a character occupies one or four bytes. Multibyte TSS characters always start with the hexadecimal byte 0x9B. So they can always be recognized within a string.
See also [String operations overview](../functions_string_operations/overview.md).

## Synopsis
| | | |
|---|---|---|
| `string` | [mb.cast$](mb.cast.md) | `( string value$ )` |
| `string` | [mb.cast.to.str$](mb.cast.to.str.md) | `( string value$ )` |
| `long` | [mb.char](mb.char.md) | `( long code_point )` |
| `long` | [mb.char.info](mb.char.info.md) | `( string ch$ )` |
| `long` | [mb.coerce.to.sb](mb.coerce.to.sb.md) | `( ref string string$ [, long setid ] )` |
| `long` | [mb.display](mb.display.md) | `( string_expr, ref string substr$, long space, [, long flags] )` |
| `long` | [mb.export$](mb.export.md) | `( ref string target$, string source$ [, long setid ] )` |
| `long` | [mb.export.raw](mb.export.raw.md) | `( ref string target$, string source$ [, long setid ] )` |
| `boolean` | [mb.hasbidi](mb.hasbidi.md) | `( string_expr )` |
| `long` | [mb.import$](mb.import.md) | `( ref string target$, string source$ [, long setid ] )` |
| `long` | [mb.import.raw](mb.import.raw.md) | `( ref string target$, string source$ [, long setid ] )` |
| `boolean` | [mb.isbidi](mb.isbidi.md) | `( )` |
| `boolean` | [mb.isbidi.language](mb.isbidi.language.md) | `( string lang )` |
| `long` | [mb.locale.enumerate](mb.locale.enumerate.md) | `( const string locale.name$() )` |
| `string` | [mb.locale.info](mb.locale.info.md) | `( long info_flag )` |
| `string` | [mb.localename$](mb.localename.md) | `( )` |
| `string` | [mb.long.to.str$](mb.long.to.str.md) | `( long code_point )` |
| `long` | [mb.nsets](mb.nsets.md) | `( )` |
| `string` | [mb.rev$](mb.rev.md) | `( string_expr [, long flags] )` |
| `long` | [mb.scrpos](mb.scrpos.md) | `( string_value$, long string_position )` |
| `long` | [mb.set.info](mb.set.info.md) | `( long setid, ref string name, ref string desc, ref long n_items )` |
| `long` | [mb.strpos](mb.strpos.md) | `( string_value$, long screen_position )` |
| `long` | [mb.type](mb.type.md) | `( void value )` |
| `long` | [mb.width](mb.width.md) | `( string_value$ )` |
| `string` | [tss.uni.normalized$](tss.uni.normalized.md) | `( const string source$, long tss.uni.normalization.form )` |
| `long` | [uni.export](uni.export.md) | `( ref string target$, const string source$ [, long sb_flag ] )` |
| `long` | [uni.import](uni.import.md) | `( ref string target$, const string source$ [, long sb_flag ] )` |
| `long` | [utf8.export](utf8.export.md) | `( ref string target$, const string source$, long option_mask )` |
| `long` | [utf8.import](utf8.import.md) | `( ref string target$, const string source$, long option_mask )` |
