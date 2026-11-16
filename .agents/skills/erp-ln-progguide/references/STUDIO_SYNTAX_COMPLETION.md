# Infor LN Studio Syntax & Code Completion Reference

> Extracted from Infor LN Studio 10.8 Build 0640 (`lnstudio_commonui.jar` & `common.core_*.jar`).

## 1. 4GL Keywords (80)

`and`, `and`, `array`, `at`, `base`, `based`, `boolean`, `break`, `bset`, `call`, `case`, `common`, `const`, `continue`, `default`, `delete`, `delete`, `deleteempty`, `deleteerror`, `dim`, `dllusage`, `domain`, `double`, `elif`, `else`, `endcase`, `enddelete`, `enddllusage`, `endfor`, `endfunctionusage`, `endif`, `endupdate`, `endwhile`, `eq`, `escape`, `extern`, `false`, `fixed`, `for`, `function`, `functionusage`, `ge`, `global`, `goto`, `gt`, `if`, `index`, `input`, `integer`, `le`, `long`, `lt`, `mb`, `multibyte`, `ne`, `not`, `null`, `or`, `print`, `prompt`, `raw`, `real`, `ref`, `reference`, `return`, `right`, `static`, `step`, `string`, `substr`, `table`, `then`, `to`, `true`, `until`, `updateempty`, `updateerror`, `void`, `whereused`, `while`

## 2. Embedded SQL Keywords (92)

`alike`, `all`, `as`, `as prepared set`, `as set with n rows`, `asc`, `avg`, `between`, `buffer`, `by`, `cSqlAnnotation_SelectAllDataLanguages`, `cast`, `clear`, `clearunref`, `count`, `cross`, `current_date`, `current_timestamp`, `date`, `date.num`, `date.to.num`, `desc`, `distinct`, `empty`, `endselect`, `escape`, `exists`, `fetching`, `first`, `for update`, `from`, `group`, `group by`, `having`, `hint`, `hint all rows`, `hint array fetching`, `hint array size <n>`, `hint buffer <n> rows`, `hint first rows`, `hint no array fetching`, `hint ordered`, `hint use index <n> on <table>`, `hints`, `in`, `index`, `inner`, `inrange`, `is`, `join`, `last`, `left`, `like`, `no`, `on`, `order`, `order by`, `ordered`, `outer`, `path`, `prepared`, `refers`, `refers to`, `repeat`, `repeat last row`, `retry`, `right`, `row`, `rows`, `select`, `selectbind`, `selectdo`, `selectempty`, `selecteos`, `selecterror`, `set`, `setunref`, `size`, `skip`, `sql.statement`, `subhint`, `substr`, `sum`, `timestamp`, `union`, `unref`, `update`, `use`, `where`, `wherebind`, `with`, `with retry`

## 3. Program Sections

- `declaration:`
- `before.program:`
- `after.form.read:`
- `on.error:`
- `after.program:`
- `after.update.db.commit:`
- `before.display.object:`
- `before.new.object:`
- `functions:`

## 4. Subsections

- `after.choice:`
- `after.delete:`
- `after.display.object:`
- `after.display:`
- `after.field:`
- `after.form:`
- `after.group:`
- `after.input:`
- `after.layout:`
- `after.read:`
- `after.rewrite:`
- `after.skip.delete:`
- `after.skip.rewrite:`
- `after.skip.write:`
- `after.write:`
- `after.zoom:`
- `before.checks:`
- `before.choice:`
- `before.delete:`
- `before.display:`
- `before.field:`
- `before.form:`
- `before.group:`
- `before.input:`
- `before.layout:`
- `before.read:`
- `before.rewrite:`
- `before.write:`
- `before.zoom:`
- `check.input:`
- `domain.error:`
- `init.field:`
- `init.form:`
- `init.group:`
- `on.choice:`
- `on.entry:`
- `on.exit:`
- `on.input:`
- `read.view:`
- `ref.display:`
- `ref.input:`
- `selection.filter:`
- `when.field.changes:`

