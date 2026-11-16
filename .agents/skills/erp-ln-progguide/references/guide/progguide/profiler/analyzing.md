# Analyzing the Call Graph Profile
The Call Graph Profiler is a tool for performance analysis. Performance analysis is all about combining the knowledge of the business logic that is being executed and the Call Graph Profile that is collected with the available tools. Each of these do not lead to performance improvements easily; the combination of both can be very powerful.
Some hints on how to determine whether there are improvement possibilities:

- Match the object summary info against the expectation of the developer who knows the functionality of the session and/or business process. Unexpected patterns should be investigated. When the run time in some objects is much longer than the CPU time the reason should be investigated. The long run time may be because the application waits for user input. The long run time may also be because of long running SQL statements, in which case the next step might be an investigation of long running SQL statements.

- Look at the functions that are the most expensive in the [Flat Profile](output.md#flat_profile). If the cost is significant it may be useful to try to optimize the implementation of these functions.

- Look in the [Query Summary](output.md#query_summary) for SQL statements that have a long run time, or for SQL statements that have much higher number of fetch operations than expected.

- Walk through the [Call Graph](output.md#call_graph) from the `main()` function. Look for details in child functions that contribute significantly to the cost of the session. Remember your knowledge of the business logic in the session and try to understand whether it is really necessary to do the things you see and to do these things the number of times you see them being done.

- Remember the numeric characteristics of the business process that was executed (e.g. 5 orders with 10 order lines each, in which 6 different items play a role) and see if the number of calls in the sessions and dlls in the process match your expectations.

- If you see something that looks strange or that unexpectedly takes a significant amount of time and you have no idea why it happens or whether it can be improved, or if it is not 'your area': do not ignore it, but raise the issue with colleagues and figure out whether there is an improvement possibility.

- When functions are called very often it may be helpful to walk a couple of levels up in the Call Graph, to the parent function and the parents parent function etcetera. The reason for the behavior of the code may become clear by studying the various levels of the call stack. For example: a large number of fld.display() calls in the 4GL Engine may be related to a call to display.all() in a section of the UI script (e.g. when.field.changes:).

## Related topics
- [Using the Call Graph Profiler](using.md)

- [The Call Graph Profile](output.md)

- [Call Graph Profiler Example](example.md)

- [Call Graph Profiler Glossary](glossary.md)
