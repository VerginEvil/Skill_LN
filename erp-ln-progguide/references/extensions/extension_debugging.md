# Extension debugging

For debugging the extensions in Infor LN you can use:

- LN UI. Use this debugger for simple extensions debugging or when Debug Workbench, which runs within you do not have Infor LN Studio installed.

- debugger. Use this debugger for more complex extensions where also new components LN Studio (developed in LN Studio) are involved. For more information about the setup of the connection to the LN server and debugging in LN Studio, see the Infor LN Studio Application Development Guide. The information about the setup of LN Studio in combination with extension development is described in the same guide.

## Debug Workbench

The Debug Workbench is mainly meant for debugging the generated extension scripts.

See Extension scripts on page 26

Other script components, such as UI scripts of sessions, DALs and other libraries can also be debugged with de Debug Workbench.

## Starting the Debug Workbench

The Debug Workbench can be started in these ways:

- Extensions (ttext1500m000) session. Starting from the

- Starting from Debug and Profile 4GL.

### Starting from the Extensions (ttext1500m000) session

1 Select Tools > Application Extensibility > Extensions. 2 Select the extension to debug. Note that the extension is debugged in the context of the current selected Activity. If no Activity is selected, the committed version of the extension is debugged.

3 Click Start Debugger under Actions. 4 Specify this information:

### Starting from Debug and Profile 4GL

1 Select Debug and Profile 4GL in the Options menu. 2 Select the Debug Mode option. 3 Select Debug Workbench as the Debug UI. 4 Application Name and Activity Name should show the Application and Activity, that you have current in LN Studio. If Application and/or Activity are not specified with the current Activity, change the fields. 5 Click OK.

## Selection of sources

If you started the Debug Workbench with the Extensions (ttext1500m000) session, the generated script for the selected extension is already loaded in the Debug Workbench.

To load (additional) scripts into the Debug Workbench:

1 Select Select Components (magnifier glass). 2 Specify the selection string (package, module and remainder of code) in the Selection field. For example, specifying `tx` displays all script components in the Extension package. Specifying `txess` displays the generated extension scripts for session extensions. 3 Select one or more components and click OK.

### Breakpoints and watchpoints

Before you start the session to debug the script, you must set a breakpoint or watchpoint, otherwise the session process is not suspended. A condition watchpoint suspends the process if the variable changes to a defined value. A modification watchpoint suspends the process if the variable changes.

Breakpoints and watchpoints are visible in the Breakpoints view. In this view the breakpoints and watchpoints can be deleted or temporarily disabled.

#### Setting or deleting breakpoints

1 Go to the line to set a breakpoint on, or for which to delete the breakpoint. 2 Double-click the line in the area before the line number.

#### Setting a watchpoint

1 Select a variable to create the watchpoint. 2 Right-click Select Condition Watchpoint or Modification Watchpoint. 3 For a condition watchpoint, specify the value to suspend on. 4 Click OK.

### Run the session

After you prepared the breakpoints and watchpoints, run the session that executes the script to debug:

- For a table extension, this can be a session that uses this table as a main table. But it can also be a session for another table, which does a dependent update in your table. For example, if you have a table extension for the inventory allocations table, you can start the sales order lines session to debug your extension.

- For a report extension, you must start the print session that produces the report.

- For a session extension, you must start the session you have extended. Note that it may be necessary to start with another session if your session cannot be started directly from the menu.

- For a BOD extension, you must start a session that publishes the BOD. This can be a session in the normal process flow, but you can also use the session that simulates the publishing of your BOD. Those sessions

can be found in the Common menu under BOD Messaging > Publish BODs.

- For a menu extension, just expand the menu.

### Variables and Expressions

The Variables view shows the values of the variables when the process suspends. Which variables are shown depends on the filter. You can change the filter by clicking the arrow down button. Because of the huge list of variables that can be displayed, table fields are not shown in the Variables view. To inspect the values of table fields you can hover over them in the script view or create an expression for it in the Expressions view.

