# local.to.utc()

## Syntax:
`function long local.to.utc( long local_days, long local_time, ref long utc, [ string local_dst ] )`

## Description
This converts a local date and time to UTC long format. Input values for local date and time must be in the signed 32-bit value range.

## Arguments
| | | |
|---|---|---|
| `long` | `local_days` |  A number of days since 01-01-0001.  |
| `long` | `local_time` |  A number of seconds since 00:00 hours.  |
| `ref long` | `utc` |  The UTC long format value corresponding to the specified local date and time.  |
| `[ string` | `local_dst ]` |  Optional argument for specifying whether Daylight Saving Time (DST) must be considered as on or off. When omitted, the current timezone rule (expressing local legislation) determines whether DST is considered as switched on or off for the supplied ( *local_days*, *local_time*) combination. DST_ON: The supplied ( *local_days*, *local_time*) combination must be considered as local time with DST on. DST_OFF: The supplied ( *local_days*, *local_time*) combination must be considered as local time with DST off. DST_ON and DST_OFF are predefined literal strings of length 6 and 7 respectively.  |

## Return values
| | |
|---|---|
| 0 | Success. The supplied reference argument *utc* now contains the UTC value of the supplied local date and time.  |
| -1 | Error. The supplied reference argument *utc* is unchanged. The cause of the error may be one of the following. The exact result is negative. The exact result is greater than the maximum value 2^( BitCountOfLong-1) - 1 of the signed BitCountOfLong-bit range. The optional argument *local_dst* is not supplied and the ( *local_days*, *local_time*) combination is in the skipped range at the begin of a DST period. See the Daylight Saving Time handling section and the examples below.  |
-
-
-

## Context
This function is implemented in the porting set and can be used in all script types.

