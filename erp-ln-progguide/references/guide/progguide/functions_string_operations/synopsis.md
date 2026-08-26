# String operations synopsis
| | | |
|---|---|---|
| string | [bytes2hex](bytes2hex.md) | `( const string bytes, long length )` |
| string | [concat$](concat.md) | `( string separator, expr, ... )` |
| string | [filter.infrastructural.details](filter.infrastructural.details.md) | `( const string bytes )` |
| long | [hex2bytes](hex2bytes.md) | `( const string hex, ref string bytes )` |
| boolean | [isdigit](isdigit.md) | `( string_expr )` |
| boolean | [isspace](isspace.md) | `( string_expr )` |
| long | [len](len.md) | `( string_expr )` |
| long | [len.in.bytes](len.in.bytes.md) | `( string_expr )` |
| long | [load.byte](load.byte.md) | `( string record$ )` |
| double | [load.double](load.double.md) | `( string record$, [ long endian ] )` |
| double | [load.float](load.float.md) | `( string record$, [ long endian ] )` |
| long | [load.long](load.long.md) | `( string record$, [ long endian ] )` |
| long | [load.short](load.short.md) | `( string record$, [ long endian ] )` |
| long | [load.utc](load.utc.md) | `( string record$, [ long endian, long byte.count ] )` |
| long | [lval](lval.md) | `( string_expr )` |
| void | [not.fixed](not.fixed.md) | `( string string_var(.) )` |
| long | [pos](pos.md) | `( string source, string part, [ long offset ] )` |
| long | [rpos](rpos.md) | `( string source, string part, [ long offset ] )` |
| long | [set.strip.mode](set.strip.mode.md) | `( long table_id, long mode )` |
| long | [set.symbol.strip.mode](set.symbol.strip.mode.md) | `( ref string str$, long mode )` |
| string | [shiftc$](shiftc.md) | `( string strg(.) )` |
| string | [shiftl$](shiftl.md) | `( string strg(.) )` |
| string | [shiftr$](shiftr.md) | `( string strg(.) )` |
| void | [store.byte](store.byte.md) | `( long value, ref string rec$ )` |
| void | [store.double](store.double.md) | `( double value, ref string rec$ )` |
| void | [store.float](store.float.md) | `( double value, ref string rec$ )` |
| void | [store.long](store.long.md) | `( long value, ref string rec$ )` |
| void | [store.short](store.short.md) | `( long value, ref string rec$ )` |
| void | [store.utc](store.utc.md) | `( long value, ref string rec$, [ long byte.count ] )` |
| string | [str$](str.md) | `( num_expr )` |
| void | [str.alloc](str.alloc.md) | `( ref string string$, long nchars )` |
| void | [str.assign](str.assign.md) | `( ref string target$, const string source$ )` |
| long | [str.compare](str.compare.md) | `( const string a$, const string b$, [ boolean ignorecase ] )` |
| boolean | [str.containsMBchar](str.containsmbchar.md) | `( const string string$ )` |
| boolean | [str.endswith](str.endswith.md) | `( const string string$, const string part$, [ boolean ignorecase ] )` |
| boolean | [str.equals](str.equals.md) | `( const string a$, const string b$, [ boolean ignorecase ] )` |
| string | [str.insert$](str.insert.md) | `( const string string$, long offset, const string part$ )` |
| boolean | [str.isalpha](str.isalpha.md) | `( const string string$ )` |
| boolean | [str.isalphanum](str.isalphanum.md) | `( const string string$ )` |
| boolean | [str.isascii](str.isascii.md) | `( const string string$ )` |
| boolean | [str.isbase64](str.isbase64.md) | `( const string string$ )` |
| boolean | [str.isemail](str.isemail.md) | `( const string string$ )` |
| boolean | [str.ishex](str.ishex.md) | `( const string string$ )` |
| boolean | [str.isnumeric](str.isnumeric.md) | `( const string string$ )` |
| boolean | [str.isurl](str.isurl.md) | `( const string string$ )` |
| boolean | [str.isuuid](str.isuuid.md) | `( const string string$ )` |
| string | [str.join$](str.join.md) | `( const string separator$, ... )` |
| long | [str_pos](str_pos.md) | `( string source, string part, [ long offset ] )` |
| string | [str.remove$](str.remove.md) | `( const string string$, long offset, long nchars )` |
| void | [str.replace](str.replace.md) | `( const string string$, const string oldstr$, const string newstr$, ref string result$ )` |
| string | [str.replace$](str.replace$.md) | `( const string string$, const string oldstr$, const string newstr$ )` |
| long | [str_rpos](str_rpos.md) | `( string source, string part, [ long offset ] )` |
| long | [str.sizeof](str.sizeof.md) | `( const string string$ )` |
| long | [str.split](str.split.md) | `( const string string$, const string separator$, long limit, ref string parts(,) )` |
| boolean | [str.startswith](str.startswith.md) | `( const string string$, const string part$, [ boolean ignorecase ] )` |
| string | [str.substring$](str.substring.md) | `( const string string$, long beginpos, [ long endpos ] )` |
| string | [str.unquote$](str.unquote.md) | `( const string string$ )` |
| string | [string.set$](string.set.md) | `( string value$, long count )` |
| long | [string.to.bounded.long](string.to.bounded.long.md) | `( string string$, long lowerbound, long upperbound, [ ref long appliedbounds ] )` |
| string | [strip$](strip.md) | `( string strg(.) )` |
| string | [tolower$](tolower.md) | `( string_expr )` |
| string | [toupper$](toupper.md) | `( string_expr )` |
| string | [trim$](trim.md) | `( string_expr )` |
| string | [quoted.string](quoted.string.md) | `( string_expr )` |
|  |  |  |
| long | [tt.align.according.domain](tt.align.according.domain.md) | `( string string_in(.), ref string string_out(), string domain_name )` |
| double | [val](val.md) | `( string_expr )` |

## Related topics
- [String operations overview](overview.md)
