# Macros - info header

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
Use these macros for mapping info header information. The 'get' macros take *info_hdr* as their input. This is filled by calling [aud_read_info_hdr()](aud_read_info_hdr.md). The 'set' macros update the *info_hdr* buffer. Use [aud_write_info_hdr()](aud_write_info_hdr.md) to update the information file header itself.
```

string aud_get_version( string info_hdr() )
```
```

string aud_get_tablename( string info_hdr() )
```
```

long aud_get_compno( string info_hdr() )
```
```

long aud_get_status( string info_hdr() )
```
```

long aud_get_from_seqno( string info_hdr() )
```
```

long aud_get_to_seqno( string info_hdr() )
```
```

long aud_get_curr_seqno( string info_hdr() )
```
```

long aud_get_curr_security( string info_hdr() )
```
```

AUD_SECU_NONE         no permissions
AUD_SECU_ALL          all permissions
AUD_SECU_PRINT        print permissions
AUD_SECU_CLEAN        purge permissions
AUD_SECU_MAINTAIN     maintain permissions
AUD_SECU_APPL_DEF     application-defined permissions
```
```

long security

security = aud_get_curr_security( info_hdr )
if (bit.and (security, AUD_SECU_NONE)) then
        | No permissions on info file
else
        if (bit.and (security, AUD_SECU_ALL)) then
                | All permissions on info file
        else

                if (bit.and (security, AUD_SECU_PRINT)) then
                        | Print permissions on info file
                endif

                if (bit.and (security, AUD_SECU_CLEAN)) then
                        | Purge permissions on info file
                endif

                if (bit.and (security, AUD_SECU_MAINTAIN)) then
                        | Maintain permissions on info file
                endif

                if (bit.and (security, AUD_SECU_APPL_DEF)) then
                        | Application-defined permissions on file
                endif

        endif
endif
```
```

long aud_get_max_audit_file_size( string info_hdr() )
```
```

void aud_set_status( long status, string info_hdr() )
```
```

void aud_set_to_seqno( long to_seq, string info_hdr() )
```
```

void aud_set_curr_seqno( long c_seq, string info_hdr() )
```
```

void aud_set_max_audit_file_size( long m_size, string
              info_hdr() )
```
```

void aud_set_security( long c_sec, string info_hdr() )
```
| | |
|---|---|
| *aud_get_version()* | This returns the current version of the info file and related sequence files.  |
| *aud_get_tablename()* | This returns the name of the table to which the specified info file relates.  |
| *aud_get_compno()* | This returns the company number of the table to which the info file relates.  |
| *aud_get_status()* | This returns the value of the status field in the info header. The status field indicates whether the sequence file reuse feature is enabled or disabled.  |
| *aud_get_from_seqno()* | This returns the starting number for sequence files related to the info file.  |
| *aud_get_to_seqno()* | This returns the maximum sequence number for sequence files related to the info file.  |
| *aud_get_curr_seqno()* | This returns the sequence number of the current sequence file. This is the sequence file to which new audit information will be written.  |
| *aud_get_curr_security()* | This returns the security permissions for the info file and associated sequence files. The return value can be a combination of the following values: For example: |
| *aud_get_max_audit_file_ size()* | This returns the maximum size (in bytes) of sequence files related to the info file.  |
| *aud_set_status()* | This stores the value of *status* in the status field of the info header.  |
| *aud_set_to_seqno()* | This stores the value of *to_seq* in the maximum sequence number field of the info header.  |
| *aud_set_curr_seqno()* | This stores the value of the *c_seq* in the current sequence number field of the info header.  |
| *aud_set_max_audit_file_ size()* | This stores the value of *m_size* in the maximum file size field of the info header.  |
| *aud_set_security()* | This stores the value of *c_sec* in the security field of the info header. For a list of valid values, see *aud_get_curr_security()*.  |

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
