# get.arg.type()

## Syntax:
`function long get.arg.type( long arg_no )`

## Description
This function returns the type of the specified argument.

## Arguments
| | | |
|---|---|---|
| `long` | `arg_no` |  The sequence number of an argument supplied to the currently executing function (i.e. the function in which *get.arg.type()* is called). The allowed range for this sequence number is 1 ... *get.argc()*.  |

## Return values
The function can return any of the following values:
| | |
|---|---|
| VAR.TYPE.LONG | The specified argument is of type long or boolean. |
| VAR.TYPE.DOUBLE | The specified argument is of type double. |
| VAR.TYPE.STRING | The specified argument is of type string. |
| VAR.TYPE.MULTIBYTE | The specified argument is of type multibyte string.  |
| VAR.TYPE.UNKNOWN | *arg_no* is out of range, or the specified argument is not of one of the allowed types.  |
For historic reasons, these values are defined in terms of other named constants. The definitions are available when the tiv level is at least 2010 or when USE_VAR_TYPE_DEFINES is defined to a non-zero value.
```

#if ES_TIV_LEVEL >= 2010 or USE_VAR_TYPE_DEFINES
#define VAR.TYPE.LONG      DB.LONG
#define VAR.TYPE.DOUBLE    DB.DOUBLE
#define VAR.TYPE.STRING    DB.STRING
#define VAR.TYPE.MULTIBYTE DB.MULTIBYTE
#define VAR.TYPE.UNKNOWN   (-1)
#endif
```

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Functions with variable number of arguments: overview](overview.md)
- [Functions with variable number of arguments: synopsis](synopsis.md)
- [Functions with variable number of arguments: sample program](example.md)
