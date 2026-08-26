# get.local.filename()

## Syntax:
`#include <bic_desktop>`
`function string get.local.filename( )`

## Description
*Deprecated.* This function returns the last client filename used by the function [server2client()](server2client.md) or [client2server()](client2server.md). When the last server2client() or client2server() function failed, this function will return an empty string.

## Return values
The client filename or an empty string

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

if server2client(bse.tmp.dir$() & "/test1.txt",
		"", false, false ) = 0 then
	client.filename = get.local.filename()
endif
```
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
