# S3 transfer functions synopsis

## Synchronous S3 transfer functions
| | | |
|---|---|---|
| `long` | [s3.transfer.copy](s3.transfer.copy.md) | `( const string s3.source, const string s3.target, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.copy.directory](s3.transfer.copy.directory.md) | `( const string s3.source, const string s3.target, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.download](s3.transfer.download.md) | `( const string s3.file, const string file, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.download.directory](s3.transfer.download.directory.md) | `( const string s3.directory, const string directory, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.upload](s3.transfer.upload.md) | `( const string s3.file, const string file, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.upload.directory](s3.transfer.upload.directory.md) | `( const string s3.directory, const string directory, long progress.listener, long timeout.ms )` |

## Asynchronous S3 transfer functions
| | | |
|---|---|---|
| `long` | [s3.transfer.start.copy](s3.transfer.start.copy.md) | `( const string s3.source, const string s3.target, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.start.copy.directory](s3.transfer.start.copy.directory.md) | `( const string s3.source, const string s3.target, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.start.download](s3.transfer.start.download.md) | `( const string s3.file, const string file, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.start.download.directory](s3.transfer.start.download.directory.md) | `( const string s3.directory, const string directory, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.start.upload](s3.transfer.start.upload.md) | `( const string s3.file, const string file, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.start.upload.directory](s3.transfer.start.upload.directory.md) | `( const string s3.directory, const string directory, long progress.listener, long timeout.ms )` |
| `long` | [s3.transfer.result](s3.transfer.result.md) | `( long s3.transfer )` |
| `long` | [s3.transfer.status](s3.transfer.status.md) | `( long s3.transfer )` |
| `boolean` | [s3.transfer.finished](s3.transfer.finished.md) | `( long s3.transfer )` |
| `[ long ]` | [s3.transfer.wait.until.finished](s3.transfer.wait.until.finished.md) | `( long s3.transfer )` |
| `[ long ]` | [s3.transfer.cancel](s3.transfer.cancel.md) | `( long s3.transfer )` |
| `void` | [s3.transfer.delete](s3.transfer.delete.md) | `( long s3.transfer )` |

## S3 transfer progress related functions
| | | |
|---|---|---|
| `long` | [s3.transfer.progress.listener](s3.transfer.progress.listener.md) | `( long s3.transfer )` |
| `double` | [s3.transfer.percentage.complete](s3.transfer.percentage.complete.md) | `( long s3.transfer )` |
| `long` | [s3.transfer.total.bytes](s3.transfer.total.bytes.md) | `( long s3.transfer )` |
| `long` | [s3.transfer.transferred.bytes](s3.transfer.transferred.bytes.md) | `( long s3.transfer )` |
| `long` | [s3.transfer.type](s3.transfer.type.md) | `( long s3.transfer )` |
| `string` | [s3.transfer.description](s3.transfer.description.md) | `( long s3.transfer )` |
| `string` | [s3.transfer.current.source](s3.transfer.current.source.md) | `( long s3.transfer )` |
| `string` | [s3.transfer.current.target](s3.transfer.current.target.md) | `( long s3.transfer )` |
