# Database Change Management (DBCM) overview

## Overview
Database Change Management has been implemented to support Document Authorization, using ION Workflow. Document Authorization is about approving or rejecting changes made to Business Objects, in a controlled way.
In case a user makes changes to a Business Object in Infor LN, e.g. a Sales Order, by modifying header data, or by adding, changing and/or removing lines, these changes have to be submitted for approval. Only once these changes have been approved, the Business Object may be processed further.
This is where DBCM comes in. DBCM provides a mechanism which allows 2 versions of the same Business Object to exist during a certain time-frame: a checked-in version and a checked-out version. When a user changes a Business Object, a checked-out version is created automatically, which is only visible in maintain sessions for that particular Business Object. The rest of the ERP system will not know about this version. This checked-out version is a kind of scratch version. A user can change whatever he likes, changes will not become visible to the rest of the system until he submits the changes, and someone approves these changes. It is also possible to undo the changes, and revert back to the original version.

## Modeling and Deploying Document Authorization
In order to support Document Authorization for a Business Object, a Model must be defined using the Object Change Management modeling sessions (ttocm0101m000). This model defines for what user actions the Application supports Document Authorization. A customer can choose for which Business Objects he wants to use Document Authorization, by specifying this in a Deployment (ttocm0111m000).
When the Model describes two Object Types A and B, and the customer uses Document Authorization for Object Type A, DBCM will not create checked-out versions for instances of Object Type B. Instances of Object Type A will be checked-out always. Depending on the active user actions in the Deployment, submitting changes will either invoke application logic to publish a Workflow BOD to ION, in order to get approval, or it will lead to an automatic check-in of the object.

## Prerequisites
In order to support Document Authorization, the application must make use of the DAL2 concept. The DAL of the root table must implement two new hooks: the [on.submit()](../functions_dal/on.submit.md) and the [on.recall()](../functions_dal/on.recall.md) hooks. This first hook is executed when changes are submitted for approval. The latter hook is executed when the submit must be recalled. Both these hooks must publish a Workflow BOD to ION Workflow.

## Application changes
In order to support Document Authorization, the application must be adapted.
Once a Business Object is checked-out, no changes to any related Business Objects of another Object Type are allowed. This means the DAL should only update tables which belong to the Business Object itself. Only during checking-in, Business Objects of other Object Types may be updated. In order to support this, function [dbcm.object.is.being.checked.in()](dbcm.object.is.being.checked.in.md) must be must be used.
When a session can be used to change data of a Business Object for which Document Authorization must be supported, this session must specify the selected Object Type, so the portingset knows whether to include checked-out versions when selecting data from the database. For maintain sessions this is done automatically by the 4GL Engine, based on the maintable. For update sessions, this must be done using functions [dbcm.select.object.type()](dbcm.select.object.type.md) or [dbcm.select.object.instance()](dbcm.select.object.instance.md).
Furthermore, the session must indicate the user action which is being performed. E.g. when the user presses the button 'Release to Warehousing', and this supports Document Authorization, the application must indicate that this action is being performed by the application logic. DBCM can then determine whether this action requires approval or not.
The 4GL Engine supports 3 standard actions: inserting, updating and deleting via the User Interface. All other (application specific) actions must be selected by the application using function [dbcm.select.object.action()](dbcm.select.object.action.md).

## Checked-out Business Object states
A Business Object can have one of the following states:
- *Draft*
- The Object is in the Draft state; it is checked-out, it can be modified and any change can be submitted, or any change can be undone by doing a "Revert to Approved" on the User Interface.
- *Draft (Revision)*
- The Object is in the Draft state, for a second time; this state is equal to the *Draft* state, except that an Object can only enter this state after a Recall of any submitted change was successful.
- *Pending*
- The Object is in the Pending state; this means all changes to the Object have been submitted and the user must wait until the changes are Approved or Rejected. The Object cannot be modified.
- *Recall Requested*
- The Object is in the Recall Requested state; the user made a request to ignore all submitted changes, as he e.g. wants to make more changes to the Object. The Object cannot be modified.
- *Rejected*
- The Object is in the Rejected state; submitted changes were not approved. The user must either make other changes and re-submit them, or perform a Revert to Approved. The Object can be modified.
- *Approval Received*
- The Object is in the Approval Received state; usually this state will not be visible to the user. It can only be visible if somehow, after receiving an Approval, the Object cannot be checked-in. In this situation an Admin must be involved in order to force a check-in, or to discard changes and perform a Revert to Approved. The Object can be modified.
- *Approved*
- The Object is in the Approved state; submitted changes have been Approved, and the Object has been checked-in. The Object can be modified.

## Related topics
- [Database Change Management operations synopsis](synopsis.md)
