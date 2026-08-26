# Extension Modeler

Use the Infor LN Extension Modeler to add the logic around CDFs and how to tailor standard components.

This list shows the extension points for Infor LN:

- Domain

- Table

- Report

- Session

- BOD / BDE

- Menu

- Process

- OData REST API

In the Extension Modeler, you can set properties and hooks for those components. The implementation of the extension point for one component is called an extension. With an extension built for an extension point you change the behavior of a component. For example, by creating an extension for a session you can add additional fields to that session.

LN ’s extensibility is built upon LN ’s pluggable architecture. The standard application components of LN are plugged into the sockets of the runtime layers, which perform all common tasks, such as database access, screen handling, etc. Extensions are additional plugs into the runtime layers; sometimes, an extension can also handle as an adapter.

You can find the Extensibility sessions in Tools > Application Extensibility

This diagram shows this architecture: 1 The LN Runtime layer (bshell) runs the LN programs and handles all RDBMS and operating system actions. 2 The LN Tools layer is responsible for all common tasks regarding tables, screens, reports, BODs, BDEs, and OData REST APIs. This layer has several sockets where the Application layer can plug-in with properties and hooks into to perform the specific application functionality. For the Extension layer, additional sockets are available in the Tools layer. 3 The Application layer has a set of standard components that have properties and pieces of code. This results in the desired behavior of the DAL, 4GL, BOD, BDE, OData, and Report engines. 4 The Extension layer has a set of components with properties and pieces of code. This causes different behavior or results in the DAL, 4GL, BOD, BDE, OData, and Report engines. 5 The standard Application layer has coded actions that must be performed on a certain event. Those actions are plugged into the socket that is meant for this event. Those actions are executed by one of the tools engines when that event occurs. Examples:

- When a record is updated in a table, also another table must be updated. For example, when the quantity is changed in a sales order line, the inventory allocation also must be updated. In this case the DAL application component has an `after.save.object()` hook to perform the update for the inventory allocation.

- When a report is printed, for each detail line also a percentage must be calculated and printed. The report script has a `before.field` hook to calculate the percentage.

6 The Tools layer has also specific sockets for the Extension layer. The plug is created by adding an extension in the Extension Modeler. Examples:

- An overview session must show some additional fields, directly from database or a complex calculation. For example, for business partners the number of open purchase orders should be displayed. This field, with the code to calculate the value, must be added in the session extension.

- Infor Reporting report requires to print sub-details. Those sub-details must be added to the XML An data source by adding additional rows. You can do this in the report extension with the `write.row()` hook.

7 Next to the specific sockets for the extensions, extensions can also act as an adapter. In this case the standard plug is adapted. There is a standard plug that does specific actions when a record is saved. For example an update on the inventory allocation when a sales order line is inserted. The extension plug can do additional actions, for example inserting data in an own table. Adapters cannot bypass the standard behavior. LN (DAL / 4 GL / BOD / Odata/ Report LN bshell Application Extension 1 2 3 4 5 9 ools T layer Engines) Runtime () layer layer 6 7 8 LN Tools layer
(DAL/4GL/BOD/Odata/
Report Engines)
LN Runtime (bshell )
Application layer
Extension layer
1
2
3
4
5 6 7 8
9 8 The extension can remove a standard plug and connects its own plug to the socket. For example, some form commands of a session can be removed, and other form commands can be added. 9 Another concept of extensibility is that the standard application itself has sockets. Functionality that had to be customized often in the past, can be influenced by plugging in some own pieces of code.

Note: The concept of application sockets is not widely implemented in LN 10.5. The Document Output Management example, mentioned on the second bullet, is available. In LN 10.6 and later and in LN Cloud this concept is used in the Infor LN application. It can be implemented as process extensions. See the Infor LN Public Interfaces and Process Extensions Reference Guide. For more information about custom plug-ins in Document Output Management, see Infor LN Document Output Management User Guide.

Examples of application sockets that can be implemented or are implemented:

