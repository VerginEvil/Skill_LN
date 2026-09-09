# Audit Information Synopsis

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Include files
```

#include <bic_audlib>
```
```

#include <bic_audhdr.h>
```

## Functions
```
long
```
```
( long seqid )
```
```
void
```
```
( const string seqhdr(), ref string colnames(,), ref long colinfo(,) )
```
```
void
```
```
( const string seqhdr(), long col_no, ref string col_name(), ref long col_type, ref long col_dep, ref long col_len )
```
```
long
```
```
( long colno, const long colinfo(,), const string rec_buff(), ref string values(,) )
```
```
long
```
```
( long seqid )
```
```
long
```
```
( long seqid, long seqno )
```
```
long
```
```
( const string host_name(), const string table_name(), long compno, long seqno )
```
```
long
```
```
( long seqid, long rec_no, ref string rec_buff() )
```
```
long
```
```
( const string host_name(), const string table_name(), long compno, ref string info_hdr() )
```
```
long
```
```
( long seqid, long seqno, ref string seqhdr() )
```
```
long
```
```
( long seqid, ref string rec_buff() )
```
```
long
```
```
( long seqid, ref string tran_hdr() )
```
```
long
```
```
( long seqid, ref string seqhdr() )
```
```
long
```
```
( long seqid, long tran_no, ref string tran_hdr() )
```
```
long
```
```
( const string table_name(), long compno, long user_interaction, ref string host_name() )
```
```
long
```
```
( long seqid, const string seqhdr )
```
```
long
```
```
( const string host_name(), const string table_name(), long compno, const string info_hdr )
```
```
long
```
```
( long seqid, const string seqhdr() )
```
| | | |
|---|---|---|
|  | [aud_close_audit()](aud_close_audit.md) |  |
|  | [aud_get_audit_dd()](aud_get_audit_dd.md) |  |
|  | [aud_get_col_info()](aud_get_col_info.md) |  |
|  | [aud_get_fld_values()](aud_get_fld_values.md) |  |
|  | [aud_get_hdr_size()](aud_get_hdr_size.md) |  |
|  | [aud_get_info_seq_hdr_size()](aud_get_info_seq_hdr_size.md) |  |
|  | [aud_open_audit()](aud_open_audit.md) |  |
|  | [aud_read_audit_rec()](aud_read_audit_rec.md) |  |
|  | [aud_read_info_hdr()](aud_read_info_hdr.md) |  |
|  | [aud_read_info_seq_hdr()](aud_read_info_seq_hdr.md) |  |
|  | [aud_read_next_audit_rec()](aud_read_next_audit_rec.md) |  |
|  | [aud_read_next_tran()](aud_read_next_tran.md) |  |
|  | [aud_read_seq_hdr()](aud_read_seq_hdr.md) |  |
|  | [aud_read_tran()](aud_read_tran.md) |  |
|  | [aud_select_host()](aud_select_host.md) |  |
|  | [aud_update_infofile()](aud_update_infofile.md) |  |
|  | [aud_write_info_hdr()](aud_write_info_hdr.md) |  |
|  | [aud_write_seq_hdr()](aud_write_seq_hdr.md) |  |

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Macros - info header](macros_info_header.md)

- [Macros - sequence header](macros_sequence_header.md)

- [Macros - transaction header](macros_transaction_header.md)

- [Macros - transaction record](macros_transaction_record.md)

- [Macros - transaction dates and times](macros_transaction_dates_and_times.md)

- [Macros - dates and times](macros_dates_and_times.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
