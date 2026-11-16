# Chapter 9: Script Editor

The LN Studio script editor is used to edit the source code of UI scripts, libraries, DALs, functions, and report
scripts.
The script editor is embedded in the Source tab of these multipage editors:
- Function Editor
- Library Editor
- Report Editor
- Session Editor
- Table Editor
You can edit multiple software components simultaneously. Each component is displayed in a separate tab.
Associated with the script editor is an Outline view, which shows the structure of the active source code. The
Outline view is updated automatically when you edit the source code.
See the following figure for an example.
Editing source code
To edit the source code of a component, go to the Source tab of the corresponding multipage editor:
- To edit the source code of a function, open the function in the Function Editor and go to the Source tab.
- To edit the source code of a library, open the library in the Library Editor and go to the Source tab.
- To edit the source code of a report script, open the corresponding report in the Report Editor and go to
the Source tab.
Note: You can also start a separate script editor to set breakpoints in the report's debug script.
See Using breakpoints on page 68.
- To edit the source code of a UI script, open the corresponding session in the Session Editor and go to
the Source tab.
- To edit the source code of a DAL script, open the corresponding table in the Table Editor and go to the
Source tab.
Note: The Source tab is only displayed if the source code is available.
The editor displays error markers to indicate errors in the source code. When you save a component which
contains errors, the component is only stored in your local workspace but is not saved to the server. In the
Activity Explorer, the component has a dirty state ( ) decorator in the bottom right corner of the software
component image. When you solve the error and save the component, the component is saved to the server
again and the decorator disappears.
Alternative ways to open source code
You can also start the script editor in the following ways:
- Through the Open Declaration command.
See Open Declaration on page 288.
- From various views, such as the Problems view, the Tasks view and the Bookmarks view. For example:
- When you double-click a problem, task, or bookmark associated with a specific component, the
editor opens the corresponding source.
- When you double-click a problem, task, or bookmark associated with a specific line in a specific
component, the editor opens the corresponding source on that line.
Note: The editor is not started when you double-click a generic problem, task, or bookmark not associated
with any specific component.
Instead of double-clicking, you can use the Go To command on the view's shortcut menu.
Script editor features
This topic focuses primarily on the LN Studio specific features. It does not describe the standard Eclipse editor
functionality, such as the Cut, Copy, Paste, Delete, and Save commands.
For details on the standard Eclipse editor features, see the Workbench User Guide.
For details on the LN Studio specific editor features, see these sections:
- Comparing Source Code Versions on page 278
- Source Tab on page 270
- Comments on page 282
- Open Declaration on page 288
- Keyword Search on page 286
- Code Assist on page 279
- Incremental Find on page 286
- Generating Source from WSDL on page 294
- Folding on page 284
- ToDo Comments on page 293
- Toggle Breakpoints on page 294
- Text Hovering on page 293
- Application Search on page 278
- Mark Occurrences on page 287
- Quick Outline view on page 292
- Outline view on page 323
- Executing Assignment Expressions on page 68 (only during debugging)
Note: All features listed are available if you start the editor in the Application perspective. When you debug
software components, the editor starts automatically in the Debug perspective. During the debugging, only
a part of the editor's functionality is available.
For information on preference settings for the editor, see Script Editor Preferences on page 269.
For information on the limitations of the editor, see LN Studio Limitations on page 75.
## Script Editor Preferences