- To change the compose invoices algorithm: Items that have a different value in a specific customer defined field, must not be combined in one invoice. In the application extension, you can check whether the CDF has a different value. If so, then inform the standard application that this line cannot be added to the invoice. It must be on a separate one.

- ’s Document Output Management is flexible. If you require an output channel that is not supported LN in the standard application, then add your own output channel in the application extension.

## Cloud readiness

We recommend that you build your extensions in a way that they are ready for the cloud. Although you may not consider making that move with LN now, but you can save much effort in migrating your extensions when you decide to move.

In general, cloud readiness is related to these topics:

- Upgradability. Upgrades to new versions must not be impeded by the presence of extensions. This applies both to efforts required to upgrade extensions and the possibility that extensions can break the upgrade itself.

- Stability and performance. Extensions must not affect the infrastructure in such a way that other customers within the cloud environment are experiencing adverse effects.

- Security. Ensure that extensions cannot have access to information of the infrastructure that is a security risk.

The mechanisms that are built in LN ’s Extensibility layer to govern the extensions are described in Governance on page 155.

## Getting started with extensions

To get started with extensions:

1 Start the Initialize Extensibility (ttext0200m000) session. If your current package combination already has the Extensions (`tx`) package, this package VRC is displayed. You cannot change this VRC. If your current package combination does not have the Extensions package, you can use the default VRC (`B61O_a_ext`). If required, you can change the VRC name. Do not choose an existing VRC that is already used in another package combination. All package combinations require a different VRC for the Extensions (`tx`) package.

Note: Developing extensions always applies to the current package combination. There is no inheritance through a VRC-derivation structure. It is not supported to have a derivation structure for the `tx` package.

2 To use Software Configuration Management (SCM), select Use SCM and specify a Development VRC to be created. The Use SCM option is only available if your LN server is prepared to use SCM. For more information about Software Configuration Management, see the Infor LN Studio Application Development Guide.

Note: Activating SCM is not required to keep the revisions of your extensions. History of extensions is always available and you can restore old revisions; see Extension history. If you use SCM, you can isolate checked-out changes from other extension developers when you share development activities.

3 Click Initialize. Close the session. 4 Select Restart in the Options menu, to restart your LN environment. 5 By default, your Extensibility environment is setup with the Extensions Ready for Cloud setting. See Cloud readiness. If you are not running LN in a cloud environment, you can switch off this setting: Start the Extensibility Parameters (ttext0100m000) session. Clear the Extensions Ready for Cloud check box and click Save.

6 Start the Extensions (ttext1500m000) session to create extensions. For the procedure to create the extensions, see the Extension development procedure.

## Extension development procedure

For the development of extensions, you must set a current activity. An activity groups the different extensions, which you must create for a functional unit. Multiple developers can work in the same activity.

For more information about activity based development, see the Infor LN Studio Application Development Guide.

## Setting a current activity

To set a current activity: 1 Start the Extensions (ttext1500m000) session. 2 Click Actions and select Select Current Activity. The screen to select a current activity is always displayed if you have not yet selected a current activity and the required action requires one.

3 Select the activity and click OK. 4 If your activity is not in the list, you can create a new activity. Continue with the next step, otherwise this procedure is finished and you can start to build an extension. 5 To create a new activity, click New. 6 Specify at least Activity Name. The other fields are optional. Activity Documentation is used as default revision text during check-in of extensions. 7 Click Save changes and exit. 8 Click OK.

## Building an extension

To build an extension:

1 Start the Extensions (ttext1500m000) session and click New. 2 Select the Extension Point and specify the Component Name . Accept the proposed default in Library or specify your own Library code. Note that the package (`tx`) and the proposed module (esb, esm, esr, ess, est; see Extension scripts) cannot be changed.

