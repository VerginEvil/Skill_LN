# The GOTO statement
The GOTO statement transfers control unconditionally to a specified point in the program. You use a label to indicate a position to which the statement can transfer control. The label name can consist of letters, digits, underscores [_], and periods [.]. It must begin with an alphabetic character.
Examples of labels:
```

LABEL_1:
START_OF_PROCESS_A:
```
Examples of GOTO statements:
```

GOTO LABEL_1
GOTO START_OF_PROCESS_A
```
Both the GOTO statement and the label to which it refers must be within the same function. You cannot transfer control to a label in another function.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Transfer of control](transfer_of_control.md)
