# DsCstatusBar

## Description
A DsCstatusBar object provides a status bar that displays help and status information in a main window (DsCmwindow object). Each main window can include one DsCstatusBar object. The status bar is positioned at the bottom of the window. It occupies part of the client area of the window. When a status bar is added to a main window, the window size is adjusted so that the size of the client area is not affected.
The help and status messages are displayed in one or more panes in the status bar. There are three types of status bar panes:
- Default text pane. This displays the status field strings and tooltip strings for commands/buttons, as defined in the DsNcommandStrings attribute of the DsCmwindow object. This pane occupies the full width of the status bar not occupied by other status panes.The application can also write text to this pane using *change.object()*. Messages defined by the DsNcommandStrings attribute temporarily overwrite this text. But when these disappear, the last message sent to the default pane by the application is restored.
- Application-defined text panes. The application supplies text for these panes using *change.object()*. The application must specify the length of the panes when creating the status bar.
- Indicator panes. These indicate the current status of certain keyboard keys (for example, NUM LOCK and CAPS LOCK). Microsoft Windows supplies the text for the panes. The application must specify the availability of the panes when creating the status bar.

## Events
A DsCstatusBar object does not generate events.

## Attributes
| | | |
|---|---|---|
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNstatusIndicator (long)  | [CG] |  This specifies the indicators to be shown on the status bar. You can specify any combination of the following values: DSCAPS Caps Lock indicator. DSNUM Num Lock indicator. DSSCRL Scroll Lock indicator. DSKANA Kana Lock indicator (Japanese systems only). Indicators are displayed on the status bar in the above order.  |
|  DsNstatusLength (long array)  | [C] | Specifies the length (in characters) of application-defined text panes in the status bar. The number of entries in the array determines the number of application-defined panes displayed.  |
|  DsNstatusPane (long)  | [SQ] | This selects a status bar text pane for the DsNstatusText attribute. The pane numbers range from 0 to the total number of panes defined by DsNstatusLength. The default text pane is indexed by 0; this is also the default value.  |
| DsNstatusText | [SQ] | The text for the status bar text pane specified by DsNstatusPane. If DsNstatusPane is not set, the text is displayed in the default text pane. To clear a text pane, set this attribute to an empty string.  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
