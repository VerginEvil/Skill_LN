# The debugger
The debugger is an interactive statement interpreter that enables you to control and test the execution of a program. Its principal features include:

- simultaneous program execution and display of debug information

- source instructions and debug information are displayed in their own windows, separate from the application

- source instructions are displayed in a window that you can move and resize

- on non-graphical displays, debug information is displayed in screen columns 81 to 132

- the debugger supports variable tracing during program execution (that is, all changes to the values of specified variables are displayed during program execution)

- the debugger is fully symbolic – machine addresses are not used

- the debugger is fully integrated with the bshell.

The debugger works only with source programs that have been compiled with the debug option (-l in the case of the BAAN Compiler). When you start such a program, two additional windows are displayed. One displays the source code being executed (the line currently being processed is highlighted). The other is a command window where you input debugger commands and where command results and error messages are displayed.
For information about other debug facilities, see the Logic Server section in the Infor Enterprise Server Technical Manual.

## Related topics
- [Debugger commands](debugger_commands.md)

- [Debugger mouse actions](mouse_actions.md)
