# Programmable dialogs synopsis

## Overview
Use these functions for programmable dialogs.

## Synopsis
| | | |
|---|---|---|
| `long` | [dialog.new()](dialog.new.md) | `( string dialogName() [, long attribute, value] ... )` |
| `long` | [dialog.add.field()](dialog.add.field.md) | `( long dlg, const string fldName(), const string fldLabel() [, long attribute, value] ... )` |
| `long` | [dialog.add.listbox()](dialog.add.listbox.md) | `( long dlg, const string fldName(), const string fldLabel(), long no.items, long enum.vals(), string enum.desc(,) [, long attribute, value] ... )` |
| `long` | [dialog.add.text()](dialog.add.text.md) | `( long dlg, const string text() [, long attribute, value] ... )` |
| `long` | [dialog.add.button()](dialog.add.button.md) | `(long dlg, const string btnFunction(), const string btnLabel())` |
| `long` | [dialog.show()](dialog.show.md) | `( long dlg [, long previous_window, long load_defaults] )` |
| `long` | [dialog.refresh.field()](dialog.refresh.field.md) | `( long dlg, const string fldName() )` |
| `long` | [dialog.set.initial.enum.values.for.field()](dialog.set.initial.enum.values.for.field.md) | `( long dlg, const string fldName, [ALL__ENUMS_EXCEPT], enum_value, ... )` |
| `long` | [dialog.add.chart()](dialog.add.chart.md) | `( long dlg, long initial.type [, long allowed.types] )` |
| `long` | [chart.set.title()](chart.set.title.md) | `( long chart, const string title [,const string subtitle] )` |
| `long` | [chart.set.axis.type()](chart.set.axis.type.md) | `( long chart, long axis, long type )` |
| `long` | [chart.set.axis.title()](chart.set.axis.title.md) | `( long chart, long axis, const string title )` |
| `long` | [chart.add.series()](chart.add.series.md) | `( long chart , const string title )` |
| `long` | [chart.add.line.series()](chart.add.line.series.md) | `( long chart , const string title )` |
| `long` | [chart.add.data.point()](chart.add.data.point.md) | `( long series , (long|string|double) x, (long|double) y )` |
| `long` | [chart.clear.data()](chart.clear.data.md) | `( long chart )` |
| `long` | [chart.new()](chart.new.md) | `( long type, [ long width, long height ] )` |
| `long` | [chart.write()](chart.write.md) | `( long chart , const string filename , long width , long height )` |
| `long` | [chart.delete()](chart.delete.md) | `( long chart )` |
Note  Grids are not supported by programmable dialogs.

## Related topics
- [Programmable Dialogs Example](example.md)
- [Example chart](examplechart.md)
