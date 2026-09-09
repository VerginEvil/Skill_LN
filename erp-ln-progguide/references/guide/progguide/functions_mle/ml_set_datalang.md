# ml_set_datalang()

## Syntax:
`function long ml_set_datalang( const string datalang )`

## Description
Sets a new data language for the user.

## Arguments
| | | |
|---|---|---|
| `const string` | `datalang` |  a valid Data Language code  |

## Return values
| | |
|---|---|
| 0 | OK |
| <> 0 | Error |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Note
It is important to keep track of the current data language when switching to another data language, so that it is possible to switch back to the original data language again. This is equal to switching to another company!

## Example
```

        domain  ttiso.dlan      currlang | string(5)
        long                    ret

        | save current datalang, returns e.g. "en_US" for this user
        currlang = ml_get_datalang()
        | switch to dutch data language
        ret = ml_set_datalang("nl_NL")

        | as of here data on the user interface and report is displayed
        | in the "nl_NL" language

        | switch back to original datalang
        ret = ml_set_datalang(currlang)

        | as of here data on the user interface and report is displayed
        | in the "en_US" language again
```

## Related topics
- [Multi Language Data overview](overview.md)

- [Multi Language Data synopsis](synopsis.md)

- [Multi Language Data support code examples](examples.md)