You can define various preference settings for the Script Editor.
LN Studio preferences
Use these pages to define LN Studio-specific preferences:
- Preferences - Editor
Use this page to define various editor preferences. You can specify the "Marker Identifier" used in
maintenance comments, and define background color settings for the editor. You can also enable Mark
Occurrences, and indicate whether the editor must highlight matching brackets.
- Preferences - Syntax
Use this page to define different font colors for the various sections in the 4GL scripts and libraries.
- Preferences - Code Assist
Use this page to define Code Assist settings, such as background color and foreground colors for
completion proposals, and the auto activation trigger character.
- Preferences - Folding
Use this page to define the preference settings for Folding. For example: you can select the region types
for which folding must be enabled, and you can specify whether folding must be enabled when you open
a new editor.
- Preferences - Templates
Use this page to define templates for various 4GL programming statements, such as case, for, repeat
and while. You can use Code Assist to include these templates in your scripts or libraries.
To access these preference pages:
1 Select Window > Preferences.
2 In the left pane of the Preferences window, select Infor LN Studio Application > Editor.
Standard Eclipse preferences
There are various pages you can use to define standard Eclipse preferences.
For example:
- Use the Preferences - Editors page to define various preferences. For example: You can specify the size
of the recently opened files list, and indicate whether you wish to show multiple editor tabs.
- Use the Preferences - Annotations page to specify where and how the different annotation types (such
as error markers, warning markers, and task markers) are displayed in the editor. For example: you can
specify per annotation type whether markers must be displayed in the text or in the overview ruler.
- Use the Preferences - Quick Diff page to configure settings for the Quick Diff feature. Quick Diff
automatically adds color-coded change indicators in the marker bar while you are typing. In the preference
page you can, for example, define colors for the change indicators.
- Use the Preferences - Text Editors page to define appearance options for the editor. For example: You
can specify whether the current line must be highlighted, and whether line numbers must be displayed
on the left side of the text editor.
To access these preference pages:
1 Select Window > Preferences.
2 In the left pane of the Preferences window, select General > Editors.
See the Workbench User Guide and the online help of the pages mentioned.
Note: Alternatively, you can access the standard Eclipse text editor preference pages through the Preferences
command in the shortcut menu of the script editor's marker bar.
### Source Tab

The LN Studio script editor is embedded in the Source tab of various multipage editors. In this tab, you can
edit the source code of UI scripts, libraries, DALs, functions, and report scripts.
This figure shows the source tab and its shortcut menu:
## Markers and Marker bar

A marker is like a yellow sticky note stuck to (a line in) a script or library. On a marker you can record
information, such as location and severity, about a problem or a task to be performed. Or you can simply
record a location for a marker as a bookmark.
The Marker bar is the vertical bar located at the left of the editor area.
This bar is used to display various types of markers, for example: error markers, warning markers, breakpoint
markers, task markers, and so on.
This figure shows an example:
Each marker is related to the line next to which it is displayed. When you hover over a marker, the description
of the corresponding error, warning, breakpoint, etc. is displayed in a ToolTip. For example, when you hover
over the warning marker in the previous figure, the following description is displayed: "Statement not reached".
The following markers can appear in the marker bar:
For details on breakpoints and on the corresponding breakpoint markers, see these sections:
- Using breakpoints on page 68
- Breakpoints view on page 308
For details on VSC warnings, see Verifying software components on page 56.
For details on the other marker types, see the Markers topic in the Workbench User Guide.
> [!NOTE]
- The markers are not only displayed in the marker bar, but they are also shown in various views, such as
the Problems view, the Breakpoints view and the Tasks view. From these views, you can quickly jump
to the marked location within the corresponding source. For example, when you double-click a problem
in the Problems view, the script editor opens the corresponding source on the involved line.
- The appearance of the different markers in the marker bar depends on the settings in the Annotations
preferences page. You can access this preference page via the Preferences dialog.
See Script Editor Preferences on page 269.
Marker bar shortcut menu
Right-click the marker bar to display the marker bar's shortcut menu. This menu contains the following
commands:
Command
Add /Remove Bookmark Add /Remove
Task
Show Quick Diff
Show Line Numbers
Show Mark Occurrences
Highlight Matching
Brackets
Description
Adds or removes a bookmark or task for a line.
To define a bookmark or task for a specific line in your source code, right-click on
the marker bar next to that line, and click the relevant command on the context
menu. A dialog appears where you can enter the bookmark or task properties.
When finished, a new bookmark or task marker appears in the marker bar.
Note: You can also view (and modify or remove) the new bookmark or task in the
Bookmarks view or in the Tasks view.
To remove a bookmark or task, right-click the corresponding marker in the
marker bar, and click the relevant Remove command on the shortcut menu.
Enables / disables the QuickDiff feature. QuickDiff automatically adds color-coded
change indicators in the marker bar while you are typing. The colors show additions, deletions, and changes to the editor buffer as compared to a reference, for
example, the contents of the file on disk. When you hover the mouse cursor over
a change indicator in the marker bar, the original content is displayed.
You can configure QuickDiff settings, such as colors for the change indicators, in
the Quick Diff - Preferences page. You can access this preference page via the
Preferences dialog.
See Script Editor Preferences on page 269 and the Workbench User Guide.
Note: This command is not only used to enable the QuickDiff feature, but is also
used to disable QuickDiff.
Toggle to display line numbers.
Enables/disables the Mark Occurrences feature.
See Mark Occurrences on page 287.
Enables/disables the highlighting of matching brackets in the source code.
If this option is selected, the corresponding bracket is highlighted automatically
when you place the cursor directly behind a bracket.
This functionality applies to the following types of brackets:
- Parentheses: (, ).
- Braces: {, }.
Command
Show Whitespace
Characters
Preferences
Description
Enables/disables the whitespace characters.
Folding/Collapse All
Folding/Expand All
Toggle Breakpoint
Opens the Eclipse Text Editors preferences page. See the Workbench User Guide.
Note: To change the LN Studio script editor preferences, start the Preferences -
Editor page.
See Setting user preferences on page 32.
Collapses all expanded code elements such as functions.
See Folding on page 284.
Expands all folded code elements such as functions.
See Folding on page 284.
Adds or removes a line breakpoint for the current line.
If the current line is part of a function header, the command adds or removes a
method breakpoint.
> [!NOTE]
- When you define a method breakpoint, the corresponding marker is always
displayed next to the line that contains the word "function".
- Alternatively, you can double-click in the marker bar to add or remove a line
breakpoint or a method breakpoint.
- You can also use the Breakpoints view to disable, enable, or remove breakpoints.
See Using breakpoints on page 68.
Note: The following marker types cannot be added via the marker bar:
Error and warning mark- These markers are system-generated. You can view the corresponding error
and warning details in the Problems view.
These markers are generated by the search command. The corresponding
search result details are displayed in the Search view.
ers
Search result markers
## Overview ruler

