# get.client.timezone()

## Syntax:
`#include <bic_desktop>`
`function string get.client.timezone( )`

## Description
This returns the current Windows Timezone name of the local client (if available).
In case of LN UI the local client is not accessible. For backward compatibility the timezone of the back-end user is converted to the Windows Timezone.
In case of Baan Windows this is the client machine on which BW is running.
In case of WebUI, this is the client machine on which the Internet Browser is running when running on a Windows system.
When the WebUI runs on a non-Windows operating system, an empty string is returned.
The following time-zones are not supported by Microsoft:
1. Pacific\Chatham
1. Pacific\Kiritimati
1. Pacific\Marquesas
1. Pacific\Norfolk  These time-zones are matched with a near known time-zone. The conversion can be found in timezone table (session ttaad0160m000).

## Return values
| |
|---|
| The current Windows Timezone name of the client. The maximum length is 32 characters. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
