# Chapter 6: LN Studio Limitations

> Summary treatment for this release: orientation-level coverage. The full cleaned source text is preserved below; consult the source guide for exhaustive detail.

This section describes these topics:
- General limitations
- Script Editor limitations
- Configuration Management (CM) limitations
- Build limitations
- Debugger limitations
- Web UI limitations
## General limitations

Connections
Take care of the following when you use Worktop and LN Studio simultaneously.
When you close the Worktop, this message is displayed:
There are still running sessions including integrations.
These integrations may not work anymore after closing.
Close all sessions?
Click No if there are any connections, used by LN Studio, running on the LN server. If you click Yes, your
connections are closed. As a result, LN Studio cannot communicate with the server, and therefore will not
respond anymore.
## Script Editor limitations

Recognition of syntax patterns
The script editor does not recognize syntax patterns as no syntax parser is available in this release. Therefore,
if a variable has a name identical to a keyword such as "domain", "function", or "case", the variable is colored
as a keyword.
For example, you add the following code to the declaration section of a UI script: long case.
case is colored as a keyword, since the editor does not recognize it as a variable.
Debugging
There are also some editor limitations that are related to debugging. See "Debugger limitations" later in this
section.
## Configuration Management (CM) limitations

Blocking
CM actions are currently performed in a foreground process, and will as such block any user actions until the
CM actions have finished.
Dirty state decorator
The dirty state for sessions, tables and reports can not be determined accurately, because the modification
date is not available in LN.
## Build limitations

“Use checked out version of script with development vrc …” message
Building files checked out by yourself, or by someone else in the same SCM group, results in the following
error message: “use checked out version of script with development vrc …”.
Failure to build without a clear reason
For some reason, the storage or build of a component on the development system may fail. In certain cases,
no error is displayed to the user. It is necessary to check the LN Business Adapter log file to discover the reason
why a build failed.
To find the location of this log file, start the LN Business Adapter Console. Expand the Logging node to display
a list of machines. Select your PC from the list. The name and location of the log file, and other logging
parameters, are displayed.
## Debugger limitations

This section describes the debugger limitations.
## Debug View

“An error has occurred. See error log for more details” error message
Sometimes, while debugging, the message “An error has occurred. See error log for more details.” may be
given by Eclipse. This is not a fatal error, so you can click OK and resume debugging.
## Variables view

Filters not correctly initialized
The filters in the Variables view ( Show Global Variables and Show Local Variables) are not correctly
initialized. To correct the settings, click the stack frame twice or select a variable in the Variables view.
## Expressions view

Limited to variables
Currently, it is only possible to evaluate expressions that are actually variables. It is not possible to evaluate
other expressions, such as I=0.
Changing values not reflected in UI
The value of an expression is not updated, when the value of the contained variable is changed. To solve this,
use the Reevaluate Watch Expression command on the expression.
## Script Editor

Multiple instruction pointers
Eclipse does not always remove an existing instruction pointer. This may lead to multiple instruction pointers
being displayed in a script editor. To solve this, close the editor. The editor will automatically be re-opened
at the next step/suspend action.
Editing while debugging
LN does not support hot code replacement, so changes made in a script will only take effect the next time a
script is run. Changing a script while debugging can also lead to incorrect breakpoint handling, as the line
numbers do no longer match the lines of the (already) running object.
Run/Debug preferences
The Reuse editor when displaying source code option in the Run/Debug preferences dialog is not supported.
You must disable this option when you use the Step Into command in the Debug view. If this option is enabled,
and you use the Step Into command while the script is not in the workspace, an error page is displayed in
some situations.
## Watchpoint

You can not set a watchpoint on array elements.
## Web UI limitations

Labels
If you run a session in Web UI, any new or changed labels are only displayed if the session is compiled and
linked to your activity.
