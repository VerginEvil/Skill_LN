# getenv$()

## Syntax:
`function string getenv$( string env_var )`

## Description
This returns the value of a specified [environment variable](../misc/bshell_environment_variables.md) of the operating system. It returns an empty string if the variable is not available.

## Arguments
| | | |
|---|---|---|
| `string` | `env_var` |    |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string name(15)
name = getenv$("LOGNAME")
```

## Related topics
- [setenv()](setenv.md)

- [Bshell environment variables](../misc/bshell_environment_variables.md)

- [System and user information overview and synopsis](overview_and_synopsis.md)