If enabled, the overview ruler is displayed at the right hand side of the editor area, and shows all markers
concerning the entire document.
This screenshot shows an example:
The markers are displayed relative to their position in the document and do not move as you scroll the
document.
You can click a marker to navigate to the corresponding location in the source code. When that portion of
the document is visible, there usually is a corresponding marker on the marker bar at the left hand side of
the editor area.
Note: The appearance of the different markers in the overview ruler depends on the settings in the Annotations
preferences page. You can access this preference page through the Preferences dialog.
For more information, see Script Editor Preferences on page 269.
### Editor shortcut menu

When you right-click on any location in the source code, a shortcut menu is displayed.
This table shows the shortcut menu commands, except basic commands, such as copy and paste:
Command
Compare With
Description
Contains commands to compare different versions of the source code.
See Comparing Source Code Versions on page 278.
Description
Opens a cleaned version of the source in a separate editor.
In the cleaned source, all code marked as old is removed: The script editor removes
the following:
- Lines that contain the "|#<Current ActivityName>.o" comment.
- Blocks where the first line contains the "|#<Current ActivityName>.so" comment and the last line contains the "|#<Current ActivityName>.eo" comment.
In code marked as new, the script editor removes the corresponding comments:
- "|#<Current ActivityName>.sn"
- "|#<Current ActivityName>.en"
- "|#<Current ActivityName>.n"
For details on code marked as old, and code marked as new, see Comments on
page 282.
> [!NOTE]
- The cleaned source is read-only.
- When you close the cleaned source, the corresponding file is removed from
the workspace.
Use these commands to comment out and uncomment lines of code. You can
Mark as New / Mark as toggle comments, mark modified lines, mark new lines, and add comments.
Old / Add Comment
Command
Clean Source
Toggle Comment /
Add Linked Library
See Comments on page 282.
Use this command to link a library to the component that you are editing.
Use this command as follows:
1 In the source code, select a function call.
The selected function must be stored in a library. The function name must
meet the coding standards.
For example, the source contains this code: RETIFNOK(tcmcs.dll0095.read.p
arm("tdsls000")). Select tcmcs.dll0095.read.parm("tdsls000").
2 Right-click and run this command.
The library in which the selected function is stored, for example tcmcs.dll0095,
is added to the list of linked libraries in the Script tab.
Generate Source from Use this command to generate LN 4GL code, based on a URL or a Web Services
Description Language (WSDL) file, for a general library.
See Generating Source from WSDL on page 294.
Use this command to search in which LN software components the expression,
that you selected in the script editor, is used.
See Application Search on page 278.
Performs a keyword search in the online help.
See Keyword Search on page 286.
WSDL
## Application Search

