# Debugger commands
Debugger commands consist of from one to three words; the words can be separated from each other by one or more spaces. The assignment command is an exception. Here the variable and the value to be assigned are separated by a ':=' sign. Most commands require a line number and/or a source name. If no source name is specified, the default is the current source.
When you start the debugger for an object, the source used by the debugger is first searched for by using the directions in the file fd *x.x*.<pack.comb.> (where *x.x* is the bshell version), then it is searched for in the $BSE/tmp directory, and finally in the current directory.
| | |
|---|---|
| Command | Action |
| `b [[source] line_number]` |  Toggle a break point on the current or specified line of the current or specified source. The line is highlighted, when break point is set. Note that you cannot set break points in included parts in a source. Instead the break point must be set in the included file.  |
| `B [source]` | Display all set break points in the current or specified source.  |
| `c [number]` | Continue (execute the source) up to the next break point. If you specify a number, the debugger skips that number of break points. The executed source lines are not displayed.  |
| `CC [number]` | Same as 'c', except that the executed source lines are displayed.  |
| `cc` | Change the size of the command window. This is valid only when application and debugger are in the same window.  |
| `cs` | Change the size of the source window. This is valid only when the application and debugger are in the same window.  |
| `d [source line_number]` | Delete the break point on the specified line number in the source. If you do not specify a line number, the debugger provides the opportunity to interactively delete any break point in the current source file.  |
| `D [source]` | Delete all set break points in the specified or current source.  |
| `delete all` | Delete all traces and stop instructions. |
| `delete number` | Delete a specified trace or stop instruction. |
| `ds` | Delete the source window. |
| `dd` | Generate a dump of the data dictionary. |
| `<expression>` | Execute the specified expression. |
| `f [noarg|noname][number]` |  Display stack trace (present nesting of functions), with the arguments of the functions. If you specify a number, only that number of nestings is displayed. noarg only the names of functions are displayed noname arguments are displayed but not their names  |
| `fdebug` | Show the open tables on the command window. |
| `Fdebug` | Print the open tables to the spooler. |
| `g [source] line_number` | Continue program execution at the specified line number (goto).  |
| `help (or ?)` | Start the Help Viewer for debugger options. |
| `l` | Display the full list of program variables. |
| `L` | Display the list of program variables that have a value, and display their current values. To stop displaying the contents of an array, enter 'n' at the question 'More ?'.  |
| `lp` | Print the output of the 'l' command. |
| `Lp` | Print the output of the 'L' command. |
| `mem` | Generate a dump including information about the memory allocated.  |
| `p` | Go to the source line currently being processed (this is useful after the view or seek command). The line is indicated by a greater than (>) sign before the line number.  |
| `q` | Exit the debugger (quit). |
| `return` | Continue execution until the end of the current function.  |
| `s [number]` | Execute the program step by step, the specified number of instructions at a time (default is 1). During execution, the intermediate source lines are not displayed.  |
| `S [number]` | Similar to 's', except that a function call is executed as a single statement.  |
| `slow [number]` | Reduce the rate of running source code. The maximum number is 100; the minimum (and default) number is 0.  |
| `split number` | Split the command and source window. The specified number is the last line of the command window. This is often used after resizing the Debugger window.  |
| `status [trace|stop|number]` | Display traced variables and/or stop instructions. If you specify a number, only that traced variable or stop instruction is displayed.  |
| `stop if <expression>` | Stop execution when expression is True. |
| `stop in <function>` | Stop execution when function is entered. |
| `sym` | Generate a dump of the symbol table. |
| `trap off` | Disables ‘trap on’. This command is available only when the bshell was started with the -dbgcpu flag. |
| `trap on` | The debugger stops after execution of every function call. This command is available only when the bshell was started with the -dbgcpu flag.  |
| `swin off` | There is a separate window for stack, array and long string in debugger. The appearence of this second window can be switched off with "swin off".  |
| `swin on` | There is a separate window for stack, array and long string in debugger. The appearence of this second window can be switched on with "swin on".  |
| `t variable` | Trace the specified variable during program execution. The execution of the program stops every time the value of the variable is changed. You cannot trace array variables or common variables.  |
| `T variable [value]` | Same as 't', except that program execution is not stopped when the variable changes. If you specify a value, execution stops when the variable gets that value.  |
| `u [variable]` | Stop tracing the specified variable. If no variable is specified, you can stop tracing each variable interactively.  |
| `U` | Stop tracing all variables currently being traced.  |
| `v [source] line_number` | Display a specified source line in the source window (view). If *line_number* is greater than the total number of lines, the last line is displayed.  |
| `v {+-} number` | Shift the display to the source line that is *number* lines before or after the current source line.  |
| `/pattern` | Seek a matching text pattern in the current source and display that line.  |
| `[function.]variable [/option]` |  Display the value of a specified variable. If you specify a function, the value of the local variable of that function is displayed. Otherwise, the value of the variable of the current function or the global variable is displayed. If a variable has no value (empty string or zero number), the value is not displayed. / *option* can have the following values:  |
| `variable := value` |  Assign a value to a variable. The value can be: a string constant or expression a numeric constant or expression a variable name  |
| `vi` | Activate the vi editor for the current source at the current source line. Changing the source has no influence on the source displayed by the debugger in the source window.  |
| `width value` | Change the width of command and source window. You can specify any value in the range 80 to 132.  |
| `<Ctrl>D/<Ctrl>U` | Page down or up in source. |
| `<Esc>` | Toggle between normal and history mode. |
| `<Arrow up>/ <Arrow down>` | In history mode, these display previously executed commands on the command line. In normal mode, these move the cursor through the source.  |

## Related topics
- [The debugger](the_baan_debugger.md)
- [Debugger mouse actions](mouse_actions.md)
