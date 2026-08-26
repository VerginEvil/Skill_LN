# Long expressions (ON CASE)
The expression of type LONG after ON CASE is evaluated and compared with the various CASE expressions that follow. All expressions in the case labels must be of type LONG.
```

ON CASE weekday
CASE 1:
        day = "Sunday"
        BREAK
CASE 2:
        day = "Monday"
        BREAK
CASE 3:
        day = "Tuesday"
        BREAK
DEFAULT:
        day = "other day"
ENDCASE
```
It is also possible to execute a statement for multiple labels. For example:
```

ON CASE weekday
CASE 1:
CASE 2:
CASE 3:
CASE 4:
        beginweek()
        BREAK
CASE 5:
CASE 6:
CASE 7:
        endweek()
        BREAK
ENDCASE
```

## Related topics
- [The ON CASE statement](the_on_case_statement.md)
- [3GL programming language features: overview](overview.md)
- [Transfer of control](transfer_of_control.md)
