# utc.to.local()

## Syntax:
`function long utc.to.local( long utc, ref long local_days, ref long local_time, [ ref string local_dst ] )`

## Description
This converts a UTC long format value to local date and time.

## Arguments
| | | |
|---|---|---|
| `long` | `utc` |  The UTC long format value.  |
| `ref long` | `local_days` |  The local date as the number of days since 01-01-0001.  |
| `ref long` | `local_time` |  The local time as the number of seconds since 00:00 hour.  |
| `[ ref string` | `local_dst ]` |  Optional reference argument for receiving whether Daylight Saving Time (DST) is on or off, according to the current timezone rule (expressing local legislation). DST_ON: DST is on at the moment determined by the supplied *utc* value, DST_OFF: DST is off at the moment determined by the supplied *utc* value, DST_ON and DST_OFF are predefined literal strings of length 6 and 7 respectively.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 |  Error. For example: Any intermediate result involves a date before the year 1 or past the year 9999.  |
-

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
This example shows how to deal with Daylight Saving Time.
```

function main () {

    long    ret
    long    local_days
    long    local_time
    string  local_dst(7)

    long    Before_DST_01.00.00
    long    After_DST_04.00.00
    long    UTCTime

    | 03/28/2004 Begin of DST
    | At 02:00 clock is set to 03:00 DST
    Before_DST_01.00.00 = date.to.utc( 2004, 03, 28, 01, 00, 00 ) | one hour before begin of DST
    | Before_DST_01.00.00 = 1080432000

    UTCTime = Before_DST_01.00.00
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 3600 which means 01:00:00
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_OFF
    | local_time is 3600 which means 01:00:00

    UTCTime = Before_DST_01.00.00 + 1*60*60 -1 | almost 1 hour after 01:00; 1 second before DST
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 7199 which means 01:59:59
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_OFF
    | local_time is 7199 which means 01:59:59

    UTCTime = Before_DST_01.00.00 + 1*60*60 | 1 hour after 01:00; begin of DST
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 10800 which means 03:00:00
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_ON
    | local_time is 10800 which means 03:00:00

    | 10/31/2004 End of DST
    | At 03:00 DST clock is set to 02:00
    After_DST_04.00.00 = date.to.utc( 2004, 10, 31, 04, 00, 00 ) | two hours after end of DST
    | After_DST_04.00.00 = 1099191600

    UTCTime = After_DST_04.00.00
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 14400 which means 04:00:00
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_OFF
    | local_time is 14400 which means 04:00:00

    UTCTime = After_DST_04.00.00 - 1*60*60 - 30*60 | 1.5 hours before 04:00
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 9000 which means 02:30:00
    | Same result as one hour earlier (see below)!
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_OFF
    | One hour earlier (see below), local_dst results in DST_ON
    | local_time is 9000 which means 02:30:00

    UTCTime = After_DST_04.00.00 - 2*60*60 - 30*60 | 2.5 hours before 04:00
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 9000 which means 02:30:00
    | Same result as one hour later (see above)!
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_ON
    | One hour later (see above), local_dst results in DST_OFF
    | local_time is 9000 which means 02:30:00

    UTCTime = After_DST_04.00.00 - 4*60*60 | 4 hours before 04:00
    ret = utc.to.local(UTCTime,local_days,local_time)
    | local_time is 3600 which means 01:00:00
    ret = utc.to.local(UTCTime,local_days,local_time,local_dst)
    | local_dst is DST_ON
    | local_time is 3600 which means 01:00:00

}
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
