# Dynamic SQL queries synopsis
| | | |
|---|---|---|
| `long` | [sql.break](sql.break.md) | `( long sql_id )` |
| `long` | [sql.close](sql.close.md) | `( long sql_id )` |
| `long` | [sql.exec](sql.exec.md) | `( long sql_id )` |
| `long` | [sql.fetch](sql.fetch.md) | `( long sql_id )` |
| `boolean` | [sql.get.select.all.data.languages](sql.get.select.all.data.languages.md) | `( )` |
| `long` | [sql.parse](sql.parse.md) | `( string query(.), [ long mode, ref string error.msg, ref.long error.line, const string annotation,... ] )` |
| `long` | [sql.select.bind](sql.select.bind.md) | `( long sql_id, long pseudo_var, var_name(.) )` |
| `long` | [sql.set.rds.full](sql.set.rds.full.md) | `( long sql.id, long size )` |
| `boolean` | [sql.set.select.all.data.languages](sql.set.select.all.data.languages.md) | `( boolean select.all.data.languages )` |
| `long` | [sql.where.bind](sql.where.bind.md) | `( long sql_id, long pseudo_var, var_name(.) )` |

## Related topics
- [Dynamic SQL queries overview](overview.md)
