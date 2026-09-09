# Debugger commands
Debugger commands consist of from one to three words; the words can be separated from each other by one or more spaces. The assignment command is an exception. Here the variable and the value to be assigned are separated by a ':=' sign.
Several commands require a line number and/or a source name. If no source name is specified, the current source is used.
When you start the debugger for an object, the source used by the debugger is first searched for by using the directions in the file fd *x.x*.<pack.comb.> (where *x.x* is the bshell version), then it is searched for in the $BSE/tmp directory, and finally in the current directory.
| |
|---|
| `<expression>` |
| |
|---|
| Evaluate the specified expression and display the result. The syntax and semantics of the expression are the same as described for [runtime expressions](../functions_expressions_runtime/expr.compile.md#expression). |
| | |
|---|---|
| noarg | only the names of functions are displayed |
| noname | arguments are displayed but not their names |
| |
|---|
| Display the list of program variables that have a value, and display their current values. To stop displaying the contents of an array, enter 'n' at the question 'More ?'. |
| |
|---|
| `[<function>.]<variable> [/<option>]` |
| |
|---|
| Display the value of the specified variable. If you specify a function, the value of the local variable of that function is displayed. Otherwise, the value of the variable of the current function or the global variable is displayed. If a variable has no value (empty string or zero number), the value is not displayed. |
| */option* can have the following values: |
| | |
|---|---|
| `/` | Use to display the value of a variable that has the same name as a Debugger command. For example, ‘b/’ displays the value of variable b. |
| `/d` | Print the flags of the variable and the dimension for arrays. |
| `/D` | Display the number of bytes allocated in a long or double variable. Display the number of bytes for one element in a string array. |
| `/g` | For a string containing the compact string representation of a UUID, display the standard string representation of the UUID. See [UUID overview](../functions_uuid/uuid_overview.md). |
| The following options are useful for record buffers and binary data. They display the value of a string variable with its full declared length, regardless of [NULL characters](../3gl_features/null_characters_in_strings.md). |  |
| `/x` | NULL characters are displayed as ‘^@’. |
| `/X` | Characters with values 0 to 31 are displayed as ‘\x<value in hex>’. |
| `/b` | All characters are displayed as ‘ \x<value in hex>’. |
| `/l` | Interpret field as UTC field and print in local time and prints current time zone. |
| `/u` | Interpret field as UTC field and print in utc time. |
| |
|---|
| `<variable>:= <expression>` |
| |
|---|
| Evaluate the specified assignment and display the result. The syntax and semantics of the assignment are the same as described for [runtime expressions](../functions_expressions_runtime/expr.compile.md#expression). |

## Related topics
- [The debugger](the_baan_debugger.md)

- [Debugger mouse actions](mouse_actions.md)
