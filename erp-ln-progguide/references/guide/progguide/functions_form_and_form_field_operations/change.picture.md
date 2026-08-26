# change.picture()

## Syntax:
`function long change.picture( const string fname, const string icon, [ const string absolute.file ] )`

## Description
Static pictures stored on the server can be displayed on a form. Pictures can be added to the form using the DFE. For display of an icon, the picture must be one of the pictures in the Icon Group "form_<pp>", where pp is the package-code of the picture's session. For display of an image from a local file on the server, the optional argument absolute.file must be filled.

## Arguments
| | | |
|---|---|---|
| `const string` | `fname` |  The name of the field whose picture must be set.  |
| `const string` | `icon` |  Name of the icon in icongroup "form_pp" where 'pp' is the package-code of the form.  |
| `[ const string` | `absolute.file ]` |  The file name (including the path) in which a picture is stored. The picture being displayed must be of type .gif when displaying in Worktop. Webtop, LN-Ui and later supports .gif, .jpg, .png. When the file name is passed as an argument, the icon argument is ignored.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | session is not dynamic |
| -2 | field not found |
| -3 | field not a picture field |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example showing a picture
```

	Declaration:
	 Extern string show.picture |(variable which is used in the dynamic form editor)
	 long return.value

	field.show.picture:
	 before.display:
	 return.value = change.picture("showpic","", "subdir/pipi.gif")
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
