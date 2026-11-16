# Macros - transaction header

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
Use these macros for mapping transaction header information. All the macros take as their input. This is filled by calling [aud_read_tran()](aud_read_tran.md) or [aud_read_next_tran()](aud_read_next_tran.md).
```

long aud_get_tran_bytes( string tran_hdr() )
```
```

string aud_get_tran_commit_date( string tran_hdr() )
```
```

string aud_get_tran_commit_time( string tran_hdr() )
```
```

long aud_get_tran_entries( string tran_hdr() )
```
```

long aud_get_tran_id( string tran_hdr(), long g1, long g2)
```
```

string aud_get_tran_sess( string tran_hdr() )
```
```

long aud_get_tran_status( string tran_hdr() )
```
```

AUD_COMMITTED   transaction committed
AUD_ABORTED     transaction canceled
AUD_PREPARED    it is not certain whether the transaction has
                   been committed or aborted
```
```

string aud_get_tran_tuname( string tran_hdr() )
```
```

long aud_get_tran_uuid( string tran_hdr() )
```
| | |
|---|---|
| *aud_get_tran_bytes()* | This returns the total size in bytes of the transaction data. |
| *aud_get_tran_commit_date()* | This returns the UTC commit date from the transaction header. |
| *aud_get_tran_commit_time()* | This returns the UTC commit time from the transaction header. |
| *aud_get_tran_entries()* | This returns the number of audited actions in the transaction. |
| *aud_get_tran_id()* | This reads the transaction id from the transaction header. The transaction id consists of two longs which together form a unique identification. |
| *aud_get_tran_sess()* | This returns the name of the session that committed the transaction. |
| *aud_get_tran_status()* | This returns the commit status of the transaction. Possible values are: |
| *aud_get_tran_tuname()* | This returns the BAAN user name of the user who performed the transaction. |
| *aud_get_tran_uuid()* | This returns the UNIX user id of the user who performed the transaction. |

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
