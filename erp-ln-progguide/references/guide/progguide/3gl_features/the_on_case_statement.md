# The ON CASE statement
This statement has the following syntax:
```

ON CASE expression
CASE expr_1:
        statements_1
        break
CASE expr_2:
        statements_2
        break
CASE expr_3:
        statements_3
        break
DEFAULT:                    | optional
        statements
ENDCASE
```
The ON CASE statement is a multiple-way decision table. It evaluates an expression and compares the result with the expressions of each specified CASE. When a match is found, control transfers to that branch and the code for that particular CASE is executed. If no match is found, the DEFAULT code is executed. If there is no DEFAULT label, the program continues with the first statement after ENDCASE. CASES and the DEFAULT label can occur in any order.
The CASE statements serve as labels. This means that after execution of the statements related to a particular CASE, the remaining CASES continue to be evaluated. However, if two CASE expressions give the same result, only the first is executed.
You can use the BREAK command to skip evaluation of other CASES after the code for the matching CASE has been executed. You include this command at the end of the code for each CASE. When the command is executed, execution of the ON CASE statement ends. In the case of nested CASES, the BREAK command cancels execution of the CASE statements at the same level only.
The ON CASE expression must be either a [Long expressions (ON CASE)](long_expressions_on_case.md) or a [String expressions (ON CASE)](string_expressions_on_case.md).
Undefined behavior with duplicate case values  If an ON CASE statement contains a duplicate CASE, the order in which the CASE is evaluated is undefined. The BIC compiler may raise a warning or error on a duplicate CASE if the compiler is able to detect it. Otherwise, the runtime behavior is undefined too. In case if duplicate CASE values cannot be prevented, e.g. because they are not known at compile time, use IF ... THEN ... ELSE ... ENDIF statement to have full control regarding the order of evaluation.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Transfer of control](transfer_of_control.md)
