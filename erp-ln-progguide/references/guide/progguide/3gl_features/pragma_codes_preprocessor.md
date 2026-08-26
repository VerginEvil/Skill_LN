# Pragma codes (preprocessor)
Pragma codes represent compiler options. The following pragma codes are available:
| | |
|---|---|
| `#pragma nodebug` | Do not show the source while debugging. |
| `#pragma debug` | Show the source while debugging. |
| `#pragma nowarnings` | Do not give warnings about the source. As of [porting set TIV](../tiv/tiv_overview.md) [level 2030](../tiv/tiv_2030.md), this pragma code does not suppress warnings triggered by [bic compiler option -W32](compiler.md).  |
| `#pragma warnings` | Give warnings about the source. |
| `#pragma notransactions` | The source contains only read actions; there are no transactions. So, it is sufficient to start one database server.  |
| `#pragma warning <text>` | The programmer generates his own warning. (Warning level 15). See example.  |
| `#pragma strict_boolean` | Give errors instead of warnings in case of improper usage of booleans.  |
| `#pragma fatal <text>` | The programmer generates his own error. |
| `#pragma sticky` | Do not remove the object out of memory when the process ends.  |
| `#pragma used <component> <code>` | See below. |

## Example
```

#pragma warning This is not a fine solution !

| After compilation the following warning appears:
| <Source(line)>: Warning(15): This is not a fine solution !
```

## Where-used list
In some cases the where-used list is not updated automatically. For example, when a session code is entered but not expected:
```

message("ttadv2130m000")
        or
bms.send("command", event, "ttaad3100m000", pr.id)
```
To put this session code into the where-used list, enter the following command line:
```

#pragma used session     ttadv2130m000
```
The following example illustrates the pragma codes to update the where-used list:
```

#pragma used include    <file>
#pragma used table      <table code>
#pragma used field      <field code>
#pragma used domain     <domain code>
#pragma used message    <message code>
#pragma used question   <question code>
#pragma used session    <session code>
#pragma used menu       <menu code>
#pragma used dll        <dll objectname>
#pragma used chart      <chart code>
#pragma used label      <label code>
```
Usually the where-used list is updated. In the case of functions, the where-used list is updated if the function call contains the string value. For example:
```

mess("ttadvs0000", 1)   | Where-used list will be updated

str = "ttadvs0000"
mess(str, 1)            | Where-used list will not be updated

#pragma used message ttadvs0000
```

## Location of pragma codes
You can place pragma codes anywhere in the source. For example, if you set the following pragma at the start of the source:
```

#pragma nowarnings
```
you can enter the following pragma after a number of lines:
```

#pragma warnings
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Preprocessor](preprocessor.md)
