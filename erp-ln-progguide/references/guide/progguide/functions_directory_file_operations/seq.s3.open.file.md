# seq.s3.open.file()

## Syntax:
`function long seq.s3.open.file( long bucket, string name, string modifier )`

## Description
This function opens an S3 element for either reading or writing, which then acts very similar to an ordinary file stream. Most seq.* functions can then be used to act on the stream that is returned. Exceptions are functions that move the file pointer, which cannot be used on writing streams. Tell and seek presently work with reading streams, but are not guaranteed to continue to work.
An S3 element opened for reading is not locked and may be removed or replaced. If it is replaced, its behavior depends on whether versioning is enabled on the bucket in question. With versioning enabled, the stream will stick to the same version until the file is reopened.
Similarly, no object is created when it is opened for writing. The element is only constructed when seq.close() is called on the writing stream. When there are multiple elements with the same bucket and name created simultanenously, later versions will replace the object that already exists. However, if versioning is enabled on the bucket, then the previous object will continue to be accessible, at least until previous versions are purged based on the bucket rules.
Note that accessing objects in a versioned bucket requires a different AWS S3 permission level than accessing objects in ordinary buckets. You may get a permission denied error when attempting to read from such an object, if you lack this permission. In that case, you may request your AWS S3 administrator to grant you that permission, or as a last resort add a resource to lib/defaults/all: s3_disable_versioning:1.
By default, writes to S3 are buffered. Upload streams have a buffer of 5 MB, while downloads have a buffer of 16kB. This is efficient for most cases, but when there are a lot of calls to read small amounts of data, it may be very slow. In such cases, the download buffer size may be customized. This is done by adding {s3_download_bufsize=[number]} to the beginning. Note that this increases memory usage, and discretion is advised both with extremely large buffer sizes, as well as with larger buffers for streams that are kept open for a long time. Upon closing, the buffer memory is freed.
Sharing S3 streams between 3GL processes is not allowed.
Note that all data written to an S3 stream will be lost if seq.close() is not called on a writing stream before the 3GL process exits.

## Arguments
| | | |
|---|---|---|
| `long` | `bucket` |  The location (bucket and prefix) on S3. Currently, S3.location.appdata and S3.location.tmp are supported (which may be the same). The difference is normally that anything uploaded to the tmp bucket is automatically deleted within a certain period of time.  |
| `string` | `name` |  The name which is appended to the key base.  |
| `string` | `modifier` |  The mode in which the element is opened. On S3, only "r" (read) and "w" (write) are supported.  |

## Return values
| | |
|---|---|
| >=1 | Success; S3 stream pointer returned for use in subsequent operations.  |
| <1 | Error; that is, the negative value of the equivalent of the system error (for example, for a permission error, the function returns -13, or when opening a non-existent object for reading, the function returns -ENOENT).  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2450.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long fd
| Effective path: s3://$(BUCKET)/$(KEY_BASE)/test/test2
fd = seq.open.file(S3.location.appdata, "test/test2", "w")
seq.write("test", 4, fd)
seq.close(fd)

string buffer(512)
fd = seq.open.file(S3.location.appdata, "test/test2", "r")
seq.read(buffer, 512, fd)
| Closing a read stream does nothing except free up resources in the bshell itself.
seq.close(fd)

| Increase download buffer size to 1 MB. This stream uses 1 MB of memory regardless of whether it is actually used.
fd = seq.open.file(S3.location.appdata, "{s3_download_bufsize=1048576}test/test2", "r")
| Free the 1 MB of memory.
seq.close(fd)
```

## Related topics
- [seq.s3.ls()](seq.s3.ls.md)
- [file.s3.rm()](file.s3.rm.md)
