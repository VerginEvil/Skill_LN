# PCM_OT_BUTTON – button object

## Overview
On the planning board you can create buttons to which you can link sessions or options. You must create a PCM_OT_BUTTON object for each button.

## Attributes
| | |
|---|---|
| PcmButtonId (long) | The unique identification number of the button. This is included in PCM_EVTPUSSBUTTON events, in order to identify the button that the user selected. |
| PcmButtonName(50) (string) | The text string for the button's label. |
| PcmButtonSensitive (long) | This indicates whether the button is currently enabled or disabled. The possible values are: true The button is enabled. false The button is disabled and cannot be selected. |

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