## Keyword Search

Description
Use this command to view the source code of the selected software component.
LN Studio opens the Source tab of the corresponding multipage editor.
See Open Declaration on page 288.
Use this command to view the properties of the selected software component.
LN Studio opens the Overview tab of the corresponding multipage editor.
See Open Declaration on page 288.
Lists the main structural elements of the source code you are editing. You can use
the displayed elements to quickly navigate to the corresponding sections in the
source code.
See Quick Outline view on page 292.
Adds a modification watchpoint for the selected variable or table field. A watch
expression is added automatically. When debugging, the session execution suspends each time the variable or table field changes.
Note: You must be sure that the selected text really is a variable or table field.
The script editor does not check this.
See Using breakpoints on page 68.
Creates a watch expression for the selected variable. When debugging, the watch
expression is evaluated each time a session suspends.
See Evaluating expressions on page 67.
Condition Watchpoint Starts a dialog where you can enter a condition watchpoint for a local or global
variable. A watch expression is added automatically. When debugging, the session
execution suspends when the variable gets a certain value.
See Using breakpoints on page 68.
Command
## Open Declaration

(source)
## Open Declaration

(properties)
Quick Outline
Modification Watchpoint
Watch
## Keyboard shortcuts

This table shows keyboard shortcuts you can use in the script editor:
Keyboard shortcut
Ctrl+.
Ctrl+,
Ctrl+Shift+Up Arrow
F3 after selecting a table
field
Description
Jump to next error line.
Jump to previous error line.
Select complete word or string.
Select a table field in the source code and press F3 to start the Table Editor.
The Fields tab is opened automatically and the properties of the selected
table field are displayed.
## Comparing Source Code Versions

In the script editor, you can compare different versions of the source code that you are editing.
To compare two source code versions, right-click in the source code and select one of these options:
- Compare With > Project
Compares the current version of the source code with the version stored in the Project VRC.
- Compare With > Activity
Compares the current version of the source code with the version stored in the Activity VRC.
When you run these commands, the Text Compare window is displayed. This window shows both versions
of the source code side by side. The differences between the versions are highlighted.
## Application Search

You can use the Application Search command to find out in which LN software components an element,
selected in the script editor, is used.
The application search functionality depends on the Enterprise Server version of the LN server.
Application search procedure for servers with Enterprise Server
8.6 and lower
To find out in which LN software components an element is used:
1 Select the desired element in your source code. For example, select a domain code, a message code, or
a function call.
2 Right-click the selected element and, on the shortcut menu, select Application Search. The Search
Script items (tlanl0400m000) session starts.
The first time you use Application Search, you must define appropriate defaults for this session. To do
this, select all types of components and enter the full range of packages, scripts, functions and reports.
Subsequently, click Save Defaults, close the dialog, and run the Application Search command again.
3 Specify the desired selection ranges and parameters and click Continue. The Select Device (ttstpsplopen
) session starts.
4 Select an output device and print the search results.
Application search procedure for servers with Enterprise Server
8.7 and higher
To find out in which LN software components an element is used:
1 Select the desired element in your source code. For example, select a domain code, a message code, or
a function call.
2 Right-click the selected element and select Application Search. The Search dialog box starts.
3 In the Application Search tab, specify the desired selection ranges and parameters and click Search.
See the online help of the Application Search dialog box.
The search results are displayed in the Search view.
4 Double-click a search result to open the corresponding script or library at the line where the result occurs.
If the script or library is not present in your work area, it is automatically retrieved from the LN server
and stored in your work area.
## Code Assist

