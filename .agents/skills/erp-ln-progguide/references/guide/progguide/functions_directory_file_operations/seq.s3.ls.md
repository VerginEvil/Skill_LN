# seq.s3.ls()

## Syntax:
`function long seq.s3.ls( long bucket, string name, [ long options ] )`

## Description
This function returns a list of objects present in a given S3 location. It returns a JSON array with the objects sorted lexicographically.
Note that it is not recursive and only one level is returned: further prefixes (the S3 version of directories) and objects contained therein are omitted.
If there are no objects with a given prefix, an empty JSON array will be returned.
*Behavior when TIV level of object is*[2490](../tiv/tiv_2490.md)*or above:*
A third optional argument may be provided (see the argument section for the details).

## Arguments
| | | |
|---|---|---|
| `long` | `bucket` |  The location (bucket and prefix) on S3. Currently, S3.location.appdata and S3.location.tmp are supported (which may be the same).  |
| `string` | `name` |  The name which is appended to the key base. Note that this must end in a '/' for all elements with a given prefix to be returned.  |
| `[ long` | `options ]` |  To include directories to only display them, the options S3.ls.include.directories or S3.ls.only.directories may be used. Note that these options are mutually incompatible.  |

## Return values
| | |
|---|---|
| >=1 | Success; returned a valid but possibly empty JSON array. |
| <1 | Error. S3 credentials may be lacking, or the user may not have access to that particular bucket or location. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2460.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long json
json = seq.s3.ls(s3.location.appdata, "test/test")

| The directories/prefixes will be shown at the top, in lexicographical order,
| and they will end with the '/' character.
json = seq.s3.ls(s3.location.appdata, "test/test", S3.ls.include.directories)

| Objects are hidden.
json = seq.s3.ls(s3.location.appdata, "test/test", S3.ls.only.directories)
```

## Related topics
- [seq.s3.open.file()](seq.s3.open.file.md)

- [file.s3.rm()](file.s3.rm.md)