## 5. Choice Sections

- `choice.abort.program:`
- `choice.add.set:`
- `choice.attachments:`
- `choice.bms:`
- `choice.change.frm:`
- `choice.change.order:`
- `choice.cmd.insert.in.detail:`
- `choice.cmd.ssi.export.a:`
- `choice.cmd.ssi.export.q:`
- `choice.cmd.ssi.import:`
- `choice.cont.process:`
- `choice.create.job:`
- `choice.def.find:`
- `choice.deselect.all:`
- `choice.display.set:`
- `choice.dupl.occur:`
- `choice.end.program:`
- `choice.find.data:`
- `choice.first.frm:`
- `choice.first.set:`
- `choice.first.view:`
- `choice.get.defaults:`
- `choice.global.copy:`
- `choice.global.delete:`
- `choice.interrupt:`
- `choice.last.frm:`
- `choice.last.set:`
- `choice.last.view:`
- `choice.mark.delete:`
- `choice.mark.occur:`
- `choice.modify.set:`
- `choice.next.frm:`
- `choice.next.set:`
- `choice.next.view:`
- `choice.prev.frm:`
- `choice.prev.set:`
- `choice.prev.view:`
- `choice.print.data:`
- `choice.recover.set:`
- `choice.resize.frm:`
- `choice.restart.input:`
- `choice.rotate.curr:`
- `choice.run.job:`
- `choice.save.defaults:`
- `choice.select.all:`
- `choice.start.query:`
- `choice.start.set:`
- `choice.text.manager:`
- `choice.update.db:`
- `choice.user.0:`
- `choice.user.1:`
- `choice.user.2:`
- `choice.user.3:`
- `choice.user.4:`
- `choice.user.5:`
- `choice.user.6:`
- `choice.user.7:`
- `choice.user.8:`
- `choice.user.9:`
- `choice.zoom:`

## 6. Report Sections

- `before.report:`
- `after.report:`
- `header.`
- `detail.`
- `before.`
- `after.`
- `before.layout:`
- `after.layout:`
- `footer.`

## 7. Predefined Variables (176)

