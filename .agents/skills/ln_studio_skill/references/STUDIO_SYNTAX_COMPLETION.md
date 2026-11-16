# LN Studio Syntax & Code Completion Reference Catalog

> Canonical reference extracted from LN Studio 10.8 (build 0640).
> **Source Installation**: `D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64`

## Summary

- **Keywords**: 80
- **SQL Keywords**: 92
- **Program Sections**: 9
- **Subsections**: 43
- **Choice Sections**: 60
- **Report Sections**: 9
- **Predefined Variables**: 176
- **Standard Defines**: 49
- **DAL Object Hooks**: 15
- **DAL Field Hook Suffixes**: 10
- **Code Templates**: 12

---

## 1. Program Sections (`IScriptEditorProgramSections`)

Top-level execution sections in LN 4GL scripts:

| Section Header | Description |
|---|---|
| `after.form.read:` | Standard LN Studio program section |
| `after.program:` | Standard LN Studio program section |
| `after.update.db.commit:` | Standard LN Studio program section |
| `before.display.object:` | Standard LN Studio program section |
| `before.new.object:` | Standard LN Studio program section |
| `before.program:` | Standard LN Studio program section |
| `declaration:` | Standard LN Studio program section |
| `functions:` | Standard LN Studio program section |
| `on.error:` | Standard LN Studio program section |

### Dynamic Program Sections
- `field.<field_name>:` — Field-specific UI logic (e.g., `field.txcmg011.cdec:`)
- `choice.<choice_name>:` — Form command / standard choice handler
- `form.<form_num>:` — Form-level event handler
- `group.<group_num>:` — Form group handler
- `header.<report_num>:`, `detail.<report_num>:`, `before.<report_num>:`, `after.<report_num>:` — Report layout sections
- `functions:` — 3GL/4GL function definitions

---

## 2. Subsections (`IScriptEditorSubSections`)

Subsections nested inside program sections (e.g., `field.*:`, `choice.*:`, `main.table.io:`):

| Subsection | Category |
|---|---|
| `after.choice:` | Choice Hook |
| `after.delete:` | Table IO Hook |
| `after.display.object:` | Field Hook |
| `after.display:` | Field Hook |
| `after.field:` | Field Hook |
| `after.form:` | Field Hook |
| `after.group:` | Field Hook |
| `after.input:` | Field Hook |
| `after.layout:` | Field Hook |
| `after.read:` | Table IO Hook |
| `after.rewrite:` | Table IO Hook |
| `after.skip.delete:` | Table IO Hook |
| `after.skip.rewrite:` | Table IO Hook |
| `after.skip.write:` | Table IO Hook |
| `after.write:` | Table IO Hook |
| `after.zoom:` | Field Hook |
| `before.checks:` | Field Hook |
| `before.choice:` | Choice Hook |
| `before.delete:` | Table IO Hook |
| `before.display:` | Field Hook |
| `before.field:` | Field Hook |
| `before.form:` | Field Hook |
| `before.group:` | Field Hook |
| `before.input:` | Field Hook |
| `before.layout:` | Field Hook |
| `before.read:` | Table IO Hook |
| `before.rewrite:` | Table IO Hook |
| `before.write:` | Table IO Hook |
| `before.zoom:` | Field Hook |
| `check.input:` | Field Hook |
| `domain.error:` | Field Hook |
| `init.field:` | Field Hook |
| `init.form:` | Field Hook |
| `init.group:` | Field Hook |
| `on.choice:` | Choice Hook |
| `on.entry:` | Field Hook |
| `on.exit:` | Field Hook |
| `on.input:` | Field Hook |
| `read.view:` | Table IO Hook |
| `ref.display:` | Field Hook |
| `ref.input:` | Field Hook |
| `selection.filter:` | Field Hook |
| `when.field.changes:` | Field Hook |

---

## 3. Choice Sections (`IScriptEditorChoiceSections`)

Standard choice events in UI sessions:

