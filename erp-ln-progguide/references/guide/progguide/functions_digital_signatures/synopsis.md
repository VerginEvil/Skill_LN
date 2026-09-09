# Digital Signatures synopsis
| | | |
|---|---|---|
| General functions |  |  |
| `long` | [sig.get.keys.info](sig.get.keys.info.md) | `(string i.user, ref long o.keyinfo.node)` |
| `void` | [sig.destroy.request](sig.destroy.request.md) | `(long i.request)` |
| Sign request |  |  |
| `long` | [sig.init.sign.request](sig.init.sign.request.md) | `()` |
| `long` | [sig.sign.execute.request](sig.sign.execute.request.md) | `(long i.request)` |
| `void` | [sig.sign.set.document](sig.sign.set.document.md) | `(long i.request, string i.document)` |
| `void` | [sig.sign.set.output](sig.sign.set.output.md) | `(long i.request, string i.document)` |
| `void` | [sig.sign.set.string](sig.sign.set.string.md) | `(long i.request, string i.string)` |
| `string` | [sig.sign.get.output.string](sig.sign.get.output.string.md) | `(long i.request)` |
| `void` | [sig.sign.set.key.info](sig.sign.set.key.info.md) | `(long i.request, boolean i.on.hsm, long i.slot, string i.password, [string i.alias])` |
| `void` | [sig.sign.set.format](sig.sign.set.format.md) | `(long i.request, string i.format)` |
| `void` | [sig.sign.set.packaging](sig.sign.set.packaging.md) | `(long i.request, string i.packaging)` |
| `void` | [sig.sign.set.container](sig.sign.set.container.md) | `(long i.request, string i.type)` |
| `void` | [sig.sign.set.level](sig.sign.set.level.md) | `(long i.request, string i.level)` |
| `void` | [sig.sign.set.digest.algorithm](sig.sign.set.digest.algorithm.md) | `(long i.request, string i.digest)` |
| `long` | [sig.sign.set.visual.representation](sig.sign.set.visual.representation.md) | `(long i.request, string i.text, string i.image.path, i.signature.field)` |
| `void` | [sig.sign.set.visual.representation.position](sig.sign.set.visual.representation.position.md) | `(long i.request, long i.visual.representation, long i.xpos, long i.ypos, [long i.width, long i.height])` |
| `void` | [sig.sign.set.visual.representation.image.alignment](sig.sign.set.visual.representation.image.alignment.md) | `(long i.request, long i.visual.representation, string i.vertical)` |
| `void` | [sig.sign.set.visual.representation.text.position](sig.sign.set.visual.representation.text.position.md) | `(long i.request, long i.visual.representation, string i.horizontal.alignment, string i.position)` |
| `void` | [sig.sign.set.visual.representation.text.color](sig.sign.set.visual.representation.text.color.md) | `(long i.request, long i.visual.representation, long i.foreground, long i.background)` |
| `long` | [sig.sign.set.visual.representation.text.font](sig.sign.set.visual.representation.text.font.md) | `(long i.request, long i.visual.representation, string i.name, long i.size, boolean i.bold, boolean i.underlined, boolean i.italic)` |

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures examples](examples.md)
