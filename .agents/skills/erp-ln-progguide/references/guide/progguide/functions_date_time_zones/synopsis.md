# Dates, times, time zones synopsis

## Local dates/times
| | | |
|---|---|---|
| `long` | [date.num()](date.num.md) | `( )` |
| `string` | [date.to.inputstr$()](date.to.inputstr.md) | `( long dayno, string format(7), long length )` |
| `long` | [date.to.iso()](date.to.iso.md) | `( long local.date )` |
| `long` | [date.to.num()](date.to.num.md) | `( long yearno, long monthno, long month_dayno )` |
| `string` | [dte$()](dte.md) | `( )` |
| `long` | [inputstr.to.date()](inputstr.to.date.md) | `( string inputstr(.), string format(7) )` |
| `long` | [iso.to.date()](iso.to.date.md) | `( const string iso.string )` |
| `long` | [num.to.date()](num.to.date.md) | `( long dayno, ref long yearno, ref long monthno, ref long month_dayno )` |
| `string` | [num.to.date$()](num.to.dates.md) | `( long dayno, long mode )` |
| `long` | [num.to.week()](num.to.week.md) | `( long dayno, ref long week_dayno, ref long year_dayno, ref long weekno [, ref long yearno] )` |
| `long` | [time.num()](time.num.md) | `( )` |
| `long` | [week.to.num()](week.to.num.md) | `( long weekno, long yearno, long week_dayno )` |

## UTC conversion
| | | |
|---|---|---|
| `long` | [date.to.utc()](date.to.utc.md) | `( long yearno, long monthno, long month_dayno, long hours, long minutes, long seconds )` |
| `long` | [date.with.timezone.info.to.utc()](date.with.timezone.info.to.utc.md) | `( long yearno, long monthno, long month_dayno, long hours, long minutes, long seconds, long utcdiff )` |
| `long` | [input.to.utc()](input.to.utc.md) | `( const string value(), const string format() )` |
| `long` | [inputstr.to.utc()](inputstr.to.utc.md) | `( const string date.inputstr(), string date.format(7), const string time.inputstr(), string time.format(7) )` |
| `long` | [iso.to.utc()](iso.to.utc.md) | `( const string iso.string )` |
| `long` | [local.to.utc()](local.to.utc.md) | `( long local_days, long local_time, ref long utc [, string local_dst] )` |
| `long` | [local.with.timezone.info.to.utc()](local.with.timezone.info.to.utc.md) | `( long local_days, long local_time, long utcdiff, ref long utc )` |
| `long` | [utc.num()](utc.num.md) | `( )` |
| `long` | [utc.add()](utc.add.md) | `( long i.utc, long year, long month, long day, long hour, long minutes, long second, ref long o.utc )` |
| `long` | [utc.to.date()](utc.to.date.md) | `( long utc, ref long yearno, ref long monthno, ref long month_dayno, ref long hours, ref long minutes, ref long seconds )` |
| `long` | [utc.to.date.with.timezone.info()](utc.to.date.with.timezone.info.md) | `( long utc, ref long yearno, ref long monthno, ref long month_dayno, ref long hours, ref long minutes, ref long seconds, ref long utcdiff )` |
| `long` | [utc.to.input()](utc.to.input.md) | `( long lvalue, const string format() )` |
| `long` | [utc.to.inputstr$()](utc.to.inputstr.md) | `( long utc, string date.format(7), string time.format(7), ref string local.date(), ref string local.time() )` |
| `string` | [utc.to.iso()](utc.to.iso.md) | `( long utc, long format )` |
| `long` | [utc.to.local()](utc.to.local.md) | `( long utc, ref long local_days, ref long local_time [, ref string local_dst] )` |
| `long` | [utc.to.local.with.timezone.info()](utc.to.local.with.timezone.info.md) | `( long utc, ref long local_days, ref long local_time, ref long utcdiff )` |
| `long` | [utc.to.week()](utc.to.week.md) | `( long utc, ref long week_dayno, ref long year_dayno, ref long weekno, ref long hours, ref long minutes, ref long seconds [, ref long yearno] )` |
| `long` | [week.to.utc()](week.to.utc.md) | `( long weekno, long yearno, long week_dayno, long hours, long minutes, long seconds )` |

## Time zones
| | | |
|---|---|---|
| `long` | [choose.time.zone.from.list()](choose.time.zone.from.list.md) | `( )` |
| `long` | [date.to.date()](date.to.date.md) | `( long in_date, long in_time, const string in_zone(), const string out_zone(), ref long out_date, ref long out_time )` |
| `long` | [get.time.zone()](get.time.zone.md) | `( ref string time_zone() )` |
| `long` | [set.time.zone()](set.time.zone.md) | `( string time_zone(50) )` |
| `boolean` | [timezone.exists()](timezone.exists.md) | `( string time_zone(50) )` |

## Related topics
- [Dates, times, time zones overview](overview.md)