When you specify text in the editor, Code Assist can provide you with a list of suggested completions for
partially specified strings.
To use code assist:
1 Press Ctrl+Spacebar directly after the last character of the string you want to complete.
A list of completion proposals is displayed. This list can contain:
- Various types of 4GL elements, such as functions, predefined variables, keywords, and program
sections. These are read from the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
- Templates for programming statements, such as the on case statement and the while statement.
These templates are defined in the Preferences - Templates dialog.
- Functions that are declared in the source you are editing.
- Functions declared in includes and libraries that are used in the source you are editing.
- Domains.
- Enumerated constants.
- Tables.
- Table fields.
- Index fields in the where clause of a select statement.
- External functions in the DAL that is selected in the dal.start.business.method function. You must
press Ctrl+Spacebar after the comma behind the first argument of the dal.start.business.method
function.
2 Double-click the completion proposal you want to use. The completion proposal, for example a function
name, or a template text, is added to your source code.
See the following figures for some examples.
The following is displayed when you start Code Assist after typing "crea" (functions from Infor ES Programmers
Guide (Infor Customer Portal KB2924522)):
The following is displayed when you start Code Assist after typing "on":
When you double-click the on case statement in the previous figure, the template is inserted in the editor:
Note: After inserting a template in the editor, press Tab to navigate through the template's variables.
Icons
Code Assist can display suggestions for various types of 4GL elements. The following icons are used to
distinguish the different element types:
> [!NOTE]
- Code Assist can also display suggestions for keywords, SQL statements, some standard macro definitions,
and various sub sections. However, these types are displayed without icons.
- Code Assist does not display report main sections and form.<form number> sections.
Preferences
You can define various preferences for Code Assist, such as the following:
- Automatic insert of completion proposals
- Background color for the completion proposal
- Foreground color for the completion proposal
- Auto activation trigger character (default is the dot (.) sign). Code Assist is started automatically when
you type this character.
- Important: the auto activation trigger character is used as part of the search string. For example,
when you type "aud.", Code Assist shows a list of functions whose names start with "aud." (including
the dot sign!); for example "aud.audit.is.on.for.table" and "aud.close.selection". Function names
starting with "aud" (without the dot sign), such as "aud_close_audit" and "aud_get_audit_dd", are
not displayed.
To define preferences for Code Assist:
1 Select Window > Preferences. The Preferences dialog box is displayed.
2 In the tree structure in the left pane of the dialog box, select Infor LN Studio Application > Editor > Code
Assist. The Preferences - Code Assist dialog box is displayed. See the dialog box's online help for details.
Code Assist Templates
LN Studio contains predefined templates for various programming statements, such as on case, for, repeat
and while. You can use Code Assist to include these templates in your scripts or libraries. See the previous
figures for an example on the on case statement.
You can also add you own templates and use them in the same way as the predefined templates.
To add your own templates:
1 Select Window > Preferences. The Preferences dialog box is displayed.
2 In the tree structure in the left pane of the dialog box, select Infor LN Studio Application > Editor >
Templates. The Preferences - Templates dialog box is displayed.
3 Click New to add a template. A details dialog box is displayed.
4 In the Name field, enter the name for the template. This name does not have to be unique. It is used as
a display name only.
5 In the Description field, enter a brief description of the template.
6 Specify the template pattern in the Pattern field. The pattern may contain pre-defined variables.
See Preferences - Templates on page 120.
7 Click OK to return to the Preferences - Templates dialog.
8 Click Apply to save the new template.
9 Click OK to close the Preferences dialog.
You can now use Code Assist to insert the template in your scripts and libraries.
## Comments

The LN Studio Script Editor enables you to easily comment out and uncomment lines of code. You can toggle
comments, mark modified lines, mark new lines, and add comments.
## Toggling comments

Use the Toggle Comment command to (un)comment one or more lines:
1 Put the cursor in the desired line, or select the desired lines.
2 Right-click and select Toggle Comment.
When you comment lines, a comment pipe symbol [|] appears at the beginning of each of the selected lines.
This prevents the lines from being compiled or interpreted.
This figure shows an example:
The comment pipe symbols are removed when you uncomment the lines.
## Maintenance comments

