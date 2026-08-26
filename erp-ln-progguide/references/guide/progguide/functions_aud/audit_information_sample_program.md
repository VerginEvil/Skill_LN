# Audit Information Sample Program

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)
This sample program illustrates the general sequence of reading audit records in a sequence file and displaying audit field information. It also shows how to write application information to a sequence header.
Assume that the table has the following DD:
Field 1 : integer (2 bytes)
Field 2 : float (4 bytes)
```

#include <bic_audlib>
#include <bic_audhdr.h>
long    seqid
long    seq_hdr_size
string  seq_hdr(1)        based
string  colnames(1,1)     based
long    colinfo(1,1)      based
string  tran_hdr(AUD_TRAN_HDR_SIZE)
string  rec_buff(AUD_MAX_REC_SIZE)
long    no_recs
long    no_trans
long    audit_flds
string  appinfo(4)
string  values(AUD_MAX_FLD_SIZE,2)
long    type

| open a seqid to table aabdb000, company 0, sequence file 0
seqid = aud_open_audit( "", "aabdb000", 0, 0 )

if ( seqid = -1 ) then
                error
endif

| get the size of the sequence file header
seq_hdr_size = aud_get_hdr_size( seqid )
alloc.mem( seq_hdr, seq_hdr_size )

| read the sequence file header
if ( aud_read_seq_hdr( seqid, seq_hdr ) = -1 ) then

                error
endif

audit_flds = aud_get_no_audit_flds( seq_hdr )
no_trans = aud_get_no_trans( seq_hdr )

| write 16 bytes of application-specific information to seqhdr
appinfo(1) = "aaaa"
aud_set_app_info1(appinfo, seqhdr)
appinfo(1) = "aaaa"
aud_set_app_info2(appinfo, seqhdr)
appinfo(1) = "aaaa"
aud_set_app_info3(appinfo, seqhdr)
appinfo(1) = "aaaa"
aud_set_app_info4(appinfo, seqhdr)

alloc.mem( colnames, AUD_COL_NAME_LEN, audit_flds )
alloc.mem( colinfo, 3, audit_flds )

aud_get_audit_dd( seq_hdr, colnames, colinfo )

for i = 1 to no_trans
                if ( aud_read_tran(seqid, i, tran_hdr) = -1 ) then
                                error
                endif

                | get number of records
                no_recs = aud_get_tran_entries(tran_hdr)


                for j = 1 to no_recs
                                | read audit records
                                if
(aud_read_audit_rec(seqid,j,rec_buff) = -1) then

                                                error
                                endif

                                for k = 1 to audit_flds
                                                ind =
aud_get_fld_values(k, colinfo, rec_buff, values)
                                                if ( ind = 1 ) then

    | both new and old values exist

type = colinfo(1,k)

print_value(type, values(1,1)) | print old value

print_value(type, values(2,1)) | print new value
                                                endif
                                                if ( ind = 0 ) then

    | only one value exists

type = colinfo(1,k)

print_value(type, values(1,1)) | print unchanged value
                                                endif
                                endfor
                endfor
endfor

| write sequence header
if ( aud_write_seq_hdr(seqid, seq_hdr) = -1 ) then

                error
endif

| close seqid
if ( aud_close_audit(seqid) = -1 ) then
                error
endif

| Function to format and print the values

print_value( long type, const string values() )
{
                float   fval
                long    sval

                on case type

                DB.FLOAT:
                                fval = load.float( values(1) )
                                                | print fval
                DB.INTEGER:
                                sval = load.short( values(1) )
                                                | print sval
                ...

                endcase
}
```

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