`actual.occ`, `attr.adju`, `attr.bitset.mask`, `attr.changed`, `attr.conv`, `attr.currency$`, `attr.currkey`, `attr.dbase`, `attr.dbmaxlen`, `attr.deflt$`, `attr.descr$`, `attr.diga`, `attr.digv`, `attr.divf`, `attr.domain$`, `attr.domm$`, `attr.dorp`, `attr.echo`, `attr.element`, `attr.enum.mask$`, `attr.format.addition$`, `attr.helpfile$`, `attr.ille$`, `attr.imax`, `attr.inpfld`, `attr.input`, `attr.lega$`, `attr.mandatory`, `attr.maxlen`, `attr.message$`, `attr.minlen`, `attr.multioccur`, `attr.nowait$`, `attr.oformat$`, `attr.permission`, `attr.previous$`, `attr.rang`, `attr.rang$`, `attr.reallen`, `attr.refpath`, `attr.rndm`, `attr.rotate`, `attr.sttp`, `attr.textfield$`, `attr.textkw1$`, `attr.textkw2$`, `attr.textkw3$`, `attr.textkw4$`, `attr.textlang$`, `attr.textmaxlines`, `attr.textmode`, `attr.textopt$`, `attr.textstart`, `attr.textzoomsession$`, `attr.type`, `attr.zoomcode`, `attr.zoomreturn$`, `attr.zoomsession$`, `auto.nextform`, `background`, `before.update.check`, `breakview`, `chartgrp`, `chm.name`, `chm.owner`, `chm.title`, `chm.user`, `choice`, `curr.key`, `curr.pacc$`, `date`, `date$`, `deprecated`, `e`, `error.bypass`, `exit.val$`, `fattr.currfld$`, `fattr.descr$`, `fattr.ftype`, `fattr.helpfile$`, `fattr.horizontal`, `fattr.init`, `fattr.nextfld$`, `fattr.nrtabs`, `fattr.occurnr`, `fattr.prevfld$`, `fattr.row`, `fattr.scrollbar`, `fattr.seqno`, `fattr.step`, `fattr.toplines`, `fattr.total.line`, `fattr.vdate$`, `fattr.version$`, `fattr.width`, `filename$`, `filled.occ`, `firstweek$`, `form.curr`, `form.next`, `form.prev`, `free$`, `graphical.mode`, `ignore.first.event`, `in.ret`, `initial.resize`, `job.device`, `job.device.requested`, `job.process`, `job.report`, `job.skip.date.question`, `language$`, `lattr.autobefores`, `lattr.autoreset`, `lattr.break`, `lattr.enddata`, `lattr.header`, `lattr.language$`, `lattr.lineno`, `lattr.multicol`, `lattr.multicol.count`, `lattr.multicol.repeat`, `lattr.pageno`, `lattr.print`, `lattr.prline`, `lattr.recordtimes`, `lattr.textexpand`, `lattr.textlang$`, `lattr.textline`, `lattr.textlineno`, `lattr.textlines.max`, `lattr.textlines.min`, `logname$`, `main.table$`, `mark.status`, `mark.table()`, `marked`, `max.formtabs`, `maxdouble`, `modify.prim.key`, `number.forms`, `parent`, `pid`, `previous.choice`, `procesinfo$`, `prog.name$`, `query.extension`, `reportgrp`, `reportno`, `sattr.combined`, `spool.date`, `spool.device`, `spool.fileout`, `spool.fontnumber`, `spool.id`, `spool.left.mrg`, `spool.paper.type`, `spool.pg.length`, `spool.pg.width`, `spool.pr.copies`, `spool.pr.line`, `spool.report`, `spool.ssrs`, `spool.time`, `spool.view.rtl`, `spool.xml`, `stp.abort.error`, `stp.check.input.error`, `stp.skip.error`, `term$`, `time`, `trusted`, `update.status`, `user.type$`, `zoomfield$`, `zoomreturn$`

## 8. Standard Defines (49)

`ALL_ENUMS_EXCEPT`, `BIC_TIV_LEVEL`, `DALDBERROR`, `DALHOOKERROR`, `DALNOMETHOD`, `DALNOOBJECT`, `DALNOOBJPERM`, `DALNOSETPERM`, `DAL_DESTROY`, `DAL_FIND`, `DAL_GET_CURR`, `DAL_GET_FIRST`, `DAL_GET_LAST`, `DAL_GET_NEXT`, `DAL_GET_PREV`, `DAL_GET_SPECIFIED`, `DAL_NEW`, `DAL_NOLOCK`, `DAL_UPDATE`, `DISABLE`, `ENABLE`, `ES_TIV_LEVEL`, `HOOK_ALL`, `HOOK_IS_APPLICABLE`, `HOOK_IS_DERIVED`, `HOOK_IS_MANDATORY`, `HOOK_IS_READONLY`, `HOOK_IS_VALID`, `HOOK_UPDATE`, `INCLUDE_ENUMS`, `MODAL`, `MODELESS`, `MSG.ALL`, `MSG.ERROR`, `MSG.INFO`, `MSG.SUCCESS`, `MSG.WARNING`, `PI`, `PROGRESS.BAR`, `PROGRESS.CANCEL`, `PROGRESS.NOAUTODESTROY`, `PROGRESS.RESIZEABLE`, `PROGRESS.STOP`, `PROGRESS.TIMER`, `READONLY`, `XML_DATA`, `XML_DTD`, `XML_ELEMENT`, `XML_PI`

## 9. DAL Object Hooks (15)