| Choice Section | Description |
|---|---|
| `choice.abort.program:` | Standard Session Choice Section |
| `choice.add.set:` | Standard Session Choice Section |
| `choice.attachments:` | Standard Session Choice Section |
| `choice.bms:` | Standard Session Choice Section |
| `choice.change.frm:` | Standard Session Choice Section |
| `choice.change.order:` | Standard Session Choice Section |
| `choice.cmd.insert.in.detail:` | Standard Session Choice Section |
| `choice.cmd.ssi.export.a:` | Standard Session Choice Section |
| `choice.cmd.ssi.export.q:` | Standard Session Choice Section |
| `choice.cmd.ssi.import:` | Standard Session Choice Section |
| `choice.cont.process:` | Standard Session Choice Section |
| `choice.create.job:` | Standard Session Choice Section |
| `choice.def.find:` | Standard Session Choice Section |
| `choice.deselect.all:` | Standard Session Choice Section |
| `choice.display.set:` | Standard Session Choice Section |
| `choice.dupl.occur:` | Standard Session Choice Section |
| `choice.end.program:` | Standard Session Choice Section |
| `choice.find.data:` | Standard Session Choice Section |
| `choice.first.frm:` | Standard Session Choice Section |
| `choice.first.set:` | Standard Session Choice Section |
| `choice.first.view:` | Standard Session Choice Section |
| `choice.get.defaults:` | Standard Session Choice Section |
| `choice.global.copy:` | Standard Session Choice Section |
| `choice.global.delete:` | Standard Session Choice Section |
| `choice.interrupt:` | Standard Session Choice Section |
| `choice.last.frm:` | Standard Session Choice Section |
| `choice.last.set:` | Standard Session Choice Section |
| `choice.last.view:` | Standard Session Choice Section |
| `choice.mark.delete:` | Standard Session Choice Section |
| `choice.mark.occur:` | Standard Session Choice Section |
| `choice.modify.set:` | Standard Session Choice Section |
| `choice.next.frm:` | Standard Session Choice Section |
| `choice.next.set:` | Standard Session Choice Section |
| `choice.next.view:` | Standard Session Choice Section |
| `choice.prev.frm:` | Standard Session Choice Section |
| `choice.prev.set:` | Standard Session Choice Section |
| `choice.prev.view:` | Standard Session Choice Section |
| `choice.print.data:` | Standard Session Choice Section |
| `choice.recover.set:` | Standard Session Choice Section |
| `choice.resize.frm:` | Standard Session Choice Section |
| `choice.restart.input:` | Standard Session Choice Section |
| `choice.rotate.curr:` | Standard Session Choice Section |
| `choice.run.job:` | Standard Session Choice Section |
| `choice.save.defaults:` | Standard Session Choice Section |
| `choice.select.all:` | Standard Session Choice Section |
| `choice.start.query:` | Standard Session Choice Section |
| `choice.start.set:` | Standard Session Choice Section |
| `choice.text.manager:` | Standard Session Choice Section |
| `choice.update.db:` | Standard Session Choice Section |
| `choice.user.0:` | Standard Session Choice Section |
| `choice.user.1:` | Standard Session Choice Section |
| `choice.user.2:` | Standard Session Choice Section |
| `choice.user.3:` | Standard Session Choice Section |
| `choice.user.4:` | Standard Session Choice Section |
| `choice.user.5:` | Standard Session Choice Section |
| `choice.user.6:` | Standard Session Choice Section |
| `choice.user.7:` | Standard Session Choice Section |
| `choice.user.8:` | Standard Session Choice Section |
| `choice.user.9:` | Standard Session Choice Section |
| `choice.zoom:` | Standard Session Choice Section |

---

## 4. DAL Object Hooks (`CodeCompletion.DAL_OBJECT_HOOKS`)

Object-level DAL 2 hooks executed during CRUD lifecycle:

| Hook Name | Lifecycle Phase |
|---|---|
| `before.open.object.set()` | Standard DAL 2 Object Hook |
| `before.get.object()` | Standard DAL 2 Object Hook |
| `after.get.object()` | Standard DAL 2 Object Hook |
| `before.new.object()` | Standard DAL 2 Object Hook |
| `after.new.object()` | Standard DAL 2 Object Hook |
| `before.change.object()` | Standard DAL 2 Object Hook |
| `after.change.object()` | Standard DAL 2 Object Hook |
| `before.destroy.object()` | Standard DAL 2 Object Hook |
| `after.destroy.object()` | Standard DAL 2 Object Hook |
| `before.save.object()` | Standard DAL 2 Object Hook |
| `after.save.object()` | Standard DAL 2 Object Hook |
| `after.commit.transaction()` | Standard DAL 2 Object Hook |
| `after.abort.transaction()` | Standard DAL 2 Object Hook |
| `method.is.allowed()` | Standard DAL 2 Object Hook |
| `set.object.defaults()` | Standard DAL 2 Object Hook |