You can easily add maintenance comments to existing scripts or libraries. You can mark existing lines that
you modified, and new lines that you added.
When you add a maintenance comment, the editor generates a comment text that consists, among other
things, of a Marker Identifier. The Marker Identifier is determined by the editor preferences, and can be the
name or requirement ID of your current activity or project.
See Preferences - Editor on page 116.
Note: When you use the Toggle Comment command to uncomment a line, only the pipe symbol [|] at the
beginning of the line is removed. Comment text at the end of the line (for example maintenance comment
text such as " |#myactivity.so ") is not removed.
Marking modified lines
You can also easily mark modified script parts:
1 Put the cursor in the desired line, or select the desired lines.
2 Right-click and, on the shortcut menu, select Mark as Old.
- All selected lines are commented out (a pipe symbol [|] appears at the beginning of each line)
- Behind the first old line a comment is inserted with the following text: " |#<Marker Identifier>.so
". (" so " means Start - Old)
- Behind the last old line a comment is inserted with the following text: " |#<Marker Identifier>.eo
". (" eo " means End - Old)
- Note: if you selected only one line, the comment text is: " |#<Marker Identifier>.o ".
This figure shows an example:
Marking new lines
You can also easily mark new lines that you added to your script:
1 Put the cursor in the desired line, or select the desired lines.
2 Right-click and, on the shortcut menu, select Mark as New.
- Behind the first new line a comment is inserted with the following text: " |#<Marker Identifier>.sn
". (" sn " means Start - New)
- Behind the last new line a comment is inserted with the following text: " |#<Marker Identifier>.en
". (" en " means End - New)
- Note: If you selected only one line, the comment text is: " |#<Marker Identifier>.n ".
This figure shows an example:
## Adding comments

You can use the Add Comment command to read descriptions, such as domain and table descriptions, from
the data dictionary on the LN server. These descriptions are added as comments in your script.
To add these comments to your script:
1 Right-click and select Add Comment.
2 A message is displayed: you are prompted to save changes and to perform the action. Click OK to add
the comments.
This sample code shows table names that were added through the Add Comment command:
table tttaad300 |* Device Data
table tttaad305 |* Report Defaults
table tttaad310 |* Paper Types
table tttaad311 |* Fonts by Paper Type
table tttaad312 |* Windows Paper Size
## Folding

In the script editor you can fold and unfold code elements (regions). When you fold a code element, the
element is collapsed so that the corresponding source code is hidden. The folding of elements can provide
a better overview of the script structure, especially in large scripts.
The script editor supports folding of the following region types:
- functions
- header comments. Note: only header lines with a double *, for example lines starting with “|**”, are
folded.
- macros
- sections
To fold a region, click the minus sign that is displayed at the beginning of the region. A plus sign is displayed
at the beginning of the folded region.
This figure shows an example:
To unfold the region again, click this plus sign.
When you hover over a folded 4GL element, the hidden code is displayed.
This figure shows an example:
Note: You can unfold all folded code elements in one go: right-click the marker bar (located at the left of the
editor area) and select Collapse All.
## Defining folding preferences

You can define various preferences for Folding.
To define these preferences:
1 Select Window > Preferences. The Preferences dialog box is displayed.
2 In the tree structure in the left pane of the dialog box, select Infor LN Studio Application > Editor >
Folding. The Preferences - Folding dialog box is displayed.
3 Define the preference settings, for example:
- Specify whether folding must be enabled when you open a new editor.
- Select the region types for which folding must be enabled.
See the dialog's online help.
## Incremental Find

You can use the Incremental Find Next and Incremental Find Previous commands to search for expressions
in the active editor. As you type the search expression, the cursor incrementally jumps to the next or previous
exact match in the active editor.
To use the Incremental Find Next command:
1 Press CTRL+J in the script editor or select Edit > Incremental Find Next.
2 Type the expression you are searching for. The search expression is displayed in the Workbench status
line. As you type, the editor finds the next exact match of the text and updates the selection after each
character typed.
For example:
- when you type the character "a", the cursor jumps to the next exact match of the character "a".
- When you subsequently type an "s", the cursor jumps to the next exact match of the string "as"
- When you subsequently type a "c", the cursor jumps to the next exact match of the string "asc"
Note: to undo the last action, press Backspace.
3 Use the Up Arrow and Down Arrow keys to navigate between matches.
4 To cancel the search, press one of the following keys: Left Arrow, Right Arrow, Enter or Esc.
The Incremental Find Previous command works in a similar way. When you type an expression, the editor
finds the previous exact match of the text and updates the selection after each character typed. To start this
command: press Ctrl+Shift+J in the script editor or, on the Edit menu, select Incremental Find Previous.
## Keyword Search

In the script editor you can select a piece of text, and perform a keyword search to get more information on
it.
The Keyword Search feature searches for multiple string hits of the selected text in the LN Studio online help.
This online help includes the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
To perform a keyword search:
1 Select the text for which you want to perform the search.
2 Right-click and select KeyWord Search.
For example, you select the text zoom.from in the source and you run the KeyWord Search command. This
figure shows the information that is displayed:
Note: When you use KeyWord Search for the first time, the help is indexed automatically. This may take a
while.
## Mark Occurrences

