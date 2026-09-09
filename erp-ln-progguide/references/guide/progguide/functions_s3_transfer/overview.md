# S3 transfer functions overview

## Overview
The S3 transfer functions support transferring files and directories from and to AWS S3.

## Asynchronous transfers
If required, transferring can be done in an asynchronous way. The calling program can then continue doing other processing.
The following functions start a transfer in an asynchronous way:

- [s3.transfer.start.copy](s3.transfer.start.copy.md)

- [s3.transfer.start.copy.directory](s3.transfer.start.copy.directory.md)

- [s3.transfer.start.download](s3.transfer.start.download.md)

- [s3.transfer.start.download.directory](s3.transfer.start.download.directory.md)

- [s3.transfer.start.upload](s3.transfer.start.upload.md)

- [s3.transfer.start.upload.directory](s3.transfer.start.upload.directory.md)

## Progress reporting via a progress listener
The S3 transfer functions support reporting progress via a progress listener object. This is an object that defines callback functions for when progress reporting starts, when progress is updated, and when progress reporting stops. You can use function [s3.transfer.progress.listener](s3.transfer.progress.listener.md) and pass that to the functions that start or perform the transfer. In this way, at the right times, a progress indicator will be created, updated and destroyed.

## S3 paths, URIs, buckets, keys and locations
See [S3 functions overview](../functions_s3/overview.md) for more information.

## Error handling
The synchronous S3 transfer functions return an error code and set a DAL error message when an error occurs. The asynchronous S3 transfer functions return a transfer object that keeps track of the status of the transfer. In case of an error, this transfer object contains a result code that can be used by the application, but no DAL error message is set.

## Related topics
- [S3 transfer functions synopsis](synopsis.md)
