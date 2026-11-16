# curl.version()

## Syntax:
`function string curl.version( )`

## Description
Retrieves the current version of the cURL library that is being used and the versions of the other major components (like OpenSSL), as space-separated strings. This can be used to easily verify the level of support offered by the current bshell. The website of cURL lists the "available from version" for every feature and option.

## Return values
Example:
libcurl/7.57.0 OpenSSL/1.1.0g

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Example
```

string lversion(100)
lversion = curl.version()
```

## Related topics
- [cURL handling overview](overview.md)
