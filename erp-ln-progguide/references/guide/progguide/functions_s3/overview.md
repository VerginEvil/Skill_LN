# S3 functions overview

## Overview
The S3 functions can be used to to deal with S3 paths, URIs and locations, as well as S3 objects and S3 folders.

## S3 paths, URIs, buckets, keys and locations
For each tenant, Infor LN supports 2 predefined S3 locations:
- the *S3 appdata location*; this is meant for long term storage
- the *S3 tmp location*; this is meant for short term storage   S3 stores objects in a *bucket*. Each object has a name which is called a *key*. The predefined S3 locations determine the bucket that is being accessed, as well as the first part of the key of the object, this is called the *prefix*. The bucket is different for each farm (Dev, QA, Pre-Prod, Prod), and the prefix of the key is tenant specific. In this way each tenant has its own unique S3 locations for storing objects.
An *S3 path* is a combination of a bucket and a key in the format: `<bucket>/<key>`. As the first part of the *key* is fixed, you can also say the format is: `<predefined-bucket>/<predefined-prefix>/<key>`. And as the combination of *predefined-bucket* and *predefined-prefix* is always one of the 2 supported S3 locations, you can also say the format is: `<predefined-location>/<key>`.
To support these predefined locations in a convenient way, Infor LN supports the following symbolic names:
- `${AWS_S3}`; this points to the S3 appdata location for the current tenant
- `${AWS_S3_TMP}`; this points to the S3 tmp location for the current tenant
- `AWS_S3`; this the File Manager way of referring to the S3 appdata location for the current tenant
- `AWS_S3_admin/tmp`; this is the File Manager way of referring to the S3 tmp location for the current tenant   Some external applications that interact with S3 do not use S3 paths, but use the bucket and key. Other applications use S3 URIs, which are S3 paths prefixed with `s3://`. To support exchanging information with these external applications via S3, functions are available to:
- expand an S3 path containing symbolic names to an S3 path containing the real bucket and key
- symbolize an S3 path containing a real bucket and key to an S3 path containing symbolic names
- get the bucket and key of an S3 path
- convert an S3 path to an S3 URI
- convert an S3 URI to an S3 path  It is also possible to convert an S3 path to an S3 location indicator (this is a long, like `S3.location.appdata`) and S3 key and vice vera. These are used by portingset functions like [seq.s3.open.file](../functions_directory_file_operations/seq.s3.open.file.md).
All S3 functions that access S3 will normalize the S3 path before accessing S3. That means that e.g. the following paths are referring to the same S3 object:
- `AWS_S3/documents/temp/../expenses.csv`
- `${AWS_S3}/documents/./expenses.csv`
- `AWS_S3/documents//expenses.csv`
- `${AWS_S3}/documents/expenses.csv`

## S3 objects and folders
S3 is not a real file system, but a so-called key-value store. The stored values are called objects, and can be files of any kind. The keys are the names of these files. Contrary to a file system there is no directory structure with parent and child directories or folders. For S3 a key like `path/to/my/s3-file.txt` is just a string to which a value (the file contents) is associated. The only difference with a key like `path-to-my-s3-file.txt` is that forward slashes are used instead of dashes, but these forward slashes have no meaning to S3.
Yet S3 provides a way to *simulate* a file system with a directory structure. When multiple S3 objects have the same prefix, ending on a certain delimiter character (e.g. the forward slash), then S3 can be used in a way that it seems like these S3 objects are stored in a directory. LN makes use of this behavior, but be aware that in fact it is not a directory structure in reality. This will become clear when doing actions like renaming a folder. On a regular file system, this is an atomic action of just changing the name of a single directory. On S3 this is not an atomic action, as it involves copying all files having the same prefix to files with a different prefix, and then deleting all original files.
As S3 can only store key value pairs, a folder is simulated by creating an S3 object with a size of 0 bytes having a name ending with a forward slash. E.g. `documents/` denotes a folder, while `documents` denotes a file.
Functions are available to read, write and remove, copy and move single S3 objects, to upload and download S3 objects from and to the regular file system, as well as to do actions on folders like listing their contents, and moving, copying, downloading and uploading complete folders with all of their contents.

## Error handling
All S3 functions that interact with S3 and return an error code, also set the predefined `e` variable. Common error values are:
| | |
|---|---|
| `EPERM (1)` | The operation is not permitted |
| `ENOENT (2)` | The S3 object was not found |
| `EIO (5)` | An I/O error occurred |
| `EBADF (9)` | An invalid stream handle was specified, e.g. the stream may have already been closed |
| `EAGAIN (11)` | The max number of open streams is reached, try again at a later time |
| `EACCES (13)` | Access to the specified S3 object is forbidden |
| `EEXIST (17)` | The specified S3 object or folder already exists |
| `EISDIR (21)` | The operation is not possible as the specified S3 object is a folder |
| `EINVAL (22)` | One of the function arguments has an invalid value |
| `EFBIG (27)` | The S3 object is too big |
| `ENOSPC (28)` | There is not enough space on either S3 or the regular file system (e.g. when downloading from S3 or uploading to S3) |
You can use [s3.error.argument$](s3.error.argument$.md) to get the name of the argument that is causing the error.

## Related topics
- [S3 functions synopsis](synopsis.md)