3 Click Save changes and Exit. 4 Select the Extension. Click Actions and select Check-Out. 5 Click Extension Modeler. 6 In the Extension Modeler specify the Properties on component level, if applicable. 7 To implement a hook, right-click the hook and select Add Implementation or double-click the hook. 8 Click Add to add other extension types for the extension and fill the properties and hooks for those levels. The extension types, hooks and properties depend on the extension point to build an extension for. For some extension types, it is important in what order they are shown in the UI. For example calculated fields in a session, or custom menu items in a menu require a specific order. Use drag-and-drop in the extension types tree to define the desired order.

9 Click Save to save the extension. The extension script is automatically generated during save. Compilation issues can be displayed in the Problems view. Solve those problems and click Save.

Note: If a compilation problem must be solved in another component, for example a library which you created with LN Studio, click Generate and Compile after changing that other component.

10 Test the extension by starting the session(s) that would open the extension functionality. For testing a BOD extension, we recommend that you run the relevant BOD publishing session in simulation mode. Go to the Common menu under BOD Messaging > Publish BODs.

11 Close the Extension Modeler. 12 Click Actions and select Check-In. 13 Accept the default revision text or type your own text and click Save changes and exit. Before you checked-in the extension, the new extension or the new version of the extension was only available for you. After check-in, the most recent version of the extension is available to all users who set their activity context to your activity.

14 Click Actions and select Commit. The, new version of the, extension is available to all users.

## Activity context

When starting the Extensions (ttext1500m000) session, the activity context is automatically set to your current activity. The activity context is changed when you select another current activity.

After the activity context is set, the sessions that are started run within this context. The sessions include the functionality that is added in the extensions.

With Options and Debug and Profile 4GL you can also set activity context.

When the extensions are committed, the sessions include the extension functionality without the requirement to set the activity context.

Activity in title of session tab

This section is only applicable if LN runs on-premises.

Hint: To ensure your session runs in the correct activity context, add the activity to the title that is used for the session tab in LN UI. To achieve this:

1 Select Options > Settings and select your current profile. 2 Add `–set BAAN_WIN_TITLE=”%S-%a` to the Command field in your User Profile Details. The `%a` shows the activity context. The result is, for example, Item Defaults-act0001.

## Extension scripts

For each extension, an extension script is generated. This extension script contains the hooks that are programmed in the Extension Modeler and other generated functions. They are called by the different tools engines to do the required actions of the extension. Those extension scripts are DLLs (libraries), which are stored in the Extension package (`tx`).

This table shows the modules within the tx-package that are reserved for extension scripts:

| Module | Description |
|---|---|
| esb | Extension Scripts for BODs |
| esm Module Description | Extension Scripts for Menus |
| eso | Extension Scripts for OData REST APIs |
| esp | Extension Scrips for Processes |
| esr | Extension Scripts for Reports |
| ess | Extension Scripts for Sessions |
| est | Extension Scripts for Tables |
| Note that all module codes starting with `es` are reserved for future use. |  |

Extension scripts are visible in Infor LN Studio and can be debugged using LN Studio, see Extension debugging on page 146.

We do not recommend that you make changes in the generated scripts. The changes are lost after a change of the extension in the Extension Modeler.

## Extension history

History of extensions is kept in the extension history table.

To view the history:

1 Start the Extensions (ttext1500m000) session. 2 Click References and select History.

History has two levels:

- Activity level

- Extension level

The activity level history is updated each time an extension is checked-in; the revision of the extension is stored in the history. The extension level history is updated each time an extension is committed or imported into the environment. Note that during commit of an extension, the activity revisions are removed. The revision text of the last revision within the activity is used to create the revision on extension level.

## Activation and deactivation

After developing and committing an extension, the extension is active.

To deactivate the extension, go to the Extensions (ttext1500m000) session.

Click Actions and select Deactivate. The extension component itself remains in the system, but the functions of the generated extension script are not executed anymore by the tools engines. You can use this deactivation to check whether problems with the system are caused by your extension or by the standard software.

Click Actions and select Activate to activate the extension again.

Note: Restarting your sessions can be required to see the result of (de)activation.

Note: During import of extensions deactivated extensions always remain deactivated. Active extensions can be deactivated during import if the extension is not active in the file being imported. See Extension Deployment on page 161.
