# Text fields synopsis
```

#include <bic_text>
```
```
void
```
```

long
```
```

void
```
```

void
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

long
```
```

boolean
```
```

boolean
```
```

boolean
```
```

long
```
```

long
```
```

long
```
```

long
```
| | | |
|---|---|---|
|  | [copy.to.clipboard()](copy.to.clipboard.md) |  |
|  | [set.multiline.text.in.html.mode()](set.multiline.text.in.html.mode.md) | `( const string field.name.string )` |
|  | [remove.textfields()](remove.textfields.md) | `( const string field.name.string,... )` |
|  | [set.file.for.textfield()](set.file.for.textfield.md) | `( const string field.name.string, const string filename )` |
|  | [text.copy()](text.copy.md) | `( string text_field_to(17), string text_field_from(17), string kw1(17) mb, string kw2(17) mb, string kw3(17) mb, string kw4(17) mb, string tgroup(8), string edit_opt(15) )` |
|  | [text.copy.between.companies()](text.copy.between.companies.md) | `( string text_field_to(17), string text_field_from(17), long source_company, long target_company, string kw1(17) mb, string kw2(17) mb, string kw3(17) mb, string kw4(17) mb, string tgroup(8), string edit_opt(15) )` |
|  | [text.copy.language()](text.copy.language.md) | `( long textnr, string lang_from, string lang_to )` |
|  | [text.defaults()](text.defaults.md) | `( string text_field(17), ref string tgroup(8), ref string edit_opt(15), [long comp_number] )` |
|  | [text.delete()](text.delete.md) | `( string text_field(17), string lang )` |
|  | [text.edit()](text.edit.md) | `( string text_field(17), string lang, string kw1(17) mb, string kw2(17) mb, string kw3(17) mb, string kw4(17) mb, string tgroup(8), string edit_opt(15), long mode )` |
|  | [text.present.in.language()](text.present.in.language.md) | `( long textnr, string lang [, ref long nr_lines ] )` |
|  | [text.read()](text.read.md) | `( string text_field(17), string lang, ref string kw1(17) mb, ref string kw2(17) mb, ref string kw3(17) mb, ref string kw4(17) mb, ref string tgroup(8), ref string edit_opt(15), string tmp_file(256), long lock [,string rtf_file(256)] )` |
|  | [text.rewrite()](text.rewrite.md) | `( string text_field(17), string lang, string kw1(17) mb, string kw2(17) mb, string kw3(17) mb, string kw4(17) mb, string tgroup(8), string edit_opt(15), string tmp_file(256) [, long bidi, string rtf_file(256)] )` |
|  | [text.to.buf()](text.to.buf.md) | `( string text_field(17), string lang, long nr_lines, ref string buf(,) [, long rtf.text] )` |
|  | [text.buf.to.field()](text.buf.to.field.md) | `( string text_field(17), string buf )` |
|  | [text.set.keywords()](text.set.keywords.md) | `( string text_field(17), string kw1(17), [, string kw2(17), string kw3(17),, long kw4(17)] )` |
|  | [text.set.language()](text.set.language.md) | `( string text_field(17), string language(1))` |
|  | [textfield.to.database()](textfield.to.database.md) | `( string text_field(17) )` |
|  | [textfield.to.buf()](textfield.to.buf.md) | `( string text_field(17), ref string buffer )` |
|  | [text.window()](text.window.md) | `( string edit_opt(15), ref long start_column, ref long start_row, ref long number_columns, ref long number_rows )` |
|  | [text.write()](text.write.md) | `( string text_field(17), string lang, string kw1(17) mb, string kw2(17) mb, string kw3(17) mb, string kw4(17) mb, string tgroup(8), string edit_opt(15), string tmp_file(256) [, long bidi, string rtf_file(256)] )` |

## Related topics
- [Text fields overview](overview.md)
