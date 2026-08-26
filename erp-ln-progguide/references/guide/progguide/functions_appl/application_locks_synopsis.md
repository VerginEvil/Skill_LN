# Application locks: synopsis
| | | |
|---|---|---|
| `long` | [appl.delete()](appl.delete.md) | `( const string name )` |
| `long` | [appl.delete.excl()](appl.delete.excl.md) | `( const string name )` |
| `long` | [appl.get.user()](appl.get.user.md) | `( const string name, ref string user(12), [ref string session(13)] )` |
| `long` | [appl.get.user.excl()](appl.get.user.excl.md) | `( const string name, ref string user(12), [ref string session(13)] )` |
| `long` | [appl.get.owner()](appl.get.owner.md) | `( const string name )` |
| `long` | [appl.get.owner.excl()](appl.get.owner.excl.md) | `( const string name )` |
| `long` | [appl.modify()](appl.modify.md) | `( const string name, long old.owner, long new.owner )` |
| `long` | [appl.modify.excl()](appl.modify.excl.md) | `( const string name, long old.owner, long new.owner )` |
| `long` | [appl.set()](appl.set.md) | `( const string name, long mode )` |
| `long` | [appl.set.excl()](appl.set.excl.md) | `( const string name )` |

## Related topics
- [Application locks: overview](application_locks_overview.md)
