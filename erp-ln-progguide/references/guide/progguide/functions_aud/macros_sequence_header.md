# Macros - sequence header

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
Use these macros for mapping sequence header information. The 'get' macros take *seq_hdr* as their input. This is filled by calling [aud_read_seq_hdr()](aud_read_seq_hdr.md) or [aud_read_info_seq_hdr()](aud_read_info_seq_hdr.md). The 'set' macros update the *seq_hdr* buffer. Use [aud_write_seq_hdr()](aud_write_seq_hdr.md) or [aud_update_infofile()](aud_update_infofile.md) to update the sequence header itself in the sequence file and info file respectively.
Dates are returned as UTC in the form YYYYMMDD. Times are returned as UTC in the form HHMMSS.
```

void aud_get_app_info1( string seq_hdr(),string app1(4) )
void aud_get_app_info2( string seq_hdr(),string app2(4) )
void aud_get_app_info3( string seq_hdr(),string app3(4) )
void aud_get_app_info4( string seq_hdr(),string app4(4) )
```
```

string aud_get_creat_date( string seq_hdr() )
```
```

string aud_get_creat_time( string seq_hdr() )
```
```

long aud_get_no_audit_flds( string seq_hdr() )
```
```

long aud_get_no_prim_flds( string seq_hdr() )
```
```

long aud_get_no_trans( string seq_hdr() )
```
```

long aud_get_seqno( string seq_hdr() )
```
```

long aud_get_seq_status( string seq_hdr() )
```
```

AUD_TERM_MAX_SIZE     file terminated because it reached its
                                  maximum size
AUD_TERM_DD_CHGD      file terminated because table definitions in
                       data dictionary have been changed
AUD_TERM_USER_FRCD    file forcibly terminated by user
AUD_TERM_CORRUPT      file terminated because of mismatch between
                                 sequence headers in info file and
sequence file
AUD_SEQ_REMOVED       sequence file removed using session
                                "ttaad4161m000" (Purge Audit Files)

AUD_TERMINATE_VERSION file terminated because a new audit
                                server has been activated
```
```

long term_status

term_status = aud_get_seq_status(seq_hdr)
if ( bit.and (term_status,AUD_TERM_MAX_SIZE) ) then
                | Termination because of reaching max size.
endif
if ( bit.and (term_status,AUD_TERM_DD_CHGD) ) then
                | Termination because of dd change.
endif
if ( bit.and (term_status,AUD_TERM_USER_FRCD) ) then
                | Termination forced by user.
endif
```
```

long aud_get_seq_full_status( string seq_hdr() )
```
```

long aud_get_seq_version( string seq_hdr() )
```
```

string aud_get_term_date( string seq_hdr() )
```
```

string aud_get_term_time( string seq_hdr() )
```
```

void aud_set_app_info1( string app1(4), string seq_hdr() )
void aud_set_app_info2( string app2(4), string seq_hdr() )
void aud_set_app_info3( string app3(4), string seq_hdr() )
void aud_set_app_info4( string app4(4), string seq_hdr() )
```
```

void aud_set_term_date( string t_date(), string seq_hdr())
```
```

void aud_set_term_time( string t_time(), string seq_hdr())
```
```

void aud_set_seq_status( long st, string seq_hdr() )
```
| | |
|---|---|
| *aud_get_app_info1()* to *aud_get_app_info4()* aud_get_app_info4() | These fill their second argument with the application-specific information from the sequence header. |
| *aud_get_creat_date()* | This returns the creation date (in UTC) of the sequence file. Use [utc.to.local()](../functions_date_time_zones/utc.to.local.md) to convert the UTC date to a local date. |
| *aud_get_creat_time()* | This returns the creation time (in UTC) of the sequence file. Use [utc.to.local()](../functions_date_time_zones/utc.to.local.md) to convert the UTC time to a local time. |
| *aud_get_no_audit_flds()* | This returns the number of audited fields in the sequence file. |
| *aud_get_no_prim_flds()* | This returns the number of primary key fields among the audited fields in the sequence file. |
| *aud_get_no_trans()* | This returns the number of transactions in the sequence file. |
| *aud_get_seqno()* | This returns the sequence number of the sequence file. |
| *aud_get_seq_status()* | This returns a value indicating the termination status of the sequence file. Possible values are: This value can be bitwise anded with predefined constants to determine the reason for termination of a particular sequence file. For example: |
| *aud_get_seq_full_status()* | This returns the value of the status field in the sequence header. Note that you cannot use this value because the version information is included in the status. Use *aud_get_seq_status()* instead. |
| *aud_get_seq_version()* | This returns the version of the sequence file as stored in the sequence header. |
| *aud_get_term_date()* | This returns the termination date (in UTC) of the sequence file (if the file is terminated). Use [utc.to.local()](../functions_date_time_zones/utc.to.local.md) to convert the UTC date to a local date. |
| *aud_get_term_time()* | This returns the termination time (in UTC) of the sequence file (if the file is terminated). Use [utc.to.local()](../functions_date_time_zones/utc.to.local.md) to convert the UTC time to a local time. |
| aud_set_app_info1() to aud_set_app_info4() | These write application-specific information to *seq_hdr*. |
| *aud_set_term_date()* | This stores the content of *t_date* in the termination date field of the sequence header. |
| *aud_set_term_time()* | This stores the content *t_time* in the termination time field of the sequence header. |
| *aud_set_seq_status()* | This stores the content of *st* in the status field of the sequence header. |

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
