# Parallel Application Processing synopsis

## Client side functions
| | | |
|---|---|---|
| long | [par.get.no.of.server](par.get.no.of.server.md) | `( )` |
| long | [par.init.client.to.server](par.init.client.to.server.md) | `(long nr.of.servers, string server.session, [string support.session])` |
| boolean | [par.client.start.servers](par.client.start.servers.md) | `(long group.id, [long options])` |
| boolean | [par.client.send.message](par.client.send.message.md) | `(long group.id, string comm.string, [long server.number])` |
| long | [par.client.get.status](par.client.get.status.md) | `(long group.id, long server.number, ref long messages)` |
| long | [par.client.get.message](par.client.get.message.md) | `(long group.id, ref string comm.string)` |
| boolean | [par.client.wait.ready](par.client.wait.ready.md) | `([long group.id, long server.number])` |
| boolean | [par.client.close.servers](par.client.close.servers.md) | `(long group.id)` |

## Server side functions
| | | |
|---|---|---|
| boolean | [par.init.server.to.client](par.init.server.to.client.md) | `(ref long group.number, ref long server.number, [ref long tot.nr.servers])` |
| long | [par.server.get.message](par.server.get.message.md) | `(ref string comm.string)` |
| boolean | [par.server.send.message](par.server.send.message.md) | `(string comm.string)` |
| boolean | [par.server.question](par.server.question.md) | `(string question, ref string answer)` |
| long | [par.server.id](par.server.id.md) | `( )` |
| void | [par.server.retry.point](par.server.retry.point.md) | `( )` |
| void | [par.server.retry.hit](par.server.retry.hit.md) | `( )` |

## Support session functions
| | | |
|---|---|---|
| boolean | [par.support.init](par.support.init.md) | `(ref long group.number, ref long tot.nr.servers)` |
| long | [par.support.get.question](par.support.get.question.md) | `(ref string question)` |
| boolean | [par.support.send.answer](par.support.send.answer.md) | `(string answer, long server.number)` |

## Common functions
| | | |
|---|---|---|
| void | [par.abort.client.server](par.abort.client.server.md) | `(string error.message)` |
| boolean | [par.server.running](par.server.running.md) | `( )` |
| boolean | [par.client.running](par.client.running.md) | `( )` |
| boolean | [par.support.running](par.support.running.md) | `( )` |

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing Examples](examples.md)
