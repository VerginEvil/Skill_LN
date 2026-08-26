# Multi Language Data support code examples

## Example
```

function print.records()
{
        domain  ttiso.dlan      currlang | New domain, string(5)
        domain  ttiso.dlan      datalang
        long                    ret

        | save current datalang
        currlang = ml_get_datalang()

        select  tdsls400.*, tdsls401.*, tcibd001.*
        from    tdsls400, tdsls401, tcibd001
        where   <where clause>
        order by tdsls400._index1
        selectdo
                | retrieve datalang of bus. partner
                datalang = get.bus.partner.datalang(tdsls400.ofbp)
                | switch to datalang of bus. partner
                ret = ml_set_datalang(datalang)
                | this prints data to the report in bus. partner's language
                | e.g. the item description
                print.record()
        endselect

        | switch back to previous datalang
        ret = ml_set_datalang(currlang)
}

function domain ttiso.dlan get.bus.partner.datalang(
                domain  tccom.bpid      i.bpid)
{
        domain  tclang          softlang
        domain  ttiso.dlan      datalang

        select  tcmcs046.lang:softlang
        from    tcmcs046, tccom100
        where   tcmcs046.clan = tccom100.clan
        and     tccom100.bpid = :i.bpid
        as set with 1 rows
        selectdo
                datalang = ml_get_datalang_of_softlang(softlang)
        selectempty
                datalang = ""
        endselect

        if isspact(datalang) then
                | no mapping present between soft- and datalang
                | use base language
                datalang = ml_get_baselang()
        endif

        return(datalang)
}
```

## Related topics
- [Multi Language Data overview](overview.md)
- [Multi Language Data synopsis](synopsis.md)
