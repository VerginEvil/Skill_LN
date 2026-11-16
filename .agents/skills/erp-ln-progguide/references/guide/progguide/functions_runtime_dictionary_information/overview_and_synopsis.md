# Runtime dictionary information overview and synopsis

## Overview
Use these functions to retrieve information from the runtime dictionary.

## Include files (for tt.* functions)
`#include <bic_tt>`

## Synopsis
```
string
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

string
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

string
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

long
```
```

long
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
```
long
```
```
string
```
```
string
```
```
long
```
```
long
```
```

string
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

string
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
string
```
```
string
```
```

string
```
```

string
```
```

boolean
```
```
void
```
```
string
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

boolean
```
```

string
```
```

boolean
```
```

string
```
```

string
```
```

boolean
```
```

string
```
```

long
```
```

long
```
```

string
```
```
string
```
```

string
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
| | | |
|---|---|---|
|  | [domainof()](domainof.md) | `( variable )` |
|  | [rdi.audit.hosts()](rdi.audit.hosts.md) | `( string table_name(9), long comp_nr, ref string hosts() )` |
|  | [rdi.column()](rdi.column.md) | `( string column_name(18), ref string domain_name(14), ref long offset, ref long size, ref long dept, ref long type, ref long flag, ref string default_val(.) )` |
|  | [rdi.column.combined()](rdi.column.combined.md) | `( string column_name(18), ref string child_columns(18,32) )` |
|  | [rdi.date.input.format$()](rdi.date.input.format.md) | `( string date_format(7) [, ref string display_format() ] )` |
|  | [rdi.domain()](rdi.domain.md) | `( string domain_name(14), ref string oformat(.), ref string lechar(.), ref string ilchar(.), ref long adjust, ref string errmess(.), ref long range_expr_id [, ref long plen, ref string iformat(.) ] )` |
|  | [rdi.domain.byte()](rdi.domain.byte.md) | `( string domain_name(14), ref long digits )` |
|  | [rdi.domain.combined()](rdi.domain.combined.md) | `( string domain_name(14), ref string child_domains(14,32) )` |
|  | [rdi.domain.date()](rdi.domain.date.md) | `( string domain_name(14), ref long digits )` |
|  | [rdi.domain.double()](rdi.domain.double.md) | `( string domain_name(14), ref long digits_before, ref long digits_after, ref long divide_factor, ref long round_code )` |
|  | [rdi.domain.enum()](rdi.domain.enum.md) | `( string domain_name(14), ref long no_enum_items )` |
|  | [rdi.domain.enum.value()](rdi.domain.enum.value.md) | `( string domain_name(14), long enum_item, string language, ref string keyword(.), ref string descr(.), ref long value )` |
|  | [rdi.etoc$()](rdi.etoc.md) | `( string domain_name(14), long enum_value )` |
|  | [rdi.ctoe()](rdi.ctoe.md) | `( string domain_name(14), string enum_name(256) )` |
|  | [rdi.domain.float()](rdi.domain.float.md) | `( string domain_name(14), ref long digits_before, ref long digits_after, ref long divide_factor, ref long round_code )` |
|  | [rdi.domain.integer()](rdi.domain.integer.md) | `( string domain_name(14), ref long digits)` |
|  | [rdi.domain.long()](rdi.domain.long.md) | `( string domain_name(14), ref long digits )` |
|  | [rdi.domain.raw()](rdi.domain.raw.md) | `( string domain_name(14), ref long length )` |
|  | [rdi.domain.set()](rdi.domain.set.md) | `( string domain_name(14), ref long no_enum_items )` |
|  | [rdi.domain.set.value()](rdi.domain.set.value.md) | `( string domain_name(14), long enum_item, string language, ref string keyword(.), ref string descr(.), ref long value )` |
|  | [rdi.domain.string()](rdi.domain.string.md) | `( string domain_name(14), ref long length, ref long convert )` |
|  | [rdi.domain.text()](rdi.domain.text.md) | `( string domain_name(14), ref long digits )` |
|  | [rdi.first.day.of.week()](rdi.first.day.of.week.md) | `( )` |
|  | [rdi.format.digits()](rdi.format.digits.md) | `( string format(), ref long digits.before, ref long digits.after [, ref string display.format()] )` |
|  | [rdi.index()](rdi.index.md) | `( string table_name(9), long index_no, ref long parts(32,3), ref boolean duplicate, ref boolean active )` |
|  | [rdi.is.application.column()](rdi.is.application.column.md) | `( string column.name()[, long column.type, long column.offset, long table.real.length] )` |
|  | [rdi.reference()](rdi.reference.md) | `( string column_name(18), ref string ref_column(18), ref long ref_mode, ref string ref_mess() [, ref boolean check_by_db, ref long ref_update_mode, ref long ref_delete_mode] )` |
|  | [rdi.table()](rdi.table.md) | `( string table_name(9), ref long no_keys, ref long no_columns, ref long int_length, ref long real_length, [ref long no_cdf, ref boolean mlf_table_all_languages] )` |
|  | [rdi.table.column()](rdi.table.column.md) | `( string table_name(9), long column_number, ref string column_name(18), ref string domain_name(14), ref long offset, ref long size, ref long dept, ref long type, ref long flag, ref string default_val(.) )` |
|  | [rdi.table.referenced()](rdi.table.referenced.md) | `( string table_name(9), long referring_index, ref string referring_column_name(18), ref long ref_mode )` |
|  | [switch.to.role()](switch.to.role.md) | `(string role)` |
|  | [tt.bobject.desc()](tt.bobject.desc.md) | `( string b_object(10), [ref string desc() mb])` |
|  | [tt.bobject.desc.by.lang()](tt.bobject.desc.by.lang.md) | `( string b_object(10), string language(1), [ref string desc() mb])` |
|  | [tt.cdf()](tt.cdf.md) | `( string cdf, ref boolean active, ref boolean internal )` |
|  | [tt.cdf.label()](tt.cdf.label.md) | `( string cdf, ref string labelCode )` |
|  | [tt.chart.desc()](tt.chart.desc.md) | `( string chart, [ref string desc() mb] )` |
|  | [tt.chm.appl.desc()](tt_chm.appl.desc.md) | `( string appl(40), ref string desc() mb )` |
|  | [tt.chm.application()](tt_chm.application.md) | `( string appl(40) )` |
|  | [tt.chm.chart()](tt_chm.chart.md) | `( string appl(40), string chart_name(16) )` |
|  | [tt.chm.charttype()](tt_chm.charttype.md) | `( string appl(40), string chart_type(16) )` |
|  | [tt.comp.desc()](tt.comp.desc.md) | `( [ref string desc() mb] )` |
|  | [tt.company()](tt.company.md) | `( long company, ref string comp_desc() mb, ref string deflt_curr(), ref long first_weekday )` |
|  | [tt.currency()](tt.currency.md) | `( string cur(3), ref string cur_desc() mb, ref string thous_sign, ref string dec_sign, ref string symbol() )` |
|  | [tt.device()](tt.device.md) | `( string device(9), ref string desc() mb, ref long device type )` |
|  | [tt.current.role()](tt.current.role.md) | `()` |
|  | [tt.demrole()](tt.demrole.md) | `()` |
|  | [tt.field.desc()](tt.field.desc.md) | `( string field(17), [ref string desc() mb] )` |
|  | [tt.index.desc()](tt.index.desc.md) | `( string tabl(8), long indexnr, [ref string desc() mb] )` |
|  | [tt.is.domain.separated()](tt.is.domain.separated.md) | `( const string domain(), [ref long numberOfSeparators, ref string separatorCharacter()] )` |
|  | [tt.init.vars()](tt.init.vars.md) | `( ref void variable, [,...] )` |
|  | [tt.label.desc()](tt.label.desc.md) | `( string label_code(19), domain ttadv.cont label_context, [ref string desc() mb] )` |
|  | [tt.langdesc()](tt.langdesc.md) | `( string language, ref string desc() mb )` |
|  | [tt.language()](tt.language.md) | `( string lang, ref string desc() mb, ref string dec_sign, ref string thous_sign, ref string date_sep, ref string time_sep )` |
|  | [tt.languages()](tt.languages.md) | `( boolean isolanguagecodes, ref long languages )` |
|  | [tt.library()](tt.library.md) | `( string library.code(14), ref string library.desc() mb )` |
|  | [tt.menu.desc()](tt.menu.desc.md) | `( string menu(13), string par_menu, [ref string desc() mb] )` |
|  | [tt.menu.present()](tt.menu.present.md) | `( string menu(13), string par_menu )` |
|  | [tt.reports()](tt.reports.md) | `( string i.session.code, ref long o.nr.reports, ref long o.rprt.group(), ref long o.rprt.nr(), ref string o.rprt.code(,), ref boolean o.is.standard() )` |
|  | [tt.report.desc()](tt.report.desc.md) | `( string reprt(15), [ref string desc() mb] )` |
|  | [tt.reportgroup.exists()](tt.reportgroup.exists.md) | `( string session(13), long report_group )` |
|  | [tt.session.desc()](tt.session.desc.md) | `( string session(13), [ref string desc() mb, string language] )` |
|  | [get.session.permission()](get.session.permission.md) | `( string session(13) )` |
|  | [tt.session.present()](tt.session.present.md) | `( string session(13) )` |
|  | [tt.short.field.desc()](tt.short.field.desc.md) | `( string field(17), long length, [ref string desc() mb] )` |
|  | [tt.role()](tt.role.md) | `()` |
|  | [tt.table.desc()](tt.table.desc.md) | `( string table(8), [ref string desc() mb] )` |
|  | [tt.user()](tt.user.md) | `( string user(12), ref string name() mb )` |
|  | [tt.user.data()](tt.user.data.md) | `( string user(12), property,... )` |
|  | [rdi.report.sensitivity()](rdi.report.sensitivity.md) | `( [const string reportname] )` |
|  | [rdi.tablefield.sensitivity()](rdi.tablefield.sensitivity.md) | `( string tablefield )` |
|  | [rdi.session.sensitivity()](rdi.session.sensitivity.md) | `( )` |
