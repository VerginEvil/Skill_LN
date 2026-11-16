# Creating a chart manager client application
The window preferences, fonts, charts, chart types, and option sets for a particular Chart Manager session are defined in a Chart Manager application. When you start the Chart Manager from a program script, you specify the particular Chart Manager application you want to use.
To create a Chart Manager application, use the following steps.

- Start the Chart Manager Application Data session (ttchm1500m000)).

- Create a new application record.

- Define the option sets (Chart-Specific Options).

- Create a default window setting (Window Preferences).

- Start the Chart Manager from the Chart Manager Application Data session (ttchm1500m000).

- Create the chart types required to present the data.

By using the Business Chart Manager functions described in this document, you can create a client application that starts the Business Chart Manager and that sends data to and receives data from the Business Chart Manager. For further details on using the Chart Manager, see the session help.
The Business Chart Manager functions fall into three groups:
| | |
|---|---|
| Input functions | These send data from the application to the Chart Manager. The function names in this group end in.in |
| Output functions | These functions send data from the Chart Manager to the application. The function names in this group end in.out. Within this group, there is a further subdivision: Functions with the extension.first retrieve the first value for a particular object from the Chart Manager. Functions with the extension.next retrieve the next value for a particular object from the Chart Manager. Before you can call a.next function, you must already have retrieved the first value by calling the relevant.first function. |
| Other functions | Miscellaneous functions. For example, control functions or functions to start and end the Business Chart Manager. |

## Related topics
- [Chart manager overview](overview.md)

- [Chart manager synopsis](synopsis.md)

- [Chart manager example](example.md)