- `before.open.object.set`
- `before.get.object`
- `after.get.object`
- `before.new.object`
- `after.new.object`
- `before.change.object`
- `after.change.object`
- `before.destroy.object`
- `after.destroy.object`
- `before.save.object`
- `after.save.object`
- `after.commit.transaction`
- `after.abort.transaction`
- `method.is.allowed`
- `set.object.defaults`

## 10. DAL Field Hook Suffixes (10)

| Suffix | Return Value | Arguments | Default Body |
|---|---|---|---|
| `.is.never.applicable` | `extern boolean` | `` | `return(false)` |
| `.is.applicable` | `extern boolean` | `` | `return(true)` |
| `.is.readonly` | `extern boolean` | `` | `return(false)` |
| `.is.derived` | `extern boolean` | `` | `return(false)` |
| `.is.mandatory` | `extern boolean` | `` | `return(true)` |
| `.is.valid` | `extern boolean` | `` | `return(true)` |
| `.update` | `extern void` | `long i.mode` | `` |
| `.make.valid` | `extern long` | `long i.mode` | `return(0)` |
| `.check` | `extern long` | `long has_changed` | `return(0)` |
| `.set.defaults` | `extern long` | `long has_changed` | `return(0)` |

## 11. Official 4GL Templates (12)

### ON CASE - Template (`%template.fourglcode.case`)
*The ON CASE statement is a multiple-way decision table.*
```baan
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

### DllUsage - Template (`%template.fourglcode.dllusage`)
*DllUsage is mandatory for external Infor LN functions, because it contains often processing, starting a session, or calculations.*
```baan
DllUsage
Expl:	${text}
Pre:	${preconditions}
Post:	${postconditions}
Input:	${input_arg}
Output:	${output_arg}
Return:	${returnType}
EndDllUsage
```

### FunctionUsage Template (`%template.fourglcode.functionusage`)
*FunctionUsage is mandatory for every function in Infor LN and beyond, only very simple functions are excluded.*
```baan
FunctionUsage
Expl:	${text}
Pre:	${preconditions}
Post:	${postconditions}
Input:	${input_arg}
Output:	${output_arg}
Return:	${returnType}
EndFunctionUsage
```

### All Function Arguments Template (`%template.fourglcode.all.args`)
*Inserts all arguments from the current function (comma separated).*
```baan
${all_args_cs}
```

### For - Template (`%template.fourglcode.for`)
*For Control Flow Statement*
```baan
for ${num_var} = ${num_expr_1} to ${num_expr_2}
	${statement}
endfor
```

### For Step - Template (`%template.fourglcode.for.step`)
*For Step Control Flow Statement*
```baan
for ${num_var} = ${num_expr_1} to ${num_expr_2} step ${num_expr_3}
	${statement}
endfor
```

### Repeat - Template (`%template.fourglcode.repeat`)
*Repeat Control Flow Statement*
```baan
repeat
	${statement}
until ${expression}
```

### While - Template (`%template.fourglcode.while`)
*While Control Flow Statement*
```baan
while ${expression}
	${statement}
endwhile
```

### IF...THEN (`%template.fourglcode.if`)
*This tests a condition. If the condition evaluates to TRUE, the statements following the IF...THEN statement are executed.*
```baan
if ${condition} then
	${statement}
endif
```

### IF...THEN...ELSE (`%template.fourglcode.if.then.else`)
*This tests a condition. If the condition evaluates to TRUE, the statements following the IF...THEN statement are executed. If the condition evaluates to FALSE, the statements following the ELSE statement are executed.*
```baan
if ${condition} then
	${statement1}
else
	${statement2}
endif
```

### Select - Template (`%template.fourglcode.select`)
*Select Statement*
```baan
select	${table}.*
from	${table}
where	${table}._index${cursor}
selectdo
	|* todo: add operation(s) on all selected records
selectempty
	|* todo: add operation(s) if nothing has been selected 
endselect
```

### Comment Block - Template (`%template.fourglcode.comment.block`)
*Inserts a comment block on the current position*
```baan
${comment_block}
```