## Daylight Saving Time handling
Local time with Daylight Saving Time (DST) on is a fixed amount of time (typically one hour) ahead of local time with DST off. Default local time is equal to one of these, and the current timezone rule (expressing local legislation) determines when default local time switches from DST off to DST on and back to DST off.
At the moment that DST is switched on, the default local time is moved forward. The skipped default local time interval simply does not exist. It cannot be converted to UTC.
At the moment that DST is switched off, the default local time is moved backward. A certain default local time interval (typically one hour) occurs twice: first just before the switch moment and then again just after the switch moment. When a default local time in this ambiguous interval is converted to UTC, DST will be judged to be on, so it is judged to be before the switch moment. When it must be interpreted as after the switch moment, then DST_OFF must be explicitly specified in the *local_dst* argument.
As an example, the tables below show how DST is switched on and off in timezone Europe/Amsterdam.
| | | | |
|---|---|---|---|
| Begin of DST |  |  |  |
| local days: last Sunday in March |  |  |  |
| local time | DST |  |  |
| DST off | DST on | default |  |
| 00:00:00 … 00:59:59 | 01:00:00 … 01:59:59 | 00:00:00 … 00:59:59 | off |
| 01:00:00 … 01:59:59 | 02:00:00 … 02:59:59 | 01:00:00 … 01:59:59 | off |
|  |  | 02:00:00 … 02:59:59 (skipped) |  |
| 02:00:00 … 02:59:59 | 03:00:00 … 03:59:59 | 03:00:00 … 03:59:59 | on |
| 03:00:00 … 03:59:59 | 04:00:00 … 04:59:59 | 04:00:00 … 04:59:59 | on |
| | | | |
|---|---|---|---|
| End of DST |  |  |  |
| local days: last Sunday in October |  |  |  |
| local time | DST |  |  |
| DST off | DST on | default |  |
| 00:00:00 … 00:59:59 | 01:00:00 … 01:59:59 | 01:00:00 … 01:59:59 | on |
| 01:00:00 … 01:59:59 | 02:00:00 … 02:59:59 | 02:00:00 … 02:59:59 (ambiguous, favored) | on |
| 02:00:00 … 02:59:59 | 03:00:00 … 03:59:59 | 02:00:00 … 02:59:59 (ambiguous, ignored) | off |
| 03:00:00 … 03:59:59 | 04:00:00 … 04:59:59 | 03:00:00 … 03:59:59 | off |

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

    | get local_days
    ret = utc.to.local(Before_DST_01.00.00,local_days,local_time,local_dst)

    local_time = 60*60
    ret = local.to.utc(local_days,local_time,UTCTime,DST_ON)
    | UTCTime = 1080428400
    | which is 60 minutes before Before_DST_01.00.00

    ret = local.to.utc(local_days,local_time,UTCTime,DST_OFF)
    | UTCTime = 1080432000
    | which is Before_DST_01.00.00

    ret = local.to.utc(local_days,local_time,UTCTime)
    | UTCTime = 1080432000
    | same as DST_OFF, because at this time DST is not yet valid

    local_time = 2*60*60 + 30*60
    ret = local.to.utc(local_days,local_time,UTCTime,DST_ON)
    | UTCTime = 1080433800
    | which is 30 minutes after Before_DST_01.00.00

    ret = local.to.utc(local_days,local_time,UTCTime,DST_OFF)
    | UTCTime = 1080437400
    | which is 90 minutes after Before_DST_01.00.00

    ret = local.to.utc(local_days,local_time,UTCTime)
    | ret = -1
    | Default local time 02:30 does not exist on this day

    local_time = 4*60*60
    ret = local.to.utc(local_days,local_time,UTCTime,DST_ON)
    | UTCTime = 1080439200
    | which is 120 minutes after Before_DST_01.00.00

    ret = local.to.utc(local_days,local_time,UTCTime,DST_OFF)
    | UTCTime = 1080442800
    | which is 180 minutes after Before_DST_01.00.00

    ret = local.to.utc(local_days,local_time,UTCTime)
    | UTCTime = 1080439200
    | same as DST_ON, because at this time DST is valid

    | 10/31/2004 End of DST
    | At 03:00 DST clock is set to 02:00
    After_DST_04.00.00 = date.to.utc( 2004, 10, 31, 04, 00, 00 ) | two hours after end of DST
    | After_DST_04.00.00 = 1099191600

    | get local_days
    ret = utc.to.local(After_DST_04.00.00,local_days,local_time)

    local_time = 60*60
    ret = local.to.utc(local_days,local_time,UTCTime,DST_ON)
    | UTCTime = 1099177200
    | which is 240 minutes before After_DST_04.00.00

    ret = local.to.utc(local_days,local_time,UTCTime,DST_OFF)
    | UTCTime = 1099180800
    | which is 180 minutes before After_DST_04.00.00

    ret = local.to.utc(local_days,local_time,UTCTime)
    | UTCTime = 1099177200
    | same as DST_ON, because at this time it is DST

    local_time = 2*60*60 + 30*60
    ret = local.to.utc(local_days,local_time,UTCTime,DST_ON)
    | UTCTime = 1099182600
    | which is 150 minutes before After_DST_04.00.00

    ret = local.to.utc(local_days,local_time,UTCTime,DST_OFF)
    | UTCTime = 1099186200
    | which is 90 minutes before After_DST_04.00.00

    ret = local.to.utc(local_days,local_time,UTCTime)
    | Default local time 02:30 is ambiguous: DST may be on or off.
    | DST on is favored, DST off is ignored.
    | UTCTime = 1099182600
    | same as DST_ON

    local_time = 4*60*60
    ret = local.to.utc(local_days,local_time,UTCTime,DST_ON)
    | UTCTime = 1099188000
    | which is 60 minutes before After_DST_04.00.00

    ret = local.to.utc(local_days,local_time,UTCTime,DST_OFF)
    | UTCTime = 1099191600
    | which is After_DST_04.00.00

    ret = local.to.utc(local_days,local_time,UTCTime)
    | UTCTime = 1099191600
    | same as DST_OFF, because at this time it is not DST anymore

}
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
