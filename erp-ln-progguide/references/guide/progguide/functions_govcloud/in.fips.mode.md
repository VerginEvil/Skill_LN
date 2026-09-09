# in.fips.mode()

## Syntax:
`function long in.fips.mode( )`

## Description
Function to determine whether the bshell runs in FIPS-140-2 compliant mode. This function supports the 3GL/4GL engineer to write FIPS specific compliant code.

## Return values
| | |
|---|---|
| 1 | Bshell runs in FIPS-140-2 mode. NOTE: The function may return other values for other secure modes in the future. Make sure you test for values "1" (and not just "true") when you want to test for FIPS-140-2 mode. |
| 0 | Bshell does not run in a secure mode. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Related topics
- [GovCloud functions overview](overview.md)

- [GovCloud functions synopsis](synopsis.md)
