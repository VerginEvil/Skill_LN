# Database Change Management operations synopsis

## DBCM Table functions
| | | |
|---|---|---|
| `long` | [dbcm.get.type.name()](dbcm.get.type.name.md) | `( const string tbl.name$, ref string obj.type$ )` |
| `long` | [dbcm.get.deployed.type.name()](dbcm.get.deployed.type.name.md) | `( const string tbl.name$, ref string obj.type$, [long comp] )` |
| `boolean` | [dbcm.is.cm.active()](dbcm.is.cm.active.md) | `( const string tbl.name$, [ long comp ] )` |
| `boolean` | [dbcm.is.root.table()](dbcm.is.root.table.md) | `( const string tbl.name$ )` |
| `boolean` | [dbcm.is.deployed.root.table()](dbcm.is.deployed.root.table.md) | `( const string tbl.name$, [long comp] )` |

## DBCM Object Type functions
| | | |
|---|---|---|
| `string` | [dbcm.get.object.type$()](dbcm.get.object.type$.md) | `( )` |
| `[ long ]` | [dbcm.select.object.type()](dbcm.select.object.type.md) | `( const string obj.type$ )` |
| `[ long ]` | [dbcm.select.session.object.type()](dbcm.select.session.object.type.md) | `( const string obj.type$ )` |
| `[ long ]` | [dbcm.set.object.type()](dbcm.set.object.type.md) | `( const string obj.type$ )` |

## DBCM Action functions
| | | |
|---|---|---|
| `string` | [dbcm.get.object.action$()](dbcm.get.object.action$.md) | `( )` |
| `boolean` | [dbcm.is.action.active()](dbcm.is.action.active.md) | `( )` |
| `[ long ]` | [dbcm.select.object.action()](dbcm.select.object.action.md) | `( const string action.id$ )` |

## DBCM Object functions
| | | |
|---|---|---|
| `long` | [dbcm.find.object.by.workflow.id()](dbcm.find.object.by.workflow.id.md) | `( const string wf.id$, ref string toid$ )` |
| `enum` | [dbcm.get.cm.status()](dbcm.get.cm.status.md) | `( const string toid$ )` |
| `string` | [dbcm.get.cm.status.desc$()](dbcm.get.cm.status.desc$.md) | `( const string toid$, enum prev_stat, enum curr_stat )` |
| `string` | [dbcm.get.cm.action$()](dbcm.get.cm.action$.md) | `( const string toid$ )` |
| `string` | [dbcm.get.object.id$()](dbcm.get.object.id$.md) | `( )` |
| `string` | [dbcm.get.root.table$()](dbcm.get.root.table$.md) | `( const string toid.or.obj.type$ )` |
| `string` | [dbcm.get.functional.id$()](dbcm.get.functional.id$.md) | `( const string toid$, [ long comp ] )` |
| `long` | [dbcm.get.user()](dbcm.get.user.md) | `( const string toid$, ref string user$ )` |
| `long` | [dbcm.get.workflow.definition()](dbcm.get.workflow.definition.md) | `( const string toid$, ref string wf.def$ )` |
| `long` | [dbcm.get.workflow.id()](dbcm.get.workflow.id.md) | `( const string toid$, ref string wf.def$ )` |
| `long` | [dbcm.get.workflow.status.description()](dbcm.get.workflow.status.description.md) | `( const string tbl.name$, ref string wf.status.desc$, [string fld.name$, void fld.value, ...] )` |
| `boolean` | [dbcm.object.check.out.is.being.undone()](dbcm.object.check.out.is.being.undone.md) | `( const string toid$ )` |
| `boolean` | [dbcm.object.is.being.checked.in()](dbcm.object.is.being.checked.in.md) | `( const string toid$ )` |
| `boolean` | [dbcm.object.is.checked.in()](dbcm.object.is.checked.in.md) | `( const string toid$ )` |
| `boolean` | [dbcm.object.is.checked.out()](dbcm.object.is.checked.out.md) | `( const string toid$ )` |
| `long` | [dbcm.object.remains.checked.in()](dbcm.object.remains.checked.in.md) | `( ref long tbl.id, long cmac, ref boolean b.eval)` |
| `long` | [dbcm.read.object()](dbcm.read.object.md) | `( const string toid$, [ long comp ] )` |
| `long` | [dbcm.select.object.instance()](dbcm.select.object.instance.md) | `( const string toid$ )` |
| `long` | [dbcm.set.workflow.definition()](dbcm.set.workflow.definition.md) | `( const string toid$, const string wf.def$ )` |
| `long` | [dbcm.set.submitted()](dbcm.set.submitted.md) | `( const string toid$, const string wf.id$ )` |
| `long` | [dbcm.set.draft()](dbcm.set.draft.md) | `( const string toid$ )` |
| `long` | [dbcm.set.recalled()](dbcm.set.recalled.md) | `( const string toid$ )` |
| `long` | [dbcm.set.approved()](dbcm.set.approved.md) | `( const string toid$ )` |
| `long` | [dbcm.set.not.started()](dbcm.set.not.started.md) | `( const string toid$ )` |
| `long` | [dbcm.reject()](dbcm.reject.md) | `( const string toid$, const string reason$ )` |

## DBCM Record functions
| | | |
|---|---|---|
| `long` | [dbcm.get.rcd.action()](dbcm.get.rcd.action.md) | `( long tbl.id )` |
| `enum` | [dbcm.get.rcd.prst()](dbcm.get.rcd.prst.md) | `( ref long tbl.id )` |
| `string` | [dbcm.get.rcd.toid$()](dbcm.get.rcd.toid$.md) | `( long tbl.id )` |
| `void` | [dbcm.set.rcd.toid()](dbcm.set.rcd.toid.md) | `( long tbl.id, const string toid$ )` |

## DBCM Check functions
| | | |
|---|---|---|
| `boolean` | [dbcm.checked.out.objects.present()](dbcm.checked.out.objects.present.md) | `( long comp, [string tbl.name$] )` |
| `long` | [dbcm.select.checked.in.mode()](dbcm.select.checked.in.mode.md) | `( boolean value )` |

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
