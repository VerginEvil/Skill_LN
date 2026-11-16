# Macros - dates and times

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
The input to these macros is a date string in the form YYYYMMDD or a time string in the form HHMMSS.
```

long aud_get_date_yyyy( string s_dat() )
```
```

long aud_get_date_mm( string s_dat() )
```
```

long aud_get_date_dd( string s_dat() )
```
```

long aud_get_time_hh( string s_tim() )
```
```

long aud_get_time_mm( string s_tim() )
```
| | |
|---|---|
| *aud_get_date_yyyy()* | This retrieves the year value from the date string *s_dat*. The year is represented by four digits. |
| *aud_get_date_mm()* | This retrieves the month value from the date string *s_dat*. |
| *aud_get_date_dd()* | This retrieves the day value from the date string *s_dat*. |
| *aud_get_time_hh()* | This retrieves the hours value from the time string *s_tim*. |
| *aud_get_time_mm()* | This retrieves the minutes value from the time string *s_tim*. |

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
