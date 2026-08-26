# start.ext.desk()

## Syntax:
`function long start.ext.desk( string application, [ long options, string title ] )`

## Description
Start the Workbench (desk) application. This function will return when the Workbench application is closed by the user.

## Arguments
```

<serverurl>/<sessioncode>_<version>_<release>[_<customer>]/<application>
```

##

##

##

##
```

https://nlbavwtech5.infor.com:8442/tdpur8350m000_B60_a_sy59/BuyerDesk.aspx
```

##

##

##
| | | |
|---|---|---|
| `string` | `application` |  This is the Web application name which implements the Workbench application. In case of a Silverlight based Workbench, this is the final part of the Web application on the Web server. For example: "BuyerDesk.aspx". In case of a HTML based Workbench, this is always fixed to the string: "workbench". This function will construct the complete URL to start the Workbench application as follows: serverurl This is the URL configured in session "Workbench Web Server (ttaad7530m000)" sessioncode This is the code of the current (3GL) Workbench session" version This is the version part of the VRC of the additional file related to the current (3GL) Workbench session" customer This is the customer part of the VRC of the additional file related to the current (3GL) Workbench session (may be empty)" So for example a complete URL might look like: |
| `[ long` | `options ]` |  Optional argument in which Workbench startup options can be specified. The options which can be specified here are: DSK.STATUSBAR This means that a standard status bar should be shown for this session. When this option is not passed, no status bar will be shown for this session. DSK.SINGLEINSTANCE This means that only one instance of this application can be started per user per Bshell. DSK.HTML This means that this is a HTML based Workbench which is based on the Workbench SDK. The default value (so when this option is not present) is: DSK.STATUSBAR + DSK.SINGLEINSTANCE  |
| `[ string` | `title ]` |  Optional argument in which a non-standard title of the Workbench session can be specified. When this argument is not present, the session description is used as the Workbench title. This argument can be useful when the same workbench application should have a different title which can only be determined at runtime.  |

## Return values
| | |
|---|---|
| 0 | on success |
| -1 | when this function fails |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Workbench Sessions overview](overview.md)
- [Workbench Sessions synopsis](synopsis.md)