You can use this feature to mark occurrences of the selected element in the current source code.
If Mark Occurrences is enabled, the script editor can display markers to indicate where a variable, method,
type, or other element is referenced.
Enabling Mark Occurrences
To enable Mark Occurrences, complete one of these steps:
- Right-click the script editor's marker bar and select Show Mark Occurrences.
- Select the Show Mark Occurrences check box in the Preferences - Editor dialog box. You can access
this preference page via the Preferences dialog box.
See Script Editor Preferences on page 269.
Marking occurrences
To mark occurrences of an element, double-click the element. The script editor shows markers in the marker
bar and overview ruler, to indicate references of the selected element.
This figure shows an example:
Note: The appearance of the markers depends on the settings in the Annotations preferences page. You can
access this preference page through the Preferences dialog box.
See Script Editor Preferences on page 269.
## Open Declaration

Use the Open Declaration command to view detailed information on an element in your source code, such
as a domain code, a table code, a message code, or a function call.
Open Declaration can display the general properties or the source code of the selected element.
> [!NOTE]
- Open Declaration only works on compiled scripts.
- Open Declaration does not work for all types of 4GL elements. See the following section.
### Viewing general properties

To view the general properties of an element:
1 In the script editor, select the desired element.
2 Press SHIFT+F3 or, right-click the selected element and select Open Declaration (properties). The
Overview tab of the corresponding multipage editor starts.
Example
In the script editor, you select the ttccom000 table code. Then you press SHIFT+F3. The Overview tab of the
Table Editor starts. The properties of tccom000 are displayed.
## Viewing source code

To view the source code of an element:
1 In the script editor, select the desired element.
2 Press F3 or, right-click the selected element and select Open Declaration (source). The Source tab of
the corresponding multipage editor starts.
Example
In the script editor, you select the ttccom000 table code. Then you press F3. The Source tab of the Table
Editor starts. The source code of the DAL script of tccom000 is displayed.
## Functions and arguments

The following table shows a list of functions and, per function, the argument types that support Open
Declaration.
- If you run Open Declaration for one of these functions, the corresponding help is displayed.
- If you run Open Declaration for one of the function argument types listed below, the corresponding
multipage editor starts.
Argument
message
Function
abort.io
skip.io
act.and.sleep
activate
wait.and.activate
ask.enum
session
question
Function
brp.open
brp.open.language
spool.open
dal.set.error.message
dal..warning.message
dal.set.info.message
dialog.add.button
dialog.add.field
dialog.add.listbox
disable.satellite
enable.satellite
satellite.invisible
enum.descr$
form.text$
Argument
report
message
label
session
domain
message
session
library
get.session.permission
load_dll
exec_dll_function
get_function
parse_and_exec_function
mess
message
session
domain
pcm.activate.session
set.max
set.min
set.fmax
set.fmin
set.input.error
message
set.synchronized.dialog session
session
start.synchronized.child session
session
start.session
substitute.session
Function
tt.align.according.domain
tt.index.desc
tt.is.domain.separated
tt.label.desc
tt.report.desc
tt.session.desc
tt.session.present
tt.table.desc
zoom.to$
Argument
domain
table
domain
label
report
session
session
table
session
Example
A script contains the following code: spooler = spool.open("rtccom040101000","D",0).
When you run Open Declaration for the spool.open function, the function's help text is displayed.
When you run Open Declaration for the rtccom040101000 argument, LN Studio opens the tccom040101000
report in the Report Editor.
## Miscellaneous elements

This table shows a number of elements and the actions that are performed when you run Open Declaration
for those elements.
Action
Adds the DLL to the workspace. Opens the DLL in the LN Studio script editor.
Element
#pragma used
dll
Macro call
Local Functions For example: You use Open Declaration on a name of a function that is declared somewhere else in the same script or library. The focus is set on the function declaration.
The cursor jumps to the macro definition.
## Quick Outline view

