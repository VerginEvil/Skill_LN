# Macros - transaction record

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
Use these macros for mapping transaction records. All the macros take *rec_buff* as their input. This is filled by calling [aud_read_audit_rec()](aud_read_audit_rec.md) or [aud_read_next_audit_rec()](aud_read_next_audit_rec.md).
```

void aud_get_rec_app_info( string appinfo(4),
                 string rec_buff() )
```
```

string aud_get_rec_op_type( string rec_buff() )
```
| | |
|---|---|
| I | insert record |
| D | delete record |
| U | update record |
| L | clear table |
| R | drop table |
| C | create table |
```

long aud_get_rec_seqno( string rec_buff() )
```

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
