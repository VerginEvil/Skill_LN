# Form and form field operations synopsis
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
long
```
```
long
```
```
long
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
boolean
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
string
```
```
long
```
```
long
```
```
long
```
```
boolean
```
```
void
```
```
long
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
void
```
```
void
```
```
long
```
```
long
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
long
```
```
void
```
```
void
```
```
long
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
void
```
```
boolean
```
```
void
```
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [add.sync.fields](add.sync.fields.md) | `( const string satelliteSessionCode, [const string controllerVariableName, const string satelliteFieldName])` |
|  | [add.sync.fields.nokey](add.sync.fields.nokey.md) | `( const string satelliteSessionCode, [const string controllerVariableName, const string satelliteVariableName])` |
|  | [add.sync.fields.once](add.sync.fields.once.md) | `( const string satelliteSessionCode, [const string controllerVariableName, const string satelliteFieldName])` |
|  | [add.variable.to.defaults](add.variable.to.defaults.md) | `(string var_name, long var_type)` |
|  | [add.view.field](add.view.field.md) | `( long index.nr, const string fname )` |
|  | [blank.all](blank.all.md) | `( )` |
|  | [change.field.label](change.field.label.md) | `( const string fname, long element, const string label1[, const string label2[,const string label3]] )` |
|  | [change.group.label](change.group.label.md) | `( const long groupId, const string label)` |
|  | [change.picture](change.picture.md) | `( const string fname, string icon )` |
|  | [change.satellite.label](change.satellite.label.md) | `( const string session.code, const string description )` |
|  | [check.all.input](check.all.input.md) | `( )` |
|  | [choice.again](choice.again.md) | `( )` |
|  | [change.dal.field](change.dal.field.md) | `( string field, void value )` |
|  | [clear.easy.filter](clear.easy.filter.md) | `( )` |
|  | [defaults.saved](defaults.saved.md) | `()` |
|  | [disable.commands](disable.commands.md) | `( command [, command]... )` |
|  | [disable.fields](disable.fields.md) | `( [ long mode,] string field [, occurrence] [, string field [, occurrence]]... )` |
|  | [disable.group](disable.group.md) | `( long group.nr, [long disable.mode, long occurrence] )` |
|  | [disable.pagemode](disable.pagemode.md) | `( )` |
|  | [disable.personalize.form](disable.personalize.form.md) | `()` |
|  | [disable.personalize.view](disable.personalize.view.md) | `()` |
|  | [disable.quick.flow](disable.quick.flow.md) | `( frmcmd [, frmcmd]... )` |
|  | [disable.satellite](disable.satellite.md) | `( const string session.code )` |
|  | [disable.save.on.occ.change](disable.save.on.occ.change.md) | `( )` |
|  | [disable.zoom.buttons](disable.zoom.buttons.md) | `(string field [,occurrence]...)` |
|  | [display](display.md) | `( field )` |
|  | [display.all](display.all.md) | `( field )` |
|  | [display.curr.occ](display.curr.occ.md) | `( field )` |
|  | [display.fld](display.fld.md) | `( field )` |
|  | [display.occ](display.occ.md) | `( field )` |
|  | [display.total.fields](display.total.fields.md) | `( string fieldname1, value1 [, string fieldname2, value2]... )` |
|  | [do.all.occ](do.all.occ.md) | `( function_name [,...] )` |
|  | [do.occ](do.occ.md) | `( long occurrence, function_name [,...] )` |
|  | [do.occ.without.update](do.occ.without.update.md) | `( long occurrence, function_name [,...] )` |
|  | [do.selection](do.selection.md) | `( long mode, function_name [,...] )` |
|  | [enable.commands](enable.commands.md) | `( command [, command]... )` |
|  | [enable.fields](enable.fields.md) | `( string field [, string field]... )` |
|  | [enable.group](enable.group.md) | `( long group.nr, [long occurrence] )` |
|  | [enable.qflow](enable.quick.flow.md) | `( frmcmd [, frmcmd]... )` |
|  | [enable.satellite](enable.satellite.md) | `( const string session.code )` |
|  | [enable.save.on.occ.change](enable.save.on.occ.change.md) | `( )` |
|  | [enable.zoom.buttons](enable.zoom.buttons.md) | `(string field [,occurrence]...)` |
|  | [execute](execute.md) | `( long command )` |
|  | [execute.form.command](execute.form.command.md) | `( const string form.command )` |
|  | [field.hidden](field.hidden.md) | `( long group.nr )` |
|  | [fields.autocomplete](fields.autocomplete.md) | `( boolean try.autocomplete [,const string fieldname ]... )` |
|  | [get.active.satellite](get.active.satellite.md) | `([ref long satellite.nr])` |
|  | [get.current.field.label](get.current.field.label.md) | `( const string fname, long element, ref string label1 mb, ref string label2 mb, ref string label3 mb )` |
|  | [get.field.label](get.field.label.md) | `( const string fname, long element, ref string label1 mb, ref string label2 mb, ref string label3 mb )` |
|  | [get.initial.field.label](get.initial.field.label.md) | `( const string fname, long element, ref string label1 mb, ref string label2 mb, ref string label3 mb )` |
|  | [get.prev.value](get.prev.value.md) | `( variable )` |
|  | [get.screen.defaults](get.screen.defaults.md) | `( )` |
|  | get.screen.defaults.from.xml | `( long screenDefaultsXml)` |
|  | [group.invisible](group.invisible.md) | `( long group.nr )` |
|  | [group.hidden](group.hidden.md) | `( long group.nr )` |
|  | [hide.selection.column](hide.selection.column.md) | `( )` |
|  | [input.again](input.again.md) | `( )` |
|  | [inputfield.invisible](inputfield.invisible.md) | `( string field_name(18) [, string field_name(18)]... )` |
|  | [inputfield.password](inputfield.password.md) | `( string field_name(18) [, string field_name(18)]... )` |
|  | [inputfield.visible](inputfield.visible.md) | `( string field_name(18) [, string field_name(18)]... )` |
|  | [is.current.view.personalized](is.current.view.personalized.md) | `()` |
|  | [is.field.invisible](is.field.invisible.md) | `( string field_name(18) )` |
|  | [is.field.multi.currency](is.field.multi.currency.md) | `( string field_name(18) )` |
|  | [is.mmt.controller](is.mmt.controller.md) | `( )` |
|  | [is.mmt.satellite](is.mmt.satellite.md) | `( )` |
|  | [is.scrolling.active](is.scrolling.active.md) | `( )` |
|  | [is.view.field](is.view.field.md) | `( const string fieldname )` |
|  | [is.webpart.session](is.webpart.session.md) | `( )` |
|  | [job.add.field](job.add.field.md) | `( string fld_name, [long fld_element, long fld_type, string fld_descr] )` |
|  | [make.current](make.current.md) | `( )` |
|  | [mark.occ](mark.occ.md) | `( long occurrence )` |
|  | [move.imagefield.to.grid](move.imagefield.to.grid.md) | `( const string image.field )` |
|  | [occ.independent.stat.fields](occ.independent.stat.fields.md) | `([boolean independent.state])` |
|  | [occ.independent.view.field](occ.independent.view.field.md) | `( string field.name )` |
|  | [on.old.occ](on.old.occ.md) | `( function_name [,...] )` |
|  | [print.const](print.const.md) | `( [string fill_string(127)] )` |
|  | [publish.webpart.message](publish.webpart.message.md) | `( const string type, long fromNode, [long toNode] )` |
|  | [refresh.all.occs](refresh.all.occs.md) | `( )` |
|  | [refresh.curr.occ](refresh.curr.occ.md) | `( )` |
|  | [refresh.total.line](refresh.total.line.md) | `( )` |
|  | [register.webpart.handler](register.webpart.handler.md) | `( const string type, const string handler )` |
|  | [remove.field.from.view](remove.field.from.view.md) | `( const string view.field )` |
|  | [remove.form.commands](remove.form.commands.md) | `( string command [, string command]... )` |
|  | [remove.session.index](remove.session.index.md) | `( long session.index )` |
|  | [remove.mark](remove.mark.md) | `( )` |
|  | [remove.quick.flow](remove.quick.flow.md) | `( frmcmd [, frmcmd]... )` |
|  | save.screen.defaults.to.xml |  |
|  | [satellite.invisible](satellite.invisible.md) | `( const string session.code )` |
|  | [set.checked.command](set.checked.command.md) | `( string command, boolean checked )` |
|  | [set.fields.default](set.fields.default.md) | `( )` |
|  | [set.list.values.for.field](set.list.values.for.field.md) | `( const string field.name.string, long no.list.values, const string list.values(,))` |
|  | [set.starting.satellite](set.starting.satellite.md) | `( const string satelliteSessionCode` |
|  | [standard.commands.off](standard.commands.off.md) | `( long command,... )` |
|  | [synchronize.satellite](synchronize.satellite.md) | `( long command,... )` |
|  | [to.field](to.field.md) | `( field )` |
|  | [to.form](to.form.md) | `( long form_number )` |
|  | [to.group](to.group.md) | `( long group.nr )` |
|  | [to.satellite](to.satellite.md) | `( long selected.tab )` |
|  | [unlink.from.maintable](unlink.from.maintable.md) | `( string field, [ string field, ]... )` |
|  | [update.occ](update.occ.md) | `( )` |

## Related topics
- [Overview](overview.md)
