# String expressions (ON CASE)
The expression of type STRING after ON CASE is evaluated and compared with the various CASE expressions that follow. All expressions in the case labels must be of type STRING. For example:
```

ON CASE choice_char
CASE "A":
CASE "E":
        abort()
CASE "N":
        next_screen()
        BREAK
CASE "P":
        last_screen()
        BREAK
CASE chr$(27):
        escape()
        BREAK
DEFAULT:
        message("unknown choice")
ENDCASE
```

## Related topics
- [The ON CASE statement](the_on_case_statement.md)
- [3GL programming language features: overview](overview.md)
- [Transfer of control](transfer_of_control.md)
