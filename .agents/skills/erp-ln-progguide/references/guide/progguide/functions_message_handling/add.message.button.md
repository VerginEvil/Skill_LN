# add.message.button()

## Syntax:
`function long add.message.button( string msgCode, string buttonLabel, string library, string fnc, long autg, string Session )`

## Description
Add an additional button to a message or a question. This button will execute the specified function from the specified Library.

## Arguments
| |
|---|
| SESSION_NO_PERMISSION |
| SESSION_DELETE_PERMISSION |
| SESSION_INSERT_PERMISSION |
| SESSION_MODIFY_PERMISSION |
| SESSION_DISPLAY_PERMISSION |
| SESSION_PRINT_PERMISSION |

## Return values
| | |
|---|---|
| 0 | Button correctly added |
| -1 | Library not found |
| -2 | Function not found in library |
| -3 | Max number of additional buttons (4) exceeded |
| -4 | Not authorized |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Example
```

|* UI Script of a session
|****************************** program section ******************************
long	ret
after.form.read:
	|* Define an additioanl button for message tccom00016
	ret = add.message.button(
		"tccom00016",							|Message Code
		| Concept '%1$s' has not been implemented in %2$s.
		"tchp.concepts",						|Button Label
		| Concepts and methods
		"otccomdll1234",						|Library to be executed
		"tccom.dll1234.open.parameter.session",	|Function to be executed
		SESSION_DELETE_PERMISSION+SESSION_MODIFY_PERMISSION,	|Authorization level
		"tccom0500m000"							|User should have the above perm for this session
		)
	)

|* script tccomdll1234
function extern long tccom.dll1234.open.parameter.session(const string message)
{
	|* function can be used to start a session but also to
	|* to start functionality to correct data.
	if strip$(message) = "tccom00016" then
		start.session(MODAL, "tccom0500m000", prog.name$, "")
	endif
	return (1)	|return 1 close the message, 0 stay in the message
}
```
Note  Do not use this function in the before.program section. (The authorizations are then not initialized) The added buttons are not shown when running in DEM context The library function is executed in the current session context. Commit and retry in the library function will influence the current transaction wherein the message is given. If doing updates in this function then the commit will be done in the code where the message is given. (So no commit should be done in this function code)

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
