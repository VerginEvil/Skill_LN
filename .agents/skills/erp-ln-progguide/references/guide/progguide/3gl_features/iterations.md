# Iteration statements
Iteration statements ( [WHILE](iterations.md#while_statement), [FOR](iterations.md#for_statement), and [REPEAT](iterations.md#repeat_statement)) repeatedly execute some statements (the 'loop body') as long as (or until) a specified condition evaluates to TRUE.
The [CONTINUE statement](iterations.md#continue_and_break) prematurely terminates the execution of the loop body and jumps to the evaluation of the condition that decides about the next iteration of the loop body.
The [BREAK statement](iterations.md#continue_and_break) prematurely terminates the complete iteration statement.

## The WHILE statement
The WHILE statement has the following form:
```

WHILE <condition>
	<statements>
ENDWHILE
```
The <condition> is evaluated repeatedly. Each time that the result is TRUE, the <statements> are executed. The first time that the result is FALSE, the loop is terminated. For example:
```

LONG counter
counter = 1
WHILE counter <= 10000
	counter = counter + 1
ENDWHILE
```
The <condition> must be a boolean expression.
If the <condition> is an expression of type long, implicit [long to boolean type conversion](type_conversions.md#long_to_boolean_type_conversion) is performed. This will cause a compilation warning; in the future it will cause a compilation error.

## The FOR statement
The FOR statement has the following form:
```

FOR <loop_variable> = <initial_expression> TO <target_expression> [ STEP <step_expression> ]
	<statements>
ENDFOR
```
The <initial_expression> is evaluated and the resulting value is assigned to the <loop_variable>. The <target_expression> specifies the targeted end value of the loop variable. The optional <step_expression> specifies the step size for each iteration. The default step size is 1. It is possible to use a negative step size.
The <target_expression> is evaluated repeatedly and the <loop_variable> is compared to the evaluation result. If the <loop_variable> did not reach or pass the value of the <target_expression>, the <statements> are executed.
After execution of the <statements>, the <step_expression> is evaluated and the result is added to the <loop_variable>. This is repeated until the <loop_variable> reaches or passes the value of the <target_expression>. For example:
```

LONG total, i
FOR i = 1 TO 100 STEP 2
	total = total + i
ENDFOR
```

## The REPEAT statement
The REPEAT statement differs from the WHILE statement, in that the REPEAT statement evaluates and tests the condition *after* execution of the loop statements rather than *before* execution of the loop statements. Consequently the statements within a REPEAT statement are executed at least once.
The syntax of the REPEAT statement is:
```

REPEAT
	<statements>
UNTIL <condition>
```
The <statements> are executed repeatedly. After each repetition, the <condition> is evaluated. Each time that the result is FALSE, a new repetition is started. The first time that the result is TRUE, the loop is terminated.
The <condition> must be a boolean expression.
If the <condition> is an expression of type long, implicit [long to boolean type conversion](type_conversions.md#long_to_boolean_type_conversion) is performed. This will cause a compilation warning; in the future it will cause a compilation error.

## Using the CONTINUE and BREAK statements in an iteration statement
Use the CONTINUE statement to skip the remaining part of the loop body and to jump to the evaluation of the condition for the next iteration of the immediately enclosing iteration statement.
Use the BREAK statement in order to prematurely terminate the immediately enclosing iteration statement (regardless of any loop condition) or [ON CASE statement](the_on_case_statement.md). For example:
```

LONG numbers( 100 ), i
FOR i = 1 TO 100
	IF numbers( i ) <= 0 THEN
		CONTINUE	| Next iteration
	ENDIF
	IF NOT process( numbers( i ) ) THEN
		BREAK	| Exit FOR statement
	ENDIF
ENDFOR
```
The CONTINUE and BREAK statements can be very useful in a program, but take great care when using them.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Transfer of control](transfer_of_control.md)
