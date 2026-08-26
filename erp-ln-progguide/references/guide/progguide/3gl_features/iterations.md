# Iterations
Iterative statements repeat the associated statements until a specified condition becomes FALSE.

## WHILE statement
This statement has the following form:
```

WHILE expression
        statement(s)
ENDWHILE
```
The expression is evaluated. If the result is TRUE (that is, non-zero), the statements between WHILE and ENDWHILE are executed. The process is then repeated until the expression is FALSE (that is, zero). When the expression evaluates to FALSE, control passes to the statement after ENDWHILE. For example:
```

LONG counter
counter = 1
WHILE counter <= 10000
        counter = counter + 1
ENDWHILE
```

## FOR statement
This statement has the following form:
```

FOR num_var = num_expr_1 TO num_expr_2 [STEP num_expr_3]
        statement(s)
ENDFOR
```
The *num_var* variable is referred to as the loop variable. *Num_expr_1* specifies the initialization of the loop variable. *Num_expr_2* specifies the end value of the loop variable. *Num_expr_3* specifies the step size for each iteration. The latter variable is optional; the default step size is 1. It is possible to use a negative step size.
After execution of the statements within the loop, *num_expr_3* is added to the loop variable. The *num_expr_2* expression is then evaluated. If the loop variable does not pass *num_expr_2*, the statements are executed again. This process continues until the loop variable passes its end value. For example:
```

LONG total, i
FOR i = 1 TO 100 STEP 2
        total = total + i
ENDFOR
```

## REPEAT ... UNTIL statement
The REPEAT ... UNTIL differs from the WHILE statement, in that the REPEAT ... UNTIL statement tests the condition after execution of the loop statements instead of before execution of the loop statements. Consequently the statement(s) within a REPEAT ... UNTIL statements are executed at least once.
The syntax of this statement is:
```

REPEAT
        statement(s)
UNTIL expression
```
The loop iterates until the result of the expression becomes non-zero.

## Using BREAK and CONTINUE (iterations)
You can use the BREAK command in an iterative statement in order to cancel the loop, regardless of the value of the loop condition. After a BREAK, control passes to the statement following the terminated loop. It is important to note that with nested loops the BREAK statement cancels the innermost loop only.
The CONTINUE command also interrupts an iteration loop. But, in this case, the expression is immediately evaluated again for the next iteration. For example:
```

LONG numbers(100), i
FOR i = 1 TO 100
        IF numbers(i) <= 0 THEN
                CONTINUE                     | Next iteration
        ENDIF
        IF NOT process(numbers(i)) THEN
                BREAK                        | Exit FOR statement
        ENDIF
ENDFOR
```
The BREAK and CONTINUE commands can be very useful in a program, but you should take great care when using them.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Transfer of control](transfer_of_control.md)