---

## 5. DAL Field Hook Suffixes (`CodeCompletion.DAL_FIELD_HOOK_SUFFIXES`)

Property hooks for DAL 2 scripts and Table Extensions (`.est`):

| Suffix | Return Type | Arguments | Default Body |
|---|---|---|---|
| `<table.column>.is.never.applicable` | `extern boolean` | `` | `return(false)` |
| `<table.column>.is.applicable` | `extern boolean` | `` | `return(true)` |
| `<table.column>.is.readonly` | `extern boolean` | `` | `return(false)` |
| `<table.column>.is.derived` | `extern boolean` | `` | `return(false)` |
| `<table.column>.is.mandatory` | `extern boolean` | `` | `return(true)` |
| `<table.column>.is.valid` | `extern boolean` | `` | `return(true)` |
| `<table.column>.update` | `extern void` | `long i.mode` | `` |
| `<table.column>.make.valid` | `extern long` | `long i.mode` | `return(0)` |
| `<table.column>.check` | `extern long` | `long has_changed` | `return(0)` |
| `<table.column>.set.defaults` | `extern long` | `long has_changed` | `return(0)` |

---

## 6. Predefined Variables & Standard Defines

- **Total Predefined Variables**: 176
- **Total Standard Defines**: 49

Commonly used:
- `actual.occ`, `attr.changed`, `attr.conv`, `curr.key`, `dal.change.object`, `spool.device`
- `DAL_GET_FIRST`, `DAL_GET_NEXT`, `DAL_GET_PREV`, `DAL_GET_LAST`, `DAL_GET_CURR`, `DALHOOKERROR`

---

## 7. 4GL Code Templates

### ON CASE - Template
> The ON CASE statement is a multiple-way decision table.

```4gl
on case ${variable}
case ${value_1}:
	${statement_1}
	break
case ${value_2}:
	${statement_2}
	break
default:
	${statement_3}
	break
endcase
```

### DllUsage - Template
> DllUsage is mandatory for external Infor LN functions, because it contains often processing, starting a session, or calculations.

```4gl
DllUsage
Expl:	${text}
Pre:	${preconditions}
Post:	${postconditions}
Input:	${input_arg}
Output:	${output_arg}
Return:	${returnType}
EndDllUsage
```

### FunctionUsage Template
> FunctionUsage is mandatory for every function in Infor LN and beyond, only very simple functions are excluded.

```4gl
FunctionUsage
Expl:	${text}
Pre:	${preconditions}
Post:	${postconditions}
Input:	${input_arg}
Output:	${output_arg}
Return:	${returnType}
EndFunctionUsage
```

### All Function Arguments Template
> Inserts all arguments from the current function (comma separated).

```4gl
${all_args_cs}
```

### For - Template
> For Control Flow Statement

```4gl
for ${num_var} = ${num_expr_1} to ${num_expr_2}
	${statement}
endfor
```

### For Step - Template
> For Step Control Flow Statement

```4gl
for ${num_var} = ${num_expr_1} to ${num_expr_2} step ${num_expr_3}
	${statement}
endfor
```

### Repeat - Template
> Repeat Control Flow Statement

```4gl
repeat
	${statement}
until ${expression}
```

### While - Template
> While Control Flow Statement

```4gl
while ${expression}
	${statement}
endwhile
```

### IF...THEN
> This tests a condition. If the condition evaluates to TRUE, the statements following the IF...THEN statement are executed.

```4gl
if ${condition} then
	${statement}
endif
```

### IF...THEN...ELSE
> This tests a condition. If the condition evaluates to TRUE, the statements following the IF...THEN statement are executed. If the condition evaluates to FALSE, the statements following the ELSE statement are executed.

```4gl
if ${condition} then
	${statement1}
else
	${statement2}
endif
```

### Select - Template
> Select Statement

```4gl
select	${table}.*
from	${table}
where	${table}._index${cursor}
selectdo
	|* todo: add operation(s) on all selected records
selectempty
	|* todo: add operation(s) if nothing has been selected 
endselect
```

### Comment Block - Template
> Inserts a comment block on the current position

```4gl
${comment_block}
```
