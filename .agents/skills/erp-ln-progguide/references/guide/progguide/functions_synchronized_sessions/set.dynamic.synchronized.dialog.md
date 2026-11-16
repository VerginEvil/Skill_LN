# set.dynamic.synchronized.dialog()

## Syntax:
`function void set.dynamic.synchronized.dialog( const string sessioncode, [ const string parent.field, const string child.field,... ] )`

## Description
This function can be used to set the synchronize session when the session to start depends on data of the record, or when the synchronized session uses a child table.
Note that the session must have a regular synchronized dialog set for this function to work. Using this function also implies that adding records is done via the grid or via form commands that start the appropriate session directly.

## Arguments
| | | |
|---|---|---|
| `const string` | `sessioncode` |  The session code of the child session.  |
| `[ const string` | `parent.field ]` |    |
| `[ const string` | `child.field,... ]` |  The parent.field and child.field parameters can be used to define the field mapping between the sessions, if the main table differs. This can be used to use a child table as synchronized session. When these arguments are specified, the synchronized session will be started in overview ( `MULTI_OCC`) mode.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example for multiple synchronized dialogs on the same table
```

before.program:
	| Note that if the dialog is used for inserting, add.set should not be enabled
	set.synchronized.dialog()(prog.name$, true, true)

choice.display.set:
before.choice:
	determine.detail.session()

choice.dupl.occur:
before.choice:
	determine.detail.session()

choice.modify.set:
before.choice:
	determine.detail.session()

functions:
function void determine.detail.session()
{
	string session(13)

	on case tpppc200.cotp
	case tppdm.cotp.materials:
		session = "tppin2100m100"
		break
	case tppdm.cotp.tasks:
		session = "tppin2100m200"
		break
	case tppdm.cotp.equipment:
		session = "tppin2100m300"
		break
	case tppdm.cotp.subcontracting:
		session = "tppin2100m400"
		break
	case tppdm.cotp.indirect:
		session = "tppin2100m500"
		break
	case tppdm.cotp.overhead:
		session = "tppin2100m600"
		break
	default:
		break
	endcase

	set.dynamic.synchronized.dialog(session)
}
```

## Example for synchronization with a child table
```

before.program:
	| When the synchronized dialog is set on the session properties, then this call
	| can be omitted, as records are added with the grid by default.
	| The call to set.dynamic.synchronized.dialog must then be moved to after.form.read
	set.synchronized.dialog()("tirpt4101m000", true, false)
	set.dynamic.synchronized.dialog("tirpt4102m000", "tirpt401.prsh", "tirpt402.prsh")
```

## Related help topics
- [Synchronized sessions overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Child synchronization sample program](example.md)
