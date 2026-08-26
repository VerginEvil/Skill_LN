# Database operations synopsis

## Syntax
| | | |
|---|---|---|
| `void` | [abort.io()](abort.io.md) | `( string mesg( 14 ) [, ... ] )` |
| `long` | [abort.transaction()](abort.transaction.md) | `( )` |
| `void` | [activate.search()](activate.search.md) | `( )` |
| `long` | [commit.transaction()](commit.transaction.md) | `( )` |
| `long` | [count.records.in.view()](count.records.in.view.md) | `( )` |
| `long` | [dal.change.object()](dal.change.object.md) | `( string class_name )` |
| `long` | [dal.check.field()](dal.check.field.md) | `( string fld_name, [ long element, long mode ] )` |
| `long` | [dal.copy.object()](dal.copy.object.md) | `( string class_name )` |
| `void` | [dal.destroy()](dal.destroy.md) | `( string class_name, long object_set, ref long retval, long prop_check [, long mode [, long eflag ] ] )` |
| `long` | [dal.destroy.object()](dal.destroy.object.md) | `( string class_name )` |
| `void` | [dal.execute.hook()](dal.execute.hook.md) | `( long|string set_id, string name, ref long retval, long mode, long elem )` |
| `long` | [dal.get.context()](dal.get.context.md) | `( )` |
| `long` | [dal.get.field.mode()](dal.get.field.mode.md) | `( string fld_name, [ long element ] )` |
| `long` | [dal.get.object()](dal.get.object.md) | `( string class_name, long lock, key_field1, key_value1, [ key_field2, key_value2, ... ] )` |
| `long` | [dal.get.property.flag()](dal.get.property.flag.md) | `( string class_name, long object_set, string prop_name )` |
| `boolean` | [dal.is.copy.active()](dal.is.copy.active.md) | `( )` |
| `boolean` | [dal.is.field.changed()](dal.is.field.changed.md) | `( string fld.name, [ long element ] )` |
| `void` | [dal.new()](dal.new.md) | `( string class_name, long object_set, ref long retval, long prop_check [, long mode [, long eflag ] ] )` |
| `long` | [dal.new.object()](dal.new.object.md) | `( string class_name )` |
| `boolean` | [dal.parent.caused.update()](dal.parent.caused.update.md) | `( string fld.name, [ long element ] )` |
| `long` | [dal.recall()](dal.recall.md) | `( const string tbl.name )` |
| `long` | [dal.reject()](dal.reject.md) | `( const string tbl.name, const string reason$ )` |
| `long` | [dal.save.object()](dal.save.object.md) | `( string class_name, [ long eflag ] )` |
| `void` | [dal.set.array.field()](dal.set.array.field.md) | `( string fld_name, value( . ) )` |
| `long` | [dal.set.cdf.fields()](dal.set.cdf.fields.md) | `( string tbl.name )` |
| `void` | [dal.set.field()](dal.set.field.md) | `( string fld_name, void value, [ long element ] )` |
| `long` | [dal.set.property()](dal.set.property.md) | `( string class_name, long object_set, const string prop_name, value, long mode )` |
| `long` | [dal.set.property.with.check()](dal.set.property.with.check.md) | `( string class_name, long object_set, const string prop_name, value )` |
| `void` | [dal.skip.never.applicable.checks()](dal.skip.never.applicable.checks.md) | `( )` |
| `void` | [dal.start.business.method()](dal.start.business.method.md) | `( long|string set_id, string name, ref long retval [, arg ]... )` |
| `long` | [dal.store.cdf.fields()](dal.store.cdf.fields.md) | `( string tbl.name )` |
| `long` | [dal.submit()](dal.submit.md) | `( const string tbl.name )` |
| `void` | [dal.update()](dal.update.md) | `( string class_name, long object_set, ref long retval, long prop_check [, long mode [, long eflag ] ] )` |
| `long` | [dal.undo.check.out()](dal.undo.check.out.md) | `( const string tbl.name )` |
| `long` | [db.bind()](db.bind.md) | `( string table_name( 9 ) [, ref string buffer( . ) [, long comp_nr ] ] )` |
| `long` | [db.change.order()](db.change.order.md) | `( long table_id, long index_nr [, long comp_nr ] )` |
| `long` | [db.check.restricted()](db.check.restricted.md) | `( long table_id, long mode, ref string message( 256 ) )` |
| `long` | [db.check.row.changed()](db.check.row.changed.md) | `( long table_id )` |
| `long` | [db.check.row.dlocked()](db.check.row.dlocked.md) | `( long table_id )` |
| `long` | [db.check.row.domains()](db.check.row.domains.md) | `( long table_id, ref string fld_name( 18 ) )` |
| `long` | [db.clear.table()](db.clear.table.md) | `( long table_id[, long flag [, long comp_nr ] ] )` |
| `long` | [db.columns.to.record()](db.columns.to.record.md) | `( long table_id )` |
| `long` | [db.create.table()](db.create.table.md) | `( long table_id [, long comp_nr ] )` |
| `long` | [db.curr()](db.curr.md) | `( long table_id [, long lock ] )` |
| `long` | [db.delete()](db.delete.md) | `( long table_id [, long mode [, long eflag ] ] )` |
| `long` | [db.drop.table()](db.drop.table.md) | `( long table_id [, long flag ] [, long comp_nr ] )` |
| `long` | [db.eq()](db.eq.md) | `( long table_id [, long lock ] )` |
| `long` | [db.error()](db.error.md) | `( [ long table_id ] )` |
| `string` | [db.error.message()](db.error.message.md) | `( )` |
| `long` | [db.first()](db.first.md) | `( long table_id [, long lock ] )` |
| `long` | [db.flush()](db.flush.md) | `( )` |
| `long` | [db.ge()](db.ge.md) | `( long table_id [, long lock ] )` |
| `boolean` | [db.get.error.bypass()](db.get.error.bypass.md) | `( [ ref boolean with.retry ] )` |
| `long` | [db.get.physical.compnr()](db.get.physical.compnr.md) | `( string tblname, long logical.compnr )` |
| `long` | [db.gt()](db.gt.md) | `( long table_id [, long lock ] )` |
| `long` | [db.indexinfo()](db.indexinfo.md) | `( long table_id, long index_nr, ref long index_info( 32, 3 ), ref long indexparts, ref boolean indexdups, ref boolean indexactive )` |
| `long` | [db.insert()](db.insert.md) | `( long table_id [, long mode [, long eflag ] ] )` |
| `long` | [db.last()](db.last.md) | `( long table_id [, long lock ] )` |
| `long` | [db.le()](db.le.md) | `( long table_id [, long lock ] )` |
| `long` | [db.lock.table()](db.lock.table.md) | `( long table_id [, long comp_nr ] )` |
| `long` | [db.lt()](db.lt.md) | `( long table_id [, long lock ] )` |
| `long` | [db.max.retry()](db.max.retry.md) | `( )` |
| `long` | [db.next()](db.next.md) | `( long table_id [, long lock ] )` |
| `long` | [db.nr.indices()](db.nr.indices.md) | `( long table_id, ref long nr_indices )` |
| `long` | [db.nr.rows()](db.nr.rows.md) | `( long table_id, ref long nr_rows [, long comp_nr ] )` |
| `long` | [db.permission()](db.permission.md) | `( long table_id [, string field( 18 ) [, ref string buffer( . ) ] ] )` |
| `long` | [db.prev()](db.prev.md) | `( long table_id [, long lock ] )` |
| `boolean` | [db.record.changed()](db.record.changed.md) | `( long table_id )` |
| `long` | [db.record.to.columns()](db.record.to.columns.md) | `( long table_id )` |
| `long` | [db.ref.handle.mode()](db.ref.handle.mode.md) | `( string table_name( 9 ), long mode )` |
| `void` | [db.restore.record()](db.restore.record.md) | `( long table_id )` |
| `long` | [db.retry.hit()](db.retry.hit.md) | `( )` |
| `void` | [db.retry.point()](db.retry.point.md) | `( )` |
| `long` | [db.row.length()](db.row.length.md) | `( long table_id, ref long row_length )` |
| `void` | [db.set.error.bypass.off()](db.set.error.bypass.off.md) | `( )` |
| `long` | [db.set.error.bypass.on()](db.set.error.bypass.on.md) | `( [ boolean with.retry ] )` |
| `long` | [db.set.to.default()](db.set.to.default.md) | `( long table_id )` |
| `void` | [db.store.record()](db.store.record.md) | `( long table_id )` |
| `long` | [db.unbind()](db.unbind.md) | `( long table_id )` |
| `long` | [db.update()](db.update.md) | `( long table_id [, long mode [, long eflag ] ] )` |
| `void` | [for.each.record.in.view.do()](for.each.record.in.view.do.md) | `( string callback_function )` |
| `void` | [on.main.table()](on.main.table.md) | `( function_name [, ... ] )` |
| `void` | [restore.rcd.main()](restore.rcd.main.md) | `( long occurrence )` |
| `void` | [set.limits.off()](set.limits.off.md) | `( )` |
| `long` | [set.transaction.readonly()](set.transaction.readonly.md) | `( )` |
| `void` | [skip.io()](skip.io.md) | `( string mesg( 14 ) [, ... ] )` |
| `void` | [store.occ.max(), store.occ.min()](store.occ.maxmin.md) | `( )` |
| `void` | [store.occ.max(), store.occ.min()](store.occ.maxmin.md) | `( )` |
| `void` | [sum.records.in.view()](sum.records.in.view.md) | `( string column( n ), ref double result, ... )` |
| `string` | [this.dal()](this.dal.md) | `( )` |
| `void` | [to.key()](to.key.md) | `( long key_number, [ long nr.view.fields ] )` |
| `void` | [with.object.set.do()](with.object.set.do.md) | `( function_name, argument, ... )` |
| `void` | [with.old.object.values.do()](with.old.object.values.do.md) | `( function_name, argument, ... )` |
Remark  For using the DAL functions, you must include <bic_dam> in your script.

## Related topics
- [Database operations overview](overview.md)
