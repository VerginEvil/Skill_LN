# Audit Information Overview

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Audit files
For each table associated with a particular company number, the audit server stores audit information in a set of sequence files. You use the audit functions and macros to access this information.
For each table in each company number, there is also an info file. This stores information about all sequence files for the table/company number combination, and control information for creating and maintaining the sequence files for that table/company number combination.
The following diagram illustrates the overall organization of the audit files for a particular company number.
The following diagram illustrates the overall organization of the audit files for a particular table.
The audit server uses sequence files in rotation. When the last file is full, it starts writing to the first file again. So, if the current sequence file is 200, then sequence file 201 (if it exists) is the oldest sequence file and all sequence files > 200 are older than sequence files <= 200.
For full details of audit file structure and management, consult the Infor Enterprise Server Technical Reference Manual.

## Location of audit files
The file '$BSE/lib/auditdef *x*. *x'* specifies the path to BAAN audit files. All 4GL audit routines use this file to retrieve the path to the audit files.
You can override the default audit path by using the AUDIT_FILE_PATH environment variable.
For example, take the case where directory '/usr1/audit_data' contains the audit data for modules 'adv' and 'aad' in the subdirectories 'attadv' and 'attaad'. These audit files can be referred to by setting:
```

AUDIT_FILE_PATH=/usr1/audit_data
```
Do *not* specify the final directory ('attadv' or 'attaad') in the audit path.
If the host name is not included in the pathname, use [aud_select_host()](aud_select_host.md) to select the required host.

## Audit file locking
Before reading information from an audit file, the audit server locks the relevant portion of the file. Other processes can read the information, but no process can write to the locked portion of the file while the read lock is in place. The read lock is released as soon as reading is completed.
Before updating an audit file, the audit server locks the relevant portion of the file with an exclusive type lock. This prevents other processes both reading and writing to the locked portion of the file. The exclusive lock is released as soon as the update is completed.
When the info header is read from the info file, only the info header part of the file is locked. When a sequence header is read from the info file, the sequence header, and the field specifying the header size, are locked.
When the header part of a sequence file is being updated, the sequence header in the sequence file, and the corresponding sequence header in the info file, are locked. In the sequence file, the table name, company number, and sequence header length fields are also locked.

## Related topics
- [Audit Information Synopsis](audit_information_synopsis.md)

- [Macros - info header](macros_info_header.md)

- [Macros - sequence header](macros_sequence_header.md)

- [Macros - transaction header](macros_transaction_header.md)

- [Macros - transaction record](macros_transaction_record.md)

- [Macros - transaction dates and times](macros_transaction_dates_and_times.md)

- [Macros - dates and times](macros_dates_and_times.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