In the Variables view you can also change the value of variables during the debugging process.

### Call Stack

The Call stack shows all processes that are started and the state of those processes. It can be cleaned up by right-clicking the Launched Infor LN Sessions and selecting Remove All Terminated.

### Toolbar

On the toolbar, these commands are available:

Save and Exit: the state of the current Debug Workbench is saved, although without the specific process information. The open sources, breakpoints, watchpoints and expressions are saved and the next time you start the Debug Workbench, those are available. If you close the Debug Workbench with the “X” in the title bar, the state is not saved.

Search: see Selection of sources.

Resume: continue with the suspended process.

Suspend: the selected process in the Call stack is suspended.

Terminate: the selected process in the Call stack is killed.

Step Into: current line is executed, or if the current line contains a function call, the first line of the function is executed.

Step Over: current line is executed; if the current line is a function call, this function is executed completely and the debug pointer goes to next line.

Step Return: current function is executed to the end and the debug pointer goes back to the calling function.

Run to Line: debug pointer is set to the current selected line and the process continues from there.

Skip All Breakpoints: quick way to disable temporarily all breakpoints.

## LN Studio

Debugging with LN Studio is preferred when complex extensions are developed with new tables, sessions, etc. LN Studio handles also other components than scripts. Information of those components can be required during debugging as well.

## Preparations

To prepare for debugging:

1 Open Infor LN Studio. 2 If you have already a current activity in the Extension Modeler, go to step 4. Otherwise click Create a new Activity. 3 In the Create a new Activity dialog box, select your Project Name, which is typically “EXT” followed by your package combination. 4 Specify a Name, Description and Type and click Finish. 5 Click Open an Infor LN Studio Activity in the Activity Explorer view. 6 Select your Project Name and click Next. If you are prompted to configure an Administrator Connection, click Yes.

7 Configure the Connection Point as described in the Infor LN Studio Application Development Guide or click Help to get more information. Repeat those steps, if required, for the Development and Runtime connections. 8 Select your Activity Name and click Finish.

## Debugging

To debug the extension scripts:

1 After the last step of the previous paragraph the Activity Explorer can contain already some components. This is the case when the activity is also used in the Extension Modeler. If the extension script to debug is not in the Activity Explorer, you must retrieve it from the LN server. To retrieve an extension script, expand the tx package in the Component Explorer and expand Libraries. Choose the module which holds the extension script for your extension point and expand it. Select the extension script, right-click it and click Get. Alternative: Click Select a Software Component (Alt+Q), specify `txes` in Component Code and click Search Components (Ctrl+Space). Select the extension script to debug and click OK. A message whether to open the editor for the new software component is displayed. Click Yes.

2 Click Source at the bottom of the component editor. 3 Set a breakpoint or watchpoint in the source. 4 Switch to LN UI. 5 Select Debug and Profile 4GL in the Options menu. 6 Check the Debug Mode option. 7 Select LN Studio as the Debug UI. 8 Application Name and Activity Name must show the Application and Activity, that you current have in LN Studio. If Application and/or Activity are not filled with the current Activity, change the fields. 9 Click OK. 10 Start a session that executes the extension script: a For a table extension, this can be a session that uses this table as a main table. But it can also be a session for another table, which does a dependent update in your table. For example, if you have a table extension for the inventory allocations table, you can start the sales order lines session to debug your extension. b For a report extension, you must start the print session that produces the report. c For a session extension, you must start the session you have extended. Note that it can be required to start with another session if your session cannot be started directly from the menu. d For a BOD extension, you must start a session that publishes the BOD. This can be a session in the normal process flow, but you can also use the session that simulates the publishing of your BOD. Those sessions can be found in the Common menu under BOD Messaging > Publish BODs.

11 Use the available options of the debug Perspective in LN Studio to debug your extensions.
