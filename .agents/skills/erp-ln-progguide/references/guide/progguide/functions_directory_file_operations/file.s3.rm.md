# file.s3.rm()

## Syntax:
`function long file.s3.rm( long bucket, string name )`

## Description
This function removes an S3 object.
Note that it will return success even if the underlying element does not exist, like the UNIX rm command. A way to make sure that the object in question does exist, is to open it with seq.s3.open.file() in read mode, which will return -ENOENT if it does not.
If the bucket in question supports versioning, it will persist as the underlying version. Any open read streams on the element will then continue to function as expected, while they will fail if no versioning exists.

## Arguments
| | | |
|---|---|---|
| `long` | `bucket` |  The location (bucket and prefix) on S3. Currently, S3.location.appdata and S3.location.tmp are supported (which may be the same).  |
| `string` | `name` |  The name which is appended to the key base.  |

## Return values
| | |
|---|---|
| =0 | Success; S3 object deleted, or it did not exist to begin with. |
| <>0 | Error; for example, access denied or no S3 credentials. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2450.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function was renamed from seq.s3.rm() in [bshell TIV](../tiv/tiv_overview.md) [level 2450](../tiv/tiv_2450.md) to file.s3.rm() in [TIV](../tiv/tiv_overview.md) [level 2460](../tiv/tiv_2460.md).

## Example
```

long ret
| Will return 0 (success) even if the object does not exist.
ret = file.s3.rm(S3.location.appdata, "this/object/does/not/exist")

| Create an object to actually remove
long fd
fd = seq.open.file(S3.location.appdata, "test/test2", "w")
seq.write("test", 4, fd)
seq.close(fd)

| This will actually remove the object.
file.s3.rm(S3.location.appdata, "test/test2")
```

## Related topics
- [seq.s3.open.file()](seq.s3.open.file.md)

- [seq.s3.ls()](seq.s3.ls.md)
