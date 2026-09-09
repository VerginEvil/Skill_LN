# tt.user.data()

## Syntax:
`function boolean tt.user.data( string user(12), long property,... )`

## Description
This function retrieves one or more properties of an Infor LN user.
The arguments must meet the following conditions:

- at least 3 arguments

- an odd number of arguments

- a property must be a known property (i.e. in the list below)

- the data type of the argument following a property must be correct

## Arguments
| | |
|---|---|
| Property | Value |
| UD_NAME | The User Name (mb string 30) |
| UD_SECURITY_USER | The Infor Security User (mb string 132) |
| UD_PACKAGE_COMB | The user's package combination (string 8) |
| UD_COMPANY | The user's default company (long) |
| UD_FIN_COMPANY | The user's default logistical company (long); -1 means logistical/financials companies is disabled for this user |
| UD_LOG_COMPANY | The user's default financial company (long); -1 means logistical/financials companies is disabled for this user |
| UD_SOFTWARE_LANG | The user's software language, like "2" for English (string 1) |
| UD_DATA_LANG | The user's data language, like "en_US" for US English (string 5) |
| UD_EMAIL_ADDRESS | The user's e-mail address (string 80) |
| UD_PHONE_NUMBER | The user's phone number (string 20) |
| UD_FAX_NUMBER | The user's fax number (string 20) |
| UD_TIME_ZONE | The user's time zone (string 50) |

## Return values
| | |
|---|---|
| false | error; user not found or invalid input |
| true | success |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
