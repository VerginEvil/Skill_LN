# Composite Sessions overview
Composite Sessions is a UI pattern through which more than one session can be shown, side-by-side, in one frame. These sessions are started and stopped by one user action. From an end-user perspective, a composite session behaves as one session. The composite nature is an implementation detail of which the end-user should not be aware.
Technically a composite session consists of one controller session and 2, 3 or 4 child sessions. These child sessions can be synchronized (so related data is shown) and drag and drop operations between these child sessions can be implemented.

## Restrictions
Below a number of important restrictions for composite sessions are listed.
- Composite sessions can only be used in the Infor Enterprise Server Web UI (so not in Worktop/BW)
- A composite child session must be a read-only session or an editable overview session.
- A composite child session may be a plain 4GL-Session a Document Viewer or a standalone GBF session (so not a GBF session running as a DLL inside a 4GL-Session, not a Multi-Main-Table session and not a programmable dialog based session)
- A composite child session may not use dynamic index switching (causing under the hood the session to be replaced by a new instance of the same session)
- Keyboard commands are sent to the child session which has the focus and not to the other child sessions within the same composite.
- When the user changes the splitter positions, these settings are not saved. So a composite session always starts with the default splitter positions

## Composite Session Layout
The Composite Controller is responsible for defining the composite session layout. It can do so by defining so-called split panes. Each split pane divides its container in two half's, divided by a splitter bar. The splitter bar can have a horizontal orientation or a vertical orientation. To each of the split pane half's either a child session or a new split pane can be added. In the next figure an example is shown of a composite session.
In this example, the first split pane divides the composite session with a vertical splitter into two half's. The second split pane divides the left-half of the first split pane with a horizontal splitter into two half's. The top-half of pane 2 is occupied by "child 1" and the bottom-half of pane 2 is occupied by "child 2". The right side of pane 1 is occupied by "child 3" (a GBF session).

## Composite Session Characteristics
Some general characteristics of Composite Sessions are:
- There is always one Controller session
- A Composite session contains 2, 3 or 4 child sessions
- The child sessions are rendered in 1, 2 or 3 split panes  Some characteristics of a Composite Controller Session are:
- To a controller session a script of type: "3GL (Without 4GL Engine)" must be linked. This script must include the file <bic_cps>
- The Controller session defines the initial splitter positions
- The Controller session always has a title bar and a status bar
- The Controller session controls the lifecycle of all child sessions (So any File-->Close command in a child session is always handled by the Controller session)   Some characteristics of a Composite Child Session are:
- Each Child session may optionally show a Title bar, Menu bar a standard toolbar and an application toolbar. Whether or not these components are shown is set in the Controller
- A session script can use function [is.composite.child()](is.composite.child.md) to determine whether it is running in a composite session context
- The standard items shown in the menu bar and toolbar depend on the session type. It makes no difference whether or not the session is run as a composite child.
- The session script can permanently disable certain standard commands when running in the context of a composite session by calling [standard.commands.off()](../functions_form_and_form_field_operations/standard.commands.off.md)
- The session script can hide certain form commands when running in the context of a composite session by calling [remove.form.commands()](../functions_form_and_form_field_operations/remove.form.commands.md)

## Implicit saves in composite sessions
When a Composite session consists of one or more editable 4GL-child sessions, an implicit save is done in the child session as soon as the focus moves from this child session to another composite child session. For instance when a user updates a field in a composite child session and then invokes a command in another composite child session, before this command is executed, a save of pending updates is done in the first composite child. This concept is similar to the concept implemented in MMT sessions

## Data synchronization in a composite session
Data synchronization between child sessions within a composite session is not provided by the tools but must be programmed in the application script. For example synchronization from a 4GL-multi-occurrence session to a GBF session can be setup as follows:
- 4GL-Section *choice.mark.occur:*, *after.choice:* can be used to signal that another record has been selected (check whether key fields differ from previous mark.occur). From this 4GL-Section call [prcm.notify()](../functions_prcm/prcm.notify.md), passing an XML node containing the key fields with their current values of the currently selected record.
- In the GBF session during startup register for specific prcm messages by calling [prcm.register()](../functions_prcm/prcm.register.md)
- In the GBF callback function [gbf.bms.received()](../functions_generic_browser_frameworkf/gbf.bms.received.md) handle the received prcm notification.
- Some helper functions are available to store and retrieve the key fields of a table in an XML object. These functions are described [Key fields Object overview](../functions_keyfields/overview.md).

## Drag and drop in a composite session
For Composite Child Sessions, support for drag and drop operations can be created. Below a table of possible combinations is shown
| | |
|---|---|
| Drag Source | Drop Target |
| 4GL Multi-occ. Session | 4GL Multi-occ. Session |
| 4GL Multi-occ. Session | GBF Session |
| GBF Session | 4GL Multi-occ. Session |
| GBF Session | GBF Session |
The implementation of this feature is based on the following design decisions
- A session can only become a Drop source when a specific call is done in the application script during session startup (see [enable.drag()](enable.drag.md) and [gbf.init()](../functions_generic_browser_frameworkf/gbf.init.md))
- A session can only become a Drop target for specific objects when a specific call is done in the application during session startup (see [enable.drop()](enable.drop.md) and [gbf.enable.drop()](../functions_generic_browser_frameworkf/gbf.enable.drop.md))
- A GBF session cannot differentiate on beforehand which GBF nodes are valid drag objects or drop targets. So the whole GBF tree is enabled or disabled for drag/drop. When the user performs a drag/drop operation for a node type which is not permitted, the GBF application can abort the operation with an error message. This approach is similar to the behavior of the drag/drop feature within a GBF tree.
- Session codes are used as an identifier for the type of objects which can be accepted by a drop target
- During a drag/drop operation a data exchange is done between two sessions. The data exchange is standardized and based on the Key fields object which is described [Key fields Object overview](../functions_keyfields/overview.md)
- The business logic related to a drag/drop operation must be implemented in the application script of the session which acts as the drop target

## Personalization and Composite Sessions
Personalization of the Composite Controller Session is not possible.
Personalization and conditional formatting data for Composite Child Sessions is possible and is stored in a separate context. When a Composite Child Session can both be run standalone and also in the context of a Composite session, the personalization and conditional formatting data for these contexts is not shared. When the same composite child session is used in more than one composite controller session, the personalization and conditional formatting data is shared. So personalization changes made in the context of one composite session is also visible when this same child session is used in the context of another composite session

## Related topics
- [Composite Sessions synopsis](synopsis.md)
- [Composite Sessions Code Examples](examples.md)
- [Key fields Object overview](../functions_keyfields/overview.md)
