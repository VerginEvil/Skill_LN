# The IF ... THEN ... ELSE statement
The IF statement enables conditional transfer of control. The statement tests a condition, and executes the succeeding statements only if the condition is true. The condition can consist of a boolean variabele, an expression.
In the past it could be a long variable or a function that returns a long. When the condition is a long variable or a function that returns a long, the value zero is evaluated as FALSE and all other values are evaluated as TRUE.
Usage of a long in this way will cause a warning, in the future it will cause an error.

## IF...THEN
This tests a condition. If the condition evaluates to TRUE, the statements following the IF...THEN statement are executed. For example:
```

IF condition THEN
        statement(s)
ENDIF
```

## IF...THEN...ELSE
This tests a condition. If the condition evaluates to TRUE, the statements following the IF...THEN statement are executed. If the condition evaluates to FALSE, the statements following the ELSE statement are executed. For example:
```

IF condition THEN
        statement(s)_1
ELSE
        statement(s)_2
ENDIF
```

## ELIF
As of [porting set TIV](../tiv/tiv_overview.md) [level 2330](../tiv/tiv_2330.md), the ELIF keyword can be used to test multiple conditions in the specified order. It is equal to `ELSE IF condition THEN`, with the exception that no additional ENDIF is required for ELIF. For example:
```

IF condition_1 THEN
        statement(s)_1
ELIF condition_2 THEN
        statement(s)_2
ELIF condition_3 THEN
        statement(s)_3
ELSE
        statement(s)_4
ENDIF
```

## Examples
```

IF a > b THEN
        b = b + 1
ENDIF

IF bl1 THEN
        bl2 = FALSE
ENDIF

IF present AND found THEN
        count = count + 1
        do_something()
ENDIF

IF isspace(str1) THEN
        message("String is empty")
ENDIF

IF a > b THEN
        max_val = a
ELSE
        max_val = b
ENDIF

IF text(1;1) = "{" THEN
        handle_expression()
ELIF not isdigit(text(1;1)) THEN
        handle_placeholder()
ENDIF

IF align.right THEN
        output = shiftr$(text)
ELIF align.center THEN
        output = shiftc$(text)
ELSE
        output = shiftl$(text)
ENDIF
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Transfer of control](transfer_of_control.md)
