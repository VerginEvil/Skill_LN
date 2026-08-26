# set.refresh.rate()

## Syntax:
`function long set.refresh.rate( long rateInSeconds, [ long thresholdInSeconds ] )`

## Description
With this function the refresh rate of the session will be overruled temporary.
The refresh interval is part of the User Data Template. This interval is used for sessions where the Auto Refresh in standard commands is set.
This function overrules the setting of the session, also if the refresh interval is not defined on the User Data Template for the current user.

## Arguments
| | | |
|---|---|---|
| `long` | `rateInSeconds` |  The refresh rate of the session. Special values: 0: the refresh rate of the session will be set to its original refreshing rate. -1: the refreshing of the session will be stopped.  |
| `[ long` | `thresholdInSeconds ]` |  The duration of the refresh rate: 0: The refresh rate does not have an end time (default) > 0: The refresh rate will be changed for thresholdInSeconds. After thresholdInSeconds, the original refresh rate is restored.  |

## Return values
Error Code:
0: Successful completion
-1: Refresh rate must be greater than or equal to -1.
-2: Threshold must be greater than or equal to zero.
-3: No action on XML Response Node "Session Refresh"
-4: Refresh interval not supported

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
Note  This function is not supported for BW/WorkTop.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
