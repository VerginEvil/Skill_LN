# PCM_OT_MENU - menu object

## Overview
On the planning board, you can create a menu structure that consists of one or more menu items. Users can click on these items to initiate actions, such as starting a session. Each part of the menu structure consists of a parent menu item and related child menu item(s). You must create a PCM_OT_MENU object for each menu item.

## Attributes
| | |
|---|---|
| PcmMenuParent (long) | This indicates the object ID of the item's parent item. The parent ID of a parent menu item is 0. |
| PcmMenuId (long) | The unique identification number of the menu item. This is included in PCM_EVTMENUSELECT events, in order to identify the menu item to which the event relates. |
| PcmMenuName(50) (string) | The description of the menu item. |
| PcmMenuSensitive (long) | This indicates whether the menu item is currently enabled or disabled. The possible values are: true The menu item is enabled. false The menu item is disabled and cannot be selected. |
| PcmMenuChecked (long) | This specifies whether or not a tick is placed beside the menu item to indicate its 'selected' status. The possible values are: true A tick is placed beside the menu item. false No tick is placed beside the menu item, or an existing tick is removed. |

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
