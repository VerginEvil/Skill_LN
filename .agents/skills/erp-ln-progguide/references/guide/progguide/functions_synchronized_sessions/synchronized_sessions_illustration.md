# Synchronized sessions illustration
Dialog synchronization

- Sessions 1 and 2 form a set linked by dialog synchronization. Sessions 3 and 4 form another set linked by dialog synchronization.

- You open session 2 by double-clicking a record in session 1. Double-clicking a different record in session 1 updates session 2 with information from the newly selected record. You open session 4 by double-clicking a record in session 3. Double-clicking a different record in session 3 updates session 4 with information from the newly selected record.

Child synchronization

- Sessions 1 and 3 form a set linked by child synchronization.

- You open session 3 by selecting a form command in session 1. The records displayed in session 3 depend on the arguments of the function associated with the form command. You could, for example, program the synchronization in such a way that each time the user selects a new record in session 1 and activates the form command, session 3 is updated to display the child records of the selected record.
