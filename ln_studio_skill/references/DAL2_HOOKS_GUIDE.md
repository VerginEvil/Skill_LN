# Infor LN DAL 2 Hooks & Methods Catalog

In Infor ERP LN, all Data Access Layer 2 scripts must include `#include <bic_dal2>` and operate under standard transaction rules.

---

## 1. Object Hooks

Object hooks govern the lifecycle of an entire record object.

### `function extern boolean method.is.allowed(long i.method)`
Determines whether an operation (`DAL_NEW`, `DAL_UPDATE`, `DAL_DESTROY`) is permitted for the current record.
```baan
function extern boolean method.is.allowed(long i.method)
{
    on case i.method
    case DAL_NEW:
        break
    case DAL_UPDATE:
        if txptc100.stat = txstatus.inactive then
            dal.set.error.message("@record.is.inactive")
            return(false)
        endif
        break
    case DAL_DESTROY:
        return(false) | Prevent deletion
    endcase
    return(true)
}
```

### `function extern long before.save.object(long i.mode)`
Executes before the record is saved to the database. `i.mode` is either `DAL_NEW` or `DAL_UPDATE`.
- Return `0` if all validations pass.
- Return `DALHOOKERROR` if any validation fails.

### `function extern long after.save.object(long i.mode)`
Executes after the record has been written to the database buffer. Useful for logging, auditing, or triggering secondary updates.
- Return `0` on success.

### `function extern long before.destroy.object()` / `after.destroy.object()`
Executes before and after a record is deleted.

---

## 2. Property / Field Hooks

Property hooks govern individual field values.

### `function extern long <table_field>.make.valid(long mode)`
Calculates or defaults a field value when a new record is initialized.
```baan
function extern long txptc100.seqn.make.valid(long mode)
{
    domain tcpono tem.seqn
    select  txptc100.seqn:tem.seqn
    from    txptc100
    order by txptc100.seqn desc
    as set with 1 rows
    selectdo
        txptc100.seqn = tem.seqn + 1
    selectempty
        txptc100.seqn = 1
    endselect
    return(0)
}
```

### `function extern boolean <table_field>.is.valid(long mode)`
Validates that the entered value satisfies domain boundaries or business rules.
```baan
function extern boolean txptc100.cmnf.is.valid(long mode)
{
    if isspace(txptc100.cmnf) then
        dal.set.error.message("@cmnf.cannot.be.empty")
        return(false)
    endif
    return(true)
}
```

### `function extern boolean <table_field>.is.mandatory(long mode)`
Conditionally designates a field as mandatory.
```baan
function extern boolean txptc100.mpnr.is.mandatory(long mode)
{
    if txptc100.skip = txskip.by.group then
        return(true)
    endif
    return(false)
}
```

### `function extern boolean <table_field>.is.readonly(long mode)`
Conditionally designates a field as read-only.

---

## 3. Error Handling

- Always set error messages using:
  ```baan
  dal.set.error.message("@label_code")
  ```
  or with dynamic arguments:
  ```baan
  dal.set.error.message("@label_code", arg1, arg2)
  ```
- Return `DALHOOKERROR` to abort the save/action.
- Do NOT issue `commit.transaction()` or `abort.transaction()` within DAL 2 hooks.
