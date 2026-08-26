# Composite Sessions synopsis
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
long
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
| | | |
|---|---|---|
|  | [cps.init()](cps.init.md) | `([long cps.type] )` |
|  | [cps.create.splitpane()](cps.create.splitpane.md) | `(long orientation, long divider [,long splipane] )` |
|  | [cps.add.child()](cps.add.child.md) | `(const string session.code, long bars, const string title long splitpane)` |
|  | [cps.add.tree.detail.session()](cps.add.tree.detail.session.md) | `(const string detail.session.code)` |
|  | [cps.set.tree.detail()](cps.set.tree.detail.md) | `(const string tree.session.code, const string detail.session.code, [long divider, const string tree.title])` |
|  | [cps.start()](cps.start.md) | `( )` |
|  | [is.composite.child()](is.composite.child.md) | `( )` |
|  | [is.tree.detail.child()](is.tree.detail.child.md) | `( )` |
|  | [cps.status.mess()](cps.status.mess.md) | `(const string message)` |
|  | [enable.drag()](enable.drag.md) | `( )` |
|  | [on.drop()](on.drop.md) | `(long from.pid, long collection, boolean copy)` |
|  | [enable.drop()](enable.drop.md) | `(const string session.code, const string on.drop.function)` |

## Related topics
- [Composite Sessions overview](overview.md)
- [Composite Sessions Code Examples](examples.md)
