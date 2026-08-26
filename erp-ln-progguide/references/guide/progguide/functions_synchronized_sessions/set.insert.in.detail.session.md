# set.insert.in.detail.session()

## Syntax:
`function void set.insert.in.detail.session( string sess_code, [ string parent.var child.var ] )`

## Description
In sessions where the standard insert does not allow the user to insert all the fields, this function can be used to give the user an alternative session to insert the record.
This function activates the standard command insert.in.detail.
This standard command has (as other standard commands) an is.allowed before.choice and after.choice hook.

## Arguments
| | | |
|---|---|---|
| `string` | `sess_code` |  The session code of the session used for insert.  |
| `[ string` | `parent.var child.var ]` |  These are optional arguments. You use them to synchronize particular variables in the parent and child sessions. For each variable to be synchronized, specify the name of the relevant field in the parent's main table, followed by the name of the corresponding field in the child’s main table.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2350.
Notes  For this function to have effect:
- The function should be used in the before program. To have the Insert in Detail added to the action menu.
- At other places in the source this function can be executed to change the insert in detail session.

## Example
```

before.program:
	if shall.we.add.insert.in.detail() then
		set.insert.in.detail.session()"tsctm1110m300", "tsctm110.term", "tsctm110.term")
		|* tsctm1110m300 is set as the insert session when the action Insert in Detail is used
	endif


choice.insert.in.detail:
before.choice:
	|* Setting external variables that will be imported by the insert.in.detail session
	xi.term = tsctm110.term

	if term.application = tsctm.termappl.contract then
		set.insert.in.detail.sesssion("tsctm1110m300""tsctm110.term", "tsctm110.term")
	endif
	if term.application = tsctm.termappl.quotation then
		set.insert.in.detail.sesssion("tsctm1110m200""tsctm110.term", "tsctm110.term")
		|* this will overwrite the set.insert.in.detail.session from the before.program
	endif

functions:
function boolean shall.we.add.insert.in.detail()
|* own application function NOT called from the 4GL Engine
{
	if CONTRACT.MMT then
		return (true)
	endif
	return (false)
}

function extern boolean insert.in.detail.is.allowed()
{
	if not add.set.is.allowed() then
		return (false)
	endif
	if not method.is.allowed(DAL_NEW) then
		return (false)
	endif
	return (true)
}
```

## Related topics
- [Synchronized sessions synopsis](synopsis.md)
