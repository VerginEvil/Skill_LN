# Infor LN UI Script Guide (`bic_dam`)

In Infor ERP LN, UI scripts are associated with sessions (`.ses`) and handle user interaction, dynamic form behaviors, dialogs, and menu commands. They must `#include <bic_dam>`.

---

## 1. UI Script Structure

A standard UI script consists of:
1. Header comments and identification.
2. `#include <bic_dam>`
3. `declaration:` section declaring tables and global UI variables.
4. `before.program:` initialization section.
5. `main.table.io:` main table read/write event intercepts.
6. `choice.<command>:` button and menu action handlers.
7. `field.<table_field>:` field-level UI event handlers (display, change, zoom).
8. `functions:` local helper procedures.

```baan
|*******************************************************************************
|* txptc1100m000  B61O_a_ext
|* Maintain Inspection Skipping Method
|*******************************************************************************
#include <bic_dam>

declaration:
    table   ttxptc100 |* Inspection Skipping Method

before.program:
    | Form initialization

main.table.io:
before.write:
    | Logic before record write

before.rewrite:
    | Logic before record rewrite

choice.update.db:
before.choice:
    check.all.input()

field.txptc100.mpnr:
before.zoom:
    attr.zoomindex = 1
selection.filter:
    query.extend.where.in.zoom("tdipu045.cmnf = " & quoted.string(txptc100.cmnf))

functions:
function void check.all.input()
{
    | Local validation helper
}
```

---

## 2. Field-Level Events

### `before.display:`
Triggered right before the field is rendered on screen. Useful for enabling/disabling related controls:
```baan
field.txptc100.mpnr:
before.display:
    if txptc100.skip = txskip.by.mfg then
        disable.fields("txptc100.mpnr")
    else
        enable.fields("txptc100.mpnr")
    endif
```

### `when.field.changes:`
Triggered immediately when the user changes a field value on screen.

### `before.zoom:` and `selection.filter:`
Configures zoom parameters before opening a lookup session:
```baan
field.txptc100.cmnf:
before.zoom:
    attr.zoomindex = 1
selection.filter:
    query.extend.where.in.zoom("tcmcs060.cmnf <> ''")
```

---

## 3. Prohibited Practices in UI Scripts

- **Do NOT execute SQL DML (`db.insert`, `db.update`, `db.delete`).**
- **Do NOT bypass DAL.** Always let the DAL perform validations and persistence.
- **Do NOT execute database commits directly.**
