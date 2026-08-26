# BLOB handling synopsis

## Syntax
| | | |
|---|---|---|
| `long` | [db.blob.read](db.blob.read.md) | `(const string blob.locator, long offset, long num.bytes, ref string bytes.array, ref long num.bytes.read)` |
| `long` | [db.blob.read.xml](db.blob.read.xml.md) | `(const string blob.locator, long offset, ref long bytes.read, ref long xml.node, ref string error [ , long whitespacehandling ])` |
| `long` | [db.blob.read.ns.xml](db.blob.read.xml.ns.md) | `(const string blob.locator, long offset, ref long bytes.read, ref long xml.node, ref string error [ , long whitespacehandling ])` |
| `void` | [db.blob.append](db.blob.append.md) | `(const string blob.locator, long num.bytes, const string bytes.array [, long mode] [, long eflag]))` |
| `void` | [db.blob.append.xml](db.blob.append.xml.md) | `(const string blob.locator, long xml.node [, long mode] [, long eflag]))` |
| `void` | [db.blob.clear](db.blob.clear.md) | `(const string blob.locator [, long mode] [, long eflag]))` |
| `void` | [db.blob.size](db.blob.size.md) | `(const string blob.locator, ref long num.bytes)` |

## Related topics
- [BLOB handling overview](overview.md)
