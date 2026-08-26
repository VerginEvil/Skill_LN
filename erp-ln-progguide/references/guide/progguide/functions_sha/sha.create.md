# sha.create()

## Syntax:
`function long sha.create( )`

## Description
Allocates memory to contain the state of the Secure Hash Algorithm.

## Return values
An Id corresponding to the allocated state is returned. This Id can be used in subsequent calls to [sha.initialize()](sha.initialize.md), [sha.add.data()](sha.add.data.md), and [sha.compute.output()](sha.compute.output.md). The returned Id can only be used in the original BAAN process where sha.create was called, and is useless in other BAAN processes in the same bshell. The allocated memory is freed explicitly by passing the Id to [sha.destroy()](sha.destroy.md). The allocated memory is freed implicitly when the BAAN process exits. Any number of Secure Hash Algorithm states may be in use concurrently.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Secure Hash Algorithm overview](sha_overview.md)
- [Secure Hash Algorithm synopsis](sha_synopsis.md)
