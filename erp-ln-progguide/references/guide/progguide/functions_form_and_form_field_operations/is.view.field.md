# is.view.field()

## Syntax:
`function boolean is.view.field( const string fieldname )`

## Description
This function can be used to check whether a field is currently a view field. This is useful when, for example, the view can be personalized and a total line only makes sense with a specific field in the view.
Note  This function cannot be used in the `before.program` and `after.form.read` sections.

## Arguments
| | | |
|---|---|---|
| `const string` | `fieldname` |  The name of the field to check.  |

## Return values
True if the field is currently a view field

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

function display.total.line.fields()
{
	domain	tcmcs.long6	total.means.of.transport

	| Index 2 is Transport Means Group, Carrier; it only makes sense
	| to sum capacity when TMG is in the view.
	if session.current.index = 2 and
	   is.view.field("fmfmd052.cmtg") then
		e = fmfmd.dll0052.get.total.available.number.of.tmg(
					fmfmd052.cmtg,
					total.means.of.transport)
		display.total.fields(	"available.capacit",
					total.means.of.transport)
	endif
}
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
