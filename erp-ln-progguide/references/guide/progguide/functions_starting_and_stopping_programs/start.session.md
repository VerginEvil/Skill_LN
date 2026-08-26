# start.session()

## Syntax:
`function string start.session( long mode, const string session.code, const string zoomname, const string returnfld )`

## Description
This starts a session from a program script.

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  Specifies the start mode for the new session. Possible values are: MODAL The parent session is blocked until the child session exits, in case of a multi-occurrence the session will be started as a zoom session. MODELESS Parent and child are parallel sessions that can be manipulated simultaneously. MODELESS_ALWAYS Even if the session is a Dailog it will be started Modeless MODAL_OVERVIEW The parent session is blocked until the child session exits, in case of a multi-occurrence the session will be started as an overview session. For dynamic sessions, other possible values are: SINGLE_OCC The session is started as a single-occurrence (details) session. MULTI_OCC The session is started as a multioccurrence (overview) session. Note: you can combine one of these with one of the other three; so e.g. MODELESS+SINGLE_OCC  |
| `const string` | `session.code` |  The code of the session that must be started.  |
| `const string` | `zoomname` |  The name of the calling process. This is used in the [4GL zoom.from sections](../4gl_features/4gl_zoomfrom_sections.md) sections in the child session. If no name is provided here, *zoom.from* sections in the child session are not executed.  |
| `const string` | `returnfld` |  Indicates the name of the variable to be returned by the function. If you specify an empty string, the function returns the exit value of the zoom process. This argument is relevant only if the start mode is MODAL. You can also specify an index name in this variable. In this case, the values of all component fields of the index are set by the zoom session and exported back to the calling process.  |

## Return values
If you specify a variable name in the *returnfld* argument, the function returns the value of the specified variable. If you specify an index name in *returnfld*, the function returns the value of *returnfld*. If you specify an empty string in *returnfld*, the function returns the exit value of the zoom process. If the session is canceled, the function returns an empty string.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and Value of argument session.code starts with "tx" or "otx"    Notes  You can use *start.session()* in both 3GL and 4GL programs, but only for starting 4GL sessions.
You cannot use *start.session()* from a report script.
The function replaces other functions for starting sessions, such as [zoom.to$()](zoom.to.md) and *start.main.session()*.

## Example
```

string	return_str(10)

return_str = start.session(MODAL, "ppmmm1234m000", "ppmmm4321m000", "")
|* start session ppmmm1234m000 (sessioncode)
|* where the calling process is ppmmm4321m000
|* the exit value of the ppmmm1234m000 session is returned in return_str

return_str = start.session(MODAL, "ppmmm1234m000", "field", "field")
|* the value of external var field in session ppmmm1234m000 will be returned in return_str
|* NOTE the session should be a list session otherwise field/variable values are not returned
|*      if field is not of type string then it will be converted to string format.
```

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
