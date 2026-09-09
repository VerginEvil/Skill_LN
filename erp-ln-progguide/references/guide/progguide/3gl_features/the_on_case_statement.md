# The ON CASE statement
The ON CASE statement has the following syntax:
```

ON CASE <switch_expression>
CASE <expression>:		| Optional: zero or more times.
	<statements>
	BREAK		| Optional.
DEFAULT:			| Optional, at most once.
	<statements>
	BREAK		| Optional.
CASE <expression>:		| Multiple cases without <statements> and without BREAK.
			| Fall-through to next case!
CASE <expression>:		| Fall-through to next case!
CASE <expression>:		| Fall-through to next case!
CASE <expression>:
	<statements>
	BREAK		| Optional.
CASE <expression>:
	<statements>
			| No BREAK here!
			| Fall-through to next case!
CASE <expression>:
	<statements>
	BREAK		| Optional.
ENDCASE
```
The ON CASE statement is a multiple-way decision table.
The <switch_expression> must be either a [long expression](long_expressions_on_case.md) or a [string expression](string_expressions_on_case.md).
First, the <switch_expression> is evaluated.
Then, the result is compared (in an unspecified order) to the evaluation result of each CASE <expression>. When a match is found, the CASE <expression> evaluation and comparison is terminated.
Then, starting at the matching CASE label, the <statements> are executed. When no match is found and when there is a DEFAULT label, the <statements> are executed starting at the DEFAULT label. Otherwise, the ON CASE statement terminates.
CASE labels and the DEFAULT label can occur in any order.
The CASE keywords serve as labels. This means that execution of <statements> does not stop at a next CASE or DEFAULT keyword.

## Using BREAK in ON CASE statements
Use the BREAK statement to terminate the immediately enclosing ON CASE statement or [iteration statement (WHILE, FOR, or REPEAT)](iterations.md).
The BREAK statement may be used anywhere in your code. Especially, consider adding a BREAK statement after the <statements> for each CASE and DEFAULT label, in order to skip the <statements> of subsequent CASE and DEFAULT labels.
Undefined behavior with duplicate CASE values  When the <switch_expression> evaluates to a value that matches with more than one CASE <expression>, it is undefined at which of the matching CASE labels the execution of <statements> will start.
If the BIC compiler is able to detect a duplicate CASE value, it will raise a warning or error. Even without a compilation warning or error, the runtime behavior is undefined.
When duplicate CASE values cannot be prevented, e.g. because they are not known at compile time, use an [IF statement with ELIF parts and an ELSE part](the_if_then_else_statement.md#if-then-elif-then-else-endif) in order to fully determine the order of evaluation.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Transfer of control](transfer_of_control.md)
