# Chart manager synopsis
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use the chart functions in the Programmable Dialogs API.
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
| | | |
|---|---|---|
|  | [chm.axis.in()](chm.axis.in.md) | `( long axis_name, long logarithmic, long log_base, long divisions, double divisionstep, double intersection, string division_set(16) )` |
|  | [chm.axis.out()](chm.axis.out.md) | `( long axis_name, ref long logarithmic, ref long log_base, ref long divisions, ref double divisionstep, ref double intersection, ref string division_set() )` |
|  | [chm.chartman()](chm.chartman.md) | `( string chart_manager(80), string title(80), string user(14), string owner(14) [, string version(4), string release(2), string cust(4)] )` |
|  | [chm.check()](chm.check.md) | `( string chart_manager(14), string user(14), string chart_type(16) )` |
|  | [chm.data.in()](chm.data.in.md) | `( double series_value, double category_value, long data_number, double data_value, long footnote_no, [ long duplicate_option ] )` |
|  | [chm.data2domain.in()](chm.data2domain.in.md) | `( double series_value )` |
|  | [chm.delete.data()](chm.delete.data.md) | `( )` |
|  | [chm.delete.data2domains()](chm.delete.data2domains.md) | `( )` |
|  | [chm.delete.footnotes()](chm.delete.footnotes.md) | `( )` |
|  | [chm.delete.projections()](chm.delete.projections.md) | `( )` |
|  | [chm.delete.sets()](chm.delete.sets.md) | `( )` |
|  | [chm.disconnect()](chm.disconnect.md) | `( )` |
|  | [chm.domain.in()](chm.domain.in.md) | `( long domain_name, long data_type, string set_name(16), string title(16), string unit_label(16), double from_value, double to_value, double interval, string display_format(80 )` |
|  | [chm.domain.out()](chm.domain.out.md) | `( long domain_name, ref long data_type, ref string set_name(), ref string title(), ref string unit_label(), ref double from_value, ref double to_value, ref double interval, ref string display_format() )` |
|  | [chm.draw()](chm.draw.md) | `( [ double cat_from_value ] )` |
|  | [chm.first.data.out()](chm.first.data.out.md) | `( long option, ref double series_value, ref double category_value, ref long data_number, ref double data_value, ref long footnote_no )` |
|  | [chm.first.data2domain.out()](chm.first.data2domain.out.md) | `( ref double series_value )` |
|  | [chm.first.footnote.out()](chm.first.footnote.out.md) | `( ref long footnote_no, ref string footnote_text() )` |
|  | [chm.first.projection.out()](chm.first.projection.out.md) | `( ref double projection_point, ref long footnote_no )` |
|  | [chm.first.set.out()](chm.first.set.out.md) | `( string set_name(16), ref long element_number, ref string element_name() )` |
|  | [chm.footnote.in()](chm.footnote.in.md) | `( long footnote_no, string footnote_text(80) )` |
|  | [chm.get.request()](chm.get.request.md) | `( ref long chart_no, ref double category_from_value, ref double category_to_value )` |
|  | [chm.new()](chm.new.md) | `( string chart_name(16), ref string chart_type() )` |
|  | [chm.next.data.out()](chm.next.data.out.md) | `( long option, ref double series_value, ref double category_value, ref long data_number, ref double data_value, ref long footnote_no )` |
|  | [chm.next.data2domain.out()](chm.next.data2domain.out.md) | `( ref double series_value )` |
|  | [chm.next.footnote.out()](chm.next.footnote.out.md) | `( ref long footnote_no, ref string footnote_text() )` |
|  | [chm.next.projection.out()](chm.next.projection.out.md) | `( ref double projection_point, ref long footnote_no )` |
|  | [chm.next.set.out()](chm.next.set.out.md) | `( string set_name(16), ref long element_number, ref string element_name() )` |
|  | [chm.open()](chm.open.md) | `( string chart_name(16) )` |
|  | [chm.projection.in()](chm.projection.in.md) | `( double projection_point, long footnote_no )` |
|  | [chm.remove()](chm.remove.md) | `( string chart_manager(80), string owner_from(14), string owner_to(14) )` |
|  | [chm.scale.axis()](chm.scale.axis.md) | `( double from_value, double to_value, long divisions, double factor, ref double domain_from_value, ref double domain_to_value, ref double divisionstep )` |
|  | [chm.select()](chm.select.md) | `( string chart_manager(80), string title(80), long mode, string user(14), string owner(14), ref string chart_name(16), ref string chart_type(16) )` |
|  | [chm.set.in()](chm.set.in.md) | `( string set_name(16), ref long element_number, string element_name(80) )` |
|  | [chm.set.option()](chm.set.option.md) | `( long option, long flag )` |
|  | [chm.set.timer()](chm.set.timer.md) | `( long time )` |
|  | [chm.title.in()](chm.title.in.md) | `( string main_title(80), string sub_title(80) )` |
|  | [chm.title.out()](chm.title.out.md) | `( ref string main_title(), ref string sub_title() )` |

## Related topics
- [Chart manager overview](overview.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
