# The IF statement
The IF statement enables conditional transfer of control. The statement first evaluates a condition, and dependent on the result, chooses which succeeding statements to execute.
The <condition> must be a boolean expression.
If the <condition> is an expression of type long, implicit [long to boolean type conversion](type_conversions.md#long_to_boolean_type_conversion) is performed. This will cause a compilation warning; in the future it will cause a compilation error.

## IF ... THEN ... ENDIF
```

IF <condition> THEN
	<then_statements>
ENDIF
```
First, the <condition> is evaluated. If the result is TRUE, the <then_statements> are executed. Otherwise, the <then_statements> are skipped.

## IF ... THEN ... ELSE ... ENDIF
```

IF <condition> THEN
	<then_statements>
ELSE
	<else_statements>
ENDIF
```
First, the <condition> is evaluated. If the result is TRUE, the <then_statements> are executed and the <else_statements> are skipped. Otherwise, the <then_statements> are skipped and the <else_statements> are executed.

## ELIF ... THEN ...
As of [porting set TIV](../tiv/tiv_overview.md) [level 2330](../tiv/tiv_2330.md), the ELIF keyword can be used to test multiple conditions in the specified order. The code
```

ELIF <condition> THEN
	<then_statements>
<elif_tail>
ENDIF
```
is equivalent to
```

ELSE
	IF <condition> THEN
		<then_statements>
	<elif_tail>
	ENDIF
ENDIF
```
Notice the additional indentation and the double ENDIF here!
The <elif_tail> consists of any number of `ELIF <condition> THEN <then_statements>`, optionally followed by `ELSE <else_statements>`. For example:
```

IF condition_1 THEN
	statements_1
ELIF condition_2 THEN
	statements_2
ELIF condition_3 THEN
	statements_3
ELIF condition_4 THEN
	statements_4
ELIF condition_5 THEN
	statements_5
ELSE
	statements_6
ENDIF
```
Notice that each ELIF avoids one extra level of indentation and one ENDIF keyword. Without the ELIF keyword, the example above would look like this:
```

IF condition_1 THEN
	statements_1
ELSE
	IF condition_2 THEN
		statements_2
	ELSE
		IF condition_3 THEN
			statements_3
		ELSE
			IF condition_4 THEN
				statements_4
			ELSE
				IF condition_5 THEN
					statements_5
				ELSE
					statements_6
				ENDIF
			ENDIF
		ENDIF
	ENDIF
ENDIF
```

## IF ... THEN ... ELIF ... THEN ... ELSE ... ENDIF
Summarizing, the general syntax of all the variants of the IF statement is as follows.
```

  IF <condition> THEN <statements>
[ ELIF <condition> THEN <statements> ]*	| Optional: zero or more times (as of porting set TIV level 2330).
[ ELSE <statements>                  ]	| Optional: at most once.
  ENDIF
```

## Examples
```

IF a < b THEN
	a = a + 1
ENDIF

IF bl1 THEN
	bl2 = FALSE
ENDIF

IF present AND found THEN
	count = count + 1
	do_something()
ENDIF

IF isspace( str1 ) THEN
	message( "String is empty" )
ENDIF

IF a < b THEN
	max_val = b
ELSE
	max_val = a
ENDIF

IF text( 1 ; 1 ) = "{" THEN
	handle_expression()
ELIF not isdigit( text( 1 ; 1 ) ) THEN
	handle_placeholder()
ENDIF

IF align.right THEN
	output = shiftr$( text )
ELIF align.center THEN
	output = shiftc$( text )
ELSE
	output = shiftl$( text )
ENDIF
```

## Related topics
- [3GL programming language features: overview](overview.md)

- [Transfer of control](transfer_of_control.md)