This view shows an outline of the source code that is currently open in the Script Editor, and lists the main
structural elements.
This figure shows an example:
You can use the displayed elements to quickly navigate to the corresponding sections in the source code.
You can for example:
- Click a folder icon to expand the corresponding tree. Subsequently, click an element to go to the
corresponding section in the source code. The view closes automatically.
- Specify a search pattern in the input field in the upper part of the view. As you type the search expression,
the element with the first match is highlighted. Click the element to go to the corresponding section in
the source code. The view closes automatically.
- Click in the view and use the arrow keys to navigate to an element, and press ENTER to go to the
corresponding section in the source code. The view closes automatically.
If you do not want to navigate, click the Close button or press ESC to close the view.
Note: This view is similar to the Outline view.
## Text Hovering

Text hovering means that informational text is displayed when you hover over a piece of text in the editor
area.
The 4GL script editor supports text hovering for various elements, such as:
- LN standard functions: When you hover over a function name, the editor automatically shows the syntax
of the function. The function syntax is displayed as tool-tip information.
Press F2 to display the corresponding manual page from the Infor ES Programmers Guide (Infor Customer
Portal KB2924522).
- Folded code elements (regions): When you hover over a folded 4GL element, the hidden code is displayed.
For an example, see Folding on page 284.
- The markers in the marker bar (to the left of the editor area), and in the overview ruler (to the right of the
editor area). For example: When you hover over a problem marker, or over a warning marker, the
corresponding description is displayed in a ToolTip.
For more information on the marker bar and the overview ruler, see Source Tab on page 270.
- Initiated variables in the Debug perspective: For example, when you debug a session, you can hover the
cursor over an initiated variable in the editor area in the Debug perspective. The variable's value is
displayed in a ToolTip.
- Domains, enumerated constants, tables, table fields, and table indices.
- Macros: When you hover over the name of a macro, which is defined in the current script or library, the
editor displays the syntax of the macro.
- Messages and questions: when you hover over the name of a message or question, the corresponding
description is displayed.
- Enums: during debugging, when you hover over the name of an enum constant, the corresponding
numeric value and description are displayed.
Note: For all functions, you can use the Keyword Search command in the editor's shortcut menu, to view
the corresponding manual page from the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
## ToDo Comments

In the script editor, you can create to-do reminders in the script or library you are editing. These reminders
are displayed in the Tasks view in the LN Studio workbench.
To create a to-do reminder, enter "|TODO:" and type the text for the reminder.
You can type the characters "TODO" in uppercase, in lowercase, or use a combination of both cases. So,
"|ToDo:" and "|todo:" are also valid.
This diagram shows an example:
Note: To ensure the ToDo reminders are displayed in the Tasks view, click the Menu button and select Show
> Show all. All tasks, including the ToDo reminders, are displayed.
Alternatively, define and activate a filter to display only ToDo reminders:
1 To define the filter:
a Click the Menu button and select Configure Contents. The Configure Contents dialog box is
displayed.
b In the Configurations pane, select TODOs.
c Under Scope, select On any element.
d In the Types box, select Infor LN Studio Todo. Clear the other check boxes.
e Click OK.
2 To activate the filter, in the Tasks view, click the Menu button and select Show > TODOs.
## Toggle Breakpoints

A breakpoint is a point in a program that, when reached, triggers some special behavior useful to the process
of debugging.
In the LN Studio, you can define multiple types of breakpoints:
- You can easily set and remove line breakpoints, and define watchpoints, in the script editor.
- You can toggle method breakpoints in the Outline view.
For details on these types of breakpoints, and on how to define them, see Using breakpoints on page 68.
## Generating Source from WSDL

You can generate LN 4GL code, based on a URL or a Web Services Description Language (WSDL) file, for a
general library.
Note: This functionality is only available for LN servers with Enterprise Server 8.7 or higher.
To generate library code from a WSDL file:
1 Create a library of type General Library. See these sections:
- Creating a library on page 104
- Create a New Infor LN Software Component wizard on page 94
2 Check-out the new library.
3 Edit the library. In the Library Editor, click the Source tab.
4 Right-click in the source code and select Generate Source from WSDL. The Generate Library from
WSDL file dialog starts.
5 Specify the required information and click OK.
See Generate Library from WSDL file on page 145.
Note: For information on how to use the generated LN code, see "Web Services from LN " in the Infor ES
Programmers Guide (Infor Customer Portal KB2924522).
