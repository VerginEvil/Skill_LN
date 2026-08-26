# setenv()

## Syntax:
`function long setenv( string env_var, string env_value )`

## Description
This sets the value of a specified [environment variable](../misc/bshell_environment_variables.md) of the operating system. It returns non-zero in case of error.

## Arguments
| | | |
|---|---|---|
| `string` | `env_var` |  |
| `string` | `env_value` |  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | failed to set environment variable |
| 1 | name of environment variable is too long |
| 2 | value for environment variable is too long |
| 3 | both name and value are too long |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long ret

ret = setenv("MY_ENV_VAR", "this_is_the_value")
```

## Related topics
- [getenv$()](getenv.md)
- [Bshell environment variables](../misc/bshell_environment_variables.md)
- [System and user information overview and synopsis](overview_and_synopsis.md)
