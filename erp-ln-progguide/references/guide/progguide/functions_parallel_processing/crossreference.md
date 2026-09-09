# Parallel Application Processing Cross Reference
In the table below a cross reference is shown with the functions available in tccomdll0200. This table should help in migrating sessions which used tccomdll0200 for parallel bshell processing
| | |
|---|---|
| tccomdll0200 function | Tools par.* function |
| tccom.dll0200.init.client.to.server | par.init.client.to.server |
| tccom.dll0200.client.start.servers | par.client.start.servers |
| tccom.dll0200.client.server.exec | par.client.send.message |
| tccom.dll0200.client.server.ready | par.client.get.status |
| tccom.dll0200.client.disable.server | Not implemented |
| tccom.dll0200.client.enable.server | Not implemented |
| tccom.dll0200.client.get.message | par.client.get.message |
| tccom dll0200.client.send.message | par.client.send.message |
| tccom.dll0200.client.wait.for.all.ready | par.client.wait.ready |
| tccom dll0200.client.close.servers | par.client.close.servers |
| tccom.dll0200.client.export.mbox | Not implemented |
| tccom.dll0200.abort.client.server | par.abort.client.server |
| tccom.dll0200.init.server.to.client | par.init.server.to.client |
| tccom dll0200.server.send.ready | Implicit by par.server.get.message |
| tccom dll0200.server.send.message | par.server.send.message |
| tccom.dll0200.server.get.message | par.server.get.message |
| tccom.dll0200.server.retry.point | par.server.retry.point |
| tccom.dll0200.server.retry.hit | par.server.retry.hit |
| tccom.dll0200.server.end | exit |
| tccom.dll0200.get.no.of.server | par.get.no.of.server |
| tccom.dll0200.server.id | par.server.id |
| tccom.dll0200.client.running | par.client.running |
| tccom.dll0200.server.running | par.server.running |
| tccom.dll0200.set.attribute | Not implemented |

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)
