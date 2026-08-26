# Macros - transaction dates and times

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
Use these macros to retrieve transaction dates and times. All the macros take tran_hdr as their input. This is filled by calling [aud_read_tran()](aud_read_tran.md) or [aud_read_next_tran()](aud_read_next_tran.md).
```

long aud_get_tran_date_yyyy( string tran_hdr() )
```
```

long aud_get_tran_date_mm( string tran_hdr() )
```
```

long aud_get_tran_date_dd( string tran_hdr() )
```
```

long aud_get_tran_time_hh( string tran_hdr() )
```
```

long aud_get_tran_time_mm( string tran_hdr() )
```
```

long aud_get_tran_time_ss( string tran_hdr() )
```
| | |
|---|---|
| *aud_get_tran_date_yyyy()* | This retrieves the year value from transaction commit date. The year is represented by four digits.  |
| *aud_get_tran_date_mm()* | This retrieves the month value from the transaction commit date.  |
| *aud_get_tran_date_dd()* | This retrieves the day value from the transaction commit date.  |
| *aud_get_tran_time_hh()* | This retrieves the hours value from the transaction commit time.  |
| *aud_get_tran_time_mm()* | This retrieves the minutes value from the transaction commit time.  |
| *aud_get_tran_time_ss()* | This retrieves the seconds value from the transaction commit time.  |

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
